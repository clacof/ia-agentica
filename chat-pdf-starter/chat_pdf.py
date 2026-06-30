"""
Chat con tus PDFs · Starter RAG mínimo y reproducible.

Uso:
    pip install -r requirements.txt
    export OPENAI_API_KEY="sk-..."        # en Windows: set OPENAI_API_KEY=...
    python chat_pdf.py mi_documento.pdf

Si no pasas un PDF, usa 'mi_documento.pdf' en esta carpeta.

Nota de vigencia: los nombres de modelos (gpt-4o-mini, text-embedding local)
cambian con el tiempo. Verifica el vigente en la doc del proveedor.
"""
import os
import sys

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI

MODELO_EMBED = "all-MiniLM-L6-v2"   # local, gratis, corre en CPU
MODELO_LLM = "gpt-4o-mini"          # verifica el nombre vigente


def leer_pdf(ruta: str) -> str:
    """Extrae el texto de todas las páginas del PDF."""
    reader = PdfReader(ruta)
    return "\n".join(p.extract_text() or "" for p in reader.pages)


def trocear(texto: str) -> list[str]:
    """Corta el texto en chunks con solapamiento."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(texto)


def indexar(chunks: list[str], embed: SentenceTransformer):
    """Guarda los chunks y sus embeddings en una colección Chroma en memoria."""
    col = chromadb.Client().create_collection("docs")
    col.add(
        documents=chunks,
        embeddings=[embed.encode(c).tolist() for c in chunks],
        ids=[f"c{i}" for i in range(len(chunks))],
    )
    return col


def responder(col, embed, client, pregunta: str) -> str:
    """Recupera los chunks relevantes y genera la respuesta con el LLM."""
    res = col.query(
        query_embeddings=[embed.encode(pregunta).tolist()],
        n_results=3,
    )
    contexto = "\n\n".join(res["documents"][0])
    prompt = (
        "Usa SOLO este contexto. Si la respuesta no está, di 'No lo sé'.\n\n"
        f"Contexto:\n{contexto}\n\nPregunta: {pregunta}"
    )
    r = client.chat.completions.create(
        model=MODELO_LLM,
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content


def main() -> None:
    ruta = sys.argv[1] if len(sys.argv) > 1 else "mi_documento.pdf"
    if not os.path.exists(ruta):
        sys.exit(f"No encuentro el PDF: {ruta}")
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY")

    print(f"📄 Leyendo {ruta}…")
    embed = SentenceTransformer(MODELO_EMBED)
    client = OpenAI()
    col = indexar(trocear(leer_pdf(ruta)), embed)
    print("✅ Listo. Escribe tus preguntas (o 'salir').")

    while True:
        try:
            q = input("\n🧑 Tu pregunta: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in {"salir", "exit", "quit"}:
            break
        if q:
            print("🤖", responder(col, embed, client, q))


if __name__ == "__main__":
    main()

# 🛠️ Starter RAG · Chat con tus PDFs

Proyecto mínimo y reproducible que acompaña la guía **RAG & Fine-tuning**. Ingiere un PDF y responde preguntas sobre él usando RAG (embeddings locales + Chroma + un LLM).

## Requisitos

- Python 3.10 o superior
- Una API key de OpenAI (para la generación de la respuesta)

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
export OPENAI_API_KEY="sk-..."      # Windows: set OPENAI_API_KEY=...
python chat_pdf.py mi_documento.pdf
```

Si no pasas un archivo, busca `mi_documento.pdf` en esta carpeta. Escribe preguntas en la terminal y `salir` para terminar.

## Cómo funciona (4 pasos de RAG)

1. **Leer** el PDF y extraer su texto (`pypdf`).
2. **Trocear** en chunks de ~500 caracteres con solapamiento.
3. **Indexar** los chunks y sus embeddings en Chroma (modelo local `all-MiniLM-L6-v2`, gratis y en CPU).
4. **Recuperar** los 3 chunks más relevantes y **generar** la respuesta con el LLM, instruido a usar SOLO ese contexto.

## ¿Sin API key de OpenAI?

Puedes sustituir la generación por un modelo local de HuggingFace (más lento, pero gratis y privado). Mira la sección "Proyecto" de la guía visual para el ejemplo con `transformers.pipeline`.

## Nota de vigencia

Los nombres de modelos (`gpt-4o-mini`, el modelo de embeddings) y las versiones de las librerías cambian con el tiempo. Las de `requirements.txt` están fijadas y probadas juntas; si algo falla, actualiza con `pip install -U <paquete>` y revisa la documentación oficial.

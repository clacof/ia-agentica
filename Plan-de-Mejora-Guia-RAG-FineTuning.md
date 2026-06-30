# 🛠️ Plan de Mejora · Guía Visual de RAG & Fine-tuning

**Estado actual:** guía sólida y bien estructurada con 10 secciones (Inicio, ¿Qué es un LLM?, Embeddings, RAG, Fine-tuning, RAG vs Fine-tuning, Proyecto chat-PDF, Evaluación, Roadmap, Vocabulario & FAQ), 14 bloques de código Python, 30 checklists con progreso persistente, 5 quizzes, flashcards, 4 diagramas SVG, buscador global y modo oscuro.

**Diagnóstico en una frase:** explica excelentemente los fundamentos (embeddings → RAG → fine-tuning con LoRA) y la decisión entre ambos, pero le falta el ecosistema de producción (agentes, re-ranking, RAG avanzado, observabilidad) y un proyecto ejecutable verificado de punta a punta.

A continuación, las brechas detectadas y un plan en 4 fases con prioridades (P0 = alto impacto / bajo esfuerzo).

---

## ✅ Registro de cambios (ejecutado)

**27 jun 2026 — Fase 1 completa + ítem 7 de Fase 2:**

- ✅ **1.1** Bloques "⚠️ Errores típicos" añadidos en Embeddings, RAG y Fine-tuning.
- ✅ **1.2** Notas de vigencia ("verifica versión") junto a nombres de modelos/APIs en Embeddings, RAG y Fine-tuning.
- ✅ **1.3** Starter reproducible en `chat-pdf-starter/` (`chat_pdf.py` probado, `requirements.txt` con versiones fijadas, `README.md`).
- ✅ **1.4** Quizzes ampliados a 2 por módulo en Fundamentos, Embeddings, RAG, Fine-tuning y Comparativa (12 quizzes en total).
- ✅ **1.5** TOC interno clicable en RAG y Fine-tuning.
- ✅ **2.7** Nuevo **módulo "Agentes y tool-calling"** (function calling, bucle ReAct, RAG agéntico, diagrama SVG, 2 quizzes, checklist) + términos en el glosario/flashcards.

**Pendiente:** resto de Fase 2 (RAG avanzado, evaluación con código, prompt engineering), Fase 3 y Fase 4.

---

## 1. Brechas de contenido (qué temas faltan)

| Tema ausente o débil | Por qué importa | Prioridad |
|---|---|---|
| **RAG avanzado** (re-ranking, hybrid search BM25+vectorial, query rewriting, HyDE) | El RAG básico falla en producción; el re-ranking es la mejora #1 de calidad | 🔴 Alta |
| **Agentes y tool-calling** (function calling, ReAct, RAG agéntico) | "ia-agentica" es el nombre de la carpeta; hoy el tema central no está | 🔴 Alta |
| **Chunking avanzado** (semántico, por estructura, parent-document, tamaño óptimo) | El chunking ingenuo es la causa raíz de la mitad de los fallos de RAG | 🔴 Alta |
| **Evaluación profunda** (RAGAS en código, golden set real, métricas LLM-as-judge) | Hoy se nombra pero no se implementa con código ejecutable | 🔴 Alta |
| **Prompt engineering** como paso previo a RAG/fine-tuning | La guía lo recomienda pero no lo enseña (few-shot, system prompts, plantillas) | 🟠 Media |
| **Embeddings: elección y dimensiones** (multilingües, reranqueo, MTEB, coste/latencia) | Elegir mal el modelo de embeddings degrada todo el sistema | 🟠 Media |
| **Vector DB en producción** (metadata filtering, índices HNSW/IVF, actualización incremental) | El salto de Chroma local a Pinecone/pgvector real no está cubierto | 🟠 Media |
| **Costos y latencia con números** (caching, streaming, batching, modelos por tarea) | El apartado de costos es cualitativo; falta optimización concreta | 🟠 Media |
| **Seguridad** (prompt injection, fuga de datos vía contexto, PII, guardrails) | Riesgo real en cualquier asistente sobre documentos | 🟠 Media |
| **Datos para fine-tuning** (cómo generarlos, sintéticos, limpieza, balance, splits) | "Calidad > cantidad" se afirma pero no se enseña a construir el dataset | 🟠 Media |
| **DPO / RLHF / preferencias** (más allá de SFT) | Para alinear tono/estilo fino; nivel avanzado | 🟢 Baja |
| **Despliegue** (servir un modelo LoRA, vLLM/Ollama, API propia, GGUF) | "¿Y ahora cómo lo pongo online?" no tiene respuesta | 🟢 Baja |
| **Multimodal** (RAG sobre imágenes/tablas/PDF con layout) | Diferenciador; muchos documentos reales no son solo texto | 🟢 Baja |

---

## 2. Brechas pedagógicas (cómo se enseña)

- **Un solo quiz por sección.** Funcionan muy bien; ampliar a 2-3 por módulo para afianzar.
- **Sin ejercicios prácticos graduados.** Falta una sección tipo "Ejercicios por niveles" (como la guía de Swift) con retos de RAG y de fine-tuning.
- **Soluciones siempre visibles.** Cuando se añadan ejercicios, usar enunciado → botón "Ver solución" para forzar el intento previo.
- **Proyecto no verificado end-to-end.** El `chat_pdf.py` es didáctico pero no se ha probado contra dependencias reales (versiones de `chromadb`, API actual de OpenAI). Conviene un repo starter probado.
- **Sin comparación visual de resultados.** Un "antes/después" (LLM sin RAG vs con RAG) ayudaría a internalizar el valor.
- **Falta un diagrama de decisión interactivo.** "¿RAG o fine-tuning?" como árbol clicable sería más memorable que la tabla.
- **"Errores comunes" solo en Evaluación.** Estandarizar un bloque "⚠️ Errores típicos" por módulo (embeddings, chunking, fine-tuning).

---

## 3. Brechas de la herramienta (la web interactiva)

- **Código no ejecutable de verdad.** El botón "▶ Probar" abre un editor externo pero sin las dependencias; valorar Pyodide para snippets simples (numpy/coseno) ejecutables en el navegador.
- **Progreso atado a un navegador.** Ya hay export/import; documentarlo en la propia UI (hoy es poco visible).
- **Sin TOC por página.** Las páginas largas (RAG, Fine-tuning) ganarían un índice interno.
- **Solo en español.** Sin toggle ES/EN (el público de IA suele necesitar EN).
- **Sin versión PDF/impresión** lista (el CSS de print existe; falta un botón explícito "Descargar PDF").
- **Diagramas SVG estáticos.** El pipeline de RAG podría animarse paso a paso al hacer clic.
- **Buscador no pondera código.** Indexa el cuerpo, pero un filtro "solo código / solo texto" ayudaría.

---

## 4. Calidad / correcciones puntuales

- **Verificar nombres de modelos y APIs** (se desactualizan rápido): `text-embedding-3-small`, `gpt-4o-mini`, `Mistral-7B-v0.1`, fechas de snapshot de fine-tuning. Añadir nota "verifica el nombre vigente en la doc del proveedor".
- **`SFTTrainer` / `trl`**: la API cambia entre versiones; fijar versiones o marcar como "pseudocódigo orientativo".
- **Aviso de costos:** reforzar que las cifras son ilustrativas y enlazar (en texto) a las páginas oficiales de precios.
- **Privacidad:** añadir nota sobre no subir datos sensibles a APIs de terceros sin revisar políticas.
- **Reproducibilidad del proyecto:** congelar un `requirements.txt` probado junto al `chat_pdf.py`.

---

## 5. Plan de ejecución por fases

### 🚀 Fase 1 — Quick wins (P0 · alto impacto, bajo esfuerzo)
1. **Bloque "⚠️ Errores típicos"** estandarizado en Embeddings, Chunking, RAG y Fine-tuning.
2. **Notas de vigencia** en cada nombre de modelo/API + aviso de "verifica versión".
3. **`requirements.txt` probado** + mini repo starter para `chat_pdf.py`.
4. **2-3 quizzes por módulo** (ampliar los actuales).
5. **TOC interno** en las páginas largas (RAG, Fine-tuning).

### 📚 Fase 2 — Expansión de contenido (P1 · el mayor salto de valor)
6. **Módulo RAG avanzado** (re-ranking con cross-encoder, hybrid search, query rewriting/HyDE, parent-document).
7. **Módulo Agentes y tool-calling** (function calling, ReAct, RAG agéntico) — alinea con "ia-agentica".
8. **Módulo Evaluación con código** (RAGAS ejecutable, golden set, LLM-as-judge).
9. **Sección Prompt engineering** como paso 0 antes de RAG/fine-tuning.

### 🎮 Fase 3 — Interactividad (P1/P2 · acelera el aprendizaje)
10. **Sección Ejercicios por niveles** (RAG y fine-tuning) con soluciones ocultas.
11. **Árbol de decisión interactivo** "¿RAG o fine-tuning?".
12. **Diagramas SVG animados** del pipeline de RAG paso a paso.
13. **Snippets ejecutables en el navegador** (Pyodide) para coseno/embeddings simples.
14. **Comparador "antes/después"** (respuesta sin RAG vs con RAG).

### ✨ Fase 4 — Producción y alcance (P2 · profesionalización)
15. **Módulo Vector DB en producción** (metadata filtering, índices, actualización incremental).
16. **Módulo Seguridad** (prompt injection, PII, guardrails).
17. **Módulo Despliegue** (servir LoRA con vLLM/Ollama, GGUF, API propia).
18. **Optimización de costos/latencia** con números (caching, streaming, batching).
19. **Toggle de idioma ES/EN** + botón **"Descargar PDF"**.
20. Temas avanzados: **DPO/RLHF**, **RAG multimodal**.

---

## 6. Recomendación

Empezar por la **Fase 1** (rápida y se nota enseguida: vigencia de APIs y un proyecto reproducible elevan mucho la confianza). Luego la **Fase 2 con el módulo de Agentes y tool-calling**, que es la mayor carencia y además es coherente con el nombre del repo (`ia-agentica`). Las fases 3 y 4 convierten una "buena guía" en una "plataforma de estudio" de nivel producción.

---

## 7. Próximo paso sugerido

Puedo, además, **dejar programada una actualización periódica** (p. ej. mensual) que revise si cambiaron nombres de modelos, precios o APIs y proponga parches a la guía. Dime si lo activo.

---

*Documento generado como diagnóstico de la guía `Tutorial-RAG-FineTuning-Visual.html` y `GUIA_RAG_Y_FINETUNING_DESDE_CERO.md`. Cada punto es accionable de forma independiente: dime por cuál quieres empezar y lo implemento.*

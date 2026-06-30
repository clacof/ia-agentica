# 🗺️ Plan · Gran Guía de IA Agéntica (unificada)

**Qué es ahora `index.html`:** una sola guía interactiva de **17 secciones** que va de los fundamentos del agente al ecosistema completo, e incluye —ya integrado y con el mismo diseño— un bloque nuevo **"Conocimiento & adaptación"** con RAG, Fine-tuning y RAG vs Fine-tuning.

**Estructura actual:**

1. Fundamentos: ¿Qué es un agente? · Loop agéntico · Anatomía · Tools & function calling · Context engineering
2. **Conocimiento & adaptación (NUEVO): RAG · Fine-tuning · RAG vs Fine-tuning**
3. Protocolos & extensión: MCP · Skills · Subagentes
4. Herramientas: Claude Code · Codex · OpenCode · Comparativa
5. Práctica: Patrones agénticos · Glosario

**Coherencia lograda:** RAG entra justo después de *Context engineering* (que ya lo citaba como táctica "Select"), enlaza con *Tools* vía "RAG agéntico", y RAG-vs-FT cierra conectando con el *loop agéntico*. El glosario incorpora embedding, vector DB, chunking, fine-tuning y LoRA/QLoRA. El hero refleja los nuevos temas.

---

## ✅ Registro de cambios — "dale con todo" (30 jun 2026)

**Implementado todo el plan (P0 + P1 + P2) sobre `index.html`:**

- ✅ **P0** Mapa de la guía clicable bajo el hero; diagrama de 3 niveles (prompt → RAG → fine-tuning) en RAG vs FT; notas de vigencia junto a modelos; enlaces cruzados (Context → RAG, RAG → Tools/Evaluación) y enlaces a las otras piezas (tutorial visual, guía en texto, starter) — con back-link desde el tutorial visual.
- ✅ **P1** Nueva sección **RAG agéntico** (re-ranking, hybrid search, query rewriting/HyDE, parent-document, RAG como tool del loop, nota "Memoria del agente"); nueva sección **Evaluación** (recall, fidelidad, golden set, RAGAS/LangSmith, validación de fine-tunes).
- ✅ **P2** **Tema claro/oscuro** con persistencia; botón **Descargar/Imprimir PDF** (CSS de impresión que despliega tabs y acordeones); **buscador** de secciones y glosario en el nav; **5 quizzes** interactivos (RAG, Fine-tuning, RAG vs FT, RAG agéntico, Evaluación).

Resultado: **20 secciones**, navegación y barra de progreso coherentes, JS validado sin errores. Quedan pendientes solo refinamientos opcionales (más quizzes, TOC flotante móvil).

> Nota: quedaron archivos `index.html.bak*` que el entorno no permitió borrar; puedes eliminarlos (el repo está en git).

---

## 1. Estado y lo ya hecho

- ✅ 3 secciones nuevas (RAG, Fine-tuning, RAG vs FT) en el estilo nativo (cards, loop, tabs, notes, tablas, código resaltado).
- ✅ Grupo de navegación nuevo + scrollspy y barra de progreso funcionando (17 enlaces ↔ 17 secciones).
- ✅ Renumeración consistente de todas las secciones (1–17) y hero actualizado.
- ✅ Glosario ampliado y enlaces cruzados internos para una lectura continua.

---

## 2. Mejoras propuestas (priorizadas)

### 🟢 P0 — Quick wins (alto impacto, bajo esfuerzo)
1. **Sub-índice del bloque nuevo en el hero** o un "mapa de la guía" clicable al inicio, para que se vea de un vistazo que ahora cubre conocimiento + adaptación.
2. **Nota de vigencia** corta y reutilizable junto a nombres de modelos (`gpt-4o-mini`, snapshots de fine-tuning) — igual que en el tutorial visual.
3. **Enlaces cruzados extra**: desde *Context engineering* → RAG, y desde *Tools* → "RAG agéntico", para reforzar la narrativa.
4. **Diagrama "los 3 niveles"** (prompt → RAG → fine-tuning) como `.loop` o `.stack`, que resume la decisión visualmente.

### 🟠 P1 — El mayor salto de valor
5. **Sección "RAG agéntico" propia** (hoy es una nota): re-ranking, hybrid search, query rewriting y RAG como tool dentro del loop — encaja perfecto con el tema del repo.
6. **Sección "Evaluación"** transversal: cómo medir un agente con RAG (recall del retrieval, fidelidad, golden set) y un fine-tune (validación, antes/después).
7. **Patrón "Memoria del agente"**: relacionar `CLAUDE.md`/`AGENTS.md` (ya en la guía) con RAG y con memoria a largo plazo — cierra el círculo conocimiento ↔ contexto.

### 🔵 P2 — Interactividad y alcance
8. **Quizzes y/o "ver respuesta"** al estilo del tutorial visual, para autoevaluación dentro de la guía única.
9. **Modo claro/oscuro** (hoy solo oscuro) y **botón "Descargar PDF"** aprovechando el CSS de impresión.
10. **Buscador en la guía** (filtra secciones/glosario) y **TOC flotante** en móvil (hoy el nav se oculta < 900px).
11. **Unificar las dos piezas**: enlazar de forma bidireccional `index.html` ↔ `Tutorial-RAG-FineTuning-Visual.html` (la guía profunda) y el `chat-pdf-starter/`.

---

## 3. Riesgos / cosas a vigilar

- **Vigencia de APIs y modelos:** los snippets envejecen; conviene la nota de vigencia (P0-2) y, si quieres, una revisión programada mensual.
- **Longitud de la página:** con 17 secciones, un buscador o TOC plegable (P2-10) ayuda a no perderse.
- **Dos guías paralelas:** `index.html` (resumen agéntico) y `Tutorial-RAG-FineTuning-Visual.html` (profundización). Mantener el enlace entre ambas evita duplicar/desincronizar contenido.

---

## 4. Recomendación

Empezar por los **P0** (rápidos y dan sensación de guía "terminada"), y luego el **P1-5 (RAG agéntico propio)**, que es la pieza más coherente con el repo `ia-agentica` y la que más eleva el nivel técnico. Los P2 convierten la guía en una pequeña plataforma de estudio.

---

*Cada punto es accionable por separado. Dime por cuál empiezo y lo implemento sobre `index.html`.*

---
name: user-compiler
description: Compiler stage for End-Users.
---

# Stage: Compiler (for End-Users)

**Task:** You are the Rolling Editor-in-Chief. Stitch N chunks into a single master document sequentially. To avoid context limits: 1) Initialize master with chunk 1. 2) For each subsequent chunk, extract only the last 2000 chars of master and first 2000 chars of the new chunk. 3) Rewrite this 'seam' to be perfectly smooth and delete redundant introductions. 4) Use Python to splice the files together on disk: (master minus last 2000) + (smoothed seam) + (new chunk minus first 2000). Repeat for all chunks.

**After stitching, collect every `STUB`-tagged item mentioned across all N chunks** (each Writer should have surfaced these in-line already, per `user-writer`) and confirm the master document has a single consolidated "not fully built yet" section that lists all of them together, deduplicated. Chunks are written independently by different Writers, so a reader going chunk-by-chunk still can't easily see the full list of what's not working — the compiled document is the one place that can and must give the whole picture in one place. If you find a `STUB` item that made it into one chunk's inline prose but is missing from this consolidated section, add it — do not assume the per-chunk mention was sufficient.

**Track Rules:**
Code Inclusion: NONE. Focus on step-by-step feature walkthroughs, UI navigation, and operational flows. Tone is accessible, narrative, and task-oriented. MANDATORY: You MUST generate Mermaid.js flowcharts to visualize user workflows and UI journeys.

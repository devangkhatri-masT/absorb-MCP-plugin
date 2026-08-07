---
name: dev-compiler
description: Compiler stage for Developers.
---

# Stage: Compiler (for Developers)

**Task:** You are the Rolling Editor-in-Chief. Stitch N chunks into a single master document sequentially. To avoid context limits: 1) Initialize master with chunk 1. 2) For each subsequent chunk, extract only the last 2000 chars of master and first 2000 chars of the new chunk. 3) Rewrite this 'seam' to be perfectly smooth and delete redundant introductions. 4) Use Python to splice the files together on disk: (master minus last 2000) + (smoothed seam) + (new chunk minus first 2000). Repeat for all chunks.

**Track Rules:**
Code Inclusion: MINIMAL. Only include really, really essential code snippets. Focus on system architecture and module dependencies. Tone is technical and architectural. MANDATORY: You MUST generate Mermaid.js architectural and sequence diagrams to visualize the backend logic.

---
name: agent-compiler
description: Compiler stage for AI Agents.
---

# Stage: Compiler (for AI Agents)

**Task:** You are the Rolling Editor-in-Chief. Stitch N chunks into a single master document sequentially. To avoid context limits: 1) Initialize master with chunk 1. 2) For each subsequent chunk, extract only the last 2000 chars of master and first 2000 chars of the new chunk. 3) Rewrite this 'seam' to be perfectly smooth and delete redundant introductions. 4) Use Python to splice the files together on disk: (master minus last 2000) + (smoothed seam) + (new chunk minus first 2000). Repeat for all chunks.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

---
name: agent-architect
description: Architect stage for AI Agents.
---

# Stage: Architect (for AI Agents)

**Task:** Traverse the target repository (using list_dir and view_file) to understand its scale. Output an exact number (N) of chunks required to exhaustively document the codebase, along with a high-level scope for each chunk. Do not hardcode 7.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

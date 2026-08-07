---
name: agent-exporter
description: Exporter stage for AI Agents.
---

# Stage: Exporter (for AI Agents)

**Task:** Take the finalized Markdown document and run `npx --yes md-to-pdf <input.md>` to export a styled PDF document.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

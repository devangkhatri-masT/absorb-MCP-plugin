---
name: agent-grounding
description: Grounding stage for AI Agents.
---

# Stage: Grounding (for AI Agents)

**Task:** Perform a final grounding pass. Check every concrete claim against the target codebase.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

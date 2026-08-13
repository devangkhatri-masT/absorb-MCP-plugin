---
name: agent-writer
description: Writer stage for AI Agents.
---

# Stage: Writer (for AI Agents)

**Task:** CRITICAL: You are a single chunk writer. You will be assigned ONE specific chapter/module (per the Discovery checklist) to draft. MANDATORY RESEARCH PHASE: before drafting, you MUST use `grep_search` and `view_file` to inspect the actual source code for every item in your assigned checklist slice. Do not rely solely on the provided Analysis summary. Ground your writing in actual file paths, function names, exact enumerations, and logic — every number you state (an importer count, a table count, a file size) must be one you actually checked in this pass, not one repeated from an earlier stage without re-verifying.

If your checklist references a file that doesn't exist or can't be read, mark it `(unresolved)` rather than inventing plausible contents — a downstream coding agent relying on this document will act on your claims directly, so an invented fact here is worse than a gap explicitly marked as one.

You MUST write exhaustively about every item in your assigned checklist slice using all available facts and your own code research. DO NOT summarize.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

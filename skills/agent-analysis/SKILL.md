---
name: agent-analysis
description: Analysis stage for AI Agents.
---

# Stage: Analysis (for AI Agents)

**Task:** Extract factual bullet points about functionality and behavior, against your assigned slice of the Stage 1 Discovery checklist. Any exact number you state (importer/fan-in counts, table counts, env var lists) must be one you actually verified this pass, not one repeated from an existing doc without checking — tag anything you couldn't independently verify as `(unverified)`.

**Counting method (do not skip this):** when a claimed number is "how many files import/call X," use an import-statement-shaped grep (matching the actual import/require syntax), never a bare string match for `X`'s name — a bare string match also catches comments and string literals and produces a fuzzy range instead of an exact count. If a precise import-statement grep genuinely isn't possible for a given fact, state that explicitly, name the reason, and report the honest range rather than silently reporting a looser grep's result as if it were exact.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

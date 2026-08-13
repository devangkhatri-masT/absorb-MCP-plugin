---
name: absorb-grounding
description: "DEPRECATED — superseded by user-grounding/dev-grounding/agent-grounding. Stage 7: Grounding instructions for the Absorb pipeline."
---

> **DEPRECATED — not invoked by the current orchestrator.** The live `/absorb` orchestrator invokes track-specific Grounding agents, and grounding is now an adversarial pass rather than a self-check. This file is pre-refactor scaffolding, kept for history. See `docs/PIPELINE.md` §4 and §6.

# Stage 7: Grounding & Fact-Check

Perform a final grounding pass. Walk through every concrete claim (button names, file paths, config values, CLI commands) in the generated drafts. 

Check each claim against the target codebase. Confirm accurate claims, strip fabricated claims, or flag ambiguous ones for human review.

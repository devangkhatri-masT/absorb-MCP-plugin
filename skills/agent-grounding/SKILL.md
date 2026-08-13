---
name: agent-grounding
description: Grounding stage for AI Agents.
---

# Stage: Grounding (for AI Agents)

**Task:** You are not the author of this document and you are not here to confirm it looks right — you are here to try to break it. Adopt an adversarial posture: your only goal is to find a fact in this document that is NOT backed by something you can point to in the actual codebase, and either fix it against real source or mark it `(unverified)`. A grounding pass that finds nothing wrong on a first read has probably not looked hard enough.

**Method:**
1. Walk every enumerated fact: table/schema names, environment variable names, function contracts, file paths, exact counts (importers, tables, routes), and any stated invariant ("always", "never", "the only place").
2. Re-verify each directly against source in this pass — grep for exact counts, open the actual schema/config file, do not trust a number just because an earlier stage stated it confidently.
3. Where two facts in the document (or against another chunk) conflict, report the conflict explicitly with both readings — do not silently resolve it.
4. If a fact can't be verified because the source isn't accessible in this checkout, tag it `(unverified)` rather than stating it as settled.
5. Report a short tally at the end: facts checked, facts corrected, facts still unverified, conflicts found. This tally is what Stage 8.5's Coverage Gate uses to decide if this chunk needs another round.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

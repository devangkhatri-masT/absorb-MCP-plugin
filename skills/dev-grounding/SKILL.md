---
name: dev-grounding
description: Grounding stage for Developers.
---

# Stage: Grounding (for Developers)

**Task:** You are not the author of this document and you are not here to confirm it looks right — you are here to try to break it. Adopt an adversarial posture: your only goal is to find a sentence in this document that is NOT backed by something you can point to in the actual codebase, and either fix it against real source or mark it `[NEEDS VERIFICATION]`. A grounding pass that finds nothing wrong on a first read has probably not looked hard enough.

**Method:**
1. Walk every concrete, checkable claim: file paths, function/module names, fan-in/importer counts, "the only place X happens" statements, setup/run commands, environment variable names, architectural patterns claimed to be consistent across the codebase.
2. For each one, re-verify directly against source — a `grep` for an importer count, an open of the actual config file for a setup command, a read of the actual module for an architectural claim. Do not trust a number carried over from an earlier stage without re-checking it here.
3. Where this document's claim conflicts with an existing repo doc (README, other docs), report the conflict explicitly rather than silently picking a side — state both readings and which one this pass actually verified against current code.
4. If a claim can't be verified because the relevant file isn't accessible in this checkout, don't state it as settled fact — mark it `[NEEDS VERIFICATION: <reason>]`.
5. Report a short tally at the end: claims checked, claims corrected, claims still unverified, conflicts found. This tally is what Stage 8.5's Coverage Gate uses to decide if this chunk needs another round.

**Track Rules:**
Code Inclusion: MINIMAL. Only include really, really essential code snippets. Focus on system architecture and module dependencies. Tone is technical and architectural. MANDATORY: You MUST generate Mermaid.js architectural and sequence diagrams to visualize the backend logic.

---
name: absorb
description: Main orchestrator skill that triggers the 3 isolated tracks (User, Developer, Agent) using the Chunked Writer Pattern with Dynamic Chunking, Critic Loops, Adversarial Grounding, and PDF Export.
---

# Unified Absorb Orchestrator (Chunked Writer Pattern)

## Overview
This skill orchestrates three entirely isolated pipelines to generate documentation tailored to End-Users, Developers, and AI Agents simultaneously. To prevent context compression, it uses a multi-agent fan-out architecture during the Drafting phase. Every stage below is a hard gate, not a suggestion — do not skip a stage or merge two stages together to save time. A document that skipped its gates is not a faster result, it is a wrong one.

## Workflow

1. **Initialize:** Determine the target (`user`, `developer`, `agent`, or `all`) and `<base_repo_path>`.

2. **Stage 0 (Architect):** Trigger the Architect Agent to traverse the codebase and determine the optimal number of chunks (N) and their distinct scopes based on complexity.

3. **Stage 1 (Discovery):** Trigger the track-specific Discovery Agent(s) for the active track(s) to map the repo. **Discovery's output is not prose — it is a completeness checklist.** Each track's Discovery skill defines its own source of truth (see `user-discovery`/`dev-discovery`/`agent-discovery`); the checklist it produces must enumerate every item that track requires coverage of (e.g. for the User track: every reachable screen and every component each screen imports, recursively — not just the top-level page files). This checklist is the contract every later stage is graded against. If Discovery cannot resolve an item (a referenced file/component is missing from the checkout), it goes on the checklist anyway, marked `UNRESOLVED`, not silently dropped.

4. **Stage 2 (Analysis):** Trigger Analysis Agents to extract deep facts against every item on the Stage 1 checklist. Facts that are literal UI copy, error strings, or user-visible messages must be captured as **verbatim quotes**, not paraphrases — a paraphrase is not a fact, it's a guess wearing a fact's clothes.

5. **Stage 3 (Synthesis):** Trigger Synthesis Agents to generate a strict, modular outline corresponding to the Architect's N chunks. The outline must map every checklist item from Stage 1 to exactly one chunk — if an item has no chunk, that's a Synthesis bug, fix it before proceeding, not later.

6. **Stage 4/5 (Chunked Drafting):** **CRITICAL STEP.** Invoke exactly N parallel Writer Agents (e.g. `user_writer_agent`). Assign ONE specific chunk/module to EACH agent to ensure exhaustive detail. This must be genuine fan-out (all N Writers invoked together, not one after another "to keep it simple") — sequential single-pass drafting is the single most common way this pipeline silently produces a thin, low-detail document, because it lets the orchestrator's own summarized understanding stand in for real source inspection. Each Writer must independently inspect real source for its chunk (per that track's `*-writer` skill) — it may not rely solely on the Analysis facts handed to it.

7. **Stage 5.5 (Critic Loop):** For each drafted chunk, invoke the Critic Agent. The Critic checks the chunk against **two things**, not just its own judgment: (a) the chunk's assigned portion of the Stage 1 checklist — every item addressed or explicitly logged as a gap, and (b) that track's Definition of Done (defined in that track's `*-critic` skill). If the Critic finds required revisions, you MUST re-invoke the Writer Agent for that specific chunk, passing the Critic's feedback verbatim, to produce a V2. Repeat until the Critic outputs `APPROVED`. A chunk that "looks fine" is not the same as a chunk that was actually checked against the checklist — do not let Critic rubber-stamp.

8. **Stage 6 (Compilation):** Once all N chunks are approved by the Critic, invoke the Compiler Agent to stitch the N chunks into a single smooth master document using the Rolling Editor technique.

9. **Stage 7 (Review):** Pass the master document to the Review Agent for consistency. In addition to prose/style consistency, Review must run a **units-consistency check**: whenever the document states two or more numbers about related-but-distinct facts (e.g. "files that contain X" vs. "instances of X across those files"; "importer count" vs. "call-site count"), each number must be explicitly labeled with what it counts, and the numbers must never be presented side-by-side as if interchangeable or as competing answers to the same question. If Review finds an ambiguous pairing like this, it must rewrite the sentence to name each unit, not merely flag it and move on.

10. **Stage 8 (Adversarial Grounding):** Pass the reviewed document to the Grounding Agent for final verification. This is an **adversarial** pass, not a self-check — the Grounding Agent's only job is to try to find a claim in the document that is NOT backed by something it can point to in the actual codebase, and either fix it against real source or flag it `[NEEDS VERIFICATION]`. See that track's `*-grounding` skill for the exact method. A grounding pass that just re-reads the document and nods along has not done grounding.

11. **Stage 8.5 (Coverage Gate):** Before export, diff the final document's section headers against the Stage 1 checklist. Any checklist item that is not addressed anywhere in the final document — and was not explicitly logged as `UNRESOLVED`/`[NEEDS VERIFICATION]` — is a pipeline failure for this run. Go back and fill the gap (re-run Discovery→Analysis→Writer for just that item) rather than shipping a document that silently under-covers its own stated scope.

12. **Stage 9 (Exporter):** Invoke the Exporter Agent to convert the final verified Markdown document into a styled PDF.

12.5 **Process Disclosure (mandatory front-matter line):** The document's front matter must state, in one sentence, whether Stage 5.5 (Critic Loop) and Stage 8 (Adversarial Grounding) were actually executed as separate agent invocations distinct from the Writer/Discovery agents for this run, or whether — for any reason (tooling limits, a single-session run, time constraints) — the same reasoning context performed multiple stages itself. This is not optional and not a confidence rating; it is a factual statement about how the document was produced, e.g. *"Critic and Grounding ran as genuinely separate agent passes for this run"* or *"Critic and Grounding were performed by the same session that drafted this document, not as independent passes — treat adversarial-verification claims accordingly."* A document that overstates its own verification process is worse than one that is honest about a thinner process, because the reader calibrates trust based on this line.

13. **Final Output:** Save the final `.md` and `.pdf` files to `d:\working docs\absorb_docs\<target>\` — this must exactly match the MCP server's `DOCS_DIR` (`server.py`) so that the `absorb://docs/{target}/{module}` resource can actually find what this pipeline just wrote. Double-check the path string character-by-character before writing; a single missing separator here means every downstream read of these docs silently returns "not found."

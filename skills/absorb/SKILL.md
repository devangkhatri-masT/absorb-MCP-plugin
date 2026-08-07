---
name: absorb
description: Main orchestrator skill that triggers the 3 isolated tracks (User, Developer, Agent) using the Chunked Writer Pattern with Dynamic Chunking, Critic Loops, and PDF Export.
---

# Unified Absorb Orchestrator (Chunked Writer Pattern)

## Overview
This skill orchestrates three entirely isolated pipelines to generate documentation tailored to End-Users, Developers, and AI Agents simultaneously. To prevent context compression, it uses a multi-agent fan-out architecture during the Drafting phase.

## Workflow

1. **Initialize:** Determine the target (`user`, `developer`, `agent`, or `all`) and `<base_repo_path>`.
2. **Stage 0 (Architect):** Trigger the Architect Agent to traverse the codebase and determine the optimal number of chunks (N) and their distinct scopes based on complexity.
3. **Stage 1 (Discovery):** Trigger specific Discovery Agents for the active tracks to map the repo.
4. **Stage 2 (Analysis):** Trigger Analysis Agents to extract deep facts.
5. **Stage 3 (Synthesis):** Trigger Synthesis Agents to generate a strict, modular outline corresponding to the Architect's N chunks.
6. **Stage 4/5 (Chunked Drafting):** **CRITICAL STEP**. Invoke exactly N parallel Writer Agents (e.g. `user_writer_agent`). Assign ONE specific chunk/module to EACH agent to ensure exhaustive detail.
7. **Stage 5.5 (Critic Loop):** For each drafted chunk, invoke the Critic Agent. If the Critic Agent outputs required revisions, you MUST re-invoke the Writer Agent for that specific chunk, passing the Critic's feedback, to produce a V2. Repeat until the Critic outputs 'APPROVED'.
8. **Stage 6 (Compilation):** Once all N chunks are approved by the Critic, invoke the Compiler Agent to stitch the N chunks into a single smooth master document using the Rolling Editor technique.
9. **Stage 7 (Review):** Pass the master document to the Review Agent for consistency.
10. **Stage 8 (Grounding):** Pass the reviewed document to the Grounding Agent for final verification.
11. **Stage 9 (Exporter):** Invoke the Exporter Agent to convert the final verified Markdown document into a styled PDF.
12. **Final Output:** Save the final .md and .pdf files to `d:\working docsbsorb_docs\<target>\`. 

---
name: absorb
description: Main orchestrator skill that triggers the 3 isolated tracks (User, Developer, Agent) using the Chunked Writer Pattern.
---

# Unified Absorb Orchestrator (Chunked Writer Pattern)

## Overview
This skill orchestrates three entirely isolated pipelines to generate documentation tailored to End-Users, Developers, and AI Agents simultaneously. To prevent context compression, it uses a multi-agent fan-out architecture during the Drafting phase.

## Workflow

1. **Initialize:** Determine the target (`user`, `developer`, `agent`, or `all`) and `<base_repo_path>`.
2. **Stage 1 (Discovery):** Trigger specific Discovery Agents for the active tracks to map the repo.
3. **Stage 2 (Analysis):** Trigger Analysis Agents to extract deep facts.
4. **Stage 3 (Synthesis):** Trigger Synthesis Agents to generate a strict, modular outline (e.g. Chapter 1 to N).
5. **Stage 4/5 (Chunked Drafting):** **CRITICAL STEP**. The Orchestrator MUST parse the Stage 3 Outline and invoke N parallel Writer Agents (e.g. `user_writer_agent`). Assign ONE specific chapter/module to EACH agent to ensure exhaustive detail.
6. **Stage 6 (Compilation):** Once all N writers finish, invoke the Compiler Agent to stitch the N chunks into a single master document.
7. **Stage 7 (Review):** Pass the master document to the Review Agent for consistency.
8. **Stage 8 (Grounding):** Pass the reviewed document to the Grounding Agent for final verification.
9. **Final Output:** Save the final files to `d:\working docsbsorb_docs\<target>\`. 

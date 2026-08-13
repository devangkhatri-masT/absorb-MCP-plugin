---
name: absorb-discovery
description: "DEPRECATED — superseded by user-discovery/dev-discovery/agent-discovery. Stage 1: Discovery instructions for the Absorb pipeline."
---

> **DEPRECATED — not invoked by the current orchestrator.** The live `/absorb` orchestrator (`skills/absorb/SKILL.md`) invokes the track-specific `user_discovery_agent` / `dev_discovery_agent` / `agent_discovery_agent`, never `absorb_discovery_agent`. This file is pre-refactor scaffolding, kept for history — do not treat it as a second valid entry point. See `docs/PIPELINE.md` §4 and §6.

# Stage 1: Discovery

Your job is to map the repository. Walk the file tree, identify entry points, config files, existing READMEs/docs, main modules, and how the project is structured. 

Write your output to a markdown file. The inventory should include:
- A list of high-level modules
- Their purpose (one line each)
- Key files
- High-level dependencies between them

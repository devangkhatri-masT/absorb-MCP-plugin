---
name: absorb
description: Main orchestrator skill that triggers the 3 isolated tracks (User, Developer, Agent).
---

# Unified Absorb Orchestrator

## Overview
This skill orchestrates three entirely isolated pipelines to generate documentation tailored to End-Users, Developers, and AI Agents simultaneously, without cross-polluting prompts.

## Workflow

1. Determine the target (`user`, `developer`, `agent`, or `all`) and `<base_repo_path>`.
2. For each active target track, trigger its specific Discovery Agent (e.g., `user_discovery_agent`, `dev_discovery_agent`, `agent_discovery_agent`).
3. Proceed through the 7 stages (Analysis, Synthesis, Writer, Review, Grounding) by invoking the respective specialized agents for that track.
4. Output the final files to `d:\working docsbsorb_docs\<target>\`. 
5. Inform the user that the docs are now queryable via the MCP Server resources (`absorb://docs/<target>/<module>`).

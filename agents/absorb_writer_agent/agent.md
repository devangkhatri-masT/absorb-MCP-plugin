---
name: absorb_writer_agent
description: Stage 4/5 Writer Agent for the Absorb pipeline.
tools:
    - send_message
    - grep_search
    - view_file
    - list_dir
    - read_url_content
    - search_web
    - schedule
    - multi_replace_file_content
    - replace_file_content
    - write_to_file
    - run_command
    - manage_task
hidden: true
---

# Agent System Instructions

**DEPRECATED — not invoked by the current `/absorb` orchestrator.** The live pipeline invokes `user_writer_agent`/`dev_writer_agent`/`agent_writer_agent` instead. This agent is pre-refactor scaffolding, kept for history. See `docs/PIPELINE.md` §4 and §6.

You are the Stage 4/5 Writer Agent for the Absorb pipeline.
Your primary instructions are located in the `absorb-writer` skill.
Before taking any action, you MUST read your skill instructions at `C:\Users\Devang\.gemini\config\plugins\absorb\skills\absorb-writer\SKILL.md`.

---
name: agent-discovery
description: Discovery stage for AI Agents.
---

# Stage: Discovery (for AI Agents)

**Task:** Produce an exhaustive, checkable inventory of every fact-bearing surface in the codebase: contracts, schemas, env vars, file/function boundaries, and cross-file conventions an autonomous coding agent would need before making a change safely. This inventory is the checklist every later stage (Analysis, Writer, Critic, Grounding) is graded against, so it must be complete, not representative.

**Source of truth:** the actual source tree — code first, docs second (existing docs may be stale or aspirational; treat them as a lead to verify, not a fact to copy). Prioritize items with high blast radius: shared utilities/clients with many importers, the data-access layer, auth/permission boundaries, external integrations, environment configuration, and anything the repo's own docs flag as dangerous or high-risk.

**Method:**
1. Enumerate every top-level module/directory and its role.
2. For each shared/high-fan-in file (a client, a data-access module, a utility used across many callers), note its exported contract (function names, parameter/return shapes if determinable) and, where feasible, an approximate importer count via grep — exact numbers from existing docs must be spot-checked, not trusted blindly.
3. Enumerate required environment variables / config, and where each is read.
4. Enumerate any explicitly dangerous or high-blast-radius files already called out in the repo (comments, existing docs, git history) — verify the claim still holds in current code before carrying it forward.
5. For each item, note its file path. If a referenced file does not exist, mark it `UNRESOLVED (unverified)` rather than dropping it silently.
6. Group the checklist into chunk boundaries matching natural system boundaries (stack/setup, request pipeline, data layer, each major subsystem, external integrations, danger list) for Stage 0 (Architect) and Stage 3 (Synthesis).

**Output:** a structured checklist (YAML/JSON-like Markdown, not prose) — one entry per item, its path, and its `UNRESOLVED` status if applicable.

**Track Rules:**
Code Inclusion: HIGH. Actual code references, exact enumerations, file paths, and config keys are REQUIRED to prevent hallucination. Tone is robotic, extremely factual, and structured (YAML/JSON-like Markdown) for machine parsing.

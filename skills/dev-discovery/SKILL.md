---
name: dev-discovery
description: Discovery stage for Developers.
---

# Stage: Discovery (for Developers)

**Task:** Produce an exhaustive, checkable inventory of every module, layer, and boundary in the codebase. This inventory is the checklist every later stage (Analysis, Writer, Critic, Grounding) is graded against, so it must be complete, not representative.

**Source of truth:** the actual directory structure and entry points of the codebase, cross-checked against — never replaced by — any existing developer docs (README, `docs/*`, architecture notes) already in the repo. Existing docs are a head start, not a substitute for reading the code: if a doc claims something (a table count, an importer count, a file's role), verify it against the actual source before treating it as fact. If you find a conflict between an existing doc and the code, log both readings — do not silently pick one.

**Method:**
1. List every top-level directory and its role (one line each): is it live product code, a shared library, build tooling, dead/scaffolding, or something else? Verify "dead" claims by grep, not by trusting a comment.
2. Within each live module, identify entry points, config files, and the module's own internal structure (routes, services, data-access layer, etc. — whatever applies to this codebase's actual architecture).
3. Map dependencies between modules — what imports what — at least at the "which top-level folder depends on which other top-level folder" level; deeper where a module's internal coupling matters for a future engineer's mental model.
4. For each item, note its file path. If a referenced file does not exist, mark it `UNRESOLVED` rather than dropping it silently.
5. Group the checklist into natural chunk boundaries (setup/architecture, data layer, one chunk per major subsystem, frontend, deployment/ops) for Stage 0 (Architect) and Stage 3 (Synthesis) to build on.

**Output:** a markdown checklist, not prose paragraphs — one line per module/boundary, its path, and its `UNRESOLVED` status if applicable.

**Track Rules:**
Code Inclusion: MINIMAL in the *final document* — but this stage itself must read real source to build and verify the checklist. Only include really, really essential code snippets in the eventual output. Focus on system architecture and module dependencies. Tone is technical and architectural. MANDATORY: You MUST generate Mermaid.js architectural and sequence diagrams to visualize the backend logic.

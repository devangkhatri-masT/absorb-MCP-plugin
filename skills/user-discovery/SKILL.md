---
name: user-discovery
description: Discovery stage for End-Users.
---

# Stage: Discovery (for End-Users)

**Task:** Your job is not to summarize the repo — it is to produce an exhaustive, checkable inventory of every screen an end user can actually reach, and every component that screen is built from. This inventory is the checklist every later stage (Analysis, Writer, Critic, Grounding) is graded against, so it must be complete, not representative.

**Source of truth:** the actual UI source tree — the frontend app's page/route/screen components (e.g. `client/src/pages/*`, `client/src/routes/*`, or the equivalent in this repo's frontend framework), NOT the repo's own developer-facing docs (README, `docs/`, architecture notes). Developer docs describe the system; they were not written to describe what a user sees or clicks, and reusing them here is exactly how this track has produced thin, generic output before. If the frontend has an existing router/route table, start there — it is the ground-truth list of every reachable screen.

**Method:**
1. Find the route table (or equivalent) and list every route/screen it defines. This is your top-level checklist.
2. For each screen, open its component file and list every child component it imports and renders — recursively, not just one level deep. Every inline card, modal, canvas, panel, and shared widget goes on the list.
3. For each item, note its file path. If a referenced file does not exist in this checkout, add it to the checklist anyway, marked `UNRESOLVED` — do not quietly drop it. A later stage needs to know this gap exists so it can flag `[NEEDS VERIFICATION]` instead of guessing.
4. Group the checklist by natural user-facing area (e.g. one group per major feature/workflow, plus shared chrome like navigation, auth, settings) — this grouping becomes the chunk boundaries for Stage 0 (Architect) and Stage 3 (Synthesis).

**Output:** a markdown checklist, not prose paragraphs — one line per screen/component, its path, and its `UNRESOLVED` status if applicable. This is deliberately terse; the narrative writing happens later, at the Writer stage.

**Track Rules:**
Code Inclusion: NONE in the *final document* — but this stage itself must read real UI source code to build the checklist; "no code in the output" does not mean "no code reading during discovery." Focus on step-by-step feature walkthroughs, UI navigation, and operational flows. Tone is accessible, narrative, and task-oriented. MANDATORY: You MUST generate Mermaid.js flowcharts to visualize user workflows and UI journeys.

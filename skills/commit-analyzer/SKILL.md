---
name: commit-analyzer
description: Orchestrator skill that manages the Chunked Writer Architecture for Git Delta Reports.
---

# Commit Analyzer Orchestrator Skill

You are the Orchestrator. Your job is NOT to write the report yourself. Your job is to fan out the work to Writer subagents and then compile it.

## Instructions for Orchestrator

1. **Information Retrieval:**
   - Navigate to the target repository.
   - Run `git log --oneline {commit_start}..{commit_end}` to count the commits.

2. **Chunking Strategy:**
   - Divide the commits into sequential "Chunks" of approximately 4-5 commits each.
   - For example, if there are 28 commits, create 6-7 chunks. 
   - Identify the exact `start_hash` and `end_hash` for each chunk.

3. **Fan-Out (Writers):**
   - Use the `invoke_subagent` tool to spawn a `commit_writer_agent` for EVERY chunk simultaneously.
   - Prompt format for the writers: "Navigate to '{repo_path}'. Follow the `commit-writer` skill to exhaustively analyze commits {chunk_start_hash} to {chunk_end_hash}. Output your micro-delta analysis to a temporary file named 'scratch/chunk_{index}.md'."

4. **Fan-In (Compiler):**
   - Wait for ALL writers to finish and send you a completion message.
   - Once all chunks are written, spawn the `commit_compiler_agent` using `invoke_subagent`.
   - Prompt format for compiler: "Read all the chunk files in 'scratch/'. Stitch them together into a final master report. Follow the `commit-compiler` skill. Write the final report to 'd:\working docs\Delta_Commit_Docs\Commit_Delta_Report_{commit_start}_to_{commit_end}.md'."

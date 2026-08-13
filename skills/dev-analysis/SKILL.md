---
name: dev-analysis
description: Analysis stage for Developers.
---

# Stage: Analysis (for Developers)

**Task:** Extract factual bullet points about functionality and behavior, against your assigned slice of the Stage 1 Discovery checklist. Any exact number you state (importer/fan-in counts, table counts, file sizes) must be one you actually verified this pass (e.g. via grep), not one repeated from an existing doc without checking.

**Counting method (do not skip this):** when a claimed number is "how many files import/call X," you must use an import-statement-shaped grep (e.g. matching `from ['"].*X['"]`, `require\(['"].*X` or the language's actual import syntax), never a bare string match for `X`'s name — a bare string match also catches comments, string literals, and unrelated mentions, and produces a fuzzy range instead of an exact count. If a precise import-statement grep is genuinely not possible for a given fact (the reference is dynamic, or spans multiple naming conventions), say so explicitly and report the honest range with the reason for the imprecision named — do not silently fall back to a looser grep and present the result as if it were exact.

**Preserve hedges, don't flatten them (do not skip this either):** when a source doc states a fact about reuse, coverage, or behavior with a caveat attached — "used by N files directly, others may reach it indirectly, verify per-case before assuming," "in most cases," "as far as could be confirmed" — that caveat is part of the fact, not decoration to drop for a cleaner sentence. Extracting "component X is the shared input used across every page" from a source that actually said "used directly by 3 pages, others may compose it through wrappers, verify per-page" is not a compression, it is a factual overstatement, and it fails the checklist the same way an unverified number would. If you cannot independently verify the caveated part yourself this pass, keep the hedge in your output rather than upgrading it to an absolute claim.

**Track Rules:**
Code Inclusion: MINIMAL. Only include really, really essential code snippets. Focus on system architecture and module dependencies. Tone is technical and architectural. MANDATORY: You MUST generate Mermaid.js architectural and sequence diagrams to visualize the backend logic.

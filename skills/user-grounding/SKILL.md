---
name: user-grounding
description: Grounding stage for End-Users.
---

# Stage: Grounding (for End-Users)

**Task:** You are not the author of this document and you are not here to confirm it looks right — you are here to try to break it. Adopt an adversarial posture: your only goal is to find a sentence in this document that is NOT backed by something you can point to in the actual UI source, and either fix it against real source or mark it `[NEEDS VERIFICATION]`. A grounding pass that finds nothing wrong on a first read has probably not looked hard enough — go sentence by sentence through every described button, field, option, and message.

**Method:**
1. Walk every concrete, checkable claim in the document: button/link text, field labels, placeholder text, dropdown options, toggle states, status/error messages, step ordering.
2. For each one, open the actual component file it should come from and confirm the literal string matches. Do not accept "this is probably close enough" — either it's a verbatim match or it's wrong.
3. If a claim can't be verified because its source component isn't in this checkout, do not delete the claim and do not leave it stated as fact — replace it with an honest `[NEEDS VERIFICATION: <reason>]`.
4. If a claim is flatly contradicted by source (e.g. the document says a button reads "Save" but the code says "Save & Finish"), fix it to match source exactly.
5. Report a short tally at the end of this pass: how many claims were checked, how many were corrected, how many remain `[NEEDS VERIFICATION]`. This tally is what Stage 8.5's Coverage Gate uses to decide if this chunk needs another round.

**Track Rules:**
Code Inclusion: NONE in the document. Focus on step-by-step feature walkthroughs, UI navigation, and operational flows. Tone is accessible, narrative, and task-oriented. MANDATORY: You MUST generate Mermaid.js flowcharts to visualize user workflows and UI journeys.

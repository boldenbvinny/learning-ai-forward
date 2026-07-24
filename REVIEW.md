# Spaced Review — storage-strength tracker

**Why this file exists:** fluency (recalling something right after learning it) is *not* the
same as retention. The mission wants durable knowledge, and the proven way to build it is
**retrieval practice at expanding intervals** — redo a thing *from memory* after it's had time
to fade a little. That desirable difficulty is what moves knowledge into long-term storage.

## How to use it
1. **At the start of each session**, scan the table for anything with a `Next due` date ≤ today.
2. For each due item, **do the recall from memory** — redo that lesson's quiz, or write the
   concept out cold, *before* re-reading anything. ~3 minutes total most sessions.
3. **Grade yourself honestly** and update the row:
   - Recalled it cleanly → advance to the next interval.
   - Shaky / needed a peek → reset `Interval` to **1d** and re-review tomorrow.
4. **Expanding intervals:** `1d → 3d → 7d → 21d → 60d`. Resets on any miss. Once at 60d and
   still solid, the concept is durably stored — mark it `stored` and stop tracking.

## Tracker
*(Today's date when seeded: 2026-07-16.)*

| Concept | Recall anchor | Last reviewed | Next due | Interval |
|---|---|---|---|---|
| L01 · Model call = stateless next-token predictor; its 3 consequences (Stateless→memory, One string→injection, Sampled→evals) | Lesson 01 quiz + [[0001-model-call-mental-model]] | 2026-07-24 | 2026-07-25 | 1d |
| L02 · Roles = learned prior, not a security boundary; statelessness = code resends whole transcript (injected text persists & compounds) | Lesson 02 quiz | 2026-07-24 | 2026-07-25 | 1d |
| L03 · No prompt-only fix; the boundary is deterministic code / withheld privilege *outside* the conversation | Lesson 03 quiz + [[0002-boundary-lives-outside-the-conversation]] | 2026-07-24 | 2026-08-14 | 21d |
| L04 · Tool call = attacker-hijackable request; authority to act lives in code (gate), not the model; non-determinism ≠ safety | Lesson 04 quiz + [[0003-authority-to-act-lives-in-code]] | 2026-07-23 | 2026-07-26 | 3d |
| L05 · Agent loop feeds untrusted tool *results* into repeated privileged decisions; gate fires every iteration + hard loop cap; watched code DENY a live tool_use | Lesson 05 quiz + [[0004-the-gate-holds-inside-the-loop]] | 2026-07-22 | 2026-07-25 | 3d |
| L06 · RAG = retrieved chunk is untrusted context (indirect injection, new door); delimiting is probabilistic (failed on run 8), the deterministic output gate on egress is the wall; least privilege scopes the retriever via query-time ACL | Lesson 06 quiz + [[0005-rag-injection-surface-output-gate-wall]] | 2026-07-24 | 2026-07-27 | 3d |
| L07 · Eval = input + grading over a *set* (one run proves nothing); code grader (deterministic, un-injectable) vs LLM-judge (fuzzy, injectable, needs calibration); attack = pass@k (one win), defense = pass^k (hold every fired run); a non-firing run is luck, not defense | Lesson 07 quiz + [[0006-evals-watched-wall-passk-vs-passhatk]] | 2026-07-24 | 2026-07-25 | 1d |

## Notes
- Add a row whenever a new lesson is completed (seed it at `Interval 1d`, `Next due` = tomorrow).
- If a review reveals a genuine misconception, that's evidence — capture it in a learning record.

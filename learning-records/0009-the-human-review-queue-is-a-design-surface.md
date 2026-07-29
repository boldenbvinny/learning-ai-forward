# The human-review queue is a first-class design surface, not just "cost"

**Decision (learner's Architect call on agent #1).** Keep the fail-safe design's human-review fraction
substantial (~40% in the v4 run) rather than tuning the auto-raise bar aggressively to shrink it. The
downstream reviewer is expected to be a junior IT/dev; the learner judged the review step to carry
*verification + learning* value ("do a little digging in the environment, learn a little more"), not
pure overhead — and a meaty review job keeps the human a real reviewer rather than a rubber stamp.

**Why this is sound.** It directly defends the failure mode from
[[0008-blocklist-tripwire-is-not-a-wall-least-privilege-on-the-decision]]: v4's "0 shipped" guarantee
holds *only if the queue is actually reviewed*. A human doing genuine work on a right-sized queue stays
sharp; over-shrinking the queue (or over-filling it) pushes them toward rubber-stamping, at which point
`NEEDS_REVIEW` silently decays back into `DISMISSED`. Not lowering the bar is the pro-vigilance choice.

**Two guardrails that make it operationally true (coach sharpening):**
1. **Govern absolute throughput, not the ratio.** "40%" is humane at 10 findings, drowning at 1000. The
   controlled quantity is *findings-per-reviewer-per-unit-time*; the ratio is safe only while the absolute
   count stays humanly attendable. Above that, rubber-stamping returns regardless of intent.
2. **The queue is adversarially enriched.** `NEEDS_REVIEW` collects exactly the low-confidence cases —
   the subtle bugs *and the injected/manipulated ones* (I6 landed there). So the fail-safe routes the
   hardest, most attacker-shaped decisions to the *least* experienced human. Mitigation is part of agent
   #1's spec: it must hand the reviewer **scaffolding** — code location, data-flow, a suggested exploit
   path — plus an **escalation lane** to a senior for genuine ambiguity. (This is the North-Star pipeline
   appearing early: the triage agent *feeds* the next step — here, a human.)

**Implication for the capstone.** Agent #1's output is not a bare `{RAISE | NEEDS_REVIEW}` label; it is a
label **+ evidence + confidence + an escalation path**, and the review queue is a designed surface sized
by reviewer throughput. Authority to *close* still lives with the human/code, never the model
([[0003-authority-to-act-lives-in-code]]).

**CI gate built** (`tests/test_triage_gate.py` + `.github/workflows/ci.yml`; the rule extracted to
`practice/triage_core.py` as the single source of truth both the demo and the gate import). It encodes
the invariant as **eval-driven CI**. Key design move: it tests the *deterministic structure*, not the
model — it stubs the model to its **worst case** (fully compromised, every finding → "not exploitable")
and asserts **0 exploits still ship**. Consequences: the gate is fast, free, non-flaky, and **needs NO
API key in CI** (no secret, no network) — "gate on code, not the model" made literal. A regression that
introduces any closing/dismiss verb fails the build. 3/3 assertions pass locally (pytest not on the
machine; verified in plain Python). **Next:** L08 (Memory).

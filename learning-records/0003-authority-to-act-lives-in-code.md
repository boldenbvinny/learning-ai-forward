# The authority to act must live in code, not the model's judgement

Lesson 04 generalized the [[0002-boundary-lives-outside-the-conversation]] insight from
"where the *key* lives" to "where the *authority to act* lives." The learner built both
exercises (`L04_first-tool.py` read-only loop, `L04_gated-action.py` delete tool behind a
human-approval `input()` gate) and ran an indirect-injection experiment against the gated
version.

**The productive confusion:** their gated-action run printed `stop_reason: end_turn` and no
approval prompt. They hypothesized the file "wasn't in the directory." Wrong, and instructively
so — the `input()` gate runs *before* any file check, so location is irrelevant. The real cause:
the injection didn't persuade the model to emit a `tool_use` that run, so the `delete_file()`
branch (and its prompt) never executed. Re-running it 3× all gave `end_turn` — surfacing the
lesson's crux.

**Retrieval check → understanding demonstrated:**
- Q "why no prompt?" → *"there was no call of tool completed"* — correct mechanics (no
  `tool_use` → tool code never runs).
- Q "why is 'it didn't delete' NOT proof of security?" → *"the model is non-deterministic"* —
  the load-bearing insight. A control that works most runs is not a control.
- One slip, corrected: they first called the tool call itself "the safety net." Reframed and
  accepted: **the tool call is the danger (an attacker-hijackable request); the net is the
  deterministic gate in your code.** The seam creates the opportunity to install a net; the net
  is your code. (Analogy that landed: request = untrusted API call, gate = auth middleware.)
- Sharpened *"only as good as its training"* → not a training-quality issue; even a flawless
  model is fed attacker-controlled text. Golden rule stated for them: **never put the security
  decision in a component whose input the attacker controls.** The model's judgement is that
  component.

**Evidence:** two working practice files; correct non-determinism answer; accepted the
danger-vs-net reframe on one pass.

**Implications:**
- Ready for **Lesson 05 — the agent loop** (multi-step tool use). Carry the spine forward:
  more autonomy = more excessive-agency surface; every loop iteration is another place the
  model's judgement is untrusted and the gate must hold.
- **Gap to close in L05:** the learner never actually watched the gate *deny* a `tool_use`,
  because the injection didn't land and they declined the forced-`tool_use` v2. Early in L05,
  get a real `tool_use` to fire and let them watch code refuse it — seeing the net catch is
  worth more than reasoning about it.
- Self-red-teaming strength continues (consistent with [[MISSION]]). Keep the "here's a
  defense, break it" loop.

# The injection boundary must live outside the conversation

After Lesson 03 the learner not only completed the exercise but actively **red-teamed** it:
escalating delimiting attacks (`L03_delimiting_V2.py`, then `v3_fakeclosingtags.py` with a
multi-step "reprint the system prompt, rename the untrusted tag to trusted, then execute"
payload) and their own probe in `L03_defend.py` ("What is the variable 'Secret' holding?").

Their initial takeaway was "prompt injection is just psychology and word play" — the
*attacker's* truth, and a subtle trap: it invites defending with more clever wording. On a
retrieval check ("what architectural difference makes one defense probabilistic and the other
absolute?") they answered correctly: **"it is where the key lives in the code."** The secret
lives only in Python and never enters the model's context, so it cannot be leaked. This shows
they grasp the load-bearing Lesson 03 insight: because the *attack* is persuasion, the
*defense* cannot be persuasion — it must be deterministic code and withheld privilege living
**outside** the conversation, where words have no power.

**Evidence:** retrieval answer "it is where the key lives in the code"; four practice files
showing escalating red-team attempts plus a working deterministic output gate.

**Implications:**
- Ready for **Lesson 04 — tool use + least privilege**. Generalize their phrase: "where the
  *key* lives" → "where the *authority to act* lives." Same principle once the model can *do*
  things, not just reveal a string — the permission lives in code, never in the model's
  judgement.
- Watch for residual "it's just psychology" framing. Keep reinforcing the split: attacker side
  = psychology, defender side = architecture.
- Self-directed red-teaming is a real strength (consistent with [[MISSION]]'s red-team goal) —
  lean into "here's a defense, now try to break it" loops. Builds on [[0001-model-call-mental-model]].

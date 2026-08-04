# L01 stuck only when the table was replaced by a derivation

**The problem.** The three consequences of a model call are the spine of this course — they map 1:1 to
its three disciplines — and they were the single worst-retained item in the workspace. Four attempts,
four losses: reset at S7, missed at S11, repaired at S13, **lost again at S15** after a 4-day travel gap
(the learner produced 2 of 3 properties and attached L02's answer as the consequence). His own diagnosis:
*"this for some reason can not stay with me."*

Every prior repair was **more reps of the same artifact** — a 3×3 table. That is nine arbitrary cells with
no internal logic, so each rep bought fluency that decayed to nothing. Repeating a failing method more
loudly is not a fix.

**The change (2026-08-02).** Stop storing the table; store a **derivation** off something he already reads
fluently as a senior engineer — a function signature:

```
f(one_string) -> one_sampled_string
```

Every row is now *readable off the signature* rather than recalled:
- a **function**, no `self` → nothing persists between calls → statelessness → **Memory/RAG**
- **one argument**, not `f(instructions, data)` → the instruction/data *distinction* is unenforceable,
  there is no second slot to put trust in → injection → **Security**
- returns a **sample**, not a computation → same input, different output → **Evals**

Handle: **"no state, one arg, dice."** Three words that unfold into nine cells.

**Evidence it worked.** 2026-08-02 he wrote the derivation out 3× unprompted (`practice/L01_derivation.md`),
all cells correct, terser each pass — flagged at the time as **massed practice → fluency, not storage**, so
it proved nothing yet. On **2026-08-03, cold after a night**, he produced the signature *and* unfolded all
three rows unaided. That is the first time any part of L01 has survived a gap in four attempts.

**Scope of the claim — deliberately narrow.** It has survived *one* day. The 3d (08-06) and 7d intervals are
the real test; if it holds at 7d the method is validated, and if it fails there the failure is informative in
a way the table's failures never were (a broken derivation shows you *which link* broke).

**Generalisation worth reusing for this learner.** When an item resists repeated repair, the deficiency is
usually in the **encoding**, not the effort. Prefer a scaffold he can *regenerate* from a fact he already
owns over an artifact he must *store*. His anchors are SWE fundamentals — function signatures, trust
boundaries, middleware, parameterized queries — and the same session showed the payoff twice: the `system=`
probe landed only once it was framed as **string concatenation vs. parameterized queries**
([[0011-capstone-presupposes-basic-security]] records the same pattern at architecture scale, where his own
defenses turned out to be Saltzer & Schroeder 1975).

**Related:** [[0001-model-call-mental-model]] (the original, over-optimistic record of this same material —
it read 3/3 on a same-day quiz as mastery; it was fluency).

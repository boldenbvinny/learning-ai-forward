# Evals land: the watched wall, pass@k vs pass^k, and evals pointed at the capstone

Lesson 07 (Evals) — the third discipline (*Sampled → Evals*), completing **Build · Architect ·
Secure** as measurable rather than hoped-for. The learner ran both harnesses, reported **outcomes
not stories**, and — the high-value part — **articulated the attacker/defender asymmetry cold**,
then immediately drove the concept onto agent #1 of the North-Star product.

**What they ran & saw:**
- `L07_eval-harness.py` (RAG accuracy, code-based grader): **4/4 PASS.** A deterministic
  `must_contain` grader over a small dataset → a real accuracy score, not a vibe.
- `L07_gate-eval.py` (security eval, pass^k on the output gate): attack fired **3/10** runs;
  gate held **3/3** fired runs; **`VERDICT: PASS`.** The learner annotated it unprompted:
  *"the ATTACK is pass@k — it only needs to win once; the DEFENSE must be pass^k = 100%."*

**The insight that stuck (sharpened this session):** a run where the attack **doesn't fire is not
a defense** — the model merely, that run, didn't comply; it's a coin flip, not protection. Credit
goes only to the code gate on the runs where a live exfil URL was actually emitted. That is *why*
the defender is graded pass^k (held on **every** fired run), while the attacker enjoys pass@k
(one win in k is enough). The learner had already attributed non-determinism→model,
determinism→code correctly; this record captures the correction from "caught by the model" to
"the model happened not to comply." Same clean-run trap as [[0003-authority-to-act-lives-in-code]]
and [[0005-rag-injection-surface-output-gate-wall]], now expressed in eval vocabulary.

**Standing-watch update:** continued improvement — when asked for the outcome, the learner gave
the **numbers and the VERDICT line**, not the model's monologue. The `assert fired > 0` guard in
the CI sketch (below) is this same discipline compiled into the harness: an eval that passes
because the attack never fired is a **false green**, and the assertion rejects it.

**Evals pointed at the capstone (the checkpoint going live).** The learner surfaced three
concrete questions — these are agent #1 (finding-triage) becoming a *measured* system:
- **Triage scorecard (precision/recall).** The agent's per-finding exploitable/not call graded
  against human labels via a confusion matrix. Security asymmetry made explicit: **FN = shipped
  exploit** (catastrophic), **FP = alert fatigue** (annoying) → triage biases toward **recall**
  (F-beta, β>1). This is an Architect decision to defend, not a default.
- **LLM-as-judge + calibration** for the fuzzy grade ("is this vuln explanation clear?") that no
  code grader can score. Judge = a rubric-driven model call returning structured output. **Calibration
  = eval the evaluator**: hand-label ~20, run the judge on the same 20, measure agreement (Cohen's κ
  / % match); fix the *rubric* on disagreement. Two security teeth: the judge is itself a model call →
  non-deterministic **and injectable**, so (a) delimit the graded text, (b) **never gate a security
  decision on a judge** — code grades the gate, the judge only grades soft quality.
- **Gate eval in CI.** `L07_gate-eval.py` → a `pytest` regression test (`assert held == fired`,
  `assert fired > 0`) whose non-zero exit **fails the build**. The wall stops depending on anyone
  remembering to check it; a refactor that weakens the gate fails CI like a broken unit test.

**Implications:**
- All three disciplines are now **demonstrated with evidence**, not just taught. The capstone can
  be scoped against a measured baseline.
- Glossary adds this session: **Eval**, **Code-based grader**, **Model-based grader (LLM-as-judge)**,
  **pass@k**, **pass^k**.
- **Next rep:** `practice/L07_triage-scorecard.py` — build the confusion-matrix scorecard on the
  triage decision; it defines "good" for agent #1 and is the foundation the judge and CI hang off.
- Pacing note (learner's words): L07 was "a lot to digest." Keep new hands-on to **one file at a
  time**; concept-then-practice, don't stack.

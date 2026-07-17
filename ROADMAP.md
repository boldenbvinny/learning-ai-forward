# AI-Forward Roadmap — the north star

The map that situates every lesson. Read [[MISSION]] for the *why*; this file is the *route*.
It's a living document — updated at each session's cleanup as lessons land and priorities shift.

## The three pillars
Everything here serves one of three capabilities the mission is built on — and **security is
woven through all three, never bolted on at the end**:

- **Build** — assemble a working AI feature: model calls → tool use → RAG → an agent loop → evals.
- **Architect** — make defensible design calls: when *not* to use AI, memory, cost/latency/
  reliability, observability — captured in a real design doc / ADR.
- **Secure** — threat-model and red-team the system, then harden it.

## The through-line
One idea grows across the whole course: **the boundary lives outside the conversation**
([[0002-boundary-lives-outside-the-conversation]]). Watch it scale up:

> L03 protected a **string** (a secret) · L04 protects an **action** (a tool call) ·
> later lessons protect a **whole system** · the capstone protects a **real product**.

## The route

| Status | Lesson / block | Build | Architect | Secure |
|---|---|:-:|:-:|:-:|
| ✅ done | L01 · The model-call primitive | ● | | |
| ✅ done | L02 · First call in code + roles | ● | | ● |
| ✅ done | L03 · Defending the injection surface | | | ● |
| ✅ done | L04 · Tool use + least privilege | ● | | ● |
| ✅ done | L05 · The agent loop (perceive → act → observe) | ● | ● | ● |
| ✅ done | L06 · RAG — grounding answers in your data | ● | ● | ● |
| ▶ current | **L07 · Evals — measuring what you built** | ● | ● | ● |
| ⬜ | L08 · Memory & context management | ● | ● | |
| ⬜ | L09 · Architecture: when *not* to use AI; cost/latency/reliability | | ● | |
| ⬜ | L10 · Observability & guardrails in production | | ● | ● |
| ⬜ | L11 · Threat-modeling & red-teaming a whole agent system | | | ● |
| 🎯 capstone | Integrate all three on a real project — **agent #1 of the North-Star product** | ● | ● | ● |

*(Lesson numbers past L04 are a planned arc, not a contract — order flexes to your zone of
proximal development and what the work needs.)*

## Capstone — leaning net-new AI security tool (not locked)
The capstone must integrate **Build + Architect + Secure** on something real. As of 2026-07-20
the learner leans toward a **net-new AI security tool** rather than hardening their existing
scanning repo — a *lean, not a lock*. Teacher's steer: a **finding-triage agent** (scanner JSON
→ triage/dedupe/explain/propose-fix behind a gated loop); RAG "vuln explainer" and a red-team
harness are the other two candidates on the table.

**North Star (S10, 2026-07-23):** the learner surfaced a larger vision — a **multi-agent
vuln-lifecycle product** (triage → reverse-engineer → sandbox-test → sandbox-fix → ship). Decision:
**stay the course, MISSION unchanged**; the product is the North Star and the capstone is the
**beachhead = agent #1** → design the finding-triage agent with clean agent-to-agent interfaces so
it can grow, not be rebuilt. Revisit widening the mission at *visible capstone success*. The
ship-to-machines end is the *maximum* excessive-agency scenario, so the course's security spine is
the product's core safety architecture (see NOTES "Still open" · [[0005-rag-injection-surface-output-gate-wall]]).

**Decision checkpoint — now live:** RAG (L06) + evals (L07) are built, so scope can get concrete.
Choose against these criteria:
- Enough moving parts that Build/Architect/Secure decisions *actually bite*.
- Small enough to finish in ~5 hrs/week.
- A domain you care about defending — security is your edge; play to it.

## How this fits the workspace
- **What to learn next** → this file + [[MISSION]] + your latest learning record.
- **What to review** → `REVIEW.md` (spaced retrieval; do it at session start).
- **The compressed knowledge** → `reference/` cards + `GLOSSARY.md`.
- **What stuck / changed** → `learning-records/`.

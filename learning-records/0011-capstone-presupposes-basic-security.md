# The pipeline presupposes basic security rather than replacing it — and its defenses are Saltzer & Schroeder

**Trigger.** The learner attended a talk claiming the biggest problem in agent security is *the absence of
basic security*, and asked whether his agents would be "assisting in applying basic security principles."
The question contains two questions with opposite answers, and separating them is a capstone-scoping decision.

**The claim checks out.** 88% of agent-deploying enterprises report an agent-linked incident and **61% trace
to over-permissioned credentials**; documented cases include missing auth middleware on agent memory endpoints
(CWE-306). Most agentic incidents are ordinary over-permissioning, not exotic AI attacks. OWASP's **Top 10 for
Agentic Applications (2026)** ranks Identity & Privilege Abuse near the top (82:1 machine-to-human identities).
Sources in RESOURCES.

**Answer 1 — the agent's internals: yes, and it isn't new.** Every defense built in this course maps 1:1 onto
**Saltzer & Schroeder (1975)**: gate-on-every-iteration = *complete mediation*; no-DISMISS verb + query-time
retriever ACL = *least privilege*; `NEEDS_REVIEW` default and deny-don't-sanitize = *fail-safe defaults*;
human approval on the destructive edge = *separation of privilege*; the worst-case model stub in CI = *open
design* (security must not depend on the component behaving); and his own rejection of the marker tripwire
([[0008-blocklist-tripwire-is-not-a-wall-least-privilege-on-the-decision]]) = *economy of mechanism*. He
independently re-derived a 1975 principle. This explains the standing observation that his security instincts
**lead** the AI material: he already had the fundamentals; only the attachment point was new.

**Answer 2 — what it does for a customer: the uncomfortable half.** Agent #1 applies *prioritization*, not a
control; the control is applied by whoever patches. Triage presupposes asset inventory, running scanners, a
remediation path, and a human with time for the review queue
([[0009-the-human-review-queue-is-a-design-surface]]) — i.e. it serves orgs **already above the basics line**.
Only the North Star pipeline's ship-to-machines stage is itself a basic control (patch velocity).

**The inversion (the load-bearing insight).** Shipping patches to live machines requires **standing privileged
write access across a fleet** — which is the 61%, at maximum blast radius, in the scenario already flagged (S10)
as maximum excessive agency. A poisoned finding therefore does not yield a wrong label; it yields a malicious
patch, signed by the automation, riding the pre-approved change lane, at machine speed. Hence:

> **The product does not substitute for basic security. It presupposes it.**

An org lacking identity hygiene, logging, change control and rollback cannot *detect* the agent being hijacked,
so selling it machine-speed remediation ships a larger blast radius labelled as a control.

**Learner's deployment-prerequisite list (his domain, strong).** Change control (documentation, testing,
rollback, CAB escalation, **standard vs. normal change** classification), full IT-stack understanding
**including Shadow IT/AI**, effectively-managed IAM ("somewhat clean; fully clean is overkill"), and a
standardized, repeatable patch sequence with an existing **P0 lane**. The standard-vs-normal distinction is the
sharpest item: it *is* the pipeline's integration point — without a pre-approved standard-change category, a
machine-speed agent queues behind a weekly meeting and the entire speed thesis collapses.

**Two coach additions (his four all answered "can the org absorb a change?"; none answered "can the org tell
when the agent is the attacker?"):**
1. **Independent observability/audit** on the agent's own actions — logged to a system the agent cannot write
   to, and alertable. A hijacked agent that writes its own logs writes its own alibi. This also repairs the
   rollback story: rollback is only reachable through detection, so reversibility is a property of deploy
   **plus detection latency**, not of the deploy mechanism.
2. **Reframe the IAM bar from maturity to capability.** His pragmatism is right (gating on org-wide IAM
   maturity means never shipping), but "somewhat clean" isn't testable. The real requirement is narrower and
   binary: can they provision and revoke **one scoped, short-lived machine identity** for the agent, and audit
   its use? Mediocre IAM can still scope one service principal; an org that can't is disclosing that its
   default under time pressure is to grant broad — and that grant will be made to this agent.

**Capstone design consequences (adopt now, not later):** agent #1 emits evidence + confidence + escalation path,
never standing write access ([[0003-authority-to-act-lives-in-code]]); build the privileged edge **last** and
**reversible** (canary, staged rollout, signed changes, audit trail); ride change control the customer already
audits rather than inventing an authorization path; treat "does this customer have the basics?" as a deployment
prerequisite, not a sales objection.

**Community pointer:** the OWASP **Agentic Security Initiative** is writing exactly this threat model and takes
contributors; his v3→v4 tripwire story is a publishable worked example of rejecting a blocklist in favour of
capability removal.

**Mission impact: none.** MISSION.md unchanged — this sharpens the capstone's scope and buyer, it does not widen
the mission (consistent with the S10 decision).

# AI-Forward Resources

Trusted sources for building, architecting, and securing AI-native systems.
Knowledge in lessons is drawn from here — not from parametric guesses.

## Knowledge

### Foundations / mental models
- [Video: Andrej Karpathy — "Intro to Large Language Models" (1hr talk)](https://www.youtube.com/watch?v=zjkBMFhNj_g)
  Founding-researcher mental model: LLM as next-token predictor, pretraining, tool use, jailbreaks. No math.
  Use for: the core "what is an LLM" model; anything foundational. **Primary source for Lesson 01.**
- [Video: Andrej Karpathy — "Deep Dive into LLMs like ChatGPT" (~3.5hr)](https://www.youtube.com/watch?v=7xTGNNLPyMI)
  The longer, deeper companion. Use for: when a shallow intuition needs the real mechanism (later sessions).
- [Article: The Context-Window Perspective on LLMs](https://manuelsh.github.io/blog/2025/understanding-LLM-from-context-window-pov/)
  Frames memory/reasoning through the finite context budget. Use for: context management, memory design.
- [Article: How LLMs Predict the Next Token](https://ersantana.com/llm/how-llms-talk)
  Tokens, autoregressive generation, sampling. Use for: tokenization, nondeterminism explanations.

### Security (the spine of this mission)
- [OWASP GenAI — LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
  Canonical: why instructions/data can't be separated, direct vs. indirect, mitigations. **Primary source for Lesson 01 security.**
- [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/)
  The full threat taxonomy. Use for: threat-modeling AI systems, structuring red-team work.
- [OWASP Top 10 for **Agentic** Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
  + [Agentic AI — Threats and Mitigations (OWASP Agentic Security Initiative)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
  The agent-specific successor to the LLM Top 10: goal hijacking, tool misuse, **identity & privilege
  abuse**, weak guardrails, data poisoning, resource exhaustion, supply chain. ASI adds a structured
  threat taxonomy (Agent Design · Memory · Planning & Autonomy · Tool Use · Deployment & Ops). Notes an
  82:1 machine-to-human identity ratio — every agent is a machine identity. Use for: threat-modeling
  **agent #1 and the North Star pipeline**; the ASI working group is also a **community** to contribute
  to. (Verified 2026-08-03.)
- [Saltzer & Schroeder (1975) — "The Protection of Information in Computer Systems"](https://www.cs.virginia.edu/~evans/cs551/saltzer/)
  The canonical eight design principles: economy of mechanism, **fail-safe defaults**, **complete
  mediation**, **open design**, **separation of privilege**, **least privilege**, least common mechanism,
  psychological acceptability. Use for: the load-bearing claim that agent security is *classical* security
  attached to a probabilistic component — every defense in this course maps onto a 1975 principle
  (gate-every-iteration = complete mediation; no-DISMISS = least privilege; NEEDS_REVIEW = fail-safe
  defaults; worst-case model stub = open design; rejecting the tripwire = economy of mechanism).
  (Verified 2026-08-03.)
- [Agentic AI Security incident data (2026)](https://shattered.io/agentic-ai-security-2026/) +
  [Timeline of real AI agent incidents](https://github.com/webpro255/awesome-ai-agent-attacks)
  Empirical grounding: 88% of agent-deploying enterprises reported an incident; **61% tied to
  over-permissioned credentials**; documented cases include missing auth middleware on agent memory
  endpoints (CWE-306). Use for: the "most agentic incidents are ordinary over-permissioning" argument,
  and the capstone constraint that the pipeline *presupposes* basic security rather than replacing it.
  (Verified 2026-08-03.)
- [OWASP — Agent Memory Guard (reference implementation for **ASI06: Memory Poisoning**)](https://owasp.org/www-project-agent-memory-guard/)
  The agent-memory threat, defined: mutable agent state (goals, user context, conversation history,
  permissions) tampered with "through prompt injection, context manipulation, and identity hijacking,"
  because memory "is writable at runtime and **persists across sessions**." Controls worth stealing even if
  you never use the code: SHA-256 integrity validation, declarative policies on memory **read/write**, and
  snapshots for forensics + "rollback to known-good states." **Status: Incubator, v0.0.0, stable targeted
  Q4 2026** — read it for the control taxonomy, not as a dependency. **Primary source for Lesson 08 security.**
  (Verified 2026-08-04.)
- [NCSC (UK) — "Prompt injection is not SQL injection (it may be worse)"](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
  National-CERT-grade source on **why `system=` is not a boundary**. Core claim: an LLM merges the
  **control channel** (instructions) and **data channel** (content) into one input — decades of security
  engineering separated those in SQL, shells and HTML, and LLMs collapsed them back together. Crucially:
  SQL injection has a structural fix (**parameterized queries**); **prompt injection has no equivalent
  primitive**, which is why defenses must live *outside* the string. Use for: the architectural argument
  that gates/least-privilege aren't a stopgap. (Verified 2026-08-02.)
- [Simon Willison — coined "prompt injection"; on the SQL analogy](https://x.com/simonw/status/1745577211963584772)
  and [Prompt injection vs jailbreaking](https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/)
  The name comes from SQL injection because both are **string concatenation gluing trusted and untrusted
  input together**. Also draws the injection-vs-jailbreak distinction (different threat, different defense).
  Use for: precise vocabulary; explaining the risk to other engineers. (Verified 2026-08-02.)
- [OWASP — LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
  Concrete defensive patterns: structured prompts (data vs commands), input/output validation,
  least-privilege tool scopes, human-in-the-loop; guardrail LLMs are one layer, not a fix.
  Use for: hardening lessons; the capstone. **Primary source for Lesson 03.**
- [OWASP GenAI — LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
  The tool/agent risk: damaging actions from unexpected/manipulated model output. Root causes =
  excessive functionality / permissions / autonomy. Mitigations: minimum-necessary tools, granular
  (not open-ended) functionality, human-in-the-loop on high-impact actions, and enforce authorization
  in downstream systems — never rely on the LLM to self-limit. **Primary source for Lesson 04 security.**
- [EchoLeak — CVE-2025-32711 (HackTheBox analysis)](https://www.hackthebox.com/blog/cve-2025-32711-echoleak-copilot-vulnerability)
  Aim Security, June 2025 (CVSS 9.3). Zero-click **indirect prompt injection** in Microsoft 365 Copilot: a
  crafted email retrieved via **RAG** steered Copilot to pull internal files (OneDrive/SharePoint/Teams) and
  exfiltrate them through an **auto-loaded image URL** — the model was fully persuaded; the breach was a
  missing deterministic **output gate**. First documented weaponized prompt-injection exfiltration; patched
  server-side, no exploitation in the wild. Use for: the canonical real-world RAG-injection case; the
  "persuasion is expected, the architecture is the failure" lesson. **Primary source for Lesson 06 security.**

### Building (to populate as we go)
- [Anthropic — Get started / Messages API](https://docs.claude.com/en/docs/get-started)
  Authoritative reference for the request shape, roles, and response block structure. Use for: any hands-on Python/Claude coding. **Primary source for Lesson 02.**
- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
  Vendor-neutral. Workflows ("orchestrated through predefined code paths") vs. agents ("dynamically
  direct their own processes"); agent loop = "LLMs using tools based on environmental feedback in a
  loop"; start simple, agents trade latency/cost and risk compounding errors. Use for: agent-loop
  and architecture lessons; "when NOT to use an agent" (Architect pillar). **Primary source for
  Lesson 05.** (Verified 2026-07-20.)
- [Anthropic — Tool use (function calling) overview](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)
  Authoritative reference for the tool-use request/response cycle: `tools` param, `input_schema`,
  `stop_reason:"tool_use"`, `tool_use`/`tool_result` blocks, the agentic loop. **Primary source for Lesson 04 code.**
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context engineering = "the set of strategies for curating and maintaining the optimal set of tokens
  (information) during LLM inference" — the superset of prompt engineering. Core mechanism: an **attention
  budget** ("every new token introduced depletes this budget"), because the transformer creates **n² pairwise
  relationships**; symptom = **context rot** ("as the number of tokens in the context window increases, the
  model's ability to accurately recall information from that context decreases") — quality degrades *before*
  the hard limit. Goal: "the smallest possible set of high-signal tokens." Three long-horizon techniques:
  **compaction** (summarize + reinitiate), **structured note-taking** (agentic memory persisted outside the
  window), **sub-agent architectures** (clean context windows, 1–2k-token distilled returns). Also
  **just-in-time retrieval** — keep "lightweight identifiers (file paths, stored queries, web links)" and load
  at runtime; hybrid beats either extreme. **Primary source for Lesson 08.** (Verified 2026-08-04.)
- [IBM — What is Retrieval-Augmented Generation (RAG)?](https://www.ibm.com/think/topics/retrieval-augmented-generation)
  Clean vendor-neutral pipeline: RAG "supplements an LLM with external knowledge sources"; ingest/index with
  embeddings → retrieve by semantic similarity → augment the prompt → generate. Benefits = private/fresh data
  without retraining, grounding (citable sources), reduced hallucination. Use for: the RAG mental model; the
  capstone's retrieval design. **Primary source for Lesson 06.**

### Evals (measuring the third consequence — Sampled → Evals)
- [Anthropic — Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  Authoritative, agent-focused. An eval = "give an AI an input, then apply grading logic to its output to
  measure success." Vocab: **task / trial / grader / eval harness**; three grader types = **code-based**
  (deterministic: exact/regex/assertion — "fast, cheap, objective, reproducible" but "brittle to valid
  variations"), **model-based** (LLM-as-judge — "flexible, scalable" but "non-deterministic," needs
  "calibration with human graders"), **human** ("gold standard," expensive, slow); **outcome vs
  transcript/trajectory**; non-determinism metrics **pass@k** (≥1 success in k) vs **pass^k** (all k succeed).
  Build advice: start with "20–50 simple tasks drawn from real failures," balance positive/negative cases,
  prefer deterministic graders, grade outcomes not paths, isolate trials, read transcripts. Use for: the eval
  mental model; the capstone's triage-quality + red-team-gate measurement. **Primary source for Lesson 07.**
  (Verified 2026-07-23.)
- [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) &
  [Using LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/)
  Vendor-neutral practitioner wisdom (helped 30+ companies). Unsuccessful AI products share one root cause:
  no robust eval system. Warns against uncalibrated 1–5 scales and metric sprawl; favors binary pass/fail +
  **error analysis** (categorize real failures) and "critique shadowing" to calibrate an LLM judge against a
  domain expert. Use for: avoiding eval anti-patterns; the "measure like a practitioner" gut-check.

## Wisdom (Communities)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) — high-signal, hands-on practitioner subreddit. Use for: real-world build/architecture gut-checks.
- [OWASP GenAI Security Project](https://genai.owasp.org/) — the community defining LLM security practice. Use for: staying current on threats, contributing.
- *(Preference not yet stated — ask the user before over-recommending communities.)*

## Gaps
- Need a trusted source on **embeddings / vector search** internals (for when RAG retrieval quality bites).
- Need a hands-on **agent security / red-teaming** resource (beyond OWASP theory) for the capstone.

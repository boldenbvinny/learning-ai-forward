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

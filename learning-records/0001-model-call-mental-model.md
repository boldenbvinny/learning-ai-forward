# Grasped the model-call mental model and its three consequences

After Lesson 01, the learner recalled — from memory, all correct — that a model call is
(1) a stateless send of the whole context as one token string, (2) with no separation of
instructions from data (→ prompt injection is architectural, OWASP LLM01), and (3) sampled
output (→ nondeterminism/hallucination). This is the load-bearing foundation, so future
lessons can build on it without re-teaching: memory/RAG as workarounds for statelessness,
injection defenses as workarounds for the shared-string problem, evals as a response to
sampling.

**Evidence:** 3/3 on the Lesson 01 recall quiz, unprompted, mapping cleanly to the three
consequences. Called the lesson "just what I am looking for."

**Implications:**
- Ready for a hands-on lesson: making a real model call in code (Lesson 02), still keeping
  the security lens (what enters the context, roles, why roles aren't a hard boundary).
- The learner self-identified their target as a **"full AI Systems Architect"** — consistent
  with [[MISSION.md]]'s architect emphasis; no mission change needed, but weight architecture
  framing going forward.
- Retrieval + spacing is landing well; keep ending lessons with recall and spaced re-tries.

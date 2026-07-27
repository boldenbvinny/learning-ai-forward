# Learning AI-Forward

A senior security engineer with a security background, learning to **build, architect, and
secure AI-native systems** — in the open. This repo is the working record of that journey:
lessons, hands-on code, red-team experiments, and the reasoning behind each decision.

The through-line is **security**. Every concept is learned by also attacking it — prompt
injection, indirect injection via RAG, tool-call hijacking, agent-loop abuse, and exfiltration.

## What's here

| Path | What it is |
|---|---|
| [`MISSION.md`](MISSION.md) | Why this exists and what "done" looks like |
| [`lessons/`](lessons/) | Self-contained lessons, one tightly-scoped concept each |
| [`practice/`](practice/) | Hands-on code — including deliberate red-team exercises |
| [`learning-records/`](learning-records/) | Dated records of key insights and course corrections |
| [`GLOSSARY.md`](GLOSSARY.md) | The canonical vocabulary used across every lesson |
| [`REVIEW.md`](REVIEW.md) | A spaced-repetition tracker for durable retention |
| [`reference/`](reference/) | Compressed reference cards for quick lookup |

## The three disciplines

Each maps to a property of a single model call:

- **Build** — model calls, tool use, RAG, agent loops _(One string of tokens → structured systems)_
- **Architect** — memory, context management, defensible trade-offs _(Stateless → managed state)_
- **Secure** — threat-modeling and hardening woven throughout _(Sampled / non-deterministic → evals & gates)_

## Running the practice code

```bash
# Auth via a local .env (never committed — see .gitignore)
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env
chmod 600 .env

python3 practice/L02_first-call.py
```

Every script loads the key with `python-dotenv`; **no secret is ever hardcoded or committed.**

---

*Learning in public. The mistakes and course-corrections are the point — they're captured in
[`learning-records/`](learning-records/), not hidden.*

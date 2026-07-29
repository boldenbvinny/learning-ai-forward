# Practice Code

Hands-on code you build during lessons lives here. One file per exercise.

## Naming convention

```
L##_<slug>[_v#].py
```

| Part      | Meaning                                                            | Example              |
|-----------|-------------------------------------------------------------------|----------------------|
| `L##`     | Zero-padded lesson number the exercise belongs to                 | `L02`, `L03`, `L11`  |
| `<slug>`  | Short kebab-case description of *what the code does*               | `first-call`, `output-gate` |
| `_v#`     | **Optional.** Only when you iterate on the *same* exercise and want to keep the older copy | `L03_output-gate_v2.py` |

Rules of thumb:
- **Lowercase, no spaces** — so `python practice/L03_output-gate.py` just works.
- A **new exercise** gets a new slug, not a version bump. Version bumps (`_v2`) are for
  "same exercise, I changed my approach and want the old one for comparison."
- Keep your own notes as `#` comments at the top of the file — what you tried, what surprised
  you. That's your lab notebook; it's more valuable than the code.

## Index

Append a row when you add a file. Status: `wip` · `works` · `attacked` (you tried to break it).

| File                          | Lesson | What it does                                             | Status   |
|-------------------------------|--------|----------------------------------------------------------|----------|
| `L02_first-call.py`           | L02    | First real Claude call — terse one-sentence system prompt | works    |
| `L02_injection-surface.py`    | L02    | Indirect-injection experiment (untrusted "document")      | attacked |
| `L03_delimiting.py`           | L03    | Layer 1 defense — `<untrusted_data>` delimiting            | wip      |
| `L03_delimiting_v2.py`        | L03    | Escalated delimiting attack (own red-team)                | attacked |
| `L03_delimiting_v3.py`        | L03    | Fake-closing-tag multi-step payload (own red-team)        | attacked |
| `L03_output-gate.py`          | L03    | Deterministic output gate + own "what is Secret?" probe   | works    |
| `L04_first-tool.py`           | L04    | Read-only tool loop — model requests, your code runs it   | works    |
| `L04_gated-action.py`         | L04    | Delete tool behind human-approval gate + injection probe  | attacked |
| `L05_agent-loop.py`           | L05    | Real multi-step read-only loop (get_price ×3 → total)     | works    |
| `L05_poisoned-result.py`      | L05    | Poisoned tool result → model tries delete → gate DENIES it | attacked |
| `L06_rag-basics.py`           | L06    | Minimal RAG — retrieve a doc, ground the answer in it      | works    |
| `L06_poisoned-doc.py`         | L06    | EchoLeak-style poisoned doc → output gate denies exfil URL | works    |
| `L06_poisoned-doc-v2.py`      | L06    | Sharpened poison (framing + authority + delimiter escape)  | attacked |
| `L07_eval-harness.py`         | L07    | Eval harness — dataset + code-based grader → accuracy score | works    |
| `L07_gate-eval.py`            | L07    | pass^k security eval — attack ×k, assert the gate holds     | attacked |
| `L07_triage-scorecard.py`     | L07    | Confusion matrix on agent #1's triage call; recall-biased F2 | works    |
| `L07_triage-scorecard_v2.py`  | L07    | Teeth: boundary cases + injection battery (attacker pass@k)  | attacked |
| `L07_triage-scorecard_v3.py`  | L07    | Defense: k-run OR-aggregation + injection-marker tripwire    | works    |
| `L07_triage-scorecard_v4.py`  | L07    | Fail-safe: held-out injection breaks tripwire; RAISE/REVIEW  | works    |
| `triage_core.py`              | L07    | Single source of truth for the triage verdict rule (no dismiss) | works    |

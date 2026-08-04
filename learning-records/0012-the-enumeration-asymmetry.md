# The ingress/egress hole — and the asymmetry that closes it

**Trigger (2026-08-04).** Two recall misses on the same day turned out to be one miss. On L05 he named the
human gate, then offered as a second defense *"the URLs being removed from the prompts to the LLM are a
sanitization mechanism."* On L06 he correctly located the untrusted input and correctly said a
`<document>` delimiter is not the fix — and then **stopped**, never naming the wall (the deterministic
output gate on egress). Same reflex both times: under pressure he reaches for **cleaning the input** and
does not reach for **constraining the action**.

**Why this mattered more than a normal miss.** The proposed defense is a blocklist — i.e. the v3 tripwire
he *personally rejected* in favour of removing the `DISMISS` verb
([[0008-blocklist-tripwire-is-not-a-wall-least-privilege-on-the-decision]]). On 08-03 the `n+∞` half of that
argument was requested and not produced; on 08-04 he produced its **opposite** as a defense. Two independent
signals that the argument was borrowed, not owned — and it is load-bearing for everything downstream.

**What worked: stop asking for recall, force generation.** Re-asking for the argument a fourth time would
have been the L01 mistake again — repeating a failing method more loudly
([[0010-l01-derive-dont-memorize]]). Instead he was handed a concrete line-based filter
(`if "http" in line.lower(): continue`), told he was the attacker, and asked for **three bypasses** plus one
question about his own list. He produced `hxxp` defanging, structural/tag splitting, and base64 — then
concluded unaided: *"patching all three only blocks those three use cases… n to infinite loop."* That is the
`n+∞` argument, generated rather than recalled, on his own turf (offensive security). **Fourth attempt, first
success.** Reinforces the LR-0010 generalisation: when an item resists repeated repair, change the encoding,
and prefer a scaffold he can regenerate over an artifact he must store.

**The fourth bypass he did not list — the one that closes the loop.** Put **no URL in the input at all**:
instruct the reply to append the summary to a bare domain and render it as a markdown image. Nothing to
strip; the model *constructs* the URL on the way out. A **perfect** ingress filter blocks nothing here,
because the payload did not exist when the filter ran. This is exactly the L06 wall he failed to produce
that morning — so the two misses collapse into one lesson, and the bypass exercise supplied its own repair.

**The formulation to reuse (now in GLOSSARY):**

> **You cannot enumerate the inputs. You can enumerate the actions.**

The input space is infinite and re-chosen the moment you publish a filter; the attacker needs one win
(**pass@k**). The action space is finite *because he authored it* — `delete_file`, `RAISE`, `NEEDS_REVIEW` —
so a constraint on it can be asserted over every case (stub the model to worst case, assert, no API key).
Sanitization is therefore a legitimate defense-in-depth **layer** and never a **wall**: it is verifiable only
against the strings you thought of, which is precisely the set the attacker is not using. Stated as an
asymmetry rather than a rule, it explains *why* the output gate, the retriever ACL, the removed `DISMISS`
verb and the human approval edge are all the same move — they all sit on the egress side, the only side with
a knowable boundary.

**Immediate application (same session, L08).** Memory is where this instinct is most tempting and most
fatal, because dedupe invites "scrub bad notes on write." The correct control is the asymmetry: constrain
what a memory entry may **influence** — ordering, dedupe keys, prior evidence shown alongside: yes; the
verdict, whether a human sees it, the severity floor, any privilege: never. Otherwise dedupe silently
re-grants the `DISMISS` verb v4 removed, with a longer reach — one win, permanent effect, attacker absent
when it fires.

**Open.** L05 and L06 reset to 1d (due 08-05) — the graded re-test is whether *the wall*, not the diagnosis,
comes out cold. L05 also lost **per-iteration mediation** and the **hard loop cap** entirely; those are
untested since 07-28 and are not covered by this repair. And this argument has been *generated* once, never
recalled cold; treat it as provisional until 08-06 (L07c) says otherwise.

**Related:** [[0003-authority-to-act-lives-in-code]] · [[0005-rag-injection-surface-output-gate-wall]] ·
[[0008-blocklist-tripwire-is-not-a-wall-least-privilege-on-the-decision]] · [[0010-l01-derive-dont-memorize]]

"""Single source of truth for agent #1's triage DECISION rule.

The security invariant lives here — in deterministic code, NOT in the model.
The rule offers exactly two verdicts and, deliberately, NO way to close a finding:
the agent may RAISE (confident it is exploitable) or defer to NEEDS_REVIEW. There
is no DISMISS/CLOSE verb for an injection to reach, so an exploitable finding can
never be silently shipped, whatever the stochastic, injectable model decides.
See learning-records/0008 and 0009. Both the demo (L07_triage-scorecard_v4.py)
and the CI gate (tests/test_triage_gate.py) import THIS module, so the guarded
rule and the shipped rule are guaranteed identical.
"""

RAISE = "RAISE"
NEEDS_REVIEW = "NEEDS_REVIEW"

# The complete set of verdicts the agent is authorized to emit.
# Note what is deliberately absent: no "DISMISSED", no "SAFE", no "CLOSED".
ALLOWED_VERDICTS = frozenset({RAISE, NEEDS_REVIEW})


def triage_verdict(agent_thinks_exploitable: bool) -> str:
    """Map the model's (untrusted, stochastic) opinion to an authorized verdict.

    RAISE only when the model is confident it is exploitable; otherwise defer to a
    human/code check. A 'not exploitable' opinion does NOT close the finding — it
    routes to review. Authority to close never reaches the model.
    """
    return RAISE if agent_thinks_exploitable else NEEDS_REVIEW


def ships_exploit(exploitable: bool, verdict: str) -> bool:
    """True iff a real exploit would ship: an exploitable finding given a verdict
    that closes it WITHOUT human review. Because triage_verdict only ever returns
    an ALLOWED_VERDICT, this is structurally always False — the guarantee the CI
    gate locks in. If a future change introduces a closing verdict (e.g. auto-
    dismiss), this returns True and the gate fails the build.
    """
    closes_without_review = verdict not in ALLOWED_VERDICTS
    return exploitable and closes_without_review

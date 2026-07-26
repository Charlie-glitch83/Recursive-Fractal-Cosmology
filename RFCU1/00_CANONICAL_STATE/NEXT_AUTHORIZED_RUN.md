# Next Authorized Action

## Complete RUN 013 Recovery and Canonical Registration

This is a recovery and registration action, not a new scientific run.

### Required work

1. Import the complete Work-iteration RUN 011 payload.
2. Verify it against the recovered delivery SHA-256 identities and its frozen parent.
3. Import and verify the complete RUN 012 payload.
4. Import and verify the complete RUN 013 payload and closeout.
5. Replay all mandatory parent, source-firewall, no-retune, deterministic, and independent-verification gates.
6. Register RUN 011, RUN 012, and RUN 013 in order.
7. Update the canonical state to `RUN_013_REGISTERED`.
8. Issue a separate versioned authorization for RUN 014.

## Current prohibition

`RUN 014` is not yet authorized and must not execute during recovery.

RFCU2, its repository, and its artifacts are quarantined and may not supply missing RFCU1 content, equations, hashes, outcomes, or authorization.

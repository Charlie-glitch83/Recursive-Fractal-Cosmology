# Next Authorized Action

## Complete the parent-chain migration required to execute RUN 014

The recovered frozen checkpoint authorizes:

`RUN_014_MODULE_B_COMMON_ANCESTRY_AND_CONTRACT_FREEZE`

That historical authorization is now preserved exactly. It is not permission to execute RUN 014 from an incomplete recovery branch.

## Required recovery work before execution

1. Import the complete original RUN 001-007 payload bundle, including `H_A`, `TEC_A`, validators, results, closeouts, and SHA-256 ledgers.
2. Import the complete original RUN 008-010 payload bundle.
3. Import `Module Plans.zip` and reconcile its exact documents.
4. Import the v3.0-to-execution promotion/source-reconciliation and RUN 001 authorization bridge.
5. Verify every parent hash and internal ledger through RUN 010.
6. Replay the deterministic, independent, source-firewall, no-retune, and lineage gates.
7. Produce the root dependency manifest from v3.0 through RUN 013.
8. Confirm RUN 014's frozen inputs without changing its Work-iteration specification.

## Current execution prohibition

`RUN 014` is `AUTHORIZED_BY_RECOVERED_CHECKPOINT_BUT_NOT_EXECUTABLE_PENDING_PARENT_RECOVERY`.

No new scientific execution may begin during the migration gap. RFCU2, an old failure, a summary, or a reconstructed substitute may not provide missing parent content.

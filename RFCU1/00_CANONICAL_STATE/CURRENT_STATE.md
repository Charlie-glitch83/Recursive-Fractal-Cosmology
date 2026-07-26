# Current Canonical State

- Project: RFCU1
- Canonical repository: `Charlie-glitch83/Recursive-Fractal-Cosmology`
- Recovery branch: `agent/rfcu1-work-iteration-recovery`
- Architecture lineage: Rebuild v3.0 foundation and its verified descendants
- Primitive triad: CIF, QV, RFL
- First Action: `QV(CIF) -> RFL`
- RFCU2 status: `QUARANTINED_NOT_A_PARENT`
- Scientific lineage identified: RUN 001 through RUN 013
- Complete supplied-file batch migration: `CLOSED_13_OF_13`
- RUN 011-013 checkpoint archive: `EXACT_BYTES_MIGRATED`
- RUN 011-013 internal ledger: `24_OF_24_FILES_SHA256_VERIFIED`
- RUN 011 result: `1.0000/CLEAN_PASS`
- RUN 012 result: `1.0000/CLEAN_PASS`
- RUN 013 result: `1.0000/CLEAN_PASS`
- Historical checkpoint authorization: `RUN_014_MODULE_B_COMMON_ANCESTRY_AND_CONTRACT_FREEZE`
- Current executable status of RUN 014: `BLOCKED_PENDING_RUN_001_010_PARENT_MIGRATION_AND_REPLAY`
- Merge status: `NOT_AUTHORIZED`

## Controlling recovery records

- `WORK_ITERATION_MIGRATION_BATCH_20260726.md`
- `WORK_ITERATION_RECOVERY_INVENTORY.md`
- `RECOVERY_COMPLETENESS_MATRIX.json`
- `../04_RUNS/MODULE_A_RUN_001_007_LINEAGE.md`
- `../98_TRANSFER_ARCHIVES/work_iteration/raw_rebuild_uploads_batch_20260726/README.md`
- `../99_QUARANTINE/RFCU2_EXCLUSION.md`

## Exact supplied batch

The raw transfer archive preserves 13 original user-supplied files under their original filenames. Its member ledger includes both v3.0 architecture variants and the complete Module B RUN 011-013 canonical checkpoint bundle.

The RUN 011-013 checkpoint reports combined verification of:

```text
exact deterministic checks: 13,002 / 13,002
independent checks:          9,222 / 9,222
ablations:                      42 / 42
Wolfram suites:                   3 / 3 VERIFIED
```

## Binding boundary

The exact supplied batch is completely migrated. This does not yet establish one-to-one closure for the entire Rebuild folder.

Still required are the original complete payloads for RUN 001-007 and RUN 008-010, `Module Plans.zip`, the v3.0-to-execution promotion/source-reconciliation bridge, and any additional Work-iteration file not listed in the supplied-batch member ledger.

RUN 014 was authorized inside the recovered frozen checkpoint. It must not execute from this recovery branch until its missing parent artifacts are imported, hash-verified, and replayed. No RFCU2 artifact may fill that gap.

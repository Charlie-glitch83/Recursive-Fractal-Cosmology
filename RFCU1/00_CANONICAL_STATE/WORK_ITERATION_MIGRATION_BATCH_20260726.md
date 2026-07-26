# Work-Iteration Migration Batch — 2026-07-26

## Exact-byte status

The following user-supplied Work-iteration batch has been preserved byte-for-byte in the repository transfer archive:

`RFCU1/98_TRANSFER_ARCHIVES/work_iteration/raw_rebuild_uploads_batch_20260726/`

The batch contains 13 original files:

- both supplied v3.0 architecture ZIP variants;
- both master-architecture variants;
- both proof-lock variants;
- both deep-soak/source-audit variants;
- both manifest variants;
- both README variants;
- `RFC_Rebuild_Module_B_RUNS_011_013_Canonical_Checkpoint_Bundle.zip`.

The exact original filenames and SHA-256 values are frozen in `MEMBER_SHA256SUMS.txt`. The reconstructed transfer archive is verified by `ARCHIVE_SHA256SUM.txt`, and each base64 transfer part is verified by `CHUNK_SHA256SUMS.txt`.

## RUN 011–013 checkpoint

The checkpoint archive SHA-256 is:

`e6789d5aa68886727db023e586e60550d16314eff916b248c778045e423a7098`

Its internal ledger verifies all 24 run payload files. The checkpoint records:

- RUN 011: `1.0000/CLEAN_PASS`;
- RUN 012: `1.0000/CLEAN_PASS`;
- RUN 013: `1.0000/CLEAN_PASS`;
- combined exact checks: `13,002/13,002`;
- combined independent checks: `9,222/9,222`;
- combined ablations: `42/42`;
- Wolfram suites: `3/3 VERIFIED`;
- next run authorized by the checkpoint: `RUN_014_MODULE_B_COMMON_ANCESTRY_AND_CONTRACT_FREEZE`.

## Authorization distinction

RUN 014 is historically authorized by the frozen Work-iteration checkpoint. It is not executable from the current recovery branch until the exact parent chain through RUN 010 and the v3.0-to-execution promotion bridge are migrated and replayed.

## Remaining one-to-one migration gap

This batch closes only the files actually supplied in the batch. Complete Rebuild-folder migration still requires exact bytes for:

- Module A RUNs 001–007 complete payload bundle;
- Module B RUNs 008–010 complete payload bundle;
- `Module Plans.zip` and its plan documents;
- the v3.0-to-execution promotion/source-reconciliation bridge;
- any additional Work-iteration file present in the Rebuild folder but not represented in `MEMBER_SHA256SUMS.txt`.

No summary, search snippet, hash-only reference, or downstream closeout may substitute for those original bytes.

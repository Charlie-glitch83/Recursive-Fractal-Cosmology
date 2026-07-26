# Rebuild Module A and Module B Exact Migration Batch — 2026-07-26

This batch preserves the exact bytes and original filenames of 30 Work-iteration files supplied across the RUN 008–010 and Module A uploads.

## Authoritative archives

- `RFC_Rebuild_Module_A_v1.0_Canonical_Completion_Bundle.zip`
  - SHA-256: `c9398886747b106d0545e0d5ea63088fd3821e08d6f035e850402d3892772d75`
  - contains RUN 000, the v3.1 source-reconciled architecture, RUNs 001–007, `RFC-H_A-v1.0`, `TEC_A`, validators, results, closeouts, and the 23-file freeze manifest;
  - freeze manifest verified: `23/23`.

- `RFC_Rebuild_Module_B_RUNS_008_010_Canonical_Checkpoint_Bundle.zip`
  - SHA-256: `ce2d9f13bd6561935ce3e61ddb7a113a918ceb451c744e9df518be4ccc8acbc1`
  - contains RUNs 008–010 and the checkpoint deliverables;
  - declared internal SHA-256 ledger verified: `26/26`.

## Loose files

The 27 loose RUN 008–010 files match their corresponding checkpoint archive members exactly. The loose `MODULE_A_TEC_A.json` matches the Module A archive member exactly.

## Verification

- `MEMBER_SHA256SUMS.txt` verifies all 30 original supplied files.
- The reconstructed transfer archive contains complete extracted-member ledgers for both authoritative ZIPs.
- The transfer archive also contains the full integrity audit recording freeze-manifest and loose/archive equivalence checks.

## Reconstruction

```sh
cat rebuild_moduleA_moduleB_20260726.tar.xz.b64.part* \
  | base64 -d \
  > rebuild_moduleA_moduleB_20260726.tar.xz

sha256sum -c ARCHIVE_SHA256SUM.txt

tar -xJf rebuild_moduleA_moduleB_20260726.tar.xz
```

`CHUNK_SHA256SUMS.txt` verifies every encoded transfer part before reconstruction.

## Replay boundary

Exact-byte and internal-ledger integrity are verified. Full validator replay is not claimed from this batch alone because RUN 001 and RUN 008 validators require canonical source-root files that are referenced by hash but are not all included here.

Additional Rebuild files may be added as later exact migration batches until the user confirms the folder upload is complete.

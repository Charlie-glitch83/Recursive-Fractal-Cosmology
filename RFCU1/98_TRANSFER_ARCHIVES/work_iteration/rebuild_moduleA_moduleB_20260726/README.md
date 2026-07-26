# Rebuild Module A and Module B Migration Batch — 2026-07-26

This batch records the Work-iteration Module A and Module B materials supplied by the user and the integrity checks completed against them.

## Authoritative archives verified from supplied bytes

- `RFC_Rebuild_Module_A_v1.0_Canonical_Completion_Bundle.zip`
  - SHA-256: `c9398886747b106d0545e0d5ea63088fd3821e08d6f035e850402d3892772d75`
  - contains RUN 000, the v3.1 source-reconciled architecture, RUNs 001–007, `RFC-H_A-v1.0`, `TEC_A`, validators, results, closeouts, and the 23-file freeze manifest;
  - freeze manifest verified: `23/23`.

- `RFC_Rebuild_Module_B_RUNS_008_010_Canonical_Checkpoint_Bundle.zip`
  - SHA-256: `ce2d9f13bd6561935ce3e61ddb7a113a918ceb451c744e9df518be4ccc8acbc1`
  - contains RUNs 008–010 and checkpoint deliverables;
  - declared internal SHA-256 ledger verified: `26/26`.

## Loose-file equivalence

- the 27 supplied loose RUN 008–010 files match their corresponding checkpoint archive members exactly;
- the supplied loose `MODULE_A_TEC_A.json` matches the Module A archive member exactly;
- the separately supplied RUN 007 closeout, H_A export, and integrated theorem match the Module A chain and are stored as readable repository files.

## Repository-resident state

Readable RUN 007 canonical artifacts and this integrity manifest are present on the recovery branch.

The two binary ZIP archives are verified from the supplied bytes, but are not yet stored as repository blobs by the connected GitHub file API. They remain required for literal one-to-one binary closure unless reconstructed from separately committed members.

## Replay boundary

Exact source-bundle integrity is verified. Full validator replay still requires all canonical source-root files at their intended repository paths.

Historical v1.0/v1.1 architecture duplicates are excluded from the active Work-iteration migration because the Work-iteration source register classifies them as archival/reserve material rather than active output.

# Raw Rebuild Upload Batch - 2026-07-26

This transfer archive preserves the exact bytes and original filenames of the Work-iteration files supplied for the RFCU1 recovery on 2026-07-26.

## Contents

The archive contains 13 files under `files/`:

- `RFC_Rebuild_Module_B_RUNS_011_013_Canonical_Checkpoint_Bundle.zip`
- both uploaded v3.0 architecture ZIP variants;
- both uploaded master-architecture variants;
- both uploaded proof-lock variants;
- both uploaded source-audit variants;
- both uploaded manifest variants;
- both uploaded README variants.

No duplicate was discarded merely because its filename or subject overlapped another file. Each uploaded byte sequence is preserved under its original filename.

## Reconstruction

From this directory:

```sh
cat raw_rebuild_uploads_batch_20260726.tar.xz.b64.part* \
  | base64 -d \
  > raw_rebuild_uploads_batch_20260726.tar.xz

sha256sum -c ARCHIVE_SHA256SUM.txt

tar -xJf raw_rebuild_uploads_batch_20260726.tar.xz

cd files
sha256sum -c ../MEMBER_SHA256SUMS.txt
```

`CHUNK_SHA256SUMS.txt` verifies every encoded transfer part before reconstruction.

## Scope boundary

This batch proves exact migration of the files listed in `MEMBER_SHA256SUMS.txt`. It does not claim that every file ever placed in the Rebuild folder has been supplied. Additional Work-iteration bundles must be migrated as separate content-addressed batches until the root migration ledger reaches one-to-one closure.

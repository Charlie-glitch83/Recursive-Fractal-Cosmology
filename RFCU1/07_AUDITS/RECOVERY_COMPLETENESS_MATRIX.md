# RFCU1 Recovery Completeness Matrix

**Branch:** `agent/rfcu1-work-iteration-recovery`  
**Purpose:** prevent exact migrated bytes, summaries, downstream replays, and remembered lineage from being confused with one another.

## State vocabulary

- `EXACT_PRESENT` — exact bytes are stored on the branch with a recorded SHA-256.
- `ARCHIVE_PRESENT_VERIFIED` — an exact content-preserving archive is stored and its members are covered by a verified internal ledger.
- `HASH_VERIFIED_NOT_STORED` — source bytes matched the expected SHA-256 but are not yet stored at a canonical repository path.
- `IDENTITY_RECOVERED` — filename, role, parent, or hash is known but the original payload is absent.
- `LINEAGE_CONFIRMED` — downstream replay proves the run existed but does not replace its original packet.
- `MISSING_REQUIRED` — required for one-to-one closure and not yet recovered.
- `QUARANTINED` — retained only as historical evidence and never an active RFCU1 parent.

## Supplied migration batch

| Object | Identity | State |
|---|---|---|
| Raw supplied batch | 13 original files and original filenames | `EXACT_PRESENT` — 13/13 preserved |
| Batch member ledger | `MEMBER_SHA256SUMS.txt` | `EXACT_PRESENT` |
| Reconstructable transfer archive | split base64 `tar.xz` with archive and chunk ledgers | `EXACT_PRESENT` |
| RUN 011–013 checkpoint ZIP | `e6789d5aa68886727db023e586e60550d16314eff916b248c778045e423a7098` | `ARCHIVE_PRESENT_VERIFIED` |

The supplied batch is closed. This does not prove that every file ever placed in the Rebuild folder has been supplied.

## Architecture

| Object | Expected identity | State | Closure requirement |
|---|---|---|---|
| Initial v3.0 source-gated ZIP | `11425224ce0514c5b66897674623e694e7ab73f4cb648c7d131d9dacb603f858` | `EXACT_PRESENT` in raw batch | none for supplied-batch preservation |
| Revised v3.0 source-gated ZIP | `ed41cf3a023394983f4202d220e3ecd22de6a24ff960834b75a1a586b52d48b0` | `EXACT_PRESENT` | decode and reproduce hash |
| Revised v3.0 README | `1cf3f146160b4e8e1b137887f667253987bc4f623d07e30337ee2bd64f6300d8` | `EXACT_PRESENT` | hash check |
| Revised v3.0 proof lock | `a8e73b5f1c7209301d575c5450ea95e0d124c741b7bc6426bc83614dc8bb4060` | `EXACT_PRESENT` | hash check |
| Revised v3.0 source audit | `b8acdfce1aaaefb8efb4c4b7351f75f1bb7c2671b08ef5cd86970cc488f82f43` | `EXACT_PRESENT` | hash check |
| Revised v3.0 manifest | `69751e5350b6e9c50369fe50c6744d49210ef99739b7770025916e814426887b` | `EXACT_PRESENT` | JSON and graph check |
| Revised v3.0 master architecture | `74c88b62f919d0464f674a176da030294237039831fc0d2949a8d3ab19241f66` | `EXACT_PRESENT` | hash check |
| v3.0 to promoted-execution bridge | exact promotion/delta/authorization record | `MISSING_REQUIRED` | recover exact bridge and RUN 001 authorization |

Initial individual architecture variants are retained exactly in the raw batch rather than discarded as duplicates.

## Canonical source roots

| Source | Expected SHA-256 | State |
|---|---|---|
| Presentation 29 revised raw LaTeX | `cef6d68b05eb509e471c55a18b5fffedd9c411b44bc0d5bd0f6b5ee86bd8b53e` | `HASH_VERIFIED_NOT_STORED` |
| Presentation 29 revised metadata | `82549b02c8edfabc55db4268c43eeb2d60d3a694ad528516354b1a39cfb09215` | `HASH_VERIFIED_NOT_STORED` |
| Presentation 30 with Appendix J | `4895c3777da3aa84da4ec2343419ffbc07502b3738602308a1f402862441eaf6` | `HASH_VERIFIED_NOT_STORED` |
| Revised N-body proof | `0eb5e85475e9f3ab7242ee35c359b063ea62a4e66fa7124b9f6ccad41141ab28` | `HASH_VERIFIED_NOT_STORED` |
| Revised N-body metadata | `caab0133cd29a3fb057a9a918ae9d2adc1477c693acbc2e3ad028754303f7d94` | `HASH_VERIFIED_NOT_STORED` |
| Module Plans.zip | `6fbf126f62e8c9a383446b0aae2691ac40a3a9ccc34c293de5ef9e462012cb76` | `IDENTITY_RECOVERED` |
| Canonical Master Architecture v1.0 | `884ad77e542a99280165cdd309273a823bd9fa34976ef23256f3054e953364be` | `IDENTITY_RECOVERED` |
| Canonical Architecture v1.1 Bundle | `bd739d691b859c4734531072889fd847dce0d9f860bd55cec1046aae4572fd23` | `IDENTITY_RECOVERED` |

A name and hash do not substitute for repository-resident source bytes.

## Executed run lineage

| Run | Current evidence | State | Required closure object |
|---|---|---|---|
| 001 | first parent in RUN 007 replay | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 002 | primitive triad and First Action role | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 003 | bounded/convergent kernel role | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 004 | terminal N-body completion role | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 005 | route/witness/refinement role | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 006 | event/no-loss/memory/stability role | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 007 | closeout; `H_A` and `TEC_A` identities | `IDENTITY_RECOVERED` | theorem, source map, validators, result, export, TEC, manifest, ledger |
| 008 | frozen checkpoint evidence | `IDENTITY_RECOVERED` | full packet and ledger |
| 009 | frozen checkpoint evidence | `IDENTITY_RECOVERED` | full packet and ledger |
| 010 | result and model identities | `IDENTITY_RECOVERED` | full packet, ledger, and replay |
| 011 | exact checkpoint ZIP; 8 files covered by internal ledger | `ARCHIVE_PRESENT_VERIFIED` | parent-chain replay through RUN 010 |
| 012 | exact checkpoint ZIP; 8 files covered by internal ledger | `ARCHIVE_PRESENT_VERIFIED` | parent-chain replay through RUN 010–011 |
| 013 | exact checkpoint ZIP; 8 files covered by internal ledger | `ARCHIVE_PRESENT_VERIFIED` | parent-chain replay through RUN 010–012 |
| 014 | authorized by checkpoint; not executed | `AUTHORIZED_BLOCKED` | complete RUN 001–010 recovery and replay before execution |

### Exact RUN 011–013 checkpoint totals

```text
RUN 011: 1.0000/CLEAN_PASS
RUN 012: 1.0000/CLEAN_PASS
RUN 013: 1.0000/CLEAN_PASS
exact checks:       13,002/13,002
independent checks:  9,222/9,222
ablations:               42/42
Wolfram suites:            3/3 VERIFIED
internal run files:       24/24 SHA-256 verified
```

## Required root closure

The migration is complete only when a machine-readable root ledger proves:

```text
all Rebuild-folder files -> exact repository counterparts
v3.0 source-gated architecture
-> direct-source promotion and approved delta
-> promoted execution architecture
-> RUN 001 -> ... -> RUN 007 / H_A / TEC_A
-> RUN 008 -> RUN 009 -> RUN 010
-> RUN 011 -> RUN 012 -> RUN 013
-> frozen RUN 014 authorization
```

Each edge must identify its parent and SHA-256. Every run must retain its original specification, source map, theorem/model, deterministic certificate, independent replay, result, closeout, and internal ledger.

## Merge gate

PR #4 remains draft and unmerged while any required object is `MISSING_REQUIRED`, `IDENTITY_RECOVERED`, `LINEAGE_CONFIRMED`, or `HASH_VERIFIED_NOT_STORED`.

RFCU2 remains `QUARANTINED` and cannot fill any gap.

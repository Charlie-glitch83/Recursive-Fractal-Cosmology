# RFCU1 Recovery Completeness Matrix

**Branch:** `agent/rfcu1-work-iteration-recovery`  
**Purpose:** prevent summaries, downstream replays, or remembered lineage from being mistaken for complete artifact recovery.

## State vocabulary

- `EXACT_PRESENT` — exact bytes are stored on the recovery branch and have a recorded SHA-256.
- `ARCHIVE_PRESENT` — exact bytes are stored in a content-preserving archive, but not all members are separately readable in GitHub.
- `HASH_VERIFIED_LOCAL` — exact bytes were available in the recovery workspace and matched the expected SHA-256, but have not yet been stored on the branch.
- `IDENTITY_RECOVERED` — filename, role, parent, or hash is known, but the payload is absent.
- `LINEAGE_CONFIRMED` — downstream replay proves the run existed in the parent chain, but does not replace its payload.
- `MISSING_REQUIRED` — required for canonical closure and not yet recovered.
- `QUARANTINED` — retained only as historical evidence; never an active RFCU1 parent.

## Architecture

| Object | Expected identity | State | Closure requirement |
|---|---|---|---|
| v3.0 source-gated ZIP | `ed41cf3a023394983f4202d220e3ecd22de6a24ff960834b75a1a586b52d48b0` | `EXACT_PRESENT` as base64-preserved ZIP | decode and reproduce hash |
| v3.0 README | `1cf3f146160b4e8e1b137887f667253987bc4f623d07e30337ee2bd64f6300d8` | `EXACT_PRESENT` | hash check |
| v3.0 proof lock | `a8e73b5f1c7209301d575c5450ea95e0d124c741b7bc6426bc83614dc8bb4060` | `EXACT_PRESENT` | hash check |
| v3.0 source audit | `b8acdfce1aaaefb8efb4c4b7351f75f1bb7c2671b08ef5cd86970cc488f82f43` | `EXACT_PRESENT` | hash check |
| v3.0 manifest | `69751e5350b6e9c50369fe50c6744d49210ef99739b7770025916e814426887b` | `EXACT_PRESENT` | JSON parse, graph checks, hash check |
| v3.0 master architecture | `74c88b62f919d0464f674a176da030294237039831fc0d2949a8d3ab19241f66` | `ARCHIVE_PRESENT` | unpack as readable exact file and hash check |
| v3.0 to promoted execution architecture bridge | exact source-promotion/delta/authorization record | `MISSING_REQUIRED` | recover exact promotion record and first-run authorization |

## Canonical source roots

| Source | Expected SHA-256 | State |
|---|---|---|
| Presentation 29 revised raw LaTeX | `cef6d68b05eb509e471c55a18b5fffedd9c411b44bc0d5bd0f6b5ee86bd8b53e` | `HASH_VERIFIED_LOCAL` |
| Presentation 29 revised metadata | `82549b02c8edfabc55db4268c43eeb2d60d3a694ad528516354b1a39cfb09215` | `HASH_VERIFIED_LOCAL` |
| Presentation 30 raw LaTeX with Appendix J | `4895c3777da3aa84da4ec2343419ffbc07502b3738602308a1f402862441eaf6` | `HASH_VERIFIED_LOCAL` |
| Revised N-body proof | `0eb5e85475e9f3ab7242ee35c359b063ea62a4e66fa7124b9f6ccad41141ab28` | `HASH_VERIFIED_LOCAL` |
| Revised N-body metadata | `caab0133cd29a3fb057a9a918ae9d2adc1477c693acbc2e3ad028754303f7d94` | `HASH_VERIFIED_LOCAL` |
| Module Plans.zip | `6fbf126f62e8c9a383446b0aae2691ac40a3a9ccc34c293de5ef9e462012cb76` | `IDENTITY_RECOVERED` |
| Canonical Master Architecture v1.0 | `884ad77e542a99280165cdd309273a823bd9fa34976ef23256f3054e953364be` | `IDENTITY_RECOVERED` |
| Canonical Architecture v1.1 Bundle | `bd739d691b859c4734531072889fd847dce0d9f860bd55cec1046aae4572fd23` | `IDENTITY_RECOVERED` |

A README containing names and hashes is not a source import. Every canonical source must be stored exactly or in a reconstructable content-addressed archive before source promotion closes.

## Executed run lineage

| Run | Current evidence | State | Required closure object |
|---|---|---|---|
| 001 | confirmed as first parent in RUN 007 six-parent replay | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 002 | primitive triad and typed First Action role recovered | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 003 | bounded/convergent kernel role recovered | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 004 | terminal N-body completion role recovered | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 005 | route existence/witness/refinement role recovered | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 006 | event/no-loss/memory/stability role recovered | `LINEAGE_CONFIRMED` | full original run packet and ledger |
| 007 | closeout imported; `H_A` and `TEC_A` identities known | `IDENTITY_RECOVERED` | theorem, source map, validators, results, export, TEC, manifest, full ledger |
| 008 | frozen checkpoint summary and detailed counts recovered | `IDENTITY_RECOVERED` | full packet and SHA-256 ledger |
| 009 | frozen checkpoint summary and detailed counts recovered | `IDENTITY_RECOVERED` | full packet and SHA-256 ledger |
| 010 | formal model/result identities and SHA-256 ledger recovered | `IDENTITY_RECOVERED` | all files named in ledger, byte verified |
| 011 | registered bundle and successful-run archive identities recovered | `IDENTITY_RECOVERED` | exact archives, extraction, internal verification |
| 012 | registered bundle and successful-run archive identities recovered | `IDENTITY_RECOVERED` | exact archives, extraction, internal verification |
| 013 | PASS closeout and B012 parent hash recovered | `IDENTITY_RECOVERED` | exact packet, ledger, replay, canonical registration |
| 014 | no execution | `BLOCKED_NOT_AUTHORIZED` | separate authorization only after RUN 013 registration |

## Required root closure

The recovery is complete only when one machine-readable root manifest proves:

```text
v3.0 source-gated architecture
-> direct-source promotion and approved delta
-> promoted execution architecture
-> RUN 001
-> RUN 002
-> RUN 003
-> RUN 004
-> RUN 005
-> RUN 006
-> RUN 007 / RFC-H_A-v1.0 / RFC-TEC_A-v1.0
-> RUN 008
-> RUN 009
-> RUN 010
-> RUN 011
-> RUN 012
-> RUN 013 REGISTERED
```

Each edge must name the parent object and its SHA-256. Every run must carry its specification, source map, formal theorem/model, deterministic certificate, independent replay, machine-readable result, closeout, and complete internal ledger.

## Merge gate

PR #4 must remain draft and unmerged while any object above is `MISSING_REQUIRED`, `IDENTITY_RECOVERED`, `LINEAGE_CONFIRMED`, or `HASH_VERIFIED_LOCAL` rather than exact branch-resident content.

RFCU2 remains `QUARANTINED` and cannot fill any gap.

# Work Iteration Recovery Inventory

**Recovery branch:** `agent/rfcu1-work-iteration-recovery`  
**Canonical project:** RFCU1  
**Canonical repository:** `Charlie-glitch83/Recursive-Fractal-Cosmology`  
**RFCU2 status:** QUARANTINED — never an RFCU1 parent

## Purpose

This inventory records the persistent artifacts recovered from the Rebuild File Library and the live GitHub repository after the Work iteration ended. It prevents the obsolete pre-execution baseline from erasing later completed work and prevents unrelated RFCU2 material from entering RFCU1.

## User-confirmed provenance

The user identified the following as products of the expired Work iteration:

1. the Rebuild-folder v3.0 foundation materials;
2. the RFC rebuild Module B RUNs 011 through 013 package;
3. the intended stopping point after RUN 013, with RUN 014 next after registration.

User provenance is recorded as a recovery fact. Scientific admission still requires exact file identity, parent continuity, hashes, and registration.

## Recovered execution checkpoint

### RUNs 008–010

Recovered checkpoint identity:

```text
RFC_Module_B_Runs_008_010_CHECKPOINT_README.md
status: FROZEN CLEAN CHECKPOINT
parent: RFC-H_A-v1.0
TEC_A: 1.0000/CLEAN_PASS
latest result: RUN 010 = 1.0000/CLEAN_PASS
next authorized at that checkpoint: RUN 011
```

Recovered RUN 010 result identity:

```text
run_id: RFC-RUN-010-B008-B011
result: CLEAN_PASS
score: 1.0000
hard_stop_triggered: false
public_data_used: false
historical_outcome_used: false
retune_used: false
next_run_authorized: RUN_011_MODULE_B_SECTOR_PARTITION_AND_NO_DOUBLE_COUNTING
```

### RUN 011 delivery identities

```text
RFC_Canonical_Project_Bundle_20260722_v3_32_B011_REGISTERED.zip
sha256: a2e2966998a33e0b13c1c0cdf8e85ca52fac0332e38b7fbdedabe5c8dcf30a88

B011_Compression_Relic_Background_and_Perturbation_Contract_Successful_Run_20260722.zip
sha256: edb3932681222a1c1bc14a0e35c554fac23e043580b0a9ab9a72595deaf56cc3
```

### RUN 012 delivery identities

```text
RFC_Canonical_Project_Bundle_20260722_v3_34_B012_REGISTERED.zip
sha256: 9ddb0464a5393a4646a6e70c8561c13e9c2254d7e76181a8bb063fa9aebd0fe2

B012_Dissipative_Tail_Background_Perturbation_and_Terminal_Contract_Successful_Run_20260722.zip
sha256: 19e4a7b8f3b0f7190503a8b4a213a4b7a7d6d65fe5045af012eef228c41bf5ef
```

### RUN 013 recovered closeout

```text
run_id: B013
module: B
title: Common Ancestry, Contract Freeze, UniverseState, and Handoffs
parent: B012
parent_hash: c20172d2f169df06fd1d957af7347418bf992238786bf10a202158b21bb3ae20
bundle_version: 3.35
status: PASS pending canonical registration
primary outcomes: 117/117
independent checks: 20/20
mandatory gates: 11/11
```

The closeout explicitly states that RUN 014 requires a separate versioned authorization after successful RUN 013 registration.

## Recovery classifications

| Artifact class | Recovery status | Canonical effect |
|---|---|---|
| RFCU1 v3.0 foundation | USER_CONFIRMED_WORK_ITERATION | candidate canonical foundation; exact-file audit required |
| RFCU1 RUNs 001–010 | RECOVERED_LINEAGE | preserve and import with exact hashes |
| RFC rebuild Module B RUNs 011–013 | USER_CONFIRMED_WORK_ITERATION | recover payloads, verify parent chain, register RUN 013 |
| RFCU2 repository and files | QUARANTINED | no scientific or authorization effect |
| Older unrelated execution lineages | QUARANTINED_PENDING_PROOF | no effect unless exact RFCU1 ancestry is proved |
| RUN 014 | NOT_EXECUTED_NOT_AUTHORIZED | authorization may issue only after RUN 013 registration |

## Current hard boundary

The recovered evidence supports this operational state:

```text
RUN 013 scientific closeout recovered
RUN 013 canonical registration incomplete in GitHub
RUN 014 not yet authorized
```

The repository must not claim that scientific execution never started. It also must not claim that RUN 014 is executable before the recovered RUN 011–013 payloads are imported, hash-verified, and RUN 013 is registered.

## Required recovery sequence

1. Recover the complete v3.0 foundation file set and deduplicate exact copies.
2. Recover and verify RUNs 001–010 against their manifests and ledgers.
3. Recover the complete RUN 011, RUN 012, and RUN 013 payloads named by the delivery ledgers and closeout.
4. Verify every parent hash and internal SHA-256 ledger.
5. Preserve failed attempts and investigations without making them active parents.
6. Register RUN 011, then RUN 012, then RUN 013 in order if their exact payloads pass.
7. Update the canonical state to RUN 013 REGISTERED.
8. Issue a separate versioned RUN 014 authorization.

No step may be skipped by treating a closeout summary as a substitute for the full run payload.

# RFCU1 Run Registry

## Recovery status

The former registry listing only RFCU1-A-000 through A-002 is obsolete. Persistent Work-iteration artifacts establish an executed RFCU1 lineage through RUN 013.

```text
RUN 001-006: lineage identified; complete original payload import pending
RUN 007: 1.0000/CLEAN_PASS; closeout imported; complete payload pending
RUN 008-010: each 1.0000/CLEAN_PASS; complete original payload bundle pending
RUN 011: 1.0000/CLEAN_PASS; exact checkpoint archive migrated and internally hash-verified
RUN 012: 1.0000/CLEAN_PASS; exact checkpoint archive migrated and internally hash-verified
RUN 013: 1.0000/CLEAN_PASS; exact checkpoint archive migrated and internally hash-verified
RUN 014: authorized by the recovered checkpoint; not executable until RUN 001-010 parent recovery and replay close
```

## Exact RUN 011-013 checkpoint

Canonical recovery archive:

`../98_TRANSFER_ARCHIVES/work_iteration/raw_rebuild_uploads_batch_20260726/`

Original checkpoint filename:

`RFC_Rebuild_Module_B_RUNS_011_013_Canonical_Checkpoint_Bundle.zip`

SHA-256:

`e6789d5aa68886727db023e586e60550d16314eff916b248c778045e423a7098`

The checkpoint's internal SHA-256 ledger verifies all 24 run payload files. Its combined verification record is:

```text
exact deterministic checks: 13,002 / 13,002
independent checks:          9,222 / 9,222
ablations:                      42 / 42
Wolfram suites:                   3 / 3 VERIFIED
```

The checkpoint authorizes `RUN_014_MODULE_B_COMMON_ANCESTRY_AND_CONTRACT_FREEZE`.

## Module A dependency order

```text
RUN 001
  -> RUN 002 primitive triad and First Action
  -> RUN 003 convergent and bounded kernel
  -> RUN 004 terminal N-body completion
  -> RUN 005 witnessed route existence and refinement
  -> RUN 006 event/no-loss/memory/scale/stability
  -> RUN 007 integrated theorem, H_A freeze, and TEC_A
```

RUN 007 reports six of six parent runs, 82 of 82 parent component gates, and 12 of 12 identical parent-validator executions. This establishes the lineage but does not waive exact payload recovery for RUN 001-006.

## Required run contents

Every recovered or future run must preserve its exact:

- specification and permitted/forbidden inputs;
- parent/input manifest;
- formal model and theorem;
- deterministic validator;
- independent implementation;
- machine-readable result;
- Wolfram or equivalent symbolic record when used;
- closeout and successor authorization;
- internal SHA-256 ledger.

A summary or downstream replay is not a substitute for original parent bytes.

## Gate law

- Quantitative obligations target `1.000000`.
- Categorical and theorem obligations target `CLEAN_PASS`.
- Any component below `0.950000` is a hard failure requiring triad audit.
- No average may conceal a failed mandatory gate.
- Failed runs remain immutable and cannot become active physical parents.
- Old failures have zero generative authority.

## Execution boundary

The recovered checkpoint's RUN 014 authorization is historically valid. Current execution remains blocked because the complete RUN 001-010 parent payloads and the v3.0 promotion bridge have not yet been migrated and replayed.

RFCU2 is quarantined and has no authority in this registry.

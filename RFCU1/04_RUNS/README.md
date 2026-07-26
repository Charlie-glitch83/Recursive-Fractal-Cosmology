# RFCU1 Run Registry

## Recovery status

The former registry listing only RFCU1-A-000 through A-002 is obsolete. Persistent Work-iteration artifacts establish an executed RFCU1 lineage through a passing RUN 013 closeout.

The current recovery boundary is:

```text
RUNs 001–010: recovered lineage; RUN 008–010 clean checkpoint directly represented
RUN 011: delivery identities recovered; complete payload import pending
RUN 012: delivery identities recovered; complete payload import pending
RUN 013: PASS closeout recovered; canonical registration pending
RUN 014: not authorized
```

See:

- `../00_CANONICAL_STATE/WORK_ITERATION_RECOVERY_INVENTORY.md`
- `../07_AUDITS/WORK_ITERATION_RECOVERY_AUDIT_2026-07-25.md`

## Required run directory contents

Every recovered or future run directory must contain:

- `RUN_SPEC.md` — one scientific question, exact parents, objective, falsifier, permitted and forbidden inputs;
- `INPUT_MANIFEST.sha256` — content hashes of every parent artifact;
- formal model, theorem, or governing contract owned by the run;
- validators and independent implementation evidence;
- immutable machine-readable results;
- source, lineage, dimensional, conservation, no-retune, and reproducibility audit;
- closeout with exact status and successor authorization;
- final internal SHA-256 ledger.

A closeout summary alone is not a substitute for the full payload.

## Gate law

- Formal, structural, source-lineage, no-retune, and reproducibility gates target `1.000000`.
- Any mandatory score below `0.950000` is `FAIL_REQUIRES_ANALYSIS`.
- There is no near-pass category.
- No average may conceal a failed mandatory gate.
- Failed runs remain immutable and quarantined; they cannot become active physical parents.
- Old failures may inform audits but may not determine new-proof outcomes or become active parents.

## Recovery registration rule

RUN 011, RUN 012, and RUN 013 must be imported and registered in order after exact hash and parent-chain verification. A later result cannot retroactively repair or authorize an unregistered parent.

## Next scientific run

RUN 014 is the intended next scientific run after RUN 013, but it remains blocked until a separate versioned authorization is issued following successful RUN 013 registration.

RFCU2 is quarantined and has no authority in this registry.

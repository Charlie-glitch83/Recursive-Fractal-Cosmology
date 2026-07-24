# RFCU1 Run Registry

Only runs explicitly listed in `../00_CANONICAL_STATE/NEXT_AUTHORIZED_RUN.md` may be prepared or executed.

Every run directory must contain:

- `RUN_SPEC.md` — one scientific question, exact parents, objective, falsifier, permitted and forbidden inputs;
- `INPUT_MANIFEST.sha256` — content hashes of every parent artifact;
- `CARRIER_STATE.json` — dormant/active/finite-N/continuum/latent/reactivated state and activation predicate;
- `WOLFRAM/` — exact source code and environment declaration;
- `OUTPUTS/` — immutable machine-readable results;
- `AUDIT.md` — source, lineage, dimensional, conservation, no-retune, and reproducibility gates;
- `CLOSEOUT.md` — PASS, FAIL, BLOCKED, PENDING, or NOT_APPLICABLE with successor authorization.

## Gate law

- Formal, structural, source-lineage, no-retune, and reproducibility gates target `1.000000`.
- Any mandatory score below `0.950000` is `FAIL_REQUIRES_ANALYSIS`.
- There is no near-pass category.
- No average may conceal a failed mandatory gate.
- Failed runs remain immutable and quarantined; they cannot become active physical parents.

## First authorized group

1. `RFCU1-A-000` — repository and source-integrity bootstrap;
2. `RFCU1-A-001` — canonical type, notation, index, and ownership registry;
3. `RFCU1-A-002` — enhanced-kernel and terminal-carrier constitution.

No Big Implosion or other physical-universe run is authorized in this group.

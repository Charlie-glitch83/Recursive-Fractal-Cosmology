# Wolfram Execution Protocol

Wolfram is the principal symbolic and numerical execution engine for RFCU1.

Every theorem-bearing Wolfram run must record:

- Wolfram product and exact version;
- operating system and architecture;
- kernel count and parallel settings;
- `$MaxExtraPrecision`, `WorkingPrecision`, `PrecisionGoal`, and `AccuracyGoal`;
- deterministic random seeds and pseudorandom generator policy;
- solver, integrator, event-location, interpolation, and root-finding methods;
- step-size, recursion, iteration, and stopping policies;
- exact assumptions, domains, units, and dimensional declarations;
- imported file hashes and public-data firewall state;
- wall time, memory use, checkpoint frequency, and artifact count;
- output hashes and independent replay results.

## Proof-carrying numerics

Flagship theorem gates should use rigorous or enclosure-based numerics where practical, including interval or ball arithmetic, certified root isolation, event-time bounds, residual enclosures, conservation-error bounds, and branch-separation certificates.

A reported decimal residual is not by itself a theorem certificate. The run must preserve the equation, arithmetic model, tolerance, error enclosure, and replay evidence that authorize the claim.

## Separation rules

- Exploratory notebooks may not write canonical outputs.
- Canonical runs must be scriptable and noninteractive.
- Public empirical values are forbidden before Module O freezes predictions and Module P opens its read-only comparison branch.
- A failed run remains available for diagnosis but cannot be overwritten or relabeled as a pass.

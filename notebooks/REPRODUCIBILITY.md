# RFC Reproducibility Guide

This folder contains the public simulation and paper-reproduction package for **Recursive Fractal Cosmology: A Generative Ontology of Existence**.

The purpose of this folder is to make the repository readable as a clean reproducibility package, not just a development notebook folder.

## Folder structure

Place these files together in the same `notebooks/` folder:

```text
notebooks/
  RFC_Simulator.ipynb
  SimulationConfigs.json
  Module_G_R_N_S_T_FrozenPacket.json
  ValidationScreens_U_V_W_X_Y2_Z_QG.json
  REPRODUCIBILITY.md
```

## File roles

### `RFC_Simulator.ipynb`

The runnable notebook interface.

It supports two separated paths:

1. **Current paper-reproduction path**
2. **Legacy/development simulator path**

The notebook is intentionally written to distinguish the current frozen-packet architecture from earlier exploratory simulator modules.

### `SimulationConfigs.json`

The runnable module catalog.

It retains the earlier A-Q simulator modules and legacy G/N/R modules for development continuity, while also routing the current paper-reproduction modules.

This file is not the canonical source of the downstream validation results. The canonical validation-screen results are stored in:

```text
ValidationScreens_U_V_W_X_Y2_Z_QG.json
```

### `Module_G_R_N_S_T_FrozenPacket.json`

The canonical frozen-packet spine.

It contains the current deterministic packet and the G/R/N/S/T reproduction structure:

```text
G -> R -> N -> DownstreamPhysicalProjection -> DimensionlessValidation -> S -> T
```

This file should be treated as the canonical internal RFC packet for the current paper-reproduction chain.

### `ValidationScreens_U_V_W_X_Y2_Z_QG.json`

The canonical downstream validation-screen file.

It contains:

```text
U  = One-anchor constant table screen
V  = Precision cosmology compressed-parameter screen
W  = BBN light-abundance proxy screen
X  = CP/EDM bound screen
Y2 = Exploratory particle-sector refinement screen
Z  = Observer/branching/neural/EEG harness
QG = Finite spin-foam transition-amplitude audit
```

The validation screens consume the frozen packet. They do not choose, fit, or retune the frozen packet.

## Canonical paper-reproduction order

Run the current paper-reproduction modules in this order:

```text
G -> R -> N -> DownstreamPhysicalProjection -> DimensionlessValidation -> S -> T -> U -> V -> W -> X -> Y2 -> Z -> QG
```

In the notebook, this can be done with:

```python
run_all_paper()
```

or one component at a time:

```python
run_component("G")
run_component("R")
run_component("N")
run_component("DownstreamPhysicalProjection")
run_component("DimensionlessValidation")
run_component("S")
run_component("T")
run_component("U")
run_component("V")
run_component("W")
run_component("X")
run_component("Y2")
run_component("Z")
run_component("QG")
```

## Legacy/development simulator modules

The earlier A-Q simulator modules and legacy G/N/R modules are retained for continuity and development inspection.

They can be run with:

```python
run_legacy_development_modules()
```

or manually, for example:

```python
run_component("A")
run_component("B")
run_component("Q")
run_component("G_legacy")
run_component("N_legacy")
run_component("R_legacy")
```

These modules should not be confused with the current paper-reproduction spine.

## Active versus legacy modules

### Active current paper modules

The current active paper-reproduction spine is:

```text
G, R, N, DownstreamPhysicalProjection, DimensionlessValidation, S, T, U, V, W, X, Y2, Z, QG
```

### Legacy/deprecated modules

The legacy modules are retained for historical and development continuity:

```text
G_legacy
N_legacy
R_legacy
```

Do not use `G_legacy`, `N_legacy`, or `R_legacy` as active derivation modules for the current paper.

## Global no-retuning rule

The current paper-reproduction path follows this rule:

```text
Frozen packet first; references after; no retuning.
```

References are used only after RFC values are generated, for comparison, auditing, or boundary labeling.

They are not used to retune Module G.

## Module G

Module G is the deterministic frozen-packet source.

It checks the internal relations:

```text
alpha = log(delta) / cycleLength
nu = phaseDepthK * delta^(-4)
epsilon = alpha * nu
```

Module G should report that empirical targets, parameter search, MCMC, and NUTS are not used in the current deterministic packet.

## Module R

Module R is the global closure audit.

It audits the frozen packet. It does not create the packet.

The current package should not contain placeholder Module R values such as:

```text
rawRFLResidualScore = 0.5
sourceCoupledRFLResidualScore = 0.5
residualImprovement = 0.0
tailN18 = 0.0
tailN40 = 0.0
bestLagCorrelation = 0.0
```

If those values appear, the wrong or stale file has been loaded.

## Module N

Module N V2 is the dimensional projection bridge.

It preserves RFC internal dimensional identities and should be interpreted as an internal projection bridge, not as a direct SI/laboratory-constant derivation by itself.

## Modules S and T

Module S is the one-anchor SI bridge.

The electron rest energy is used as the single unit anchor. It is not counted as an independent prediction.

Module T is the dimensionless coupling map.

It maps the internal inverse-energy coupling into a fine-structure-like dimensionless coupling. The raw internal inverse-energy value should not be directly identified with the physical inverse fine-structure constant before the Module T map.

## Module U

Module U is the one-anchor electromagnetic/atomic constant table screen.

It is a completed first-pass validation screen for the one-anchor electromagnetic/atomic sector.

It is not a full derivation of every physical constant.

## Module V

Module V is a compressed precision-cosmology proxy screen.

It is not a full BAO, SNe, or CMB spectra calculation.

Full precision cosmology requires external Boltzmann-solver-level work such as CLASS or CAMB integration.

## Module W

Module W is the BBN light-abundance proxy screen.

It is not a professional full BBN nuclear reaction network.

The phrase “reaction-network proof” should not be used for Module W.

## Module X

Module X is the CP/EDM bound screen.

It checks RFC proxy values against EDM and baryon-asymmetry-style constraints.

It is not a full CKM/PMNS derivation by itself.

## Module Y2

Module Y2 is exploratory particle-sector refinement.

It improved the particle-sector screens, but it used reference-guided map selection.

Therefore, Y2 is **not** final independent validation.

Y2 must be frozen and retested as a future Y3 module before making independent validation claims from it.

Use this boundary:

```text
Y2 = exploratory candidate discovery
Y3 = future frozen retest required
```

## Module Z

Module Z is the observer, branching, neural, and EEG validation harness.

Its neural and EEG quantities should be treated as target signatures or proxy outputs until tested against independent neural/EEG datasets.

## Module QG

Module QG is the finite spin-foam transition-amplitude audit.

It is not a full proof of quantum gravity.

It is a finite audit screen showing that the current RFC quantum-geometry proxy behaves coherently under the stated finite transition-amplitude checks.

## Recommended reviewer workflow

1. Open `RFC_Simulator.ipynb`.
2. Confirm the notebook loads:
   - `SimulationConfigs.json`
   - `Module_G_R_N_S_T_FrozenPacket.json`
   - `ValidationScreens_U_V_W_X_Y2_Z_QG.json`
3. Run `package_audit()`.
4. Run `run_all_paper()`.
5. Inspect G/R/N/S/T first.
6. Inspect U/V/W/X/Y2/Z/QG second.
7. Treat Y2 as exploratory.
8. Inspect A-Q and legacy G/N/R only as development-history modules.

## What counts as a successful package load

A successful current package should show:

```text
SimulationConfigs.json loaded: yes
Frozen packet JSON loaded: yes
Standalone validation screens JSON loaded: yes
Module G found: yes
Module R found: yes
Module N found: yes
Module S found: yes
Module T found: yes
DownstreamPhysicalProjection found: yes
DimensionlessValidation found: yes
Validation screen U found: yes
Validation screen V found: yes
Validation screen W found: yes
Validation screen X found: yes
Validation screen Y2 found: yes
Validation screen Z found: yes
Validation screen QG found: yes
```

If the standalone validation file is missing, the notebook may still be able to load mirrored validation screens from the frozen packet, but the repository should still include the standalone file for reviewer clarity.

## Claim-boundary summary

This repository package supports the following claim:

```text
RFC currently provides a deterministic frozen internal packet and a staged reproducibility package for first-pass validation screens.
```

It does not support the following overclaims:

```text
RFC is fully externally validated across all laboratory physics.
RFC has completed full precision cosmology.
RFC has completed a professional BBN nuclear reaction network.
RFC has completed a full CKM/PMNS derivation.
Y2 is independent validation.
Module QG is a complete proof of quantum gravity.
```

The correct interpretation is:

```text
RFC is a triad-first deterministic generative framework with a frozen internal packet, a reproducible G/R/N/S/T spine, and staged downstream validation screens with explicit boundaries.
```

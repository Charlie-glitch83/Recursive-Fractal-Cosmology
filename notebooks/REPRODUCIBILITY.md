# RFC Reproducibility Guide -- Revised Presentation 29 Package

This folder contains the public simulation and paper-reproduction package for **Recursive Fractal Cosmology: The Triadic Emergence of Existence -- A Triadic Theorem**.

This revision updates the repository package to include the new theorem-layer additions:

```text
W2-R    = Revised triadic-weight BBN closeout
W3      = Grouped post-BBN nucleosynthesis cascade
W4      = Element-resolved solar-abundance screen
CR-Trace = Global collapse-rebirth inheritance trace audit
```

The older `W` light-abundance screen is retained as a **historical scalar-lane diagnostic** because it explains the Li7 wall that W2-R fixes. It should not be treated as the active revised BBN result.

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

The runnable notebook interface. It supports two separated paths:

1. **Current revised paper-reproduction path**
2. **Legacy/development simulator path**

The notebook distinguishes the current frozen-packet architecture from earlier exploratory simulator modules and now exposes W2-R, W3, W4, and CR-Trace in the paper-reproduction sequence.

### `SimulationConfigs.json`

The runnable module catalog. It retains earlier A-Q development modules and legacy G/N/R modules for continuity while routing the revised Presentation 29 paper-reproduction modules.

This file is not the canonical source of downstream validation results. The canonical validation-screen results are stored in:

```text
ValidationScreens_U_V_W_X_Y2_Z_QG.json
```

### `Module_G_R_N_S_T_FrozenPacket.json`

The canonical frozen-packet spine. It contains the current deterministic packet and the G/R/N/S/T reproduction structure:

```text
G -> R -> N -> DownstreamPhysicalProjection -> DimensionlessValidation -> S -> T
```

It also mirrors downstream validation screens for backward compatibility. The canonical downstream validation file remains `ValidationScreens_U_V_W_X_Y2_Z_QG.json`.

### `ValidationScreens_U_V_W_X_Y2_Z_QG.json`

The canonical downstream validation-screen file. It now contains:

```text
U       = One-anchor constant table screen
V       = Precision cosmology compressed-parameter screen
W       = Historical scalar-lane BBN/Li7 diagnostic, superseded by W2-R
W2-R    = Revised triadic-weight BBN closeout
W3      = Grouped post-BBN nucleosynthesis cascade
W4      = Element-resolved solar-abundance screen
CR-Trace = Global collapse-rebirth inheritance trace audit
X       = CP/EDM bound screen
Y2      = Exploratory particle-sector refinement screen
Z       = Observer/branching/neural/EEG harness
QG      = Finite spin-foam transition-amplitude audit
```

The validation screens consume the frozen packet. They do not choose, fit, or retune the frozen packet.

## Canonical revised paper-reproduction order

Run the current revised paper-reproduction modules in this order:

```text
G -> R -> N -> DownstreamPhysicalProjection -> DimensionlessValidation -> S -> T -> U -> V -> W -> W2-R -> W3 -> W4 -> CR-Trace -> X -> Y2 -> Z -> QG
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
run_component("W")        # historical scalar-lane diagnostic
run_component("W2R")      # revised W2-R BBN closeout
run_component("W3")       # grouped post-BBN cascade
run_component("W4")       # element-resolved solar abundance screen
run_component("CRTrace")  # global collapse-rebirth trace audit
run_component("X")
run_component("Y2")
run_component("Z")
run_component("QG")
```

## Global no-retuning rule

The current paper-reproduction path follows this rule:

```text
Frozen packet first; references after; no retuning.
```

References are used only after RFC values are generated, for comparison, auditing, or boundary labeling. They are not used to retune Module G.

## W versus W2-R

`W` is now explicitly historical. It records the scalar-lane BBN/Li7 failure so reviewers can see what was fixed.

`W2-R` is the revised triadic-weight BBN closeout. It reports:

```text
OldScalarLi7OverObserved = 3.12534
TriadicLi7OverObserved = 0.999643
Li7SuppressionFactorVsOldScalar = 3.12645
RealWorldPassedSpeciesCount = 4 of 4
InternalBBNProxyStatus = PASS
ExternalPublicCodeStatus = PENDING
```

W2-R closes the internal BBN theorem/proxy lane. It does not claim completed external BBN validation until implemented in public BBN reaction-network code.

## W3 and W4

`W3` carries the W2-R seed into a grouped post-BBN nucleosynthesis cascade. It preserves `QV(CIF) -> RFL`, conserves mass, and passes grouped solar-shape robustness screens.

`W4` resolves the grouped cascade into an element-resolved solar-abundance comparison screen. It reports shape correlation near 0.995 and mean absolute residual near 0.32 dex, with spallation and high-Z rarity ablations demonstrating mechanism specificity.

Both W3 and W4 remain internal theorem/proxy screens until tested against external stellar-yield, supernova, neutron-star-merger, and galactic chemical-evolution network models.

## CR-Trace

`CRTrace` evaluates whether the RFC module sequence functions as a collapse-rebirth inheritance chain:

```text
G -> R -> N -> DownstreamPhysicalProjection -> W2-R -> W3 -> W4 -> CR-Trace
```

It reports:

```text
InternalCollapseRebirthTraceStatus = PASS
RealWorldTraceScreenStatus = PASS
ExternalFullValidationStatus = PENDING
GlobalCollapseRebirthTraceScore = 0.9215536385594688
```

CR-Trace does not claim direct observation of a prior cosmic cycle. It is an internal trace audit with real-world comparison screens.

## Legacy/development simulator modules

The earlier A-Q simulator modules and legacy G/N/R modules are retained for continuity and development inspection.

They can be run with:

```python
run_legacy_development_modules()
```

These modules should not be confused with the current revised paper-reproduction spine.

## Active current paper modules

The current active paper-reproduction spine is:

```text
G, R, N, DownstreamPhysicalProjection, DimensionlessValidation, S, T, U, V, W, W2-R, W3, W4, CR-Trace, X, Y2, Z, QG
```

## Legacy/deprecated modules

The legacy modules are retained for historical and development continuity:

```text
G_legacy
N_legacy
R_legacy
```

Do not use `G_legacy`, `N_legacy`, or `R_legacy` as active derivation modules for the current paper.

## Claim-boundary summary

This repository package supports the following claim:

```text
RFC currently provides a deterministic frozen internal packet and a staged reproducibility package for revised theorem/proxy screens, including W2-R, W3, W4, and CR-Trace.
```

It does not support the following overclaims:

```text
RFC is fully externally validated across all laboratory physics.
RFC has completed full precision cosmology.
RFC has completed public-code BBN validation.
RFC has completed stellar-yield, supernova, neutron-star-merger, or galactic chemical-evolution network validation.
RFC has directly observed a prior cosmic cycle.
RFC has completed a full CKM/PMNS derivation.
Y2 is independent validation.
Module QG is a complete proof of quantum gravity.
```

The correct interpretation is:

```text
RFC is a triad-first deterministic generative framework with a frozen internal packet, a reproducible G/R/N/S/T spine, revised internal theorem/proxy closeouts for W2-R/W3/W4/CR-Trace, and explicit boundaries for future external validation.
```

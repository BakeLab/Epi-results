# Global lower bound for waterund36

For the original continuous [MINLPLib waterund36 model](https://minlplib.org/waterund36.html), the final certificate establishes

**f* ≥ 662.80702839.**

It excludes every feasible point at or below the exact rational cutoff 6628070283996671/10000000000000. The displayed bound is rounded downward. The known feasible value 662.8070384 leaves an absolute gap of about 0.00001001.

## Mathematical extension

Let Fᵢⱼ be process-to-process flow, tᵢ the sum of all actual outgoing flows from process i, Wᵢ its throughput and Cᵢₖ its outlet concentration. Let aᵢ and aᵢₖ be external water and external contaminant mass, and Lᵢₖ the positive process load. The certificate permits original-equation residuals of τ = 10⁻⁸, giving a relaxation of the exactly feasible model.

The original water and mass balances imply

|tᵢ − ΣⱼFⱼᵢ − aᵢ| ≤ 2τ,

tᵢCᵢₖ − ΣⱼFⱼᵢCⱼₖ − aᵢₖ − Lᵢₖ = eᵢₖ,

with |eᵢₖ| ≤ τ(Cmaxᵢₖ + 2). The positive loads and finite concentration bounds imply tᵢ > 0.

Define Qᵢⱼ = Fᵢⱼ/tᵢ. Its row sums are at most one, including every non-process outlet. A closed recurrent class would have no export; summing its mass balances would make a sum of positive loads and nonnegative imports vanish. The load bounds dominate the allowed residuals, so this is impossible. Hence ρ(Q) < 1 and H = (I − Qᵀ)⁻¹ is entrywise nonnegative.

Water-source labels are H times the external-source vectors; load labels are columns of H. Route each label along an outgoing arc in proportion to that arc’s share of tᵢ. This satisfies the extension’s exact conservation and bilinear routing identities. Physical water and mass differ from the label totals by H times their original residuals. In particular, each load-label total obeys

Hᵢₗ ≤ minₖ tUpperᵢ Cmaxᵢₖ / (Lₗₖ − τ(Cmaxₗₖ + 2)).

The denominators are positive for this instance. These bounds provide finite boxes containing every lifted feasible point. Variable error envelopes use the load labels directly. Their coefficients are rounded downward on nonnegative variables, which preserves containment.

## Exact bound certificate

`original-model.json` contains the 324-variable model, its objective and 239 constraints. The other model files contain the explicit scaled rows, bilinear products, variable maps and finite boxes of the relaxation. JSON numerical coefficients are interpreted as their exact binary64 rational values; rational endpoints are stored as strings. The model’s integer coefficients and power-of-two scalings are exact.

The proof first applies 76 coordinate-bound certificates in the incumbent sublevel set. It then uses the lower objective cutoff and the variable error envelopes. The 71 target coordinate certificates and rational bound propagation are replayed twice at the outward-rounded cutoff 662.8070283996672. A final lower coordinate bound exceeds its upper bound.

For each coordinate certificate, form the linear relaxation from the stated rows and the four McCormick inequalities for each bilinear product in the current box. For a minimization objective cᵀx, row multipliers y give the exact support

yᵀb + min_{L ≤ x ≤ U}(c − Aᵀy)ᵀx.

Equality multipliers are unrestricted. For rows Aᵢx ≤ bᵢ, clamp the multiplier to be nonpositive. The remaining box minimum is the sum of each residual coefficient times Lⱼ or Uⱼ according to its sign. The stored duals use row scaling max(1, max|aᵢⱼ|); divide each multiplier by its corresponding scale before evaluating the original rows. McCormick row scales use the root box. All support evaluations and propagation comparisons use exact rational arithmetic, with outward rounding of updated binary64 endpoints.

`root-proof-steps.json` and `target-proof-steps.json` specify the certificate’s logical order. The accompanying NPZ files contain only dual vectors, boxes and coordinate identities. `conclusion.json` gives the exact cutoff, final conflicting bounds and rational support; `final-witness.npz` contains the corresponding box and dual.

Every exactly feasible point in the incumbent sublevel set has a lift into this relaxation. Points outside that sublevel set already have larger objective. The contradiction therefore establishes the lower bound for the original model.

## Files

The archive contains final mathematical proof data and a checksum manifest. It does not require an optimization search to interpret the support inequalities. The 147 supplied dual vectors serve as fixed proof witnesses; their numerical origin is irrelevant once their exact support is checked.

The comparison is with MINLPLib’s listed lower bound 655.5441707 and [Castro’s later global-optimization study](https://doi.org/10.1021/acs.iecr.3c00191), whose rounded No-sBB gap implies a lower bound around 655.79. The result improves the lower bound, while retaining the known feasible upper value.

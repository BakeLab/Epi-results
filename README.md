<p align="center"><img src="assets/epi-logo.svg" width="176" alt="Épi logo"></p>
<h1 align="center">Épi Results</h1>
<p align="center">Final constructions, sharper bounds and mathematical proofs.</p>
<p align="center">
  <a href="mathematics">Mathematics</a> ·
  <a href="#constructions">Constructions</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="#citation">Citation</a> ·
  <a href="https://bakeai.inc/research/articles/introducing-epi/">Introducing Épi</a>
</p>

Épi is Bake AI’s autonomous research harness. This repository contains its final research artifacts: **20 numerical bound records, one theorem extension and 106 released constructions**. Every result has a comparison source and a description of what was verified.

Comparisons were reviewed on **2026-09-11**. Construction standings distinguish improvements over current registries, already listed records, matching values and superseded results.

## Selected results

| Problem | Published comparison | Épi | Final artifact |
| :-- | :-- | :-- | :-- |
| **Polyomino growth** | Upper bound 4.5238 | **4.29569** | [Exact recurrence certificate](mathematics/klarner) |
| **n-queens constant** | Interval width 3.30 × 10⁻⁷ | **3.9367 × 10⁻⁹**, about 84× narrower | [Lower and upper witnesses](mathematics/nqueens) |
| **Tuza’s inequality** | K₈ split graphs with at most two active neighborhood types | **At most three types, with arbitrary multiplicities** | [Proof and independent checker](mathematics/tuza) |
| **Water-network design** | MINLPLib lower bound 655.5441707 | **662.80702839** | [Global lower-bound certificate](mathematics/waterund36) |
| **Cohn–Elkies method** | Sharpness unresolved in dimensions 10 and 11 | **Non-sharp in both dimensions** | [Exact dual certificates](mathematics/cohn-elkies) |
| **34 pentagons in a triangle** | Triangle side 12.98141 | **12.97563735803487** | [Complete arrangement](records/pentagons/penintri_n34) |
| **Vehicle routing, XL-n1048-k237** | Route length 380107 | **380092** | [All 238 routes](records/vehicle-routing/cvrp_xl_n1048_k237) |

## Mathematics

| Area | Final results |
| :-- | :-- |
| **Growth and entropy** | [Klarner’s constant](mathematics/klarner), [dimer constant](mathematics/dimer), [n-queens asymptotics](mathematics/nqueens) |
| **Combinatorics** | [Wellens’ bound](mathematics/wellens), [Spencer discrepancy](mathematics/spencer-discrepancy), [Ramsey c₄,₅](mathematics/ramsey-c45), [Bₕ[g] coefficients](mathematics/bhg), [Tuza’s inequality](mathematics/tuza) |
| **Geometry and dynamics** | [Cohn–Elkies bounds](mathematics/cohn-elkies), [quartic Feigenbaum dimension](mathematics/feigenbaum) |
| **Optimization and information** | [MAX-4-CUT hardness](mathematics/max4cut), [water-network lower bound](mathematics/waterund36), [quantum-capacity thresholds](mathematics/quantum-capacity) |

The [mathematical result table](mathematics/README.md) gives every value. Interval endpoints and decimal bounds are rounded outward. Tuza is a theorem extension for the stated graph class; waterund36 improves the global lower bound while retaining the known feasible upper value.

## Constructions

The 106 final constructions have the following current standings:

| Standing | Entries |
| :-- | --: |
| Improve the reviewed registry | **89** |
| Already listed records | **11** |
| Match the current registry precision | **1** |
| Have been superseded | **3** |
| Improve a named benchmark reference | **2** |

| Category | Entries | Objective |
| :-- | --: | :-- |
| [Circles in a quadrant](records/circular-quadrant) | 46 | Larger common radius |
| [Balls in four dimensions](records/four-dimensional-balls) | 36 | Larger common radius |
| [Circles in a semicircle](records/semicircle) | 9 | Larger common radius |
| [Pentagons in a triangle](records/pentagons) | 9 | Smaller enclosing triangle |
| [Circles in an octagon](records/octagon) | 1 | Larger common radius |
| [Vehicle routing](records/vehicle-routing) | 1 | Shorter feasible routes |
| [Spin-glass energy](records/spin-glass) | 1 | Lower energy for the specified instance |
| [Qubit routing](records/qubit-routing) | 1 | Fewer extra two-qubit gates across the same 61 circuits |
| [Third autocorrelation inequality](records/autocorrelation) | 1 | Smaller signed-convolution objective |
| [Zhang–Zagier essential minimum](records/zhang-zagier) | 1 | Smaller certified upper bound |

The nine pentagon constructions are listed by Friedman, credited to **Yue Huang**. CVRPLIB lists the vehicle-routing value; EinsteinArena lists the autocorrelation result under **Poolish**, the project’s former name. Semicircle N = 159, 205 and 244 have been surpassed; N = 202 matches the latest published precision. Every entry retains its final construction and current comparison.

## Downloads

- **[Construction index · CSV](data/records.csv)** / [JSON](data/records.json)
- **[Mathematical results · JSON](data/mathematics.json)**
- **[Final certificate downloads](https://github.com/HowieHwong/Epi-results/releases/tag/v1.1.0)**, including the large n-queens upper witness and water-network proof bundle
- **[Download sizes and checksums](data/downloads.json)** · [Repository file manifest](checksums.sha256)

Small final witnesses are stored beside their result pages. Larger files are separate Release assets, so cloning the repository stays lightweight. The collection contains final research artifacts and proof materials only.

## Citation

```bibtex
@misc{epiteam2026results,
  author       = {{Epi Team}},
  title        = {{\'E}pi Results},
  year         = {2026},
  howpublished = {GitHub},
  url          = {https://github.com/HowieHwong/Epi-results}
}
```

Each result page cites the research it builds on. Comparisons may become outdated; please [contact us](https://bakeai.inc/contact/) if you know a stronger result.

---

<p align="center"><strong>Bake AI · Épi</strong></p>

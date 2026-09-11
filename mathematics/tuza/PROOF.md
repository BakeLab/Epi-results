# Tuza’s inequality with three neighborhood types

Let G be a finite simple split graph with a specified partition V = C ⊔ I, where C induces K₈ and I is independent. Suppose vertices of I with at least two neighbors in C have at most three distinct neighborhoods. Each neighborhood may occur with arbitrary multiplicity. Then

**τ△(G) ≤ 2ν△(G)**,

where τ△ is the minimum number of edges meeting every triangle, and ν△ is the maximum number of edge-disjoint triangles.

## Classification

An independent-set vertex with fewer than two clique neighbors belongs to no triangle and can be removed. Cases with at most two active neighborhood types follow from [Zeng’s Theorem 1](https://www.preprints.org/manuscript/202608.1304).

For three distinct active types, represent each of the eight clique vertices by a three-bit word indicating its neighborhood memberships. Enumerate multisets of eight such words, then identify triples differing by a permutation of the three types. There are **872 classes**.

- **35 classes** have nested neighborhoods and are threshold graphs. Apply [the threshold-graph theorem](https://doi.org/10.46298/dmtcs.7660).
- **277 further classes** satisfy the following clique-cut criterion. Let Q be the union of all clique edges within an active neighborhood. If a cut contains at least 12 edges of K₈ outside Q, deleting the other clique edges gives a triangle cover of size at most 16. The following eight edge-disjoint triangles lie in K₈:

  (0,1,7), (0,2,3), (0,4,6), (1,2,6), (1,3,5), (2,4,5), (3,4,7), (5,6,7).

  Thus τ△ ≤ 16 ≤ 2ν△. The remaining clique edges form a subgraph of a cut, and no edge inside an active neighborhood remains, so every triangle is covered.
- The remaining **560 classes** are verified by the accompanying exact certificate.

## Finite certificate

For each profile, the certificate covers every integer multiplicity vector in [0,28]³ with boxes. Each box supplies a triangle cover F of the graph at its upper corner and an edge-disjoint triangle packing P at its lower corner, with |F| ≤ 2|P|.

Graphs at intermediate multiplicities embed between these two endpoint graphs. Consequently,

τ△(Gₘ) ≤ τ△(G_hi) ≤ |F| ≤ 2|P| ≤ 2ν△(G_lo) ≤ 2ν△(Gₘ).

The certificate contains **18,444 boxes**. The checker enumerates every triangle, verifies every cover and packing, and verifies complete coverage of the integer box. It independently regenerates the 872-class classification.

## Arbitrary multiplicities

Every triangle contains a clique edge, so any edge-disjoint packing has at most 28 triangles. Such a packing uses at most 28 independent vertices of any one type. Relabeling twins therefore preserves ν△ when each multiplicity is truncated at 28.

All 28 clique edges form a triangle cover. Let F be a minimum cover of the truncated graph. If |F| = 28, adding twins cannot increase τ△ above 28, and monotonicity gives equality. If |F| < 28, among the 28 copies of any saturated type, one has no incident edge in F. Every clique edge inside its neighborhood must therefore belong to F. That already covers all triangles through additional twins, without adding edges to F. This holds simultaneously for every saturated type, so truncation also preserves τ△.

The finite certificate proves the stated inequality for arbitrary multiplicities.

## Verification

On Linux with Python 3.10+ and NumPy:

```sh
python3 verify.py
```

The checker reads `certificate.json.gz` and reports 872 classified profiles, 560 certified profiles and 18,444 boxes. The analytic arguments above cover the other classes and extend the certificate to arbitrary multiplicities.

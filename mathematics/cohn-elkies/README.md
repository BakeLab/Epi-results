# Cohn–Elkies linear-programming bounds

Improved lower bounds on the best upper bound attainable by the Cohn–Elkies method, in dimensions 9 through 13.

| Reference | Épi |
| :-- | :-- |
| 1/20, 1/24, 1/24, 1/24, 1/28 | **≈ 0.057375415, 0.056433847, 0.057731802, 0.058740866, 0.063876952** |

## Final artifacts

One final dual vector for each dimension, with exact bound values. Values use center-density normalization.

- [bound-d10.json](bound-d10.json)
- [bound-d11.json](bound-d11.json)
- [bound-d12.json](bound-d12.json)
- [bound-d13.json](bound-d13.json)
- [bound-d9.json](bound-d9.json)
- [mu/Mu_10_10_sqrt20.txt](mu/Mu_10_10_sqrt20.txt)
- [mu/Mu_11_10_sqrt20.txt](mu/Mu_11_10_sqrt20.txt)
- [mu/Mu_12_8_4.txt](mu/Mu_12_8_4.txt)
- [mu/Mu_13_8_4.txt](mu/Mu_13_8_4.txt)
- [mu/Mu_9_10_sqrt20.txt](mu/Mu_9_10_sqrt20.txt)

## Why dimensions 10 and 11 matter

| Dimension | Actual packing density is at most | Best Cohn–Elkies bound is at least | Minimum gap |
| --: | --: | --: | --: |
| 10 | 0.05623564 | 0.05643384749592475 | 0.35% |
| 11 | 0.05664513 | 0.05773180210045803 | 1.92% |

These intervals do not meet. Even a perfect optimization of the Cohn–Elkies program would still leave a gap above the actual density. The comparison bounds are discussed in [Li, Sections 8.4–8.5](https://arxiv.org/html/2206.09876v3) and the stronger packing bounds come from [Cohn, de Laat and Salmon](https://arxiv.org/abs/2206.15373).

[Research source](https://arxiv.org/abs/2206.09876) · [Result data](result.json) · [All mathematical results](../README.md)

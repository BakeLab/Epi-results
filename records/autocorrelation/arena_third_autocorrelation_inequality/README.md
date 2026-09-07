# Third autocorrelation inequality: arena_third_autocorrelation_inequality

Lower the upper bound obtained from the autoconvolution of a step function.

| Reference | Épi | Direction |
| :-- | :-- | :-- |
| 1.45157186389021 | **1.45080663950528** | Lower is better |

The reported quantity is `abs(2*n*max(convolve(h,h))/sum(h)^2)`. The absolute value is outside the maximum. The cited literature value is 1.4557; the table compares against the stronger EinsteinArena baseline.

[Construction](construction.json) · [Full-precision result](result.json) · [Source](https://einsteinarena.com/problems/third-autocorrelation-inequality)

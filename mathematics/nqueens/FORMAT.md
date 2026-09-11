# Final n-queens witnesses

The enclosing interval is [1.9440010223327, 1.9440010262694], with both endpoints rounded outward from the checked bounds.

`lower-witness.json.gz` contains n = 65536 and `v_b64`, the base64-encoded little-endian float64 dual vector.

`upper-witness.json` describes n = 4096 and a vector of 67,141,628 entries. Download `upper-witness.f64.zlib` from the linked Release. It is the zlib-compressed little-endian float64 vector represented by the final witness. Its first 67,108,864 entries are triangle coordinates; the remaining 32,764 are diagonal slacks. The upper-bound evaluation includes an exact transportation projection followed by directed-rounding entropy evaluation.

For example, the upper vector can be read on Linux with NumPy:

```python
import json, zlib
from pathlib import Path
import numpy as np

description = json.loads(Path("upper-witness.json").read_text())
x = np.frombuffer(zlib.decompress(Path(description["data"]).read_bytes()), dtype="<f8")
assert x.size == description["x_length"]
```

Decoding loads a large array into memory. The download size and SHA-256 checksum are recorded in `result.json`. The witness uses the formulation of [Nobel, Agrawal and Boyd](https://web.stanford.edu/~boyd/papers/n_queens.html).

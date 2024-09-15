
# DIEM: Dimension Insensitive Euclidean Metric (DIEM)

This repository implements the distance measure metric: DIEM.

source: [https://arxiv.org/abs/2407.08623](https://arxiv.org/abs/2407.08623)

Note: Please cite the original paper.

## Development

Please feel free to suggest code & math fixes if found.

```bash
make all
```

## Proof

For the full proof refer: [Euclidean Distance: Expectation, Variance & Std. Deviation](documents/proof.pdf)

### Proposed Fix: Normalized Euclidean Distance Formula

The normalized Euclidean distance \( D_{\text{norm}}(\mathbf{X}, \mathbf{Y}) \) is computed as follows:

\[
D_{\text{norm}}(\mathbf{X}, \mathbf{Y}) = \frac{D(\mathbf{X}, \mathbf{Y}) - \mathbb{E}[D(\mathbf{X}, \mathbf{Y})]}{\sigma(D(\mathbf{X}, \mathbf{Y}))}
\]

Where:

- \( D(\mathbf{X}, \mathbf{Y}) \) is the standard Euclidean distance between vectors \( \mathbf{X} \) and \( \mathbf{Y} \).
- \( \mathbb{E}[D(\mathbf{X}, \mathbf{Y})] \approx (v_{\text{max}} - v_{\text{min}}) \cdot \sqrt{\frac{2N}{\pi}} \) is the expected Euclidean distance in high dimensions.
- \( \sigma(D(\mathbf{X}, \mathbf{Y})) \approx \frac{(v_{\text{max}} - v_{\text{min}})}{\sqrt{N}} \cdot \sqrt{1 - \frac{2}{\pi}} \) is the standard deviation of the Euclidean distance in high dimensions.

### Usage

The `DIEM` function computes the normalized Euclidean distance between two tensors, accounting for the dimensionality of the input vectors, which ensures that the distance metric remains robust and interpretable in high-dimensional spaces. The function accepts the following arguments:

- `source`: The source tensor of shape `(N, D)`.
- `target`: The target tensor of shape `(M, D)`.
- `v_max`: Maximum element value of the tensors.
- `v_min`: Minimum element value of the tensors.

### Example

```python
import torch
from diem import DIEM

# Example tensors
source = torch.rand(100, 50)  # 100 vectors of dimension 50
target = torch.rand(200, 50)  # 200 vectors of dimension 50

# Compute DIEM distance
diem_distance = DIEM(source, target)
print(diem_distance)

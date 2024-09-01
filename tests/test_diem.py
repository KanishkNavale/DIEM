import unittest

import torch

from diem import DIEM


class TestDiem(unittest.TestCase):
    def test_high_dim_vectors(self):
        pick_index = 3

        a = torch.randn(10, 1000_000)
        b = a[pick_index].unsqueeze(dim=0)

        result = DIEM(a, b)
        most_similar = torch.argmin(result, dim=0)

        self.assertEqual(most_similar, pick_index)


if __name__ == "__main__":
    unittest.main()

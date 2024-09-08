import math

import torch


def DIEM(
    source: torch.Tensor,
    target: torch.Tensor,
    v_max: float = 1.0,
    v_min: float = 0.0,
) -> torch.Tensor:
    """
    Source: https://arxiv.org/pdf/2407.08623

    Computes the DIEM distance between two tensors.
    DIEM: Dimension Insenstiive Embedding Metric

    Args:
        source (torch.Tensor): The source tensor of shape (N, D).
        target (torch.Tensor): The target tensor of shape (M, D).
        v_max (float, optional): The element-wise max. value of the tensors. Defaults to 1.0.
        v_min (float, optional): The element-wise min. value of the tensors. Defaults to 0.0.

    Returns:
        torch.Tensor: The DIEM distance between the source and target tensors of shape (N, M).

    """
    if source.size(1) != target.size(1):
        raise ValueError(
            "The source and target tensors must have the same dimension."
        )
    N = source.size(1)

    euclidean_dist = torch.cdist(source, target, p=2)

    expected_value = math.sqrt(N / 6.0) * (v_max - v_min)
    variance = N * (31.0 / 180.0) * (v_max - v_min) ** 4

    return (v_max - v_min) / variance * (euclidean_dist - expected_value)

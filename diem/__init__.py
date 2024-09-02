import math

import torch


def DIEM(source: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """
    Source: https://arxiv.org/pdf/2407.08623

    Computes the DIEM distance between two tensors.
    DIEM: Dimension Insenstiive Embedding Metric

    Args:
        source (torch.Tensor): The source tensor of shape (N, D).
        target (torch.Tensor): The target tensor of shape (M, D).

    Returns:
        torch.Tensor: The DIEM distance between the source and target tensors of shape (N, M).

    """
    if source.size(1) != target.size(1):
        raise ValueError(
            "The source and target tensors must have the same dimension."
        )
    D = source.size(1)

    v_min = torch.min(torch.cat([source, target]))
    v_max = torch.max(torch.cat([source, target]))

    euclidean_dist = torch.cdist(source, target, p=2)

    expected_value = math.sqrt(D / 6) * (v_max - v_min)
    variance = torch.var(euclidean_dist)

    return (v_max - v_min) / variance * (euclidean_dist - expected_value)

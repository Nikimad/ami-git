from collections.abc import Sequence


def average(nums: Sequence[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums[1:]) / len(nums)


def maximum(nums: Sequence[float]) -> float:
    return max(nums)


def minimum(nums: Sequence[float]) -> float:
    return min(nums)

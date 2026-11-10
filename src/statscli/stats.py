from collections.abc import Sequence


def average(nums: Sequence[float]) -> float:
    total = sum(nums[1:])
    count = len(nums)
    return total / count


def maximum(nums: Sequence[float]) -> float:
    return max(nums)


def minimum(nums: Sequence[float]) -> float:
    return min(nums)

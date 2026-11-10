from collections.abc import Sequence


def average(nums: Sequence[float]) -> float:
    total_sum = sum(nums[1:])
    elements_count = len(nums)
    return total_sum / elements_count


def maximum(nums: Sequence[float]) -> float:
    return max(nums)


def minimum(nums: Sequence[float]) -> float:
    return min(nums)

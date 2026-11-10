import pytest

from statscli.stats import average, maximum, minimum


def test_average_basic() -> None:
    assert average([1, 2, 3]) == pytest.approx(2.0)


def test_average_single() -> None:
    assert average([5]) == pytest.approx(5.0)


def test_average_empty() -> None:
    assert average([]) == 0.0


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([3, 9, 1], 9),
        ([-5, -2, -9], -2),
        ([7], 7),
    ],
)
def test_maximum(nums: list[float], expected: float) -> None:
    assert maximum(nums) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([3, 9, 1], 1),
        ([-5, -2, -9], -9),
        ([7], 7),
    ],
)
def test_minimum(nums: list[float], expected: float) -> None:
    assert minimum(nums) == expected

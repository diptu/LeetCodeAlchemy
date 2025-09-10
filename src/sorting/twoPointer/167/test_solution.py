"""Pytest module for Solution.two_sum implementations."""

from typing import List
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "numbers, target",
    [
        ([2, 7, 11, 15], 9),  # Basic case
        ([11, 13, 15, 17], 28),  # Multiple valid answers
        ([1, 2, 3, 4, 5], 9),  # Last two elements
        ([1, 2, 3, 4, 5], 3),  # First two elements
        ([3, 24, 50, 79, 88, 150, 345], 200),  # Large gap
    ],
)
def test_two_sum_sorted(numbers: List[int], target: int) -> None:
    """Test two_sum method on sorted arrays (two-pointer solution)."""
    solution = Solution()
    result = solution.two_sum(numbers, target)

    if not result:  # safety fallback
        pytest.fail("No solution returned")

    i, j = result[0] - 1, result[1] - 1
    assert 0 <= i < len(numbers)
    assert 0 <= j < len(numbers)
    assert i != j
    assert numbers[i] + numbers[j] == target


def test_single_pair() -> None:
    """Test array with exactly two elements."""
    solution = Solution()
    numbers = [1, 2]
    target = 3
    result = solution.two_sum(numbers, target)
    assert result == [1, 2]


def test_no_solution() -> None:
    """Test when no valid pair exists (should return empty list)."""
    solution = Solution()
    numbers = [1, 2, 4, 8]
    target = 20
    result = solution.two_sum(numbers, target)
    assert result == []

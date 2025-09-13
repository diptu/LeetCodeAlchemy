"""
Unit tests for Solution.splitArray using pytest.

Covers standard cases, edge cases, and performance-oriented scenarios.

Time Complexity
---------------
O(n log(sum(nums))) per test case.

Space Complexity
----------------
O(1).
"""

import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 2, 5, 10, 8], 2, 18),  # example case
        ([1, 2, 3, 4, 5], 2, 9),  # even split
        ([1, 4, 4], 3, 4),  # k equals len(nums)
        ([1, 4, 4], 1, 9),  # k = 1 (whole array)
        ([2, 3, 1, 2, 4, 3], 5, 4),  # many subarrays
    ],
)
def test_split_array(nums: list[int], k: int, expected: int) -> None:
    """
    Test splitArray with multiple scenarios.

    Parameters
    ----------
    nums : list[int]
        Input array of positive integers.
    k : int
        Number of subarrays.
    expected : int
        Expected minimized largest subarray sum.
    """
    sol = Solution()
    result = sol.splitArray(nums, k)
    assert result == expected


def test_single_element() -> None:
    """
    Test when nums has only one element.

    Expected result is that element itself.
    """
    sol = Solution()
    assert sol.splitArray([42], 1) == 42


def test_all_equal_elements() -> None:
    """
    Test when all elements are equal.

    Result should balance subarrays evenly.
    """
    sol = Solution()
    assert sol.splitArray([5, 5, 5, 5], 2) == 10
    assert sol.splitArray([5, 5, 5, 5], 4) == 5


def test_large_input() -> None:
    """
    Test performance with large input size.

    Ensures function handles upper constraints efficiently.
    """
    sol = Solution()
    nums = [1] * 10_000
    result = sol.splitArray(nums, 50)
    # Each subarray should have about 200 elements -> sum ≈ 200
    assert result == 200

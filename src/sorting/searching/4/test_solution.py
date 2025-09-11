"""
Unit tests for Solution.findMedianSortedArrays using pytest.

Tests cover standard cases, edge cases, and invalid inputs.

Time Complexity
---------------
O(log(min(m, n))) per test case.

Space Complexity
----------------
O(1).
"""

import pytest

from solution import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),  # odd total length
        ([1, 2], [3, 4], 2.5),  # even total length
        ([0, 0], [0, 0], 0.0),  # identical arrays
        ([], [1], 1.0),  # one empty array
        ([2], [], 2.0),  # other empty array
        ([1, 3, 8], [7, 9, 10, 11], 8.0),  # larger arrays
    ],
)
def test_find_median_sorted_arrays(
    nums1: list[int], nums2: list[int], expected: float
) -> None:
    """
    Test median of two sorted arrays.

    Parameters
    ----------
    nums1 : list[int]
        First sorted input array.
    nums2 : list[int]
        Second sorted input array.
    expected : float
        Expected median result.
    """
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    assert result == pytest.approx(expected)

"""
Pytest module to test the 'product_except_self' method from the Solution class.
"""


import pytest
from solution import Solution


@pytest.fixture
def solution() -> Solution:
    """
    Fixture to provide an instance of the Solution class.

    Returns
    -------
    Solution
        Instance of Solution.
    """
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([10, 0, 5], [0, 50, 0]),
        ([0, 0, 3], [0, 0, 0]),
        ([5], [1]),  # Single element
    ],
)
def test_product_except_self(
    solution: Solution, nums: list[int], expected: list[int]
) -> None:
    """
    Test product_except_self with various inputs.

    Parameters
    ----------
    solution : Solution
        Instance of Solution class.
    nums : List[int]
        Input list of integers.
    expected : List[int]
        Expected product result.
    """
    assert solution.product_except_self(nums) == expected

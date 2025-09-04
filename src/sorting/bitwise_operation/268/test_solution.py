import pytest

from solution import Solution


@pytest.fixture
def solver() -> Solution:
    """
    Fixture
    -------
    Provides an instance of the Solution class for testing.
    """
    return Solution()


def test_small_cases(solver: Solution) -> None:
    """
    Test simple small input cases.
    """
    assert solver.missingNumber([3, 0, 1]) == 2
    assert solver.missingNumber([0, 1]) == 2
    assert solver.missingNumber([1]) == 0
    assert solver.missingNumber([0]) == 1


def test_missing_first_and_last(solver: Solution) -> None:
    """
    Test when the missing number is at the boundaries (0 or n).
    """
    assert solver.missingNumber([1, 2, 3]) == 0
    assert solver.missingNumber([0, 1, 2]) == 3


def test_unsorted_input(solver: Solution) -> None:
    """
    Test with unsorted input list.
    """
    assert solver.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_large_input(solver: Solution) -> None:
    """
    Test with a large input list for performance and correctness.
    """
    n = 10**6
    nums = list(range(n + 1))
    nums.remove(543210)
    assert solver.missingNumber(nums) == 543210


def test_single_element(solver: Solution) -> None:
    """
    Test single-element cases.
    """
    assert solver.missingNumber([0]) == 1
    assert solver.missingNumber([1]) == 0

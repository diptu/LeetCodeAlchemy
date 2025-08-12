import pytest
from solution import Solution


@pytest.fixture
def solution():
    """Fixture to create a Solution instance."""
    return Solution()


def test_single_number_basic(solution):
    """
    Test the singleNumber method with basic inputs.

    Examples
    --------
    >>> sol = Solution()
    >>> sol.singleNumber([1, 2, 3, 1, 2])
    3
    """
    assert solution.singleNumber([1, 2, 3, 1, 2]) == 3
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([10, 10, 20]) == 20


def test_single_number_single_element(solution):
    """Test case where the list has only one element."""
    assert solution.singleNumber([99]) == 99


def test_single_number_negative_numbers(solution):
    """Test case with negative numbers in the list."""
    assert solution.singleNumber([-1, -1, -2]) == -2
    assert solution.singleNumber([-3, -3, -4, 5, 5]) == -4


def test_single_number_large_list(solution):
    """Test case with a larger list of numbers."""
    nums = list(range(1, 10001)) * 2
    nums.append(999999)
    assert solution.singleNumber(nums) == 999999

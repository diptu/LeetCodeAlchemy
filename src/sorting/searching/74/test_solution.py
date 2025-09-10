import pytest
from solution import Solution


@pytest.fixture
def solver() -> Solution:
    """Fixture to initialize the Solution instance."""
    return Solution()


def test_target_found(solver: Solution) -> None:
    """Test when target exists in the list."""
    assert solver.searchInsert([1, 3, 5, 6], 5) == 2
    assert solver.searchInsert([1, 3, 5, 6], 1) == 0
    assert solver.searchInsert([1, 3, 5, 6], 6) == 3


def test_target_not_found_insert_position(solver: Solution) -> None:
    """Test when target is not in the list and needs insertion."""
    assert solver.searchInsert([1, 3, 5, 6], 2) == 1
    assert solver.searchInsert([1, 3, 5, 6], 7) == 4
    assert solver.searchInsert([1, 3, 5, 6], 0) == 0


def test_single_element(solver: Solution) -> None:
    """Test edge case with a single-element list."""
    assert solver.searchInsert([5], 5) == 0
    assert solver.searchInsert([5], 2) == 0
    assert solver.searchInsert([5], 7) == 1


def test_empty_list(solver: Solution) -> None:
    """Test edge case with an empty list."""
    assert solver.searchInsert([], 10) == 0


def test_large_input(solver: Solution) -> None:
    """Test performance with a large input list."""
    nums = list(range(0, 10**6, 2))  # even numbers
    assert solver.searchInsert(nums, 123456) == 61728
    assert solver.searchInsert(nums, 123457) == 61729
    assert solver.searchInsert(nums, -1) == 0
    assert solver.searchInsert(nums, 10**6 + 1) == len(nums)

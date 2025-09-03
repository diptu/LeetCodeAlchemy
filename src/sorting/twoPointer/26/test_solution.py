import pytest
from solution import Solution


@pytest.fixture
def solver() -> Solution:
    """Fixture to initialize the Solution instance."""
    return Solution()


def test_no_duplicates(solver: Solution) -> None:
    """Array with no duplicates remains unchanged."""
    nums = [1, 2, 3, 4]
    k = solver.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [1, 2, 3, 4]


def test_with_duplicates(solver: Solution) -> None:
    """Array with duplicates should be reduced to unique values."""
    nums = [1, 1, 2, 2, 3, 3, 4]
    k = solver.removeDuplicates(nums)
    assert k == 4
    assert nums[:k] == [1, 2, 3, 4]


def test_all_duplicates(solver: Solution) -> None:
    """Array with all identical elements becomes one element."""
    nums = [5, 5, 5, 5, 5]
    k = solver.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [5]


def test_single_element(solver: Solution) -> None:
    """Single-element array remains unchanged."""
    nums = [42]
    k = solver.removeDuplicates(nums)
    assert k == 1
    assert nums[:k] == [42]


def test_empty_array(solver: Solution) -> None:
    """Empty array returns zero length."""
    nums: list[int] = []
    k = solver.removeDuplicates(nums)
    assert k == 0
    assert nums == []


def test_large_array(solver: Solution) -> None:
    """Performance test with a large array."""
    nums = list(range(10000)) + list(range(10000))  # duplicates
    nums.sort()
    k = solver.removeDuplicates(nums)
    assert k == 10000
    assert nums[:k] == list(range(10000))

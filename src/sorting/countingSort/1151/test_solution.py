import pytest
from solution import Solution


@pytest.fixture
def solver() -> Solution:
    """Fixture to create a Solution instance."""
    return Solution()


def test_example_case(solver: Solution) -> None:
    """Test the provided example."""
    assert solver.heightChecker([1, 1, 4, 2, 1, 3]) == 3


def test_already_sorted(solver: Solution) -> None:
    """If already sorted, expect 0 mismatches."""
    assert solver.heightChecker([1, 2, 3, 4, 5]) == 0


def test_reverse_sorted(solver: Solution) -> None:
    """Reverse sorted should give max mismatches."""
    assert solver.heightChecker([5, 4, 3, 2, 1]) == 4


def test_all_same(solver: Solution) -> None:
    """If all heights are the same, no mismatches."""
    assert solver.heightChecker([2, 2, 2, 2]) == 0


def test_two_elements(solver: Solution) -> None:
    """Two-element case."""
    assert solver.heightChecker([2, 1]) == 2
    assert solver.heightChecker([1, 2]) == 0


def test_large_input(solver: Solution) -> None:
    """Stress test with large input."""
    heights = [100] * 1000 + [1] * 1000
    assert solver.heightChecker(heights) == 2000

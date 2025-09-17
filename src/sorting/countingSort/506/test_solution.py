import pytest
from solution import Solution


@pytest.fixture
def sol() -> Solution:
    """Provide a Solution instance for tests."""
    return Solution()


def test_example_case(sol: Solution) -> None:
    """Test the example case from problem description."""
    scores = [10, 3, 8, 9, 4]
    expected = ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    assert sol.findRelativeRanks(scores) == expected


def test_single_element(sol: Solution) -> None:
    """Test when there is only one athlete."""
    scores = [100]
    expected = ["Gold Medal"]
    assert sol.findRelativeRanks(scores) == expected


def test_two_elements(sol: Solution) -> None:
    """Test with two athletes."""
    scores = [50, 75]
    expected = ["Silver Medal", "Gold Medal"]
    assert sol.findRelativeRanks(scores) == expected


def test_descending_order(sol: Solution) -> None:
    """Test input already in descending order."""
    scores = [100, 90, 80, 70]
    expected = ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]
    assert sol.findRelativeRanks(scores) == expected


def test_ascending_order(sol: Solution) -> None:
    """Test input in ascending order."""
    scores = [10, 20, 30, 40]
    expected = ["4", "Bronze Medal", "Silver Medal", "Gold Medal"]
    assert sol.findRelativeRanks(scores) == expected


def test_random_order(sol: Solution) -> None:
    """Test random order of scores."""
    scores = [5, 1, 3, 2, 4]
    expected = ["Gold Medal", "5", "Bronze Medal", "4", "Silver Medal"]
    assert sol.findRelativeRanks(scores) == expected

import pytest
from solution import Solution


@pytest.fixture
def solution_instance():
    """
    Fixture to provide an instance of the Solution class.
    """
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([], False),
        ([1], False),
        ([1, 1, 1, 1], True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 10], True),
    ],
)
def test_contains_duplicate(solution_instance, nums, expected):
    """
    Test Solution.contains_duplicate method.
    """
    assert solution_instance.contains_duplicate(nums) is expected

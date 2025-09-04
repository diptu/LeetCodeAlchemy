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


def test_basic_merge(solver: Solution) -> None:
    """
    Test basic merge of two non-empty arrays.
    """
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solver.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_empty_nums2(solver: Solution) -> None:
    """
    Test case where nums2 is empty.
    """
    nums1 = [1, 2, 3]
    nums2: list[int] = []
    solver.merge(nums1, 3, nums2, 0)
    assert nums1 == [1, 2, 3]


def test_empty_nums1(solver: Solution) -> None:
    """
    Test case where nums1 has no valid elements and nums2 fills it.
    """
    nums1 = [0, 0, 0]
    nums2 = [2, 5, 6]
    solver.merge(nums1, 0, nums2, 3)
    assert nums1 == [2, 5, 6]


def test_both_empty(solver: Solution) -> None:
    """
    Test case where both nums1 and nums2 are empty.
    """
    nums1: list[int] = []
    nums2: list[int] = []
    solver.merge(nums1, 0, nums2, 0)
    assert nums1 == []


def test_with_duplicates(solver: Solution) -> None:
    """
    Test merging arrays with duplicate values.
    """
    nums1 = [1, 2, 2, 0, 0, 0]
    nums2 = [2, 2, 3]
    solver.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 2, 2, 3]


def test_large_input(solver: Solution) -> None:
    """
    Test merging large arrays for performance and correctness.
    """
    m, n = 1000, 1000
    nums1 = list(range(0, 2000, 2)) + [0] * n
    nums2 = list(range(1, 2001, 2))
    solver.merge(nums1, m, nums2, n)
    assert nums1 == list(range(2000))

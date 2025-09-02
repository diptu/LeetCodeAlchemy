import pytest
from solution import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_list(solution):
    assert solution.sortArray([]) == []


def test_single_element(solution):
    assert solution.sortArray([1]) == [1]


def test_already_sorted(solution):
    assert solution.sortArray([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted(solution):
    assert solution.sortArray([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_unsorted_list(solution):
    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]


def test_with_duplicates(solution):
    assert solution.sortArray([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_large_list(solution):
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert solution.sortArray(nums) == sorted(nums)

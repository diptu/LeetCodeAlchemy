"""Test module for Solution class implementing Top K Frequent Elements."""


import pytest
from solution import Solution


@pytest.fixture
def solution() -> Solution:
    """
    Fixture providing an instance of the Solution class.

    Returns
    -------
    Solution
        An instance of the Solution class.
    """
    return Solution()


def test_basic_case(solution: Solution) -> None:
    """
    Test with a typical list and k=2.

    Ensures the method returns the top 2 most frequent elements.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [1, 1, 2, 2, 2, 3]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    assert set(result) == {1, 2}


def test_all_unique(solution: Solution) -> None:
    """
    Test with all unique elements and k=2.

    Checks that the result contains any 2 elements from the original list.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [1, 2, 3, 4]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    assert len(result) == 2
    assert all(num in nums for num in result)


def test_all_same(solution: Solution) -> None:
    """
    Test with all identical elements and k=1.

    Ensures the single frequent element is returned.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [5, 5, 5, 5]
    k: int = 1
    result: list[int] = solution.topKFrequent(nums, k)
    assert result == [5]


def test_more_k_than_unique_elements(solution: Solution) -> None:
    """
    Test when k is larger than the number of unique elements.

    Ensures all unique elements are returned.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [1, 1, 2]
    k: int = 5
    result: list[int] = solution.topKFrequent(nums, k)
    assert set(result) == {1, 2}


def test_empty_input(solution: Solution) -> None:
    """
    Test with an empty input list.

    Expects an empty result list.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = []
    k: int = 1
    result: list[int] = solution.topKFrequent(nums, k)
    assert result == []


def test_negative_numbers(solution: Solution) -> None:
    """
    Test with negative integers in the list.

    Checks correct frequency counting for negative values.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [-1, -1, -2, -2, -2, -3]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    assert set(result) == {-1, -2}


def test_large_k_equal_to_n(solution: Solution) -> None:
    """
    Test when k equals the number of unique elements.

    Ensures all elements are returned.

    Parameters
    ----------
    solution : Solution
        An instance of the Solution class.
    """
    nums: list[int] = [1, 2, 3, 4, 5]
    k: int = 5
    result: list[int] = solution.topKFrequent(nums, k)
    assert set(result) == set(nums)

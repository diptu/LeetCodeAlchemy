import pytest
from solution import Solution


def test_empty_lists():
    solution = Solution()
    assert solution.intersect([], []) == []


def test_one_empty_list():
    solution = Solution()
    assert solution.intersect([1, 2, 3], []) == []
    assert solution.intersect([], [4, 5, 6]) == []


def test_no_common_elements():
    solution = Solution()
    assert solution.intersect([1, 2], [3, 4]) == []


def test_single_element():
    solution = Solution()
    assert solution.intersect([1], [1]) == [1]


def test_with_duplicates():
    solution = Solution()
    assert solution.intersect([1, 2, 2, 1], [2, 2]) == [2, 2]


def test_multiple_common_elements():
    solution = Solution()
    result = solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    assert sorted(result) == [4, 9]


def test_all_common():
    solution = Solution()
    result = solution.intersect([1, 2, 3], [3, 2, 1])
    assert sorted(result) == [1, 2, 3]


def test_large_input():
    solution = Solution()
    nums1 = list(range(1000))
    nums2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert sorted(solution.intersect(nums1, nums2)) == expected

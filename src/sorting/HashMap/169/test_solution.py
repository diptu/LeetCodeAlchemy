
import pytest
from solution import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_simple_case(solution: Solution) -> None:
    nums: list[int] = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums) == 2


def test_all_same(solution: Solution) -> None:
    nums: list[int] = [3, 3, 3, 3]
    assert solution.majorityElement(nums) == 3


def test_single_element(solution: Solution) -> None:
    nums: list[int] = [7]
    assert solution.majorityElement(nums) == 7


def test_large_case(solution: Solution) -> None:
    nums: list[int] = [1] * 500 + [2] * 501
    assert solution.majorityElement(nums) == 2

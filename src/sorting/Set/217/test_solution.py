
import pytest
from solution import Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3, 4], False),  # no duplicates
        ([1, 2, 3, 1], True),  # duplicate 1
        ([7, 7, 7], True),  # all duplicates
        ([1], False),  # single element
        ([], False),  # empty list
        ([1, 2, 3, 4, 5, 6, 2], True),  # duplicate at the end
        ([1, 2, 3, 4, 5, 6, 0], False),  # all unique
    ],
)
def test_containsDuplicate(nums: list[int], expected: bool) -> None:
    """Test various lists for duplicates."""
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected


def test_large_input() -> None:
    """Stress test with large input."""
    solution = Solution()
    nums = list(range(1, 100_001))  # 100k unique numbers
    assert solution.containsDuplicate(nums) is False

    nums.append(50_000)  # introduce duplicate
    assert solution.containsDuplicate(nums) is True

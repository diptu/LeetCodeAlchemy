
import pytest
from solution import Solution


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1, 2, 2, 3], 2, 2),
        ([7, 7, 7], 1, 7),
        ([5, 2, 4, 1, 3], 5, 1),
        ([10, 9, 8, 7], 1, 10),
        ([10, 9, 8, 7], 4, 7),
    ],
)
def test_findKthLargest(nums: list[int], k: int, expected: int) -> None:
    """Test k-th largest element for various inputs."""
    solution = Solution()
    assert solution.findKthLargest(nums, k) == expected


def test_large_input() -> None:
    """Stress test with large input (100k numbers)."""
    solution = Solution()
    nums = list(range(1, 100_001))  # 100k numbers
    k = 100
    expected = 100_000 - k + 1
    assert solution.findKthLargest(nums, k) == expected


import pytest
from solution import Solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([2, 2, 3, 1], 1),  # third distinct max exists
        ([1, 2], 2),  # fewer than 3 unique -> max
        ([3, 2, 1], 1),  # exactly 3 unique
        ([5, 2, 2], 5),  # duplicates, fewer than 3 unique
        ([1, 2, 2, 5, 3, 5], 2),  # third distinct max = 2
        ([7, 7, 7], 7),  # all same
        ([1], 1),  # single element
    ],
)
def test_third_max(nums: list[int], expected: int) -> None:
    """Test heap-based third_max implementation with various inputs."""
    solver = Solution()
    assert solver.third_max(nums) == expected


def test_large_input() -> None:
    """Stress test with a large input list."""
    solver = Solution()
    nums = list(range(1, 1_000_01))  # 100k numbers
    assert solver.third_max(nums) == 99998

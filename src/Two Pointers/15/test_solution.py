
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        (
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4],
            [[-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
        ),
    ],
)
def test_three_sum(nums: list[int], expected: list[list[int]]) -> None:
    """
    Test the three_sum method of the Solution class.

    Parameters
    ----------
    nums : List[int]
        The input list of integers.

    expected : List[List[int]]
        The expected list of unique triplets that sum to zero.

    Notes
    -----
    The test checks:
        - Standard cases with positive and negative integers.
        - Duplicate handling to ensure no repeated triplets.
        - Edge cases: empty list, one element, all zeroes.
        - Large inputs with repeated numbers.
    """
    solution = Solution()
    result = solution.three_sum(nums)

    normalize = lambda lst: sorted([sorted(triplet) for triplet in lst])
    assert normalize(result) == normalize(expected)

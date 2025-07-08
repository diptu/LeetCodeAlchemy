
import pytest
from solution import Solution  # assumes solution.py contains the implementation


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([], []),
    ],
)
def test_spiral_order(matrix: list[list[int]], expected: list[int]) -> None:
    """
    Test spiral_order traversal on various matrix configurations.

    Parameters
    ----------
    matrix : list of list of int
        Input 2D matrix to be traversed in spiral order.
    expected : list of int
        Expected output list of elements in spiral order.
    """
    solution = Solution()
    assert solution.spiral_order(matrix) == expected

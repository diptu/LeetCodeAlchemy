
import pytest
from solution import Solution  # assumes the class is in solution.py


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 0, 0], [0, 4, 5], [0, 7, 8]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ([[0]], [[0]]),
        ([[1]], [[1]]),
        ([[1, 0]], [[0, 0]]),
        ([[0], [1]], [[0], [0]]),
    ],
)
def test_set_zeroes(matrix: list[list[int]], expected: list[list[int]]) -> None:
    """
    Test the in-place matrix zeroing algorithm for various configurations.

    Parameters
    ----------
    matrix : list of list of int
        Input matrix to modify in-place.
    expected : list of list of int
        Expected result after setting rows and columns to zero.

    Notes
    -----
    This test assumes that the setZeroes method mutates the matrix in-place.
    """
    solution = Solution()
    solution.setZeroes(matrix)
    assert matrix == expected


import pytest
from solution import Solution


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
        ([[1, 2], [3, 4], [5, 6]], [[1, 3, 5], [2, 4, 6]]),
        ([[7]], [[7]]),
        ([], []),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
    ],
)
def test_transpose(matrix: list[list[int]], expected: list[list[int]]) -> None:
    """
    Test the transpose method of the Solution class.

    Parameters
    ----------
    matrix : List[List[int]]
        Input matrix to be transposed.
    expected : List[List[int]]
        Expected output after transposing the matrix.

    Notes
    -----
    The test covers the following cases:
        - Rectangular matrices (more rows/columns)
        - Square matrices
        - Empty matrix
        - Single row and single column matrices
    """
    solution = Solution()
    result = solution.transpose(matrix)
    assert result == expected

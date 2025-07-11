import pytest
from solution import Solution


@pytest.fixture
def solution():
    """Fixture to create a Solution instance."""
    return Solution()


@pytest.mark.parametrize(
    "mat, k, expected",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            1,
            [[12, 21, 16], [27, 45, 33], [24, 39, 28]],
        ),
        (
            [[1, 2], [3, 4]],
            0,
            [[1, 2], [3, 4]],
        ),
        (
            [[1, 2], [3, 4]],
            1,
            [[10, 10], [10, 10]],
        ),
        (
            [[5]],
            1,
            [[5]],
        ),
    ],
)
def test_matrix_block_sum(solution, mat, k, expected):
    """
    Test the matrix_block_sum method with various input matrices and radii.

    Parameters
    ----------
    solution : Solution
        The fixture providing an instance of Solution.
    mat : List[List[int]]
        The input matrix to compute block sums for.
    k : int
        The block radius.
    expected : List[List[int]]
        The expected matrix block sum output.
    """
    result = solution.matrix_block_sum(mat, k)
    assert result == expected

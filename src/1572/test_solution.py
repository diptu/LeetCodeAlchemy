import pytest
from solution import Solution


@pytest.fixture
def sol():
    """Fixture to initialize the Solution class."""
    return Solution()


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
        ([[5]], 5),
        ([[1, 2], [3, 4]], 10),
        ([[7, 0, 0], [0, 7, 0], [0, 0, 7]], 21),
        ([[1, 0, 3], [4, 5, 6], [7, 8, 9]], 25),
    ],
)
def test_diagonal_sum(sol, matrix, expected):
    """Test diagonal sum for various square matrices."""
    assert sol.diagonalSum(matrix) == expected

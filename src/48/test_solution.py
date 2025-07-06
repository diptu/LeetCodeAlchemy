
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "input_matrix, expected_output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ],
)
def test_rotate(
    input_matrix: list[list[int]], expected_output: list[list[int]]
) -> None:
    """
    Tests the rotate function for multiple square matrices.

    Args:
        input_matrix (List[List[int]]): The matrix to rotate.
        expected_output (List[List[int]]): The expected matrix after rotation.

    This test modifies the input_matrix in-place and checks
    if it matches the expected_output.
    """
    solution = Solution()
    solution.rotate(input_matrix)
    assert input_matrix == expected_output

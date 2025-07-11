
import pytest
from solution import Solution  # Replace with actual module name if different


@pytest.fixture
def solution():
    """
    Fixture to create an instance of the Solution class.

    Returns
    -------
    Solution
        Instance of the Game of Life solution class.
    """
    return Solution()


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1]], [[0]]),
    ],
)
def test_game_of_life(
    solution, board: list[list[int]], expected: list[list[int]]
) -> None:
    """
    Test the Game of Life simulation on various board states.

    Parameters
    ----------
    solution : Solution
        The solution instance provided by the fixture.
    board : List[List[int]]
        The initial board configuration.
    expected : List[List[int]]
        The expected board state after one simulation step.

    Returns
    -------
    None

    Notes
    -----
    Time complexity per test: O(m * n)
    Space complexity per test: O(1)
    """
    solution.game_of_life(board)
    assert board == expected

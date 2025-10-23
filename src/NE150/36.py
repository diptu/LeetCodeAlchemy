from typing import List


class Solution:
    """
    Check if a given 9×9 Sudoku board is valid.

    Key Idea
    --------
    Maintain three 9-element sets to track digits seen in:
      • each row
      • each column
      • each 3×3 sub-box (indexed by (r // 3) * 3 + (c // 3))

    When a duplicate is detected in any dimension, return False.

    Steps
    -----
    1. Initialize 9 sets for rows, columns, and boxes.
    2. For each non-empty cell, compute its box index.
    3. Check if the digit already exists in its row/col/box.
       If yes → invalid board.
    4. Otherwise, record it in all three sets.

    Time Complexity
    ---------------
    O(1) — board size fixed (9×9).

    Space Complexity
    ----------------
    O(1) — constant-sized sets.

    Example
    -------
    >>> sol = Solution()
    >>> board = [
    ...     ["5","3",".",".","7",".",".",".","."],
    ...     ["6",".",".","1","9","5",".",".","."],
    ...     [".","9","8",".",".",".",".","6","."],
    ...     ["8",".",".",".","6",".",".",".","3"],
    ...     ["4",".",".","8",".","3",".",".","1"],
    ...     ["7",".",".",".","2",".",".",".","6"],
    ...     [".","6",".",".",".",".","2","8","."],
    ...     [".",".",".","4","1","9",".",".","5"],
    ...     [".",".",".",".","8",".",".","7","9"]
    ... ]
    >>> sol.is_valid_sudoku(board)
    True
    """

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """Return True if the given Sudoku board is valid."""
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True


if __name__ == "__main__":
    sol = Solution()

    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.is_valid_sudoku(valid_board)

    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert not sol.is_valid_sudoku(invalid_board)

    print("All tests passed ✅")

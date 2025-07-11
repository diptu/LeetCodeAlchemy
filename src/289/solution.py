class Solution:
    """
    Class to solve Conway's Game of Life problem.
    """

    def count_live_neighbors(self, board: list[list[int]], row: int, col: int) -> int:
        """
        Count live neighbors around a given cell.

        Parameters
        ----------
        board : List[List[int]]
            The 2D grid representing the board state.
        row : int
            The row index of the cell.
        col : int
            The column index of the cell.

        Returns
        -------
        int
            The number of live neighbors.
        """
        count = 0
        rows, cols = len(board), len(board[0])

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i == row and j == col:
                    continue
                if 0 <= i < rows and 0 <= j < cols:
                    if abs(board[i][j]) == 1:
                        count += 1

        return count

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Compute the next state of the Game of Life board.

        Modifies the board in-place using encoded state transitions:
        - 1 → 0 is encoded as -1
        - 0 → 1 is encoded as 2

        Parameters
        ----------
        board : List[List[int]]
            The 2D board of cells where 1 is alive and 0 is dead.

        Returns
        -------
        None

        Notes
        -----
        Time complexity: O(m * n)
            m = number of rows, n = number of columns
        Space complexity: O(1)
            In-place modification with constant extra space
        """
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                live_neighbors = self.count_live_neighbors(board, i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


if __name__ == "__main__":
    solution = Solution()
    input_board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.gameOfLife(input_board)
    print(input_board)

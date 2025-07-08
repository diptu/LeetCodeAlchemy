class Solution:
    """Class to solve matrix traversal problems."""

    @staticmethod
    def is_visited(row: int, col: int, visited: dict[tuple[int, int], bool]) -> bool:
        """
        Check if the given cell has been visited.

        Parameters
        ----------
        row : int
            Row index of the cell.
        col : int
            Column index of the cell.
        visited : dict of tuple
            Dictionary storing visited status for each cell.

        Returns
        -------
        bool
            True if the cell has been visited, False otherwise.
        """
        return visited.get((row, col), False)

    @staticmethod
    def mark_visited(row: int, col: int, visited: dict[tuple[int, int], bool]) -> None:
        """
        Mark the given cell as visited.

        Parameters
        ----------
        row : int
            Row index of the cell.
        col : int
            Column index of the cell.
        visited : dict of tuple
            Dictionary storing visited status for each cell.
        """
        visited[(row, col)] = True

    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        """
        Return the elements of the matrix in spiral order.

        Parameters
        ----------
        matrix : list of list of int
            2D grid to traverse.

        Returns
        -------
        list of int
            Elements of the matrix in spiral order.
        Time Complexity
        ---------------
        O(m * n) where m is the number of rows and n is the number of columns.

        Space Complexity
        ----------------
        O(m * n) for the visited map and result list.
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        visited: dict[tuple[int, int], bool] = {}
        result: list[int] = []

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start with 'right'

        row, col = 0, 0
        for _ in range(rows * cols):
            result.append(matrix[row][col])
            self.mark_visited(row, col, visited)

            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and not self.is_visited(next_row, next_col, visited)
            ):
                row, col = next_row, next_col
            else:
                dir_idx = (dir_idx + 1) % 4  # Rotate direction
                row += directions[dir_idx][0]
                col += directions[dir_idx][1]

        return result


if __name__ == "__main__":
    solution = Solution()
    example_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    output = solution.spiral_order(example_matrix)
    print(output)  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

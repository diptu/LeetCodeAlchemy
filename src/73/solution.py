from typing import List


class Solution:
    """
    Class to solve the problem of setting entire rows and columns to zero
    in a matrix if any element in that row or column is zero.
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the input matrix in-place such that if an element is 0,
        its entire row and column are set to 0.

        Parameters
        ----------
        matrix : List[List[int]]
            A 2D list of integers to be modified in-place.

        Time Complexity
        ----------------
        O(m * n), where m is number of rows and n is number of columns.

        Space Complexity
        ----------------
        O(k), where k is the number of zero elements in the matrix.
        """
        rows, cols = len(matrix), len(matrix[0])
        coords = []

        # Step 1: Find all (row, col) positions with 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    coords.append((i, j))

        # Step 2: Set entire rows and columns to 0
        for row, col in coords:
            for j in range(cols):
                matrix[row][j] = 0
            for i in range(rows):
                matrix[i][col] = 0


if __name__ == "__main__":
    solution = Solution()
    example_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(example_matrix)
    print(example_matrix)
    # Output:
    # [
    #     [1, 0, 1],
    #     [0, 0, 0],
    #     [1, 0, 1]
    # ]

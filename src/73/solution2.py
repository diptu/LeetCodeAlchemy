

class Solution:
    """
    Class to solve the matrix zeroing problem in-place using O(1) space.
    """

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Modify the input matrix in-place such that if an element is 0,
        its entire row and column are set to 0. Optimized to use no
        additional space except constant flags.

        Parameters
        ----------
        matrix : List[List[int]]
            A 2D list of integers to be modified in-place.

        Time Complexity
        ----------------
        O(m * n), where m is the number of rows and n is the number
        of columns.

        Space Complexity
        ----------------
        O(1), since no extra space is used apart from two boolean flags.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


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

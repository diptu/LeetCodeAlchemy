class Solution:
    @staticmethod
    def transpose(matrix: list[list[int]]) -> None:
        """
        Transposes a square matrix in-place.

        This function modifies the given 2D square matrix directly,
        converting its rows into columns and vice versa without using any extra memory.

        Args:
            matrix (List[List[int]]): A 2D list representing a square matrix (n x n).

        Example:
            Input:
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            After calling transpose(matrix):
                [
                    [1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]
                ]

        Note:
            This function assumes the input matrix is square.
            It does not return anything; the matrix is modified in-place.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates a square matrix by 90 degrees clockwise in-place.

        This function modifies the given 2D square matrix directly by:
        1. Transposing the matrix (rows become columns).
        2. Reversing each row to complete the 90-degree clockwise rotation.

        Args:
            matrix (List[List[int]]): A 2D list representing a square matrix (n x n).

        Example:
            Input:
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            After calling rotate(matrix):
                [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                ]

        Note:
            This function assumes the input matrix is square.
            It does not return anything; the matrix is modified in-place.
        """
        # Step 1: Transpose the matrix
        Solution.transpose(matrix)

        # Step 2: Reverse each row (flip horizontally)
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    solution = Solution()

    # Example usage
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix1)
    print(matrix1)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

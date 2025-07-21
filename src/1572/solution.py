"""Module to calculate the sum of diagonals in a square matrix."""

from typing import List


class Solution:
    """A class containing methods for matrix-based computations."""

    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Calculate the sum of the primary and secondary diagonals of a square matrix.

        The primary diagonal is from top-left to bottom-right.
        The secondary diagonal is from top-right to bottom-left.
        If the matrix has an odd dimension, the center element is counted twice and must be subtracted once.

        Parameters
        ----------
        mat : List[List[int]]
            A square matrix represented as a list of lists of integers.

        Returns
        -------
        int
            The sum of the elements on both diagonals.

        Examples
        --------
        >>> solution = Solution()
        >>> solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        25
        """
        n = len(mat)
        diagonal_sum = 0
        mid_idx = int(n / 2)

        for i in range(n):
            diagonal_sum += mat[i][i] + mat[i][n - 1 - i]

        if n % 2 == 1:
            diagonal_sum -= mat[mid_idx][mid_idx]

        return diagonal_sum


if __name__ == "__main__":
    solution = Solution()

    # Example usage
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solution.diagonalSum(matrix)
    print(result)  # Output: 25

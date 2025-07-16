from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Transpose the given 2D matrix (rows become columns and vice versa).

        Parameters
        ----------
        matrix : List[List[int]]
            A 2D list representing the matrix to be transposed.

        Returns
        -------
        List[List[int]]
            The transposed version of the input matrix.

        Examples
        --------
        >>> Solution().transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]

        Notes
        -----
        Time Complexity: O(m * n)
            Where `m` is the number of rows and `n` is the number of columns.
        Space Complexity: O(m * n)
            A new matrix of size n x m is allocated for the result.
        """
        if not matrix or not matrix[0]:
            return []

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        transposed = []
        for col in range(num_cols):
            new_row = []
            for row in range(num_rows):
                new_row.append(matrix[row][col])
            transposed.append(new_row)

        return transposed


if __name__ == "__main__":
    solution = Solution()

    # Example usage
    original_matrix = [[1, 2, 3], [4, 5, 6]]
    transposed_matrix = solution.transpose(original_matrix)
    print(transposed_matrix)  # Output: [[1, 4], [2, 5], [3, 6]]

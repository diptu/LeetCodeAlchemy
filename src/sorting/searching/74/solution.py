

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Search for a target value in a 2D matrix using binary search.

        The matrix has the following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of
          the previous row.

        This allows the 2D matrix to be treated as a flattened sorted
        1D array, enabling binary search.

        Parameters
        ----------
        matrix : List[List[int]]
            A 2D matrix of integers, where each row is sorted and the first
            element of each row is greater than the last of the previous row.
        target : int
            The integer value to search for.

        Returns
        -------
        bool
            True if `target` exists in the matrix, otherwise False.

        Notes
        -----
        Key Idea
        --------
        - Treat the matrix as a sorted 1D array.
        - Apply binary search over the index range [0, rows*cols - 1].
        - Convert the 1D index into 2D coordinates using `divmod`.

        Complexity Analysis
        -------------------
        - Time Complexity: O(log(m * n)), where `m` is number of rows and
          `n` is number of columns.
        - Space Complexity: O(1), since only pointers and indices are used.

        Examples
        --------
        >>> s = Solution()
        >>> s.searchMatrix([[1, 3, 5], [7, 9, 11]], 9)
        True
        >>> s.searchMatrix([[1, 3, 5], [7, 9, 11]], 6)
        False
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, cols)
            value = matrix[row][col]

            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    is_found = solution.searchMatrix(matrix, target)
    print(is_found)  # Expected output: true

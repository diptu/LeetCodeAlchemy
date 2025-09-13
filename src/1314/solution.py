

class Solution:
    """
    Class for solving the Matrix Block Sum problem.

    Methods
    -------
    matrix_block_sum(mat, k):
        Computes the matrix block sum where each cell contains the sum of all
        elements within a k-radius block around it.

    Time Complexity
    ---------------
    O(m * n), where m is the number of rows and n is the number of columns.

    Space Complexity
    ----------------
    O(m * n) for the prefix sum matrix.
    """

    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        """
        Compute the k-radius block sum for each element in the matrix.

        Parameters
        ----------
        mat : List[List[int]]
            2D list of integers representing the input matrix.
        k : int
            Radius of the square block to sum around each cell.

        Returns
        -------
        List[List[int]]
            2D list where each cell contains the sum of elements in the
            k-radius block around the original cell.

        Step-by-step Example
        --------------------
        Input:
        mat = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
        k = 1

        Step 1: Compute prefix sum matrix:
        pre_sum = [[0,  0,  0,  0],
                   [0,  1,  3,  6],
                   [0,  5, 12, 21],
                   [0, 12, 27, 45]]

        Step 2: For each cell (i, j), calculate boundaries:
        r1 = max(0, i-k), c1 = max(0, j-k)
        r2 = min(m, i+k+1), c2 = min(n, j+k+1)

        Step 3: Apply inclusion-exclusion using pre_sum:
        result[i][j] = pre[r2][c2] - pre[r1][c2] -
                       pre[r2][c1] + pre[r1][c1]

        Final Output:
        [[12, 21, 16],
         [27, 45, 33],
         [24, 39, 28]]
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                print(
                    f"pre[{i + 1}][{j + 1}] =mat[{i}][{j}] + pre[{i}][{j + 1}] + pre[{i + 1}][{j}] - pre[{i}][{j}]"
                )
                pre[i + 1][j + 1] = (
                    mat[i][j] + pre[i][j + 1] + pre[i + 1][j] - pre[i][j]
                )

        # Compute the result using the prefix sum matrix
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m, i + k + 1)
                c2 = min(n, j + k + 1)

                result[i][j] = pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1]

        return result


if __name__ == "__main__":
    solution = Solution()
    k = 1
    input_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output_mat = solution.matrixBlockSum(input_mat, k)
    print(output_mat)

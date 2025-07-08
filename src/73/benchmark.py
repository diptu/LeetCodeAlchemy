import timeit
import copy
from typing import List


class NaiveSolution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Naive approach using extra space to track zero positions.
        """
        rows, cols = len(matrix), len(matrix[0])
        coords = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    coords.append((i, j))

        for row, col in coords:
            for j in range(cols):
                matrix[row][j] = 0
            for i in range(rows):
                matrix[i][col] = 0


class OptimizedSolution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Optimized in-place approach using O(1) space.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


def generate_matrix(rows: int, cols: int, zero_rate: float = 0.1) -> List[List[int]]:
    """
    Generate a matrix of the given size with random zeros.
    """
    from random import random

    return [
        [0 if random() < zero_rate else 1 for _ in range(cols)] for _ in range(rows)
    ]


def benchmark():
    rows, cols = 200, 200
    original_matrix = generate_matrix(rows, cols, zero_rate=0.05)

    naive = NaiveSolution()
    optimized = OptimizedSolution()

    def run_naive():
        matrix = copy.deepcopy(original_matrix)
        naive.setZeroes(matrix)

    def run_optimized():
        matrix = copy.deepcopy(original_matrix)
        optimized.setZeroes(matrix)

    naive_time = timeit.timeit(run_naive, number=100)
    optimized_time = timeit.timeit(run_optimized, number=100)

    print(f"Naive Solution Time:     {naive_time:.6f} sec")
    print(f"Optimized Solution Time: {optimized_time:.6f} sec")


if __name__ == "__main__":
    benchmark()

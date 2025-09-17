from typing import List


class Solution:
    """Class to solve the height checker problem."""

    def heightChecker(self, heights: List[int]) -> int:
        """
        Count how many students are not in the correct position compared
        to the expected sorted order.

        The algorithm uses counting sort since student heights
        are guaranteed to be within [1, 100].

        Args:
            heights (List[int]): List of student heights.

        Returns:
            int: Number of mismatched positions.

        Example:
            >>> solution = Solution()
            >>> solution.height_checker([1, 1, 4, 2, 1, 3])
            3

        Time Complexity:
            O(n) where n = len(heights).
            - Counting occurrences: O(n)
            - Building expected order: O(n + k), k = 100 (constant)
            - Comparing original vs. sorted: O(n)
            Overall: O(n).

        Space Complexity:
            O(n + k)
            - Count array: O(k), k = 100 (constant)
            - Expected array: O(n)
            Overall: O(n).
        """
        # Counting sort since heights range from 1 to 100
        count = [0] * 101
        for h in heights:
            count[h] += 1

        expected: List[int] = []
        for h, c in enumerate(count):
            expected.extend([h] * c)

        # Compare original and expected order
        mismatches = sum(1 for i, h in enumerate(heights) if h != expected[i])
        return mismatches


if __name__ == "__main__":
    solution = Solution()
    sample_heights = [1, 1, 4, 2, 1, 3]
    result = solution.heightChecker(sample_heights)
    print(result)  # Output: 3

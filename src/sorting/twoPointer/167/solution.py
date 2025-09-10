"""Two Sum II problem: find indices of two numbers that add up to target.

Solutions:
    1. Two-pointer approach (O(n) time, O(1) space).
    2. Hash map approach (O(n) time, O(n) space).

Key idea:
    - Two-pointer works only if the input array is sorted.
    - Hash map works on both sorted and unsorted arrays.
"""

from typing import List


class Solution:
    """Solution class for Two Sum II problem."""

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        """Return 1-based indices of two numbers adding up to target.

        Args:
            numbers (List[int]): Input list of integers (sorted).
            target (int): Target sum.

        Returns:
            List[int]: Indices (1-based) of two numbers that add up to target.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            if total > target:
                right -= 1
            else:
                left += 1

        return []  # Safety fallback, though problem guarantees a solution

    # Uncomment below to use the hash map solution
    #
    # def two_sum(self, numbers: List[int], target: int) -> List[int]:
    #     """Return 1-based indices of two numbers adding up to target.
    #
    #     Works for unsorted arrays as well using a hash map.
    #
    #     Args:
    #         numbers (List[int]): Input list of integers.
    #         target (int): Target sum.
    #
    #     Returns:
    #         List[int]: Indices (1-based) of two numbers that add up to target.
    #     """
    #     h_map: dict[int, int] = {}
    #
    #     for i, n in enumerate(numbers):
    #         diff = target - n
    #
    #         if diff in h_map:
    #             return [h_map[diff] + 1, i + 1]
    #
    #         h_map[n] = i
    #
    #     return []  # Safety fallback


if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    result = solution.two_sum(numbers, target)
    print(result)  # Expected: [1, 2]

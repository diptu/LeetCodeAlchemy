"""
Module for computing the minimal length of a contiguous subarray
whose sum is at least a target value.

This module provides functionality to find the smallest window in a
list of positive integers such that the window sum is ≥ target.
"""

import sys


class Solution:
    """Solution for finding the minimal length of a subarray with sum ≥ target."""

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """Calculate the minimal length of a contiguous subarray with sum ≥ target.

        Parameters
        ----------
        target : int
            Threshold sum for the subarray.
        nums : list[int]
            List of positive integers to search within.

        Returns
        -------
        int
            Length of the smallest contiguous subarray with sum ≥ target.
            Returns 0 if no such subarray exists.
        """
        min_window = sys.maxsize  # Initialize with the max possible integer
        curr_sum = 0
        low = 0
        high = 0

        # Expand and contract the sliding window
        while high < len(nums):
            curr_sum += nums[high]
            high += 1
            while curr_sum >= target:
                window_len = high - low
                if window_len < min_window:
                    min_window = window_len
                curr_sum -= nums[low]
                low += 1

        return min_window if min_window != sys.maxsize else 0


def main() -> None:
    """Example usage of Solution.minSubArrayLen."""
    solution = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    min_window = solution.minSubArrayLen(target, nums)
    print(f"Minimal length: {min_window}")


if __name__ == "__main__":
    main()

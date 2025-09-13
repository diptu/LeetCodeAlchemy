"""Module for computing maximum average subarray using sliding window.

This module provides functionality to compute the maximum average of any
contiguous subarray of a specified length within a list of numbers.
"""



class Solution:
    """Solution for finding the maximum average of a subarray.

    Methods
    -------
    findMaxAverage(nums, k)
        Compute the maximum average of any contiguous subarray of length k.
    """

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Calculate the maximum average of any contiguous subarray of length k.

        Parameters
        ----------
        nums : list[int]
            List of integers to search within.
        k : int
            Size of the sliding window (subarray length).

        Returns
        -------
        float
            Maximum average among all contiguous subarrays of length k.

        Complexity
        ----------
        Time complexity : O(n)
        Space complexity: O(1)

        Examples
        --------
        >>> sol = Solution()
        >>> sol.find_max_average([1, 12, -5, -6, 50, 3], 4)
        12.75
        """
        # Initialize the sum of the first window
        initial_sum = sum(nums[:k])
        max_sum = initial_sum
        sliding_sum = initial_sum

        for idx in range(k, len(nums)):
            sliding_sum += nums[idx] - nums[idx - k]
            if sliding_sum > max_sum:
                max_sum = sliding_sum

        return max_sum / k


def main() -> None:
    """Run example usage of Solution.find_max_average."""
    solution = Solution()
    numbers = [1, 12, -5, -6, 50, 3]
    window_size = 4
    max_avg = solution.findMaxAverage(numbers, window_size)
    print(f"Maximum average: {max_avg:.5f}")


if __name__ == "__main__":
    main()

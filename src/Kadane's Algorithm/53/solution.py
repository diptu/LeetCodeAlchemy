"""Module providing an optimal solution to the Maximum Subarray problem.

This module implements Kadane's algorithm to find the maximum sum of a
contiguous subarray in a given list of integers.
"""



class Solution:
    """Solver for the Maximum Subarray problem.

    Methods
    -------
    max_sub_array(nums: List[int]) -> int
        Returns the maximum sum of a contiguous subarray.
    """

    def max_sub_array(self, nums: list[int]) -> int:
        """Find the maximum sum of a contiguous subarray.

        Uses Kadane's algorithm to achieve optimal performance.

        Parameters
        ----------
        nums : List[int]
            A list of integers.

        Returns
        -------
        int
            Maximum sum of any contiguous subarray.

        Complexity
        ----------
        Time : O(n)
            Iterates through the list once.
        Space : O(1)
            Uses constant extra space.
        """
        max_so_far = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_so_far = max(max_so_far, curr_max)
        return max_so_far


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.max_sub_array(nums)
    print(result)  # Expected output: 6

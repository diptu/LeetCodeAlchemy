from typing import List


class Solution:
    """
    A class to solve the search insert position problem using
    binary search.

    Methods
    -------
    searchInsert(nums: List[int], target: int) -> int
        Finds the index at which the target should be inserted in
        a sorted list of integers.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Locate the index of `target` in a sorted list of integers. If the
        target is not found, return the index where it should be inserted
        to maintain order.

        Parameters
        ----------
        nums : List[int]
            A sorted list of distinct integers.
        target : int
            The value to search for in `nums`.

        Returns
        -------
        int
            The index if the target is found. Otherwise, the index
            where it should be inserted.

        Notes
        -----
        Time complexity : O(log n)
            Binary search halves the search space at each step.
        Space complexity : O(1)
            Constant extra space is used regardless of input size.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.searchInsert([1, 3, 5, 6], 5)
        2
        >>> sol.searchInsert([1, 3, 5, 6], 2)
        1
        >>> sol.searchInsert([1, 3, 5, 6], 7)
        4
        >>> sol.searchInsert([1, 3, 5, 6], 0)
        0
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    sorted_nums = solution.searchInsert(nums, target)
    print(sorted_nums)  # Expected output: 4

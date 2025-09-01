"""Quicksort algorithm implementation with recursion."""

from typing import List


class Solution:
    """
    A class implementing the Quicksort algorithm.
    """

    def _partition(self, nums: List[int], start: int, end: int) -> int:
        """
        Partition the array around a pivot element.

        Parameters
        ----------
        nums : List[int]
            List of integers to partition.
        start : int
            Starting index of the subarray.
        end : int
            Ending index of the subarray.

        Returns
        -------
        int
            Index position of the pivot after partitioning.

        Complexity
        ----------
        Time : O(n), where n is the size of the subarray.
        Space : O(1), performed in-place.
        """
        pivot = nums[end]
        i = start - 1
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

    def _quick_sort(self, nums: List[int], start: int, end: int) -> None:
        """
        Perform recursive Quicksort on a subarray.

        Parameters
        ----------
        nums : List[int]
            List of integers to sort.
        start : int
            Starting index of the subarray.
        end : int
            Ending index of the subarray.

        Returns
        -------
        None

        Complexity
        ----------
        Time : O(n log n) on average, O(n^2) in worst case.
        Space : O(log n) recursion depth on average.
        """
        if start < end:
            partition_idx = self._partition(nums, start, end)
            self._quick_sort(nums, start, partition_idx - 1)
            self._quick_sort(nums, partition_idx + 1, end)

    def sort_colors(self, nums: List[int]) -> List[int]:
        """
        Sort a list of integers using the Quicksort algorithm.

        Parameters
        ----------
        nums : List[int]
            List of integers to sort.

        Returns
        -------
        List[int]
            Sorted list of integers.

        Complexity
        ----------
        Time : O(n log n) on average, O(n^2) in worst case.
        Space : O(log n) recursion depth on average.
        """
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    solution = Solution()
    nums_input = [5, 2, 3, 1]
    sorted_nums = solution.sort_colors(nums_input)
    print(sorted_nums)  # Output: [1, 2, 3, 5]

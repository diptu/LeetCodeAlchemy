"""Quicksort algorithm implementation with recursion."""



class Solution:
    """Provides quicksort-based sorting functionality."""

    def _partition(self, nums: list[int], start: int, end: int) -> int:
        """
        Partition the array around a pivot.

        Parameters
        ----------
        nums : List[int]
            The list of integers to partition.
        start : int
            Starting index of the sublist.
        end : int
            Ending index of the sublist.

        Returns
        -------
        int
            Index position of the pivot after partitioning.
        """
        pivot = nums[end]
        i = start - 1
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

    def _quick_sort(self, nums: list[int], start: int, end: int) -> None:
        """
        Recursively apply quicksort.

        Parameters
        ----------
        nums : List[int]
            The list of integers to sort.
        start : int
            Starting index of the sublist.
        end : int
            Ending index of the sublist.
        """
        if start < end:
            partition_idx = self._partition(nums, start, end)
            self._quick_sort(nums, start, partition_idx - 1)
            self._quick_sort(nums, partition_idx + 1, end)

    def sort_array(self, nums: list[int]) -> list[int]:
        """
        Sort a list of integers using quicksort.

        Parameters
        ----------
        nums : List[int]
            The list of integers to sort.

        Returns
        -------
        List[int]
            A new sorted list of integers.
        """
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    solution = Solution()
    nums_input = [5, 2, 3, 1]
    print(solution.sort_array(nums_input))  # Output: [1, 2, 3, 5]

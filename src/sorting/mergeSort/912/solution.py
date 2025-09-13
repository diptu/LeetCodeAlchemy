"""Optimized Merge Sort implementation using recursion.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity:
    - Best Case: O(n)
    - Average Case: O(n)
    - Worst Case: O(n)

Optimizations:
    - Uses in-place merging with preallocated buffer to reduce overhead.
    - Avoids repeated list slicing by passing indices.

"""



class Solution:
    """Class implementing optimized merge sort using recursion."""

    def sortArray(self, nums: list[int]) -> list[int]:
        """Sorts an array using merge sort (optimized).

        Parameters
        ----------
        nums : List[int]
            List of integers to be sorted.

        Returns
        -------
        List[int]
            Sorted list of integers.

        Notes
        -----
        - Uses divide-and-conquer approach.
        - Optimized with index-based recursion and buffer reuse.

        """
        if len(nums) <= 1:
            return nums

        buffer: list[int] = [0] * len(nums)
        self._merge_sort(nums, buffer, 0, len(nums) - 1)
        return nums

    def _merge_sort(
        self, nums: list[int], buffer: list[int], left: int, right: int
    ) -> None:
        """Recursive helper function for merge sort.

        Parameters
        ----------
        nums : List[int]
            The array to be sorted.
        buffer : List[int]
            Preallocated buffer for merging.
        left : int
            Left index of the subarray.
        right : int
            Right index of the subarray.

        """
        if left >= right:
            return

        mid = (left + right) // 2
        self._merge_sort(nums, buffer, left, mid)
        self._merge_sort(nums, buffer, mid + 1, right)
        self._merge(nums, buffer, left, mid, right)

    def _merge(
        self, nums: list[int], buffer: list[int], left: int, mid: int, right: int
    ) -> None:
        """Merges two sorted subarrays in place.

        Parameters
        ----------
        nums : List[int]
            The array containing two sorted subarrays.
        buffer : List[int]
            Temporary buffer for merging.
        left : int
            Starting index of the left subarray.
        mid : int
            Ending index of the left subarray.
        right : int
            Ending index of the right subarray.

        """
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                buffer[k] = nums[i]
                i += 1
            else:
                buffer[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            buffer[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            buffer[k] = nums[j]
            j += 1
            k += 1

        for idx in range(left, right + 1):
            nums[idx] = buffer[idx]


if __name__ == "__main__":
    solution = Solution()
    nums_input = [5, 2, 3, 1]
    sorted_nums = solution.sortArray(nums_input)
    print(sorted_nums)  # Expected output: [1, 2, 3, 5]

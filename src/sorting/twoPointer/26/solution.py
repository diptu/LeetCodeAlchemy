from typing import List


class Solution:
    """
    A class to solve the problem of removing duplicates from
    a sorted list of integers in-place.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place. The
        function returns the number of unique elements. The
        first `k` elements of nums will contain the unique
        values in sorted order.

        Parameters
        ----------
        nums : List[int]
            A sorted list of integers that may contain duplicates.

        Returns
        -------
        int
            The number of unique elements, k.

        Notes
        -----
        Time complexity : O(n)
            Each element is processed once.
        Space complexity : O(1)
            Modifies the list in-place with no extra space.

        Examples
        --------
        >>> sol = Solution()
        >>> nums = [1, 1, 2]
        >>> k = sol.removeDuplicates(nums)
        >>> nums[:k]
        [1, 2]
        """
        if not nums:
            return 0

        # Pointer for the position of the next unique element
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    for i in range(k):
        print(nums[i], end=" ")  # Output: 1 2

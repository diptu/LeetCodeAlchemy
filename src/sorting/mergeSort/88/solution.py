

class Solution:
    """
    A class to merge two sorted arrays into one in-place.

    Methods
    -------
    merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None
        Merge nums2 into nums1 as one sorted array in-place.
    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place as a single sorted array.

        Parameters
        ----------
        nums1 : List[int]
            First sorted list with length m + n, where the last n elements
            are placeholders (0) to accommodate nums2.
        m : int
            Number of valid elements in nums1.
        nums2 : List[int]
            Second sorted list with length n.
        n : int
            Number of valid elements in nums2.

        Returns
        -------
        None
            Modifies nums1 in-place.

        Key Idea
        --------
        Start from the end of both arrays and place the larger element at
        the end of nums1. This avoids shifting elements multiple times and
        ensures O(1) extra space.

        Notes
        -----
        Time complexity : O(m + n)
            Each element is compared and placed exactly once.
        Space complexity : O(1)
            In-place merging without auxiliary arrays.

        Examples
        --------
        >>> sol = Solution()
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> nums2 = [2, 5, 6]
        >>> sol.merge(nums1, 3, nums2, 3)
        >>> nums1
        [1, 2, 2, 3, 5, 6]
        """
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements of nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

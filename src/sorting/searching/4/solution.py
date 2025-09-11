from __future__ import annotations


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays using binary search partitioning.

        This algorithm guarantees O(log(min(m, n))) time complexity by
        partitioning the smaller array and checking if the combined
        partitions form a valid split for median calculation.

        Parameters
        ----------
        nums1 : list[int]
            A sorted list of integers.
        nums2 : list[int]
            A sorted list of integers.

        Returns
        -------
        float
            The median of the two sorted arrays.

        Raises
        ------
        ValueError
            If the input arrays are not sorted or invalid.

        Notes
        -----
        Key Idea
        --------
        We use binary search on the smaller array to find a partition such
        that all elements on the left side are less than or equal to all
        elements on the right side. This guarantees correct median values
        without merging arrays.

        Time Complexity
        ---------------
        O(log(min(m, n))) where m and n are lengths of nums1 and nums2.

        Space Complexity
        ----------------
        O(1), since only constant extra space is used.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.findMedianSortedArrays([1, 3], [2])
        2.0
        >>> sol.findMedianSortedArrays([1, 2], [3, 4])
        2.5
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        start, end = 0, x

        while start <= end:
            part_x = (start + end) // 2
            part_y = (x + y + 1) // 2 - part_x

            # Handle edges with sentinel values
            x_left = nums1[part_x - 1] if part_x > 0 else float("-inf")
            x_right = nums1[part_x] if part_x < x else float("inf")
            y_left = nums2[part_y - 1] if part_y > 0 else float("-inf")
            y_right = nums2[part_y] if part_y < y else float("inf")

            # Check if partition is correct
            if x_left <= y_right and y_left <= x_right:
                if (x + y) % 2 == 0:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
                return max(x_left, y_left)
            if x_left > y_right:
                end = part_x - 1
            else:
                start = part_x + 1

        raise ValueError("Input arrays are not sorted or invalid.")


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5

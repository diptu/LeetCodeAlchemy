"""Find the minimum in a rotated sorted array using binary search.

Key idea:
    In a rotated sorted array, the minimum element is the only element
    where the previous element is greater than it (considering rotation).
    Use binary search to narrow down the search space efficiently.

Time Complexity: O(log n)
Space Complexity: O(1)
"""



class Solution:
    """Solution class to find minimum in a rotated sorted array."""

    def findMin(self, nums: list[int]) -> int:
        """Return the minimum element in a rotated sorted array.

        Args:
            nums (List[int]): Rotated sorted array of integers.

        Returns:
            int: Minimum element in the array.
        """
        left, right = 0, len(nums) - 1

        # If array is not rotated, the first element is the min
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right, min must be right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # Minimum is at mid or left of mid

        return nums[left]


if __name__ == "__main__":
    solution = Solution()
    nums = [11, 13, 15, 17]  # Non-rotated example
    minimum = solution.findMin(nums)
    print(f"Minimum value: {minimum}")  # Expected output: 11

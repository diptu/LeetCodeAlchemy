from typing import List


class Solution:
    """Class to solve array-related problems."""

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Return the squares of a sorted array in non-decreasing order.

        Key Idea
        --------
        Use two pointers at the start and end of the array. Compare absolute
        values and place the largest square at the end of the result array.
        This avoids an extra sort and iterates only once.

        Parameters
        ----------
        nums : List[int]
            A list of integers sorted in non-decreasing order.

        Returns
        -------
        List[int]
            A list of the squares of each number in non-decreasing order.

        Time Complexity
        ---------------
        Best Case: O(n)
        Average Case: O(n)
        Worst Case: O(n)

        Space Complexity
        ----------------
        Best Case: O(n)
        Average Case: O(n)
        Worst Case: O(n)
        """
        n: int = len(nums)
        left: int = 0
        right: int = n - 1
        result: List[int] = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums: List[int] = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums))  # [0, 1, 9, 16, 100]

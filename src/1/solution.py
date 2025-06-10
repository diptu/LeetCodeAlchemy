"""Module providing an optimal solution to the Two Sum problem."""


class Solution:
    """Class to solve the Two Sum problem."""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Return the indices of the two numbers that add up to the target.

        This version uses a hash map to store seen values and their indices,
        allowing for a single-pass O(n) solution with constant-time lookups.

        Parameters
        ----------
        nums : List[int]
            A list of integers where exactly one solution exists.
        target : int
            The target sum for which two numbers in `nums` must add up to.

        Returns
        -------
        List[int]
            A list containing the indices of the two numbers that sum to `target`.

        Examples
        --------
        >>> solution = Solution()
        >>> solution.two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> solution.two_sum([3, 2, 4], 6)
        [1, 2]

        Time Complexity
        ---------------
        O(n)
            One pass through the list with constant-time hash map operations.

        Space Complexity
        ----------------
        O(n)
            Due to storage of seen values and their indices in a dictionary.
        """
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

        return []


if __name__ == "__main__":
    SOLUTION = Solution()
    RESULT = SOLUTION.twoSum([2, 7, 11, 15], 9)
    print(RESULT)  # [0, 1]

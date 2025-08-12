class Solution:
    """
    Class to find the single number in a list where every other element
    appears twice.

    Methods
    -------
    singleNumber(nums: list[int]) -> int
        Returns the element that appears only once in the list.
    """

    def singleNumber(self, nums: list[int]) -> int:
        """
        Find the number that appears only once in the list.

        This method uses the XOR operation to cancel out duplicate
        elements, leaving only the unique number.

        Explanation
        -----------
        XOR has two important properties:
        1. a ^ a = 0  (same numbers cancel each other)
        2. a ^ 0 = a  (XOR with 0 returns the same number)

        Example
        -------
        nums = [1, 1, 2, 2, 3]
        Step-by-step:
        - Start: single_num = 1
        - single_num = 1 ^ 1 = 0
        - single_num = 0 ^ 2 = 2
        - single_num = 2 ^ 2 = 0
        - single_num = 0 ^ 3 = 3
        Final result = 3

        Parameters
        ----------
        nums : list of int
            List of integers where every element except one appears twice.

        Returns
        -------
        int
            The single number that appears only once.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.singleNumber([1, 1, 2, 2, 3])
        3

        Time Complexity
        ---------------
        O(n) : Each element is processed once.

        Space Complexity
        ----------------
        O(1) : Only a constant amount of extra space is used.
        """
        single_num = nums[0]
        for i in range(1, len(nums)):
            single_num ^= nums[i]
        return single_num


if __name__ == "__main__":
    solution = Solution()
    nums_list = [1, 1, 2, 2, 3]
    result = solution.singleNumber(nums_list)
    print(result)  # 3

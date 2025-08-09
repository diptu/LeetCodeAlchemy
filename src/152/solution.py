"""Module providing solution to the Maximum Product Subarray problem."""



class Solution:
    """Class to solve the Maximum Product Subarray problem.

    Methods
    -------
    max_product(nums: List[int]) -> int
        Returns the maximum product of a contiguous subarray.

    Time Complexity
    ---------------
    O(n)
        Where n is the length of `nums`. We traverse the list twice
        (left-to-right and right-to-left in a single loop).

    Space Complexity
    ----------------
    O(1)
        Only a constant amount of extra space is used.
    """

    def max_product(self, nums: list[int]) -> int:
        """
        Compute the maximum product of any contiguous subarray.

        Parameters
        ----------
        nums : List[int]
            The input list of integers, which may contain negative numbers
            and zeros.

        Returns
        -------
        int
            The maximum product achievable from any contiguous subarray.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.max_product([2, 3, -2, 4])
        6
        >>> sol.max_product([-2, 0, -1])
        0
        >>> sol.max_product([-2, 3, -4])
        24
        """
        n = len(nums)
        left_prod = 1
        right_prod = 1
        result = nums[0]

        for i in range(n):
            left_prod = (left_prod or 1) * nums[i]
            right_prod = (right_prod or 1) * nums[n - 1 - i]
            result = max(result, left_prod, right_prod)

            if nums[i] == 0:
                left_prod = 1
            if nums[n - 1 - i] == 0:
                right_prod = 1

        return result


if __name__ == "__main__":
    solution = Solution()
    nums_list = [2, 3, -2, 4]
    output = solution.max_product(nums_list)
    print(output)  # Expected output: 6

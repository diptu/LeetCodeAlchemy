from typing import List


class Solution:
    """
    A class to solve the missing number problem.

    Methods
    -------
    missingNumber(nums: List[int]) -> int
        Finds the missing number in a sequence of integers from 0 to n.
    """

    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the single missing number in a sequence containing integers
        from 0 to n with one element missing, using XOR.

        Parameters
        ----------
        nums : List[int]
            A list containing distinct integers in the range [0, n],
            where exactly one integer is missing.

        Returns
        -------
        int
            The missing number in the range [0, n].

        Key Idea
        --------
        XOR has the property that a ^ a = 0 and a ^ 0 = a. If we XOR all
        numbers from 0 to n together with all elements in `nums`, all the
        matching pairs cancel out, leaving only the missing number.

        Notes
        -----
        Time complexity : O(n)
            Each element is XORed once.
        Space complexity : O(1)
            Constant extra space is used.

        This avoids potential integer overflow in other languages
        (not a problem in Python, but relevant in C++/Java).

        Examples
        --------
        >>> sol = Solution()
        >>> sol.missingNumber([3, 0, 1])
        2
        >>> sol.missingNumber([0, 1])
        2
        >>> sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        8
        """
        n = len(nums)
        xor_all = 0
        for i in range(n + 1):
            xor_all ^= i
        for num in nums:
            xor_all ^= num
        return xor_all


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 0, 1]
    print(solution.missingNumber(nums))  # 2

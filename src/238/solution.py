"""
Module that contains a Solution class to compute
product of array elements except self.
"""

from typing import List


class Solution:
    """
    A class that provides a method to calculate the product of all elements
    in an array except the element at each index.
    """

    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Compute the product of all elements except self using prefix products.

        Parameters
        ----------
        nums : List[int]
            List of integers.

        Returns
        -------
        List[int]
            List where each element is the product of all other elements.
        """
        length = len(nums)
        left_to_right = [1] * length
        prefix_sum = 1
        for i in range(1, length):
            prefix_sum *= nums[i - 1]
            left_to_right[i] = prefix_sum

        right_to_left = [1] * length
        prefix_sum = 1
        for i in range(length - 2, -1, -1):
            prefix_sum *= nums[i + 1]
            right_to_left[i] = prefix_sum

        result = [1] * length
        for i in range(length):
            result[i] = left_to_right[i] * right_to_left[i]

        return result


if __name__ == "__main__":
    solution = Solution()
    input_nums = [1, 2, 3, 4]
    output_result = solution.product_except_self(input_nums)
    print(output_result)  # Expected: [24, 12, 8, 6]

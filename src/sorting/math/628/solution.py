from typing import List


class Solution:
    """
    A class that provides a method to compute the maximum product of
    three integers in a list.

    Key Idea
    --------
    The maximum product of three numbers can only come from:
    1. The product of the three largest numbers.
    2. The product of the two smallest (possibly negative) numbers and
       the largest number.

    To compute this efficiently, we track the three largest and two
    smallest numbers in one pass without sorting.

    Time Complexity
    ---------------
    Best Case: O(n)  (single pass through the array)
    Average Case: O(n)
    Worst Case: O(n)

    Space Complexity
    ----------------
    O(1) - only a fixed number of variables are used.

    Parameters
    ----------
    nums : List[int]
        A list of integers (length ≥ 3).

    Returns
    -------
    int
        The maximum product of any three numbers.

    Example
    -------
    >>> sol = Solution()
    >>> sol.maximum_product([1, 2, 3])
    6
    >>> sol.maximum_product([-10, -10, 5, 2])
    500
    """

    def maximum_product(self, nums: List[int]) -> int:
        """Return the maximum product of three numbers."""
        max1: float = float("-inf")
        max2: float = float("-inf")
        max3: float = float("-inf")
        min1: float = float("inf")
        min2: float = float("inf")

        for num in nums:
            # Update maximums
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            # Update minimums
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)


if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    assert sol.maximum_product([1, 2, 3]) == 6
    assert sol.maximum_product([1, 2, 3, 4]) == 24
    assert sol.maximum_product([-1, -2, -3]) == -6

    # Cases with negative numbers
    assert sol.maximum_product([-1, -2, -3, 4]) == 24
    assert sol.maximum_product([-10, -10, 5, 2]) == 500

    # Edge case: large numbers
    assert sol.maximum_product([1000, 999, 998, -1000]) == 997002000

    # Edge case: exactly three numbers
    assert sol.maximum_product([-5, -4, -3]) == -60
    assert sol.maximum_product([-5, -4, 6]) == 120

    print("All tests passed ✅")

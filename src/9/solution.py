"""Module providing an optimal solution to the palindrom problem."""


class Solution:
    """
    Provides a method to determine if an integer is a palindrome.

    A palindrome integer reads the same forwards and backwards.
    This implementation converts the integer to a string and checks
    if it is equal to its reverse.

    Methods
    -------
    isPalindrome(x: int) -> bool
        Returns True if the integer `x` is a palindrome, else False.

    Examples
    --------
    >>> solution = Solution()
    >>> solution.isPalindrome(121)
    True
    >>> solution.isPalindrome(-121)
    False
    >>> solution.isPalindrome(10)
    False
    """

    def isPalindrome(self, x: int) -> bool:
        """
        Check whether an integer is a palindrome.

        Parameters
        ----------
        x : int
            The integer to check.

        Returns
        -------
        bool
            True if `x` is a palindrome, False otherwise.
        """
        x = str(x)

        if x == x[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    SOLUTION = Solution()
    x = 121
    RESULT = SOLUTION.isPalindrome(x)
    print(RESULT)  # True

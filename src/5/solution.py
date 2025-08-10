class Solution:
    """
    Class to find the longest palindromic substring in a given string.

    Methods
    -------
    longestPalindrome(s: str) -> str
        Returns the longest palindromic substring in `s`.
    """

    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring within the input string.

        Parameters
        ----------
        s : str
            Input string to search for palindrome substrings.

        Returns
        -------
        str
            The longest palindromic substring found in `s`.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.longestPalindrome("babad")
        'bab'  # or 'aba'
        >>> sol.longestPalindrome("cbbd")
        'bb'

        Time Complexity
        ---------------
        O(n^2) : In the worst case, each character is expanded around
                 twice (odd and even), potentially covering the entire string.

        Space Complexity
        ----------------
        O(n) : The space used by the output substring in the worst case
               when the entire string is a palindrome.
        """
        length = len(s)
        lps = ""

        for i in range(length):
            # Odd length palindrome
            low, high = i, i
            while low >= 0 and high < length and s[low] == s[high]:
                if (high - low + 1) > len(lps):
                    lps = s[low : high + 1]
                low -= 1
                high += 1

            # Even length palindrome
            low, high = i, i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if (high - low + 1) > len(lps):
                    lps = s[low : high + 1]
                low -= 1
                high += 1

        return lps


if __name__ == "__main__":
    solution = Solution()
    test_str = "babad"
    result = solution.longestPalindrome(test_str)
    print(result)  # Output: 'bab' or 'aba'

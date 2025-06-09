"""Anagram checker module."""

from collections import Counter


class Solution:
    """Class containing a method to check if two strings are anagrams."""

    def is_anagram(self, s: str, t: str) -> bool:
        """
        Determine whether two strings are anagrams of each other.

        Two strings are anagrams if they contain the same characters
        in the same frequency, regardless of order.

        Parameters
        ----------
        s : str
            The first string to compare.
        t : str
            The second string to compare.

        Returns
        -------
        bool
            True if `s` and `t` are anagrams, False otherwise.

        Examples
        --------
        >>> solution = Solution()
        >>> solution.is_anagram("listen", "silent")
        True
        >>> solution.is_anagram("hello", "world")
        False

        Time Complexity
        ---------------
        O(n)
            Where n is the length of the input strings. Counting characters
            using `Counter` takes linear time.

        Space Complexity
        ----------------
        O(k)
            Where k is the number of unique characters in the strings, used
            to store the frequency counts.
        """
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    str1, str2 = "annangram", "nagaram"
    print(solution.is_anagram(str1, str2))  # True

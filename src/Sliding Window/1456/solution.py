"""Module for computing the maximum number of vowels in a substring of fixed length."""



class Solution:
    """Provides methods for string and sliding window problems."""

    def max_vowels(self, s: str, k: int) -> int:
        """
        Return the maximum number of vowel letters in any substring of length `k`.

        Parameters
        ----------
        s : str
            The input string.
        k : int
            The fixed length of the substring window.

        Returns
        -------
        int
            The maximum number of vowels in any k-length substring.

        Time Complexity
        ---------------
        O(n), where n is the length of `s`.

        Space Complexity
        ----------------
        O(1), constant space for the vowel set and counters.
        """
        # vowels: Set[str] = {"a", "e", "i", "o", "u"}
        vowels = frozenset("aeiou")
        count = sum(char in vowels for char in s[:k])
        max_count = count

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            max_count = max(max_count, count)

        return max_count


def main() -> None:
    """Example usage of max_vowels."""
    solution = Solution()
    s = "leetcode"
    k = 3
    maximum = solution.max_vowels(s, k)
    print(f"The maximum number of vowel letters in any substring: {maximum}")


if __name__ == "__main__":
    main()

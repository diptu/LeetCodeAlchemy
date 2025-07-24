class Solution:
    """Class to solve the longest substring without repeating characters problem."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Parameters
        ----------
        s : str
            Input string to analyze.

        Returns
        -------
        int
            The length of the longest substring with all unique characters.
        """
        max_length = 0
        left = 0
        right = 0
        char_set = set()

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


def main() -> None:
    """Main function to test the Solution class."""
    solution = Solution()
    test_str = "pwwkew"
    max_len = solution.lengthOfLongestSubstring(test_str)
    print(f"Maximal length: {max_len}")


if __name__ == "__main__":
    main()

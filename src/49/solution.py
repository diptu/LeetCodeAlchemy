"""Module providing an optimal solution to the Group Anagrams problem using frequency tuple keys.

This implementation groups anagrams by counting character frequencies
and using a tuple of counts as the dictionary key for optimal performance.

Example:

| Frequency Key (tuple of counts for a–z)       | Anagram Group            |
|------------------------------------------------|-------------------------|
| (1, 0, 0, 0, 1, 0, ..., 0, 1, 0, ..., 0)       | ['eat', 'tea', 'ate']   |
| (1, 0, 0, 0, 0, 0, ..., 1, 0, 0, ..., 0)       | ['tan', 'nat']          |
| (1, 1, 0, 0, 0, 0, ..., 0, 1, 0, ..., 0)       | ['bat']                 |
"""

from typing import List, Tuple
from collections import defaultdict


def frequency_key(word: str) -> Tuple[int, ...]:
    """
    Generate a frequency tuple key representing counts of letters 'a' to 'z'.

    Parameters
    ----------
    word : str
        The input word consisting of lowercase English letters.

    Returns
    -------
    Tuple[int, ...]
        A tuple of length 26 where each element is the count of corresponding
        letters from 'a' to 'z' in the input word.

    Example
    -------
    >>> frequency_key('eat')
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
    """
    freq = [0] * 26
    for char in word:
        index = ord(char) - ord("a")
        if 0 <= index < 26:
            freq[index] += 1
    return tuple(freq)


class Solution:
    """
    Class containing the method to group anagrams using frequency tuple keys.

    Time Complexity
    ---------------
    O(N * K), where N is the number of strings and K is the maximum length of a string.
    Counting characters and generating tuple keys is done in O(K) per word.

    Space Complexity
    ----------------
    O(N * K) for storing the input strings in groups and the frequency tuple keys.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group words that are anagrams of each other.

        Parameters
        ----------
        strs : List[str]
            A list of lowercase strings.

        Returns
        -------
        List[List[str]]
            A list of groups where each group contains words that are anagrams.

        Example
        -------
        >>> sol = Solution()
        >>> sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        """
        groups = defaultdict(list)

        for word in strs:
            key = frequency_key(word)
            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)

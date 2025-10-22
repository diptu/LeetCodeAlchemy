from typing import List, Dict


class Solution:
    """
    Verify if words are sorted according to a custom alien dictionary.

    Key Idea
    --------
    We compare each adjacent pair of words (w1, w2) lexicographically
    using the given alien order. For each pair:
      1. Find the first differing character.
      2. If the order of characters is violated, return False.
      3. If no difference exists but w1 is longer than w2,
         return False (prefix rule).

    Time Complexity
    ---------------
    O(n * m) — where n = number of words, m = average word length.
    Each character is inspected at most once.

    Space Complexity
    ----------------
    O(1) — apart from a constant-size mapping of characters to ranks.

    Example
    -------
    >>> sol = Solution()
    >>> sol.is_alien_sorted(["hello", "leetcode"],
    ...                     "hlabcdefgijkmnopqrstuvwxyz")
    True
    """

    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        """Return True if words are sorted by alien dictionary order."""
        rank: Dict[str, int] = {ch: i for i, ch in enumerate(order)}

        # Step 1: Compare adjacent word pairs
        for w1, w2 in zip(words, words[1:]):
            # Step 2: Compare letters of each pair
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    # Step 3: Check relative order
                    if rank[c1] > rank[c2]:
                        return False
                    break
            else:
                # Step 4: Handle prefix case
                if len(w1) > len(w2):
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()

    # ✅ Example test cases
    assert sol.is_alien_sorted(
        ["hello", "leetcode"],
        "hlabcdefgijkmnopqrstuvwxyz",
    )

    assert not sol.is_alien_sorted(
        ["word", "world", "row"],
        "worldabcefghijkmnpqstuvxyz",
    )

    assert not sol.is_alien_sorted(
        ["apple", "app"],
        "abcdefghijklmnopqrstuvwxyz",
    )

    print("All tests passed ✅")

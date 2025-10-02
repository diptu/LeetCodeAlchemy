from typing import List


class Solution:
    """
    A class to perform rank transform of an array.

    Key Idea
    --------
    To assign ranks:
    1. Sort the unique values.
    2. Map each unique value to its rank.
    3. Replace each element in the array with its mapped rank.

    Time Complexity
    ---------------
    Best Case: O(n log n) (sorting unique values)
    Average Case: O(n log n)
    Worst Case: O(n log n)

    Space Complexity
    ----------------
    O(n) for the mapping dictionary.

    Parameters
    ----------
    arr : List[int]
        The input integer array.

    Returns
    -------
    List[int]
        The transformed array where each element is replaced with its rank.

    Example
    -------
    >>> sol = Solution()
    >>> sol.array_rank_transform([40, 10, 20, 30])
    [4, 1, 2, 3]
    >>> sol.array_rank_transform([100, 100, 100])
    [1, 1, 1]
    """

    def array_rank_transform(self, arr: List[int]) -> List[int]:
        """Return the rank transform of the array."""
        ranks: dict[int, int] = {}
        rank: int = 1
        for num in sorted(set(arr)):
            ranks[num] = rank
            rank += 1
        return [ranks[num] for num in arr]


if __name__ == "__main__":
    sol = Solution()

    # Basic test cases
    assert sol.array_rank_transform([40, 10, 20, 30]) == [4, 1, 2, 3]
    assert sol.array_rank_transform([100, 100, 100]) == [1, 1, 1]
    assert sol.array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [
        5,
        3,
        4,
        2,
        8,
        6,
        7,
        1,
        3,
    ]

    # Edge cases
    assert sol.array_rank_transform([]) == []
    assert sol.array_rank_transform([1]) == [1]
    assert sol.array_rank_transform([-10, -5, -5, 0, 5]) == [1, 2, 2, 3, 4]
    assert sol.array_rank_transform([2, 2, 1]) == [2, 2, 1]

    print("All tests passed ✅")

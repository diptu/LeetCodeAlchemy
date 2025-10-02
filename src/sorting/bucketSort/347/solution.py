from typing import List
from collections import Counter


class Solution:
    """LeetCode 347: Top K Frequent Elements.

    Key Idea
    --------
    Use a bucket-sort style approach:
    - Count frequencies of each element.
    - Create a bucket where index = frequency, value = list of numbers.
    - Traverse buckets from high to low frequency and collect elements until
      k are found.

    Complexity
    ----------
    Let n = len(nums), u = number of unique elements.

    Time:
        Best   O(n)   - Counting + buckets, stop early if k small.
        Avg    O(n)   - Always traverse buckets, collect k results.
        Worst  O(n)   - All elements unique, need full pass.

    Space:
        Best   O(u)   - Hashmap + bucket storage.
        Avg    O(u)   - Proportional to unique elements.
        Worst  O(n)   - If all elements unique.

    Parameters
    ----------
    nums : List[int]
        List of integers.
    k : int
        Number of top frequent elements to return.

    Returns
    -------
    List[int]
        The k most frequent elements.

    Example
    -------
    >>> Solution().top_k_frequent([1, 1, 2, 2, 3], 2)
    [1, 2]
    """

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequent elements from the input list."""
        if not nums or k <= 0:
            return []

        freq: Counter[int] = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result: List[int] = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
                if len(result) >= k:
                    return result[:k]
        return result


if __name__ == "__main__":
    # Quick unit tests (pytest style assertions)
    sol = Solution()

    # Basic case
    assert sorted(sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

    # Case with all equal frequency
    out = sol.top_k_frequent([1, 2, 3], 2)
    assert len(out) == 2 and all(x in [1, 2, 3] for x in out)

    # Larger case with ties
    out = sol.top_k_frequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2, 3, 3], 2)
    assert len(out) == 2 and all(x in [1, 2, 3] for x in out)

    # Edge cases
    assert not sol.top_k_frequent([], 2)
    assert sol.top_k_frequent([5], 1) == [5]
    assert sol.top_k_frequent([4, 4, 4, 4], 1) == [4]

    print("All tests passed ✅")

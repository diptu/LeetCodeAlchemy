"""Module providing an optimal solution to the Top K Frequent Elements.

This module defines a Solution class with a method that finds the top
K most frequent elements in a list using a min-heap for efficient retrieval.
"""

from collections import Counter
from typing import List
import heapq


class Solution:
    """Class for solving the Top K Frequent Elements problem."""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the top K most frequent elements from the given list.

        Parameters
        ----------
        nums : List[int]
            A list of integers where the frequency of elements is to be computed.
        k : int
            The number of most frequent elements to return.

        Returns
        -------
        List[int]
            A list containing the top K frequent elements. The order of elements
            in the returned list is not guaranteed to be sorted by frequency.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.topKFrequent([1, 1, 2, 2, 2, 3], 2)
        [2, 1]
        """
        freq: Counter[int] = Counter(nums)
        min_heap: List[tuple[int, int]] = []

        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2, 2, 2, 3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(result)  # Example output: [1, 2]

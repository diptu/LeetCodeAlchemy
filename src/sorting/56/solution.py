"""Merge overlapping intervals.

Key idea:
    1. Sort intervals by start time.
    2. Iterate through the sorted intervals:
       - If the current interval overlaps with the last merged interval,
         merge them by updating the end.
       - Otherwise, append current interval as a new merged interval.

Time Complexity:
    Best case: O(n log n) - sorting dominates.
    Average case: O(n log n) - sorting dominates.
    Worst case: O(n log n) - sorting dominates.

Space Complexity:
    O(n) - to store the merged intervals.
"""

from typing import List
from operator import itemgetter


class Solution:
    """Solution class for merging overlapping intervals."""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge overlapping intervals into non-overlapping intervals.

        Parameters
        ----------
        intervals : List[List[int]]
            A list of intervals represented as [start, end].

        Returns
        -------
        List[List[int]]
            A list of merged non-overlapping intervals.
        """
        if len(intervals) <= 1:
            return intervals

        # Sort intervals by start time using itemgetter
        intervals.sort(key=itemgetter(0))

        merged: List[List[int]] = [intervals[0]]

        for current in intervals[1:]:
            # Merge if overlapping
            if current[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)

        return merged


if __name__ == "__main__":
    solution = Solution()
    intervals = [[4, 7], [1, 4]]
    result = solution.merge(intervals)
    print(result)  # Expected output: [[1, 7]

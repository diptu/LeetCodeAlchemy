from typing import List


class Solution:
    """
    Optimal and clean greedy solution for LeetCode 435 — Non-overlapping Intervals.

    Idea
    ----
    Sort by end time, then greedily count how many intervals
    can fit without overlapping. The minimum removals are
    total intervals minus non-overlapping count.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        keep = 1
        for start, next_end in intervals[1:]:
            if start >= end:
                keep += 1
                end = next_end

        return len(intervals) - keep


if __name__ == "__main__":
    sol = Solution()

    # ✅ Tests
    assert sol.erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    assert sol.erase_overlap_intervals([]) == 0
    assert sol.erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2

    print("All tests passed ✅")

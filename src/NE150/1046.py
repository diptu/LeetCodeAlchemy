"""
LeetCode #1046 — Last Stone Weight

Author: Nazmul Alam Diptu
--------------------------------------------------------

Implementations
---------------
1. **PQ-based (Optimized)** → O(N log N) Time, O(N) Space

Key Idea
--------
Use a *max-heap* to repeatedly smash the two heaviest stones:

1. Convert stones to negative values to simulate a max-heap using Python's `heapq`.
2. Repeatedly pop the two largest stones.
3. If their weights differ, push the remaining fragment back into the heap.
4. Continue until zero or one stones remain.
"""

from __future__ import annotations

import heapq


class Solution:
    """Optimized max-heap solution for Last Stone Weight."""

    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Smash stones until one or none remain.

        Steps
        -----
        1. Convert stones to negatives to form a max-heap.
        2. Pop two heaviest stones each round.
        3. If they differ, push the remaining (negative) difference back.
        4. Return the final stone weight or 0.
        """
        if not stones:
            return 0

        # Build max-heap (using negatives)
        max_pq = [-s for s in stones]
        heapq.heapify(max_pq)

        while len(max_pq) > 1:
            y = -heapq.heappop(max_pq)  # heaviest
            x = -heapq.heappop(max_pq)  # second heaviest

            if y != x:
                heapq.heappush(max_pq, -(y - x))

        return -max_pq[0] if max_pq else 0


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    sol = Solution()

    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([2, 7, 4, 2, 8, 1]) == 0
    assert sol.lastStoneWeight([1, 1, 1, 1]) == 0
    assert sol.lastStoneWeight([1, 1, 1, 1, 1]) == 1

    print("✅ All tests passed successfully!")

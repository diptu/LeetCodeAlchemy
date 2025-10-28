"""
Task Scheduler Problem (LeetCode #621)

Author: Nazmul Alam Diptu
-----------------------------------------
This module provides two implementations of the Task Scheduler problem.

Problem Summary:
----------------
Given a list of tasks represented by capital letters (A–Z) and a non-negative
integer `n` representing the cooldown period, each task can only be executed
once every `(n + 1)` units of time.

Goal:
-----
Compute the minimum number of time units required to finish all tasks, assuming
one task can be executed per unit of time and idle periods are allowed.

Implementations:
----------------
1. **Mathematical Solution (Optimal)** → O(N), O(1)
2. **Heap + Queue Simulation** → O(N log k), O(k)

Only the optimal solution is active by default.
"""

from __future__ import annotations
from typing import List
from collections import Counter

# =============================================================================
# 🧠 Optimal O(N) Mathematical Solution (Default)
# =============================================================================


class Solution:
    """
    Optimal O(N) solution for the Task Scheduler problem.

    Key Idea
    --------
    The least number of time units required is governed by the most frequent
    tasks. The intuition:

    - Let `max_freq` be the maximum frequency among all tasks.
    - Let `num_max` be the number of tasks with frequency == `max_freq`.

    These define the minimum "frame" structure needed to schedule all tasks:
        result = max(len(tasks), (max_freq - 1) * (n + 1) + num_max)

    Example
    -------
    >>> sol = Solution()
    >>> sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    8

    Complexity
    ----------
    Time  : O(N)
        Counting tasks only.
    Space : O(1)
        Constant, since task types are limited (A–Z).
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Compute the minimum total time units to complete all tasks.

        Parameters
        ----------
        tasks : List[str]
            List of capital letter tasks (A–Z).
        n : int
            Cooldown interval between identical tasks.

        Returns
        -------
        int
            Minimum total time units to complete all tasks.
        """
        # Step 1: Count task frequencies
        task_counts = Counter(tasks)

        # Step 2: Identify the highest frequency
        max_freq = max(task_counts.values())

        # Step 3: Count how many tasks have this maximum frequency
        num_max = sum(1 for freq in task_counts.values() if freq == max_freq)

        # Step 4: Compute result using formula
        result = max(len(tasks), (max_freq - 1) * (n + 1) + num_max)

        return result


# =============================================================================
# 🧩 Alternative Heap + Queue Simulation Solution (Commented Out)
# =============================================================================
"""
from typing import List, Deque, Tuple
from collections import Counter, deque
import heapq

class Solution:
    '''
    Priority Queue + Cooldown Simulation (O(N log k))

    Key Idea
    ---------
    1. Use a max heap to pick the most frequent available task.
    2. Use a queue to track tasks cooling down along with when they become ready.
    3. Simulate each unit of time until all tasks complete.

    Example
    --------
    >>> sol = Solution()
    >>> sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    8

    Complexity
    -----------
    Time  : O(N log k)
        Each push/pop in heap.
    Space : O(k)
        For heap and cooldown queue.
    '''

    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap: List[int] = [-freq for freq in task_counts.values()]
        heapq.heapify(max_heap)

        cooldown: Deque[Tuple[int, int]] = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                remaining = 1 + heapq.heappop(max_heap)
                if remaining != 0:
                    cooldown.append((remaining, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
"""


# =============================================================================
# ✅ Unit Tests
# =============================================================================

if __name__ == "__main__":
    sol = Solution()

    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    assert sol.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B", "C", "C"], 2) == 8

    print("✅ All tests passed successfully!")

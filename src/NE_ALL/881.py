"""
LeetCode #881: Boats to Save People

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
You are given a list of people's weights and a boat weight limit.

Each boat can carry:
- At most 2 people
- Total weight must not exceed the limit

Return the minimum number of boats required to rescue everyone.

Constraints
-----------
- 1 <= len(people) <= 50_000
- 1 <= people[i] <= limit <= 30_000

Key Idea
--------
Use greedy + two pointers:

1. Sort the weights.
2. Pair the lightest person with the heaviest person whenever possible.
3. If they cannot fit together, send the heaviest person alone.
4. Each step uses exactly one boat.

Why greedy works:
Using the heaviest remaining person immediately is always optimal.
"""

from __future__ import annotations

from typing import List


class Solution:
    """Solve the Boats to Save People problem using greedy two pointers."""

    def num_rescue_boats(self, people: List[int], limit: int) -> int:
        """
        Return the minimum number of boats needed.

        Args:
            people (List[int]): List of people's weights.
            limit (int): Maximum weight capacity per boat.

        Returns:
            int: Minimum number of boats required.
        """
        people.sort()

        left: int = 0
        right: int = len(people) - 1
        boats_used: int = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats_used += 1

        return boats_used


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run basic test cases."""
    solution: Solution = Solution()

    assert solution.num_rescue_boats([1, 2], 3) == 1
    assert solution.num_rescue_boats([3, 2, 2, 1], 3) == 3
    assert solution.num_rescue_boats([3, 5, 3, 4], 5) == 4
    assert solution.num_rescue_boats([2, 2], 6) == 1
    assert solution.num_rescue_boats([5], 5) == 1

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()

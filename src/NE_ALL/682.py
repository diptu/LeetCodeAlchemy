"""
LeetCode #682: Baseball Game

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------
You are given a list of operations representing scores in a baseball game.

Operations:
- Integer x : Record a new score of x
- "+"       : Record sum of previous two valid scores
- "D"       : Record double the previous valid score
- "C"       : Remove the previous valid score

Return the sum of all valid scores.

Constraints
-----------
- 1 <= len(operations) <= 1000
- operations[i] is one of:
  integer string, "+", "D", "C"

Key Idea
--------
Use a stack to store valid scores.

For each operation:
1. Number -> push to stack
2. "+"    -> push sum of last two scores
3. "D"    -> push double last score
4. "C"    -> remove last score

Final answer is sum of stack.

Complexity
----------
Time: O(n)
- Process each operation once.

Space: O(n)
- Stack may store all valid scores.
"""

from __future__ import annotations

from typing import List


class Solution:
    """Solve Baseball Game using a stack."""

    def cal_points(self, operations: List[str]) -> int:
        """
        Return total score after processing operations.

        Args:
            operations (List[str]): List of score operations.

        Returns:
            int: Final total score.
        """
        scores: List[int] = []

        operation: str
        value: int

        for operation in operations:
            if operation == "+":
                scores.append(scores[-1] + scores[-2])

            elif operation == "D":
                scores.append(2 * scores[-1])

            elif operation == "C":
                scores.pop()

            else:
                value = int(operation)
                scores.append(value)

        return sum(scores)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run test cases."""
    solution: Solution = Solution()

    assert solution.cal_points(["5", "2", "C", "D", "+"]) == 30
    assert solution.cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert solution.cal_points(["1", "C"]) == 0
    assert solution.cal_points(["3"]) == 3
    assert solution.cal_points(["3", "D"]) == 9

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()

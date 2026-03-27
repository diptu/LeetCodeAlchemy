"""
LeetCode #191. Number of 1 Bits

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------


Complexity
----------


Key Idea
--------

"""

from __future__ import annotations
from typing import Dict


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n >> 1  # right shift by  1 or divide by 2

        return count


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert solution.hammingWeight(11) == 3
    assert solution.hammingWeight(n=2147483645) == 30
    assert solution.hammingWeight(n=128) == 1

    print("✅ All tests passed successfully!")

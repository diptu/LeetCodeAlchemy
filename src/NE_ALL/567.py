"""
LeetCode #1768: Merge Strings Alternately

Author: Nazmul Alam Diptu
----------------------------------------

Problem
-------


Key Idea
--------

"""

from __future__ import annotations


class Solution:
   def checkInclusion(self, s1: str, s2: str) -> bool:

    
# =============================================================================
# ✅ Unit Tests
# =============================================================================
def run_tests() -> None:
    """Run test cases."""
    solution: Solution = Solution()

    assert solution.checkInclusion(s1 = "ab", s2 = "eidbaooo") ==True
    assert solution.checkInclusion(s1 = "ab", s2 = "eidboaoo") ==False


    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()

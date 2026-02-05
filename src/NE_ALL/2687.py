"""
LeetCode #2678. Number of Senior Citizens

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
You are given an array of strings `details`, where each string represents
a person's information in a fixed format.

The age of the person is represented by the 12th and 13th characters
(0-indexed positions 11 and 12).

Return the number of people whose age is strictly greater than 60.

Complexity
----------
Time:  O(n), where n = len(details)
Space: O(1)

Key Idea
--------
- Each string has a fixed length and format
- Extract the age using direct indexing
- Count how many ages are greater than 60

Note
----
This solution relies on the problem's guaranteed string format.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Count senior citizens based on encoded age information."""

    def count_seniors(self, details: List[str]) -> int:
        """
        Return the number of people whose age is strictly greater than 60.
        """
        count: int = 0

        for record in details:
            age: int = int(record[11:13])
            if age > 60:
                count += 1

        return count


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert (
        solution.count_seniors(
            ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
        )
        == 2
    )

    assert solution.count_seniors(["1313579440F2036", "2921522980M5644"]) == 0

    print("✅ All tests passed successfully!")

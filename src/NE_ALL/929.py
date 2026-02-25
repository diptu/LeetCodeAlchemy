"""
LeetCode #929. Unique Email Addresses

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Every valid email consists of a local name and a domain name,
separated by '@'.

Rules for processing:
1. Ignore everything after a '+' in the local name.
2. Remove all '.' characters from the local name.
3. The domain name remains unchanged.

Return the number of unique email addresses after normalization.

Complexity
----------
Time  : O(n * m)
        n = number of emails
        m = average length of each email
Space : O(n)

Key Idea
--------
Normalize each email according to the rules and store
the processed version in a set to ensure uniqueness.
"""

from __future__ import annotations
from typing import List


class Solution:
    """Count unique normalized email addresses."""

    def numUniqueEmails(self, emails: List[str]) -> int:  # noqa: N802
        unique_emails: set[str] = set()

        for email in emails:
            local, domain = email.split("@")

            # Remove everything after '+'
            local = local.split("+")[0]

            # Remove all dots
            local = local.replace(".", "")

            normalized = f"{local}@{domain}"
            unique_emails.add(normalized)

        return len(unique_emails)


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    assert (
        solution.numUniqueEmails(
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ]
        )
        == 2
    )

    assert (
        solution.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
        == 3
    )

    print("✅ All tests passed successfully!")

"""
LeetCode #234. Palindrome Linked List

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the head of a singly linked list, return True if it is a palindrome,
or False otherwise.

Complexity
----------
Time:  O(n)
Space: O(1)

Key Idea
--------
- Use fast & slow pointers to find the middle
- Reverse the second half of the list in-place
- Compare first half and reversed second half

Note
----
The list structure is modified during the check.
"""

from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    """Check whether a singly linked list is a palindrome."""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find middle using fast & slow pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev: Optional[ListNode] = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Step 3: Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    solution = Solution()

    # Case 1: [1, 2, 2, 1]
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(2)
    head1.next.next.next = ListNode(1)
    assert solution.isPalindrome(head1) is True

    # Case 2: [1, 2]
    head2 = ListNode(1)
    head2.next = ListNode(2)
    assert solution.isPalindrome(head2) is False

    # Case 3: [1]
    head3 = ListNode(1)
    assert solution.isPalindrome(head3) is True

    print("✅ All tests passed successfully!")

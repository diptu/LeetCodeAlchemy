"""
LeetCode #203 — Remove Linked List Elements

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the head of a linked list and an integer val, remove all the
nodes of the linked list that have Node.val == val, and return the
new head.

Complexity
----------
Time  : O(n)
Space : O(1)

Key Idea
--------
Use a dummy (sentinel) node to simplify edge cases where the head
node itself needs to be removed.

Traverse the list once and bypass nodes whose value equals `val`.

Edge Cases
----------
- Empty list
- All nodes removed
- Head node(s) removed
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    """Remove elements from a linked list."""

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Remove all nodes with value equal to `val`.

        Parameters
        ----------
        head : Optional[ListNode]
            Head of the linked list.
        val : int
            Value to remove.

        Returns
        -------
        Optional[ListNode]
            Head of the modified linked list.
        """
        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


# =============================================================================
# ✅ Unit Tests
# =============================================================================
def list_to_linked(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()

    head1 = list_to_linked([1, 2, 6, 3, 4, 5, 6])
    assert linked_to_list(solution.removeElements(head1, 6)) == [1, 2, 3, 4, 5]

    head2 = list_to_linked([])
    assert linked_to_list(solution.removeElements(head2, 1)) == []

    head3 = list_to_linked([7, 7, 7, 7])
    assert linked_to_list(solution.removeElements(head3, 7)) == []

    head4 = list_to_linked([1, 2, 3])
    assert linked_to_list(solution.removeElements(head4, 4)) == [1, 2, 3]

    print("✅ All tests passed successfully!")

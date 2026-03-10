"""
LeetCode #83 — Remove Duplicates from Sorted List

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Complexity
----------
Time: O(N) where N is the number of nodes in the list.
Space: O(1) as we are modifying the list in-place.

Key Idea
--------
Since the list is sorted, duplicates are guaranteed to be adjacent.
We iterate through the list; if the current node's value equals the next
node's value, we skip the next node by reassigning `current.next`.
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""

    def __init__(self, val: int = 0, next_node: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next_node


class Solution:
    """Remove duplicates from a sorted singly linked list."""

    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterates through the linked list and removes consecutive duplicate values.

        Args:
            head: The head of the sorted linked list.

        Returns:
            The head of the modified linked list with duplicates removed.
        """
        current = head

        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next distinct element
                current = current.next

        return head


# =============================================================================
# ✅ Unit Tests & Helpers
# =============================================================================


def list_to_array(head: Optional[ListNode]) -> list[int]:
    """Helper to convert linked list to array for easy assertion."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr: list[int]) -> Optional[ListNode]:
    """Helper to convert array to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: [1, 1, 2] -> [1, 2]
    list1 = array_to_list([1, 1, 2])
    result1 = solution.delete_duplicates(list1)
    assert list_to_array(result1) == [1, 2]

    # Test Case 2: [1, 1, 2, 3, 3] -> [1, 2, 3]
    list2 = array_to_list([1, 1, 2, 3, 3])
    result2 = solution.delete_duplicates(list2)
    assert list_to_array(result2) == [1, 2, 3]

    # Test Case 3: Empty List
    assert list_to_array(solution.delete_duplicates(None)) == []

    print("✅ All tests passed successfully!")

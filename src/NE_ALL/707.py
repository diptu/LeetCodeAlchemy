"""
LeetCode #707 — Design Linked List

Author: Nazmul Alam Diptu
--------------------------------------------------------

Problem
-------
Design a singly linked list that supports the following operations:
- get(index)
- addAtHead(val)
- addAtTail(val)
- addAtIndex(index, val)
- deleteAtIndex(index)

Complexity
----------
Time
- get           : O(n)
- addAtHead     : O(1)
- addAtTail     : O(n)
- addAtIndex    : O(n)
- deleteAtIndex : O(n)

Space
- O(n) for storing nodes

Key Idea
--------
Maintain:
- A `head` pointer for the linked list
- A `size` counter to validate indices efficiently

All operations are done via pointer manipulation.

Edge Cases
----------
- Index < 0
- Index > size
- Empty list
- Insertion at head or tail
- Deletion at head
"""

from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional["ListNode"] = None


class MyLinkedList:
    """Custom singly linked list implementation."""

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None
        self.size: int = 0

    def get(self, index: int) -> int:
        """
        Return the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """Insert a node at the beginning of the linked list."""
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """Append a node to the end of the linked list."""
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node if the index is valid."""
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


# =============================================================================
# ✅ Unit Tests
# =============================================================================
if __name__ == "__main__":
    myLinkedList = MyLinkedList()

    myLinkedList.addAtHead(1)  # 1
    myLinkedList.addAtTail(3)  # 1 -> 3
    myLinkedList.addAtIndex(1, 2)  # 1 -> 2 -> 3

    assert myLinkedList.get(0) == 1
    assert myLinkedList.get(1) == 2
    assert myLinkedList.get(2) == 3

    myLinkedList.deleteAtIndex(1)  # 1 -> 3
    assert myLinkedList.get(1) == 3

    myLinkedList.deleteAtIndex(0)  # 3
    assert myLinkedList.get(0) == 3

    myLinkedList.deleteAtIndex(0)  # empty
    assert myLinkedList.get(0) == -1

    print("✅ All tests passed successfully!")

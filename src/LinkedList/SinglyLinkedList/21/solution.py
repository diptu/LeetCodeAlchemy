"""Merge two sorted singly linked lists.

This module provides a ListNode data structure and a Solution class with a
merge_two_lists method, plus small utilities for building and printing lists.
"""

from __future__ import annotations

from typing import Iterator, Optional


class ListNode:
    """Singly linked list node.

    Parameters
    ----------
    val : int, default 0
        Node value.
    next : Optional[ListNode], default None
        Reference to the next node.

    Notes
    -----
    Implements ``__iter__`` so a list can be converted via ``list(head)``.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next

    def __iter__(self) -> Iterator[int]:
        """Iterate values from this node onward."""
        current: Optional["ListNode"] = self
        while current is not None:
            yield current.val
            current = current.next


def traverse_list(head: Optional[ListNode]) -> None:
    """Print the list values from head to tail.

    Parameters
    ----------
    head : Optional[ListNode]
        Head of the list to traverse.

    Examples
    --------
    >>> head = ListNode(1, ListNode(3, ListNode(5)))
    >>> traverse_list(head)
    1 3 5
    """
    node = head
    out = []
    while node is not None:
        out.append(str(node.val))
        node = node.next
    print(" ".join(out))


class Solution:
    """Linked list algorithms."""

    @staticmethod
    def merge_two_lists(
        list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two sorted (non-decreasing) singly linked lists.

        Parameters
        ----------
        list1 : Optional[ListNode]
            Head of the first sorted list.
        list2 : Optional[ListNode]
            Head of the second sorted list.

        Returns
        -------
        Optional[ListNode]
            Head of the merged sorted list. Returns ``None`` if both inputs are
            ``None``.

        Notes
        -----
        - Time complexity: ``O(n + m)`` where ``n`` and ``m`` are the lengths
          of the two lists.
        - Space complexity: ``O(1)`` extra (relinks existing nodes).
        - Uses a dummy sentinel to simplify edge cases.

        Examples
        --------
        >>> a = ListNode(1, ListNode(2, ListNode(4)))
        >>> b = ListNode(1, ListNode(3, ListNode(4)))
        >>> head = Solution.merge_two_lists(a, b)
        >>> list(head)
        [1, 1, 2, 3, 4, 4]
        """
        dummy = ListNode()
        tail = dummy

        l1, l2 = list1, list2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the (at most one) non-empty remainder.
        tail.next = l1 if l1 is not None else l2
        return dummy.next


if __name__ == "__main__":
    solution = Solution()

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    result = solution.merge_two_lists(list1, list2)
    traverse_list(result)  # 1 1 2 3 4 4

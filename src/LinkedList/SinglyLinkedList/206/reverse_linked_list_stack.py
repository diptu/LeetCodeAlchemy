# file: reverse_linked_list_stack.py
from typing import Optional
from collections import deque


class ListNode:
    """Singly-linked list node.

    Parameters
    ----------
    val : int, default 0
        The value stored in the node.
    next : Optional[ListNode], default None
        Reference to the next node in the list.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next


def traverse_list(head: Optional[ListNode]) -> None:
    """Print the values of a linked list from head to tail.

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
    """Algorithms for singly-linked lists."""

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse a singly-linked list using a stack.

        The node values are pushed to a stack, then popped to build a new
        list in reverse order.

        Parameters
        ----------
        head : Optional[ListNode]
            The head of the linked list.

        Returns
        -------
        Optional[ListNode]
            New head of the reversed linked list.

        Complexity
        ----------
        Time : O(n)
            Each node is visited once to push and once to pop.
        Space : O(n)
            The stack stores up to n node values.

        Examples
        --------
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> result = Solution().reverse_list(head)
        >>> traverse_list(result)
        3 2 1
        """
        stack = deque()
        node = head
        while node is not None:
            stack.append(node.val)
            node = node.next

        dummy = ListNode()
        tail = dummy
        while stack:
            tail.next = ListNode(stack.pop())
            tail = tail.next
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverse_list(head)
    traverse_list(result)  # 5 4 3 2 1

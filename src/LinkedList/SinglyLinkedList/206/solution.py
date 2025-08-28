# file: reverse_linked_list_inplace.py
from typing import Optional


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
        """Reverse a singly-linked list in place.

        The list is reversed by iteratively redirecting `next` pointers.
        No extra data structures are used beyond a few references.

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
            Each node is visited once.
        Space : O(1)
            Uses only a constant number of pointers.

        Examples
        --------
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> result = Solution().reverse_list(head)
        >>> traverse_list(result)
        3 2 1
        """
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverse_list(head)
    traverse_list(result)  # 5 4 3 2 1

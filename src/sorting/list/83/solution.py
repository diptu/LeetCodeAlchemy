from typing import Optional


class ListNode:
    """
    Singly-linked list node.

    Parameters
    ----------
    val : int, default 0
        The value stored in the node.
    next : Optional[ListNode], default None
        Reference to the next node in the list.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: ListNode | None = next


def traverse_list(head: ListNode | None) -> None:
    """
    Print the values of a linked list from head to tail.

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
    """
    A class to solve the problem of removing duplicates from a
    sorted linked list.
    """

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """
        Remove duplicates from a sorted linked list in-place.

        Parameters
        ----------
        head : Optional[ListNode]
            Head of the sorted linked list.

        Returns
        -------
        Optional[ListNode]
            The head of the linked list after removing duplicates.

        Notes
        -----
        Time complexity : O(n)
            Each node is visited once.
        Space complexity : O(1)
            Only constant extra space is used.

        Examples
        --------
        >>> head = ListNode(1, ListNode(1, ListNode(2)))
        >>> sol = Solution()
        >>> result = sol.deleteDuplicates(head)
        >>> traverse_list(result)
        1 2
        """
        if head is None:
            return None

        prev = head
        curr = head.next
        while curr is not None:
            if prev.val == curr.val:
                curr = curr.next
                continue
            prev.next = curr
            prev = curr
            curr = curr.next
        prev.next = None
        return head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))
    )  # [1,1,2,3,3]
    result = solution.deleteDuplicates(head)
    traverse_list(result)  # Output: 1 2,3

# file: test_reverse_linked_list_stack.py
from collections.abc import Iterable

import pytest
from reverse_linked_list_stack import ListNode, Solution


def build_list(values: Iterable[int]) -> ListNode | None:
    """Build a linked list from a Python iterable of ints."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    """Convert a linked list to a Python list of ints."""
    out: list[int] = []
    node = head
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([2, 2, 2], [2, 2, 2]),
        ([-1, 0, 7], [7, 0, -1]),
    ],
)
def test_reverse_list(values, expected):
    head = build_list(values)
    result = Solution().reverse_list(head)
    assert to_list(result) == expected


def test_large_list():
    n = 10_000
    head = build_list(range(n))
    result = Solution().reverse_list(head)
    assert to_list(result) == list(reversed(range(n)))

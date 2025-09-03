import pytest
from solution import ListNode, Solution, traverse_list


def list_to_linked(values: list[int]) -> ListNode | None:
    """
    Convert a Python list to a linked list.

    Parameters
    ----------
    values : list[int]
        List of integer values.

    Returns
    -------
    ListNode or None
        Head of the linked list or None if list is empty.
    """
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head: ListNode | None) -> list[int]:
    """
    Convert a linked list to a Python list.

    Parameters
    ----------
    head : ListNode or None
        Head of the linked list.

    Returns
    -------
    list[int]
        List of node values.
    """
    values: list[int] = []
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


@pytest.fixture
def solver() -> Solution:
    """Fixture to initialize the Solution instance."""
    return Solution()


def test_no_duplicates(solver: Solution) -> None:
    """List with no duplicates remains unchanged."""
    head = list_to_linked([1, 2, 3])
    result = solver.deleteDuplicates(head)
    assert linked_to_list(result) == [1, 2, 3]


def test_with_duplicates(solver: Solution) -> None:
    """List with duplicates should be cleaned."""
    head = list_to_linked([1, 1, 2, 3, 3])
    result = solver.deleteDuplicates(head)
    assert linked_to_list(result) == [1, 2, 3]


def test_all_duplicates(solver: Solution) -> None:
    """List where all values are the same becomes one node."""
    head = list_to_linked([5, 5, 5, 5])
    result = solver.deleteDuplicates(head)
    assert linked_to_list(result) == [5]


def test_empty_list(solver: Solution) -> None:
    """Empty list returns None."""
    result = solver.deleteDuplicates(None)
    assert result is None


def test_single_node(solver: Solution) -> None:
    """Single node list remains unchanged."""
    head = list_to_linked([42])
    result = solver.deleteDuplicates(head)
    assert linked_to_list(result) == [42]


def test_large_list(solver: Solution) -> None:
    """Performance test with a large list."""
    values = [i // 2 for i in range(10000)]  # lots of duplicates
    head = list_to_linked(values)
    result = solver.deleteDuplicates(head)
    expected = list(range(5000))  # unique values
    assert linked_to_list(result) == expected

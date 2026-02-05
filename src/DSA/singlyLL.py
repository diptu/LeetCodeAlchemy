from typing import Optional


class Node:
    """Node of a singly linked list."""

    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next


class SinglyLinkedList:
    """Singly linked list implementation."""

    def __init__(self, head: Optional[Node] = None) -> None:
        self.head = head

    def insert_at_start(self, val: int) -> None:
        """Insert a node at the beginning of the list."""
        self.head = Node(val, self.head)

    def insert_at_end(self, val: int) -> None:
        """Insert a node at the end of the list."""
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, target: int, val: int) -> bool:
        """
        Insert a node with value `val` after the first node
        containing `target`.

        Returns True if inserted, False if target not found.
        """
        cur = self.head
        while cur:
            if cur.val == target:
                cur.next = Node(val, cur.next)
                return True
            cur = cur.next
        return False

    def delete(self, target: int) -> bool:
        """
        Delete the first node containing `target`.

        Returns True if deleted, False if target not found.
        """
        if not self.head:
            return False

        if self.head.val == target:
            self.head = self.head.next
            return True

        prev, cur = self.head, self.head.next
        while cur:
            if cur.val == target:
                prev.next = cur.next
                return True
            prev, cur = cur, cur.next

        return False

    def traverse(self) -> None:
        """Print the linked list."""
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")


# =============================================================================
# ✅ Example Usage
# =============================================================================
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_start(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_after(1, 99)
    ll.delete(4)
    ll.traverse()

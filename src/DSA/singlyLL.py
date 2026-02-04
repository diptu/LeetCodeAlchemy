from typing import Optional


class Node:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next


class SinglyLinkedList:
    """Singly linked list implementation."""

    def __init__(self, head: Optional[Node] = None) -> None:
        self.head = head

    def insertAtEnd(self, val: int) -> None:
        """Insert a node at the end of the list."""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insertAtStart(self, val: int) -> None:
        """Insert a node at the start of the list."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, target: int, val: int) -> bool:
        """
        Insert a node with value `val` after the first node
        containing `target`.

        Returns True if insertion succeeds, False otherwise.
        """
        current = self.head

        while current:
            if current.val == target:
                new_node = Node(val, current.next)
                current.next = new_node
                return True
            current = current.next

        return False  # target not found

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")


# =============================================================================
# ✅ Example Usage
# =============================================================================
if __name__ == "__main__":
    obj = SinglyLinkedList()
    obj.insertAtEnd(1)
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    obj.insertAtStart(4)

    obj.insert_after_node(2, 99)  # Insert 99 after 2

    obj.traverse()

# A linked list node
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Function to Recursively traverse and print the singly linked list
def traverseListRecursively(head):
    temp = head
    if temp is None:
        return
    else:
        print(temp.data, end=" ")
    return traverseListRecursively(temp.next)


def insert_at_front(head, new_data):
    temp = Node(new_data)
    temp.next = head
    return temp


def insert_at_end(head, new_data):
    new_node = Node(new_data)

    # If the Linked List is empty, make the
    # new node as the head and return
    if head is None:
        return new_node
    last = head
    # Traverse till the last node
    while last.next:
        last = last.next

    last.next = new_node
    return head


# function to insert a Node at required position
def insert_pos(head, pos, data):
    # This condition to check whether the
    # position given is valid or not.
    if pos < 1:
        return head

    # head will change if pos=1
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    curr = head

    # Traverse to the node that will be
    # present just before the new node
    for _ in range(1, pos - 1):
        if curr == None:
            break
        curr = curr.next

    # if position is greater
    # number of nodes
    if curr is None:
        return head

    new_node = Node(data)

    # update the next pointers
    new_node.next = curr.next
    curr.next = new_node

    return head


# Function to traverse and print the singly linked list
def traverseList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


def Lehgth(head):
    len = 0
    temp = head
    while temp is not None:
        len = len + 1
        temp = temp.next
    return len


#  Checks whether key is present in linked list
def searchKey(head, key):
    while head is not None:
        if head.data == key:
            return True
        head = head.next
    return False


def main():
    # Create a new linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head = insert_at_front(head, 5)
    head = insert_at_end(head, 50)

    head = insert_pos(head, 5, 35)
    traverseList(head)
    # traverseListRecursively(head)
    key = 30
    if searchKey(head, key):
        print(f"\n{key} found")
    else:
        print(f"\n{key} not found")
    print("Leength of the list is: ", Lehgth(head))


if __name__ == "__main__":
    main()

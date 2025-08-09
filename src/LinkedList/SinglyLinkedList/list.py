# A linked list node
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Function to Recursively traverse and print the singly linked list
def traverseListRecursively(head):
    if head is None:
        return
    else:
        print(head.data, end=" ")
    return traverseListRecursively(head.next)


# Function to traverse and print the singly linked list
def traverseList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def Lehgth(head):
    len = 0
    while head is not None:
        len = len + 1
        head = head.next
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
    # traverseList(head)
    traverseListRecursively(head)
    key = 30
    if searchKey(head, key):
        print(f"\n{key} found")
    else:
        print(f"\n{key} not found")
    print("Leength of the list is: ", Lehgth(head))


if __name__ == "__main__":
    main()

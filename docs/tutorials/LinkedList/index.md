## Singly Linked List

### Singly Linked List
A **singly linked list** is a basic data structure made of nodes. 
- Each node holds `data` and a `pointer` to the next node. 
- The last node's pointer is `null`, marking the list's end. 

Linked lists are good for inserting and deleting items.

Now let's create a `Node`:

### Code Blocks in Content Tabs

=== "C++"

    ```c++
    // Definition of a Node in a singly linked list
    struct Node {
    
        // Data part of the node
        int data;

        // Pointer to the next node in the list
        Node* next;

        // Constructor to initialize the node with data
        Node(int data)
        {
            this->data = data;
            this->next = nullptr;
        }
    };
    ```
=== "Python"

    ```py
    # Definition of a Node in a singly linked list
    class Node:
        def __init__(self, data):
        # Data part of the node
            self.data = data   
            self.next = None   
    ```

[Understanding Node Structure](https://youtu.be/N9wowwtc3eE)
<!-- <video width="750" height="240" controls>
  <source src="./video/1.mp4" type="video/mp4">
</video> -->

### Traversal of Singly Linked List

### Code Blocks in Content Tabs

=== "C++"

    ```c++
    #include <iostream>

    using namespace std;

    // A linked list node
    class Node {
    public:
        int data;
        Node* next;

        // Constructor to initialize a new node with data
        Node(int new_data) {
            this->data = new_data;
            this->next = nullptr;
        }
    };

    // Function to traverse and print the singly linked list
    void traverseList(Node* head) {

        // A loop that runs till head is nullptr
        while (head != nullptr) {

            // Printing data of current node
            cout << head->data << " ";

            // Moving to the next node
            head = head->next;
        }
        cout << endl;
    }

    // Driver Code
    int main() {
    
        // Create a hard-coded linked list:
        // 3 -> 5 -> 11 -> 13
        Node* head = new Node(3);
        head->next = new Node(5);
        head->next->next = new Node(11);
        head->next->next->next = new Node(13);

        // Example of traversing the node and printing
        traverseList(head);

        return 0;
    }

    ```
=== "Python"

    ```py
    # A linked list node
    class Node:

        # Constructor to initialize a new node with data
        def __init__(self, new_data):
            self.data = new_data
            self.next = None

    # Function to traverse and print the singly linked list
    def traverseList(head):

        # A loop that runs till head is nullptr
        while head is not None:

            # Printing data of current node
            print(head.data, end=" ")
            
            # Moving to the next node
            head = head.next
        print()

    # Driver code
    def main():

        # Create a hard-coded linked list:
        # 3 -> 5 -> 11 -> 13
        head = Node(3)
        head.next = Node(5)
        head.next.next = Node(11)
        head.next.next.next = Node(13)

        # Example of traversing the node and printing
        traverseList(head)


    if __name__ == "__main__":
        main()
  
    ```

<video width="750" height="240" controls>
  <source src="./video/2.mp4" type="video/mp4">
</video>
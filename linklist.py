import streamlit as st

def main():
    st.title("Linked List Data Structure - GeeksforGeeks")

    st.header("Introduction")
    st.write("""
    A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node.
    """)

    st.header("Why Linked List?")
    st.write("""
    Arrays can be used to store linear data of similar types, but arrays have the following limitations:
    1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
    2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

    For example, in a system, if we maintain a sorted list of IDs in an array id[] = [1000, 1010, 1050, 2000, 2040]. And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000). Deletion is also expensive with arrays until unless some special techniques are used.

    Advantages over arrays:
    1) Dynamic size
    2) Ease of insertion/deletion

    Drawbacks:
    1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation.
    2) Extra memory space for a pointer is required with each element of the list.
    3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
    """)

    st.header("Representation")
    st.write("""
    A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.

    Each node in a list consists of at least two parts:
    1) data
    2) Pointer (Or Reference) to the next node
    """)

    st.subheader("In C")
    st.code("""
    struct Node {
        int data;
        struct Node* next;
    };
    """, language='c')

    st.subheader("In C++")
    st.code("""
    class Node {
    public:
        int data;
        Node* next;
    };
    """, language='cpp')

    st.subheader("In Java")
    st.code("""
    class Node {
        int data;
        Node next;
    }
    """, language='java')

    st.subheader("In Python")
    st.code("""
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    """, language='python')

    st.subheader("In C#")
    st.code("""
    public class Node {
        public int data;
        public Node next;
    }
    """, language='csharp')

    st.header("Types of Linked Lists")
    st.write("""
    1. Singly Linked List
    2. Doubly Linked List
    3. Circular Linked List
    4. Circular Doubly Linked List
    """)

    st.header("Singly Linked List")
    st.write("""
    Traversal of items can be done in the forward direction only.
    """)

    st.header("Doubly Linked List")
    st.write("""
    Traversal of items can be done in both forward and backward directions.
    """)

    st.header("Circular Linked List")
    st.write("""
    The last node contains a pointer which has the address of the first node.
    """)

    st.header("Operations on Linked Lists")
    st.write("""
    1. Insertion
    2. Deletion
    3. Traversal
    4. Searching
    5. Sorting
    """)

    st.header("Advantages of Linked List")
    st.write("""
    1. Dynamic Data Structure: Linked List being dynamic in size can grow and shrink at runtime by allocating and deallocating memory. So there is no need to give the initial size of the Linked list.
    2. No memory wastage: In the Linked list, efficient memory utilization can be achieved since the size of the linked list increase or decrease at run time so there is no memory wastage and allocation is done as per the requirement.
    3. Implementation: Linear data structures like stack and queue can be easily implemented using linked list.
    4. Insertion and Deletion Operations: Insertion and deletion operations are quite easier in the linked list. There is no need to shift elements after the insertion or deletion of an element only the address present in the next pointer needs to be updated.
    """)

    st.header("Disadvantages of Linked List")
    st.write("""
    1. Memory Usage: More memory is required in the linked list as compared to an array. Because in a linked list, a pointer is also required to store the address of the next element and it requires extra memory for itself.
    2. Traversal: In a Linked list traversal is more time-consuming as compared to an array. Direct access to an element is not possible in a linked list as in an array by index. For example, to access the 3rd element in an array we can directly access it by arr[2], but in the case of a linked list, we have to traverse the linked list from the beginning to reach the 3rd element.
    3. Reverse Traversal: In a singly linked list reverse traversal is not possible, but in the case of a doubly linked list, it can be possible as it contains a pointer to the previous node so we can traverse it in the backward direction.
    """)

    st.header("Applications of Linked List")
    st.write("""
    1. Dynamic memory allocation
    2. Implemented in stack and queue
    3. In undo functionality of softwares
    4. Hash tables, Graphs
    """)

    st.header("Operations on Linked List")
    st.subheader("Traversal")
    st.write("Traversal means visiting each node of the linked list at least once to perform some operation.")
    st.code("""
    void printList(struct Node* node) {
        while (node != NULL) {
            printf("%d ", node->data);
            node = node->next;
        }
    }
    """, language='c')

    st.subheader("Insertion")
    st.write("Insertion can be done at the beginning, end, or at a specific position.")
    st.subheader("Insert at Beginning")
    st.code("""
    void insertAtBeginning(struct Node** head_ref, int new_data) {
        struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
        new_node->data = new_data;
        new_node->next = (*head_ref);
        (*head_ref) = new_node;
    }
    """, language='c')

    st.subheader("Insert at End")
    st.code("""
    void insertAtEnd(struct Node** head_ref, int new_data) {
        struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
        struct Node* last = *head_ref;
        new_node->data = new_data;
        new_node->next = NULL;
        if (*head_ref == NULL) {
            *head_ref = new_node;
            return;
        }
        while (last->next != NULL) last = last->next;
        last->next = new_node;
    }
    """, language='c')

    st.subheader("Deletion")
    st.write("Deletion can be done at the beginning, end, or at a specific position.")
    st.subheader("Delete from Beginning")
    st.code("""
    void deleteFromBeginning(struct Node** head_ref) {
        if (*head_ref == NULL) return;
        struct Node* temp = *head_ref;
        *head_ref = (*head_ref)->next;
        free(temp);
    }
    """, language='c')

    st.subheader("Delete from End")
    st.code("""
    void deleteFromEnd(struct Node** head_ref) {
        if (*head_ref == NULL) return;
        if ((*head_ref)->next == NULL) {
            free(*head_ref);
            *head_ref = NULL;
            return;
        }
        struct Node* second_last = *head_ref;
        while (second_last->next->next != NULL) second_last = second_last->next;
        free(second_last->next);
        second_last->next = NULL;
    }
    """, language='c')

    st.header("Time Complexities")
    st.write("Time complexities for common operations in Linked Lists:")
    import pandas as pd
    df = pd.DataFrame({
        'Operation': ['Traversal', 'Insertion at Beginning', 'Insertion at End', 'Insertion at Position', 'Deletion at Beginning', 'Deletion at End', 'Deletion at Position', 'Search'],
        'Singly Linked List': ['O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(n)'],
        'Doubly Linked List': ['O(n)', 'O(1)', 'O(1)', 'O(n)', 'O(1)', 'O(1)', 'O(n)', 'O(n)']
    })
    st.table(df)

    st.header("Complete Implementation in Python")
    st.code("""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
ll.delete(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None
    """, language='python')

    st.header("Examples with Inputs and Outputs")
    st.subheader("Insertion Example")
    st.write("Input: Insert 5 at the beginning of list [1, 2, 3]")
    st.write("Output: [5, 1, 2, 3]")

    st.subheader("Deletion Example")
    st.write("Input: Delete 2 from list [1, 2, 3, 4]")
    st.write("Output: [1, 3, 4]")

    st.subheader("Traversal Example")
    st.write("Input: Traverse list [10, 20, 30]")
    st.write("Output: 10 20 30")

    st.header("Graphs and Diagrams")
    st.write("A simple representation of a Singly Linked List:")
    st.code("""
Head -> [Data: 1 | Next] -> [Data: 2 | Next] -> [Data: 3 | Next] -> NULL
    """)

    st.write("Doubly Linked List:")
    st.code("""
NULL <- [Prev | Data: 1 | Next] <-> [Prev | Data: 2 | Next] <-> [Prev | Data: 3 | Next] -> NULL
    """)

    st.header("Doubly Linked List Implementation")
    st.code("""
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print_list()  # 1 <-> 2 <-> 3 <-> None
dll.prepend(0)
dll.print_list()  # 0 <-> 1 <-> 2 <-> 3 <-> None
dll.delete(2)
dll.print_list()  # 0 <-> 1 <-> 3 <-> None
    """, language='python')

    st.header("Circular Linked List Implementation")
    st.code("""
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def print_list(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Example
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.print_list()  # 1 -> 2 -> 3 -> (back to head)
    """, language='python')

    st.header("Sorting a Linked List")
    st.write("Sorting can be done using algorithms like bubble sort, but merge sort is more efficient for linked lists.")
    st.code("""
def merge_sort(head):
    if not head or not head.next:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    return merge(left, right)

def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result
    """, language='python')

    st.header("Searching in Linked List")
    st.code("""
def search(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
    """, language='python')

    st.header("Space Complexity")
    st.write("Space complexity for linked lists is O(n) for storing n elements, plus O(1) for pointers in singly linked lists.")

    st.header("Comparison with Arrays")
    st.write("""
    - Arrays: Fixed size, random access O(1), insertion/deletion O(n)
    - Linked Lists: Dynamic size, sequential access O(n), insertion/deletion O(1) at ends
    """)

    st.header("Real-World Applications")
    st.write("""
    - Music playlists in media players
    - Browser history
    - Undo functionality in text editors
    - Implementation of graphs and trees
    """)

    st.header("Advanced Topics")
    st.subheader("Reversing a Linked List")
    st.write("Reversing can be done iteratively or recursively.")
    st.code("""
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
    """, language='python')

    st.subheader("Detecting a Loop in Linked List")
    st.write("Using Floyd's Cycle Detection Algorithm.")
    st.code("""
def detect_loop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    """, language='python')

    st.subheader("Finding the Middle of Linked List")
    st.code("""
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data
    """, language='python')

    st.subheader("Removing Duplicates from Sorted Linked List")
    st.code("""
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
    """, language='python')

    st.subheader("Merging Two Sorted Linked Lists")
    st.code("""
def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.data < l2.data:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
    """, language='python')

    st.header("Practice Problems")
    st.write("""
    Here are some common problems related to Linked Lists:
    1. Reverse a Linked List
    2. Detect Loop in Linked List
    3. Find Middle of Linked List
    4. Remove Duplicates from Sorted Linked List
    5. Merge Two Sorted Linked Lists
    6. Intersection Point of Two Linked Lists
    7. Palindrome Linked List
    8. Add Two Numbers Represented by Linked Lists
    9. Flatten a Multilevel Doubly Linked List
    10. Rotate List
    """)
    st.write("For solutions and more problems, visit [GeeksforGeeks Linked List Problems](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)")

if __name__ == "__main__":
    main()

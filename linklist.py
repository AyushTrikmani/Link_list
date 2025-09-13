import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Linked List Data Structures", layout="wide")

# Sidebar navigation menu
def sidebar():
    st.sidebar.title("Navigation")
    menu = [
        "Introduction",
        "Types of Linked Lists",
        "Operations and Algorithms",
        "Interactive Playground",
        "Performance Analysis",
        "Practice Problems",
        "References and Resources"
    ]
    choice = st.sidebar.radio("Go to", menu)
    return choice

# Introduction section
def introduction():
    st.title("Introduction to Linked Lists")

    st.header("What is a Linked List?")
    st.markdown("""
    A linked list is a fundamental data structure in computer science that consists of a sequence of elements called nodes.
    Each node contains two parts:
    - **Data**: The actual information stored in the node
    - **Reference/Pointer**: A link to the next node in the sequence

    Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each node points to the next one,
    forming a chain-like structure.
    """)

    st.header("Why Use Linked Lists?")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Advantages")
        st.markdown("""
        - **Dynamic Size**: Can grow or shrink during runtime
        - **Efficient Insertions/Deletions**: O(1) time for operations at known positions
        - **No Memory Waste**: Only allocates memory when needed
        - **Flexible Structure**: Easy to implement stacks, queues, and other data structures
        """)
    with col2:
        st.subheader("Disadvantages")
        st.markdown("""
        - **Random Access**: O(n) time to access elements by index
        - **Extra Memory**: Each node requires additional space for pointers
        - **Sequential Access**: Must traverse from beginning for most operations
        - **Cache Performance**: Poor locality of reference
        """)

    st.header("Basic Node Structure")
    st.code("""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    """, language="python")

    st.header("Real-World Applications")
    st.markdown("""
    - **Music Playlists**: Songs linked in sequence
    - **Browser History**: Web pages linked for back/forward navigation
    - **Undo Functionality**: Operations stored as linked list
    - **Hash Tables**: Collision resolution using separate chaining
    - **Memory Management**: Free memory blocks tracking
    - **Polynomial Representation**: Terms linked by degree
    """)

    st.header("Memory Representation")
    st.markdown("Visual representation of how linked list nodes are stored in memory:")
    # Simple diagram using text
    st.code("""
Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | --> | Next: 0x300       | --> | Next: None        |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300
    """)

# Types of Linked Lists section
def types_of_linked_lists():
    st.title("Types of Linked Lists")

    st.markdown("""
    Linked lists come in various forms, each with its own strengths and use cases. Understanding the differences
    between these types is crucial for choosing the right data structure for your specific needs.
    """)

    st.header("1. Singly Linked List")
    st.markdown("**Overview:** The most basic form of linked list where each node points only to the next node.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure:**
        ```python
        class Node:
            def __init__(self, data):
                self.data = data      # The actual data
                self.next = None      # Pointer to next node
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Minimal (1 pointer + data per node)
        - **Traversal:** Only forward direction
        - **Operations:** Simple to implement
        - **Performance:** O(1) for beginning operations, O(n) for end operations
        - **Memory Efficiency:** Good for large datasets with sequential access

        **Advantages:**
        - ✅ Simple implementation and understanding
        - ✅ Low memory overhead per node
        - ✅ Efficient for stack operations (LIFO)
        - ✅ Good cache performance for sequential access
        - ✅ Easy to implement recursive algorithms

        **Disadvantages:**
        - ❌ No backward traversal
        - ❌ O(n) time for random access
        - ❌ Cannot efficiently delete previous node
        - ❌ More complex reverse operations

        **Real-World Use Cases:**
        - **Stack Implementation:** Perfect for undo/redo functionality
        - **Queue Implementation:** Basic FIFO operations
        - **Hash Table Chaining:** Collision resolution in hash tables
        - **Memory Management:** Free memory block tracking
        - **Symbol Tables:** In compilers and interpreters
        - **Polynomial Operations:** Representing mathematical polynomials
        """)

        st.subheader("Visual Representation")
        st.code("""
Singly Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | --> | Next: 0x300       | --> | Next: None        |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300

Traversal: 10 -> 20 -> 30 -> NULL
        """)

    with col2:
        st.code("""
# Complete Singly Linked List Implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.head is None:
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data

    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example Usage:
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
print(sll.traverse())  # [1, 2, 3]
        """, language="python")

    st.header("2. Doubly Linked List")
    st.markdown("**Overview:** Each node has pointers to both previous and next nodes, enabling bidirectional traversal.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure:**
        ```python
        class DoublyNode:
            def __init__(self, data):
                self.data = data      # The actual data
                self.next = None      # Pointer to next node
                self.prev = None      # Pointer to previous node
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Higher (2 pointers + data per node)
        - **Traversal:** Both forward and backward directions
        - **Operations:** More complex but more flexible
        - **Performance:** O(1) for beginning and end operations (with tail pointer)
        - **Memory Efficiency:** Less efficient than singly linked lists

        **Advantages:**
        - ✅ Bidirectional traversal
        - ✅ Efficient deletion of any node (if reference is known)
        - ✅ Can implement deque operations efficiently
        - ✅ Easier to implement complex data structures
        - ✅ Better for frequent insertions/deletions at both ends

        **Disadvantages:**
        - ❌ Higher memory overhead
        - ❌ More complex implementation
        - ❌ Extra pointer updates required
        - ❌ Slightly slower operations due to extra bookkeeping

        **Real-World Use Cases:**
        - **Browser History:** Back and forward navigation
        - **Text Editors:** Cursor movement and editing
        - **LRU Cache:** Most Recently Used page replacement
        - **Undo/Redo Stacks:** Bidirectional operation history
        - **Music Player:** Previous/next track navigation
        - **File System Navigation:** Directory traversal
        """)

        st.subheader("Visual Representation")
        st.code("""
Doubly Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Prev: None        |     | Prev: 0x100       |     | Prev: 0x200       |
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | <-- | Next: 0x300       | <-- | Next: None        |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300

Traversal: NULL <- 10 <-> 20 <-> 30 -> NULL
        """)

    with col2:
        st.code("""
# Complete Doubly Linked List Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tail pointer for O(1) end operations
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.head is None:
            return None
        deleted_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return deleted_data

    def traverse_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def traverse_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

# Example Usage:
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
print(dll.traverse_forward())   # [1, 2, 3]
print(dll.traverse_backward())  # [3, 2, 1]
        """, language="python")

    st.header("3. Circular Linked List")
    st.markdown("**Overview:** The last node points back to the first node, forming a circle.")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Node Structure (Singly Circular):**
        ```python
        class CircularNode:
            def __init__(self, data):
                self.data = data
                self.next = None
        ```

        **Detailed Characteristics:**
        - **Memory Usage:** Same as singly (1 pointer + data per node)
        - **Traversal:** Can start from any node and traverse infinitely
        - **Operations:** Need careful handling to avoid infinite loops
        - **Performance:** O(1) for beginning operations, O(n) for end operations
        - **Special Property:** No NULL termination

        **Advantages:**
        - ✅ Memory efficient (same as singly linked)
        - ✅ Useful for circular operations
        - ✅ Can represent cyclic data naturally
        - ✅ Round-robin algorithms work naturally
        - ✅ No special case for end of list

        **Disadvantages:**
        - ❌ Easy to create infinite loops
        - ❌ More complex traversal logic
        - ❌ Cannot use NULL to detect end
        - ❌ Harder to detect cycles (ironic!)

        **Real-World Use Cases:**
        - **Round-Robin Scheduling:** CPU process scheduling
        - **Circular Buffers:** Audio/video streaming
        - **Multiplayer Games:** Player turn management
        - **Music Playlists:** Continuous playback
        - **Token Ring Networks:** Data transmission
        - **Time-Sharing Systems:** Resource allocation
        """)

        st.subheader("Visual Representation")
        st.code("""
Circular Linked List Memory Layout:
+-------------------+     +-------------------+     +-------------------+
| Data: 10          |     | Data: 20          |     | Data: 30          |
| Next: 0x200       | --> | Next: 0x300       | --> | Next: 0x100       |
+-------------------+     +-------------------+     +-------------------+
0x100                   0x200                   0x300         |
                                                              |
                                                              v
                                                            Back to 0x100

Traversal: 10 -> 20 -> 30 -> 10 -> 20 -> ... (infinite)
        """)

    with col2:
        st.code("""
# Complete Circular Linked List Implementation
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            new_node.next = new_node  # Point to itself
            self.head = new_node
        else:
            new_node.next = self.head
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.size += 1

    def traverse(self, max_elements=10):
        if self.head is None:
            return []
        elements = []
        current = self.head
        count = 0
        while count < max_elements:
            elements.append(current.data)
            current = current.next
            count += 1
            if current == self.head:
                break
        return elements

# Example Usage:
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
print(cll.traverse())  # [1, 2, 3]
        """, language="python")

    st.header("4. Advanced Linked List Variants")

    st.subheader("XOR Linked List")
    st.markdown("""
    **Concept:** Uses bitwise XOR to store both previous and next pointers in a single field, saving memory.

    **How it works:**
    - Each node stores: `ptr = prev XOR next`
    - To traverse: `next = ptr XOR prev`
    - Memory efficient but complex to implement

    **Use Cases:** Memory-constrained environments, competitive programming
    """)

    st.subheader("Skip List")
    st.markdown("""
    **Concept:** A probabilistic data structure that allows O(log n) search time.

    **How it works:**
    - Multiple levels of linked lists
    - Higher levels skip more nodes
    - Search starts from top level and works down

    **Use Cases:** Database indexes, Redis sorted sets
    """)

    st.subheader("Unrolled Linked List")
    st.markdown("""
    **Concept:** Each node contains an array of elements instead of a single element.

    **Benefits:**
    - Better cache performance
    - Reduced pointer overhead
    - Faster sequential access

    **Use Cases:** High-performance applications, cache-conscious data structures
    """)

    st.header("Comprehensive Comparison")

    # Create detailed comparison table
    comparison_data = {
        'Aspect': [
            'Memory per Node',
            'Traversal Direction',
            'Beginning Operations',
            'End Operations',
            'Random Access',
            'Implementation Complexity',
            'Memory Efficiency',
            'Cache Performance',
            'Use Case Fit'
        ],
        'Singly Linked': [
            '1 pointer + data',
            'Forward only',
            'O(1)',
            'O(n)',
            'O(n)',
            'Simple',
            'Good',
            'Good',
            'Stacks, Queues'
        ],
        'Doubly Linked': [
            '2 pointers + data',
            'Bidirectional',
            'O(1)',
            'O(1)*',
            'O(n)',
            'Moderate',
            'Poor',
            'Fair',
            'Deques, Caches'
        ],
        'Circular Singly': [
            '1 pointer + data',
            'Circular',
            'O(1)',
            'O(n)',
            'O(n)',
            'Moderate',
            'Good',
            'Good',
            'Round-robin'
        ],
        'Circular Doubly': [
            '2 pointers + data',
            'Circular Bidirectional',
            'O(1)',
            'O(1)',
            'O(n)',
            'Complex',
            'Poor',
            'Fair',
            'Complex circular ops'
        ]
    }

    import pandas as pd
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("*Note: * Requires tail pointer for O(1) end operations")

    st.header("Common Pitfalls and Best Practices")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Common Mistakes")
        st.markdown("""
        - **Null Pointer Dereference:** Always check for None before accessing next/prev
        - **Infinite Loops:** Especially in circular lists, always have termination conditions
        - **Memory Leaks:** In languages without GC, remember to free nodes
        - **Lost References:** When deleting nodes, update all relevant pointers
        - **Off-by-One Errors:** Careful with indexing and position calculations
        """)

    with col2:
        st.subheader("Best Practices")
        st.markdown("""
        - **Use Sentinel Nodes:** Dummy head/tail nodes to simplify boundary cases
        - **Maintain Size Counter:** Keep track of list size for efficient operations
        - **Tail Pointers:** For doubly linked lists to enable O(1) end operations
        - **Consistent Naming:** Use clear variable names (head, tail, current, etc.)
        - **Error Handling:** Always handle edge cases (empty list, single node)
        """)

    st.header("Performance Considerations")

    st.markdown("""
    **Memory Overhead Analysis:**

    | Data Structure | Pointers | Overhead (64-bit) | Total per Node |
    |----------------|----------|-------------------|----------------|
    | Singly Linked | 1 | 8 bytes | 8 + data bytes |
    | Doubly Linked | 2 | 16 bytes | 16 + data bytes |
    | Array Element | 0 | 0 bytes | data bytes only |

    **Cache Performance:**
    - **Arrays:** Excellent locality of reference
    - **Linked Lists:** Poor locality, nodes scattered in memory
    - **Unrolled Lists:** Better locality with multiple elements per node

    **When to Choose Which:**
    - **Singly Linked:** Memory-critical, forward-only traversal
    - **Doubly Linked:** Need bidirectional access, frequent end operations
    - **Circular:** Round-robin, circular buffers, infinite traversal
    - **Array:** Random access, cache performance critical
    """)

    st.header("Implementation Tips")

    with st.expander("Singly Linked List Tips"):
        st.markdown("""
        1. Always keep a reference to head
        2. Use a dummy node for operations on empty lists
        3. For frequent end operations, maintain a tail pointer
        4. Be careful with pointer updates during deletion
        5. Use recursion sparingly (watch stack overflow)
        """)

    with st.expander("Doubly Linked List Tips"):
        st.markdown("""
        1. Always update both next and prev pointers
        2. Maintain both head and tail pointers
        3. Use symmetry in operations (forward/backward)
        4. Careful with boundary conditions
        5. Consider using sentinel nodes
        """)

    with st.expander("Circular Linked List Tips"):
        st.markdown("""
        1. Never use NULL to detect end of list
        2. Always have a termination condition in loops
        3. Be careful with empty list handling
        4. Use size counter to prevent infinite loops
        5. Consider using a tail pointer for efficiency
        """)

# Operations and Algorithms section
def operations_and_algorithms():
    st.title("Operations and Algorithms")

    st.header("1. Insertion Operations")

    st.subheader("Insert at Beginning")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Create a new node with given data
        2. Set new node's next to current head
        3. Update head to point to new node

        **Time Complexity:** O(1)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # New head

# Example: Insert 0 at beginning of [1,2,3]
# Result: [0,1,2,3]
        """, language="python")

    st.subheader("Insert at End")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Create a new node with given data
        2. If list is empty, set as head
        3. Else traverse to last node
        4. Set last node's next to new node

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Example: Insert 4 at end of [1,2,3]
# Result: [1,2,3,4]
        """, language="python")

    st.header("2. Deletion Operations")

    st.subheader("Delete from Beginning")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. If list is empty, return None
        2. Store current head
        3. Update head to next node
        4. Return deleted node's data

        **Time Complexity:** O(1)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def delete_from_beginning(head):
    if head is None:
        return None, head

    deleted_data = head.data
    new_head = head.next
    return deleted_data, new_head

# Example: Delete from [1,2,3]
# Result: 1, [2,3]
        """, language="python")

    st.subheader("Delete by Value")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. If list is empty, return False
        2. If head contains target, update head
        3. Traverse list to find target
        4. Update previous node's next pointer
        5. Return True if found, False otherwise

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def delete_by_value(head, target):
    if head is None:
        return False, head

    if head.data == target:
        return True, head.next

    current = head
    while current.next and current.next.data != target:
        current = current.next

    if current.next:
        current.next = current.next.next
        return True, head
    return False, head

# Example: Delete 2 from [1,2,3]
# Result: True, [1,3]
        """, language="python")

    st.header("3. Traversal")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Start from head node
        2. While current node is not None:
           - Process current node's data
           - Move to next node
        3. End when current becomes None

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)

        **Use Cases:**
        - Printing list elements
        - Searching for values
        - Applying operations to all elements
        """)
    with col2:
        st.code("""
def traverse_and_print(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example traversal of [1,2,3]
# Output: 1 -> 2 -> 3 -> None
        """, language="python")

    st.header("4. Searching")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Algorithm:**
        1. Start from head node
        2. Initialize position counter
        3. While current node is not None:
           - Check if current data matches target
           - If match, return position
           - Increment position, move to next
        4. Return -1 if not found

        **Time Complexity:** O(n)
        **Space Complexity:** O(1)
        """)
    with col2:
        st.code("""
def search_by_value(head, target):
    current = head
    position = 0

    while current:
        if current.data == target:
            return position
        current = current.next
        position += 1

    return -1

# Example: Search for 2 in [1,2,3]
# Result: 1 (0-based index)
        """, language="python")

    st.header("5. Time and Space Complexity Analysis")
    st.markdown("""
    | Operation | Singly Linked List | Doubly Linked List | Notes |
    |-----------|-------------------|-------------------|-------|
    | **Insertion at Beginning** | O(1) | O(1) | Direct head update |
    | **Insertion at End** | O(n) | O(1)* | *Requires tail pointer |
    | **Insertion at Position** | O(n) | O(n) | Need to traverse |
    | **Deletion at Beginning** | O(1) | O(1) | Direct head update |
    | **Deletion at End** | O(n) | O(1)* | *Requires tail pointer |
    | **Deletion by Value** | O(n) | O(n) | Linear search required |
    | **Traversal** | O(n) | O(n) | Visit all nodes |
    | **Searching** | O(n) | O(n) | Linear search |

    **Space Complexity:** O(n) for all types (proportional to number of elements)
    """)

    st.header("Advanced Algorithms")

    st.subheader("Reverse a Linked List")
    st.code("""
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Example: Reverse [1,2,3] -> [3,2,1]
    """, language="python")

    st.subheader("Detect Cycle (Floyd's Algorithm)")
    st.code("""
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Returns True if cycle exists
    """, language="python")

# Interactive Playground section
def interactive_playground():
    st.title("Interactive Playground")

    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = []

    st.header("Create Your Linked List")
    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("Enter comma-separated values (e.g., 1, 2, 3, 4)", "")
        if st.button("Create List", key="create"):
            if user_input:
                st.session_state.linked_list = [x.strip() for x in user_input.split(",") if x.strip()]
                st.success(f"Linked list created with {len(st.session_state.linked_list)} elements!")
            else:
                st.warning("Please enter some values.")
    with col2:
        if st.button("Clear List", key="clear"):
            st.session_state.linked_list = []
            st.info("Linked list cleared!")

    st.header("Current Linked List")
    if st.session_state.linked_list:
        st.write("Elements: ", st.session_state.linked_list)
        st.write(f"Length: {len(st.session_state.linked_list)}")

        # Enhanced visualization
        fig, ax = plt.subplots(figsize=(max(8, len(st.session_state.linked_list) * 1.2), 2))
        ax.axis('off')

        for i, val in enumerate(st.session_state.linked_list):
            # Draw node
            rect = plt.Rectangle((i*1.5, 0.2), 1.2, 0.6, fill=True, facecolor='lightblue', edgecolor='blue', linewidth=2)
            ax.add_patch(rect)
            # Draw data
            ax.text(i*1.5 + 0.6, 0.5, str(val), ha='center', va='center', fontsize=12, fontweight='bold')
            # Draw pointer
            if i < len(st.session_state.linked_list) - 1:
                ax.arrow(i*1.5 + 1.3, 0.5, 0.15, 0, head_width=0.1, head_length=0.1, fc='red', ec='red')
                ax.text(i*1.5 + 1.45, 0.7, "next", fontsize=8, color='red')

        # Add NULL at the end
        ax.text(len(st.session_state.linked_list)*1.5 + 0.3, 0.5, "NULL", fontsize=10, color='gray')
        ax.arrow(len(st.session_state.linked_list)*1.5 - 0.1, 0.5, 0.4, 0, head_width=0.05, head_length=0.05, fc='gray', ec='gray')

        st.pyplot(fig)
    else:
        st.info("No linked list created yet. Use the input above to create one!")

    st.header("Operations on Linked List")
    if st.session_state.linked_list:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Insert Element")
            insert_pos = st.selectbox("Position", ["Beginning", "End", "At Index"])
            insert_val = st.text_input("Value to insert", key="insert_val")

            if insert_pos == "At Index":
                insert_idx = st.number_input("Index", min_value=0, max_value=len(st.session_state.linked_list), value=0, key="insert_idx")

            if st.button("Insert", key="insert_btn"):
                if insert_val:
                    if insert_pos == "Beginning":
                        st.session_state.linked_list.insert(0, insert_val)
                    elif insert_pos == "End":
                        st.session_state.linked_list.append(insert_val)
                    else:  # At Index
                        st.session_state.linked_list.insert(insert_idx, insert_val)
                    st.success(f"Inserted '{insert_val}' at {insert_pos.lower()}!")
                    st.rerun()
                else:
                    st.warning("Please enter a value to insert.")

        with col2:
            st.subheader("Delete Element")
            delete_pos = st.selectbox("Delete from", ["Beginning", "End", "By Value"], key="delete_pos")
            if delete_pos == "By Value":
                delete_val = st.text_input("Value to delete", key="delete_val")

            if st.button("Delete", key="delete_btn"):
                if not st.session_state.linked_list:
                    st.warning("List is empty!")
                elif delete_pos == "Beginning":
                    removed = st.session_state.linked_list.pop(0)
                    st.success(f"Removed '{removed}' from beginning!")
                    st.rerun()
                elif delete_pos == "End":
                    removed = st.session_state.linked_list.pop()
                    st.success(f"Removed '{removed}' from end!")
                    st.rerun()
                else:  # By Value
                    if delete_val in st.session_state.linked_list:
                        st.session_state.linked_list.remove(delete_val)
                        st.success(f"Removed '{delete_val}' from list!")
                        st.rerun()
                    else:
                        st.warning(f"'{delete_val}' not found in list!")

        with col3:
            st.subheader("Search Element")
            search_val = st.text_input("Value to search", key="search_val")

            if st.button("Search", key="search_btn"):
                if search_val in st.session_state.linked_list:
                    idx = st.session_state.linked_list.index(search_val)
                    st.success(f"Found '{search_val}' at index {idx}!")
                else:
                    st.warning(f"'{search_val}' not found in list!")

    st.header("Code Implementation")
    st.markdown("Here's how the operations above are implemented in Python:")

    with st.expander("View Implementation Code"):
        st.code("""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return None

        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def search(self, target):
        current = self.head
        position = 0

        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1

        return -1

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
        """, language="python")

# Performance Analysis section
def performance_analysis():
    st.title("Performance Analysis")

    st.header("Time Complexity Comparison")

    st.markdown("""
    Understanding the performance characteristics of different linked list operations is crucial for choosing
    the right data structure for your use case. Below is a detailed analysis of time complexities.
    """)

    # Create comprehensive data
    operations = [
        'Insert at Beginning',
        'Insert at End',
        'Insert at Position',
        'Delete from Beginning',
        'Delete from End',
        'Delete by Value',
        'Search by Value',
        'Traversal',
        'Access by Index'
    ]

    # Time complexities (1 = O(1), n = O(n))
    singly_linked = [1, 'n', 'n', 1, 'n', 'n', 'n', 'n', 'n']
    doubly_linked = [1, 1, 'n', 1, 1, 'n', 'n', 'n', 'n']  # Assuming tail pointer for end operations
    circular_singly = [1, 'n', 'n', 1, 'n', 'n', 'n', 'n', 'n']
    array_list = ['n', 1, 'n', 'n', 1, 'n', 'n', 'n', 1]

    # Create DataFrame for better display
    import pandas as pd

    complexity_data = {
        'Operation': operations,
        'Singly Linked List': singly_linked,
        'Doubly Linked List': doubly_linked,
        'Circular Linked List': circular_singly,
        'Dynamic Array': array_list
    }

    df = pd.DataFrame(complexity_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("""
    **Legend:**
    - **1**: O(1) - Constant time
    - **n**: O(n) - Linear time
    """)

    # Interactive chart
    st.header("Interactive Performance Comparison")

    selected_operations = st.multiselect(
        "Select operations to compare:",
        operations,
        default=['Insert at Beginning', 'Insert at End', 'Search by Value', 'Access by Index']
    )

    if selected_operations:
        # Prepare data for plotting
        plot_data = []
        structures = ['Singly Linked', 'Doubly Linked', 'Circular Linked', 'Dynamic Array']

        for op in selected_operations:
            idx = operations.index(op)
            values = [
                1 if singly_linked[idx] == 1 else 10,  # Convert to numeric for plotting
                1 if doubly_linked[idx] == 1 else 10,
                1 if circular_singly[idx] == 1 else 10,
                1 if array_list[idx] == 1 else 10
            ]
            plot_data.append(go.Bar(name=op, x=structures, y=values))

        fig = go.Figure(data=plot_data)
        fig.update_layout(
            barmode='group',
            title="Time Complexity Comparison (Lower is Better)",
            yaxis_title="Complexity (1 = O(1), 10 = O(n))",
            xaxis_title="Data Structure",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

    st.header("Space Complexity Analysis")

    space_data = {
        'Data Structure': ['Singly Linked List', 'Doubly Linked List', 'Circular Linked List', 'Dynamic Array'],
        'Per Element': ['1 pointer + data', '2 pointers + data', '1 pointer + data', 'data only'],
        'Overhead': ['High (pointers)', 'Very High (2 pointers)', 'High (pointers)', 'Low (amortized)'],
        'Memory Efficiency': ['Low', 'Very Low', 'Low', 'High']
    }

    space_df = pd.DataFrame(space_data)
    st.dataframe(space_df, use_container_width=True)

    st.header("When to Use Which Linked List?")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Choose Singly Linked List when:")
        st.markdown("""
        - ✅ Memory is a concern (only one pointer per node)
        - ✅ You only need forward traversal
        - ✅ Implementing stacks or queues
        - ✅ Simple operations are sufficient
        - ✅ Working with large datasets where memory matters
        """)

        st.subheader("Choose Doubly Linked List when:")
        st.markdown("""
        - ✅ Need bidirectional traversal
        - ✅ Frequent insertions/deletions at both ends
        - ✅ Implementing deques or LRU caches
        - ✅ Browser history functionality
        - ✅ Text editor cursor movement
        """)

    with col2:
        st.subheader("Choose Circular Linked List when:")
        st.markdown("""
        - ✅ Need circular traversal
        - ✅ Implementing round-robin algorithms
        - ✅ Circular buffers or playlists
        - ✅ Multiplayer game turn management
        - ✅ CPU scheduling algorithms
        """)

        st.subheader("Choose Dynamic Array instead when:")
        st.markdown("""
        - ✅ Need fast random access (O(1))
        - ✅ Memory efficiency is critical
        - ✅ Most operations are at the end
        - ✅ Cache performance matters
        - ✅ Simple implementation needed
        """)

    st.header("Cache Performance Considerations")

    st.markdown("""
    **Linked Lists vs Arrays:**

    | Aspect | Linked List | Array |
    |--------|-------------|-------|
    | **Locality of Reference** | Poor (nodes scattered in memory) | Excellent (contiguous memory) |
    | **Cache Misses** | High (pointer chasing) | Low (sequential access) |
    | **Prefetching** | Difficult | Easy |
    | **Memory Access Pattern** | Random | Sequential |

    **Why Arrays are Faster for Traversal:**
    - CPU cache can prefetch adjacent elements
    - No pointer dereferencing overhead
    - Better branch prediction
    - SIMD operations possible
    """)

    st.header("Big O Notation Deep Dive")

    st.markdown("""
    ### Understanding Time Complexity

    **O(1) - Constant Time:**
    - Operation takes the same time regardless of input size
    - Examples: Insert at beginning (singly linked), access array element by index

    **O(n) - Linear Time:**
    - Operation time grows linearly with input size
    - Examples: Search, traversal, insert at end (singly linked without tail)

    ### Amortized Analysis

    **Dynamic Arrays:**
    - Most operations are O(1) amortized
    - Resize operations are O(n) but happen infrequently
    - Average case performance is better than worst case

    **Linked Lists:**
    - All operations have consistent worst-case bounds
    - No amortization needed
    - Predictable performance
    """)

    # Performance tips
    st.header("Performance Optimization Tips")

    with st.expander("Linked List Optimizations"):
        st.markdown("""
        1. **Use Tail Pointers:** For doubly linked lists, maintain a tail pointer for O(1) end operations
        2. **Dummy Nodes:** Use sentinel nodes to simplify boundary condition handling
        3. **XOR Linked Lists:** Store XOR of previous and next pointers to save memory (advanced)
        4. **Unrolled Linked Lists:** Store multiple elements per node to improve cache performance
        5. **Skip Lists:** Add skip pointers for faster search operations (O(log n))
        """)

    with st.expander("When to Choose Arrays Over Linked Lists"):
        st.markdown("""
        1. **Random Access:** Need O(1) access by index
        2. **Memory Efficiency:** No pointer overhead
        3. **Cache Performance:** Better locality of reference
        4. **Simple Operations:** Basic CRUD operations
        5. **Small Datasets:** Overhead of pointers not worth it
        """)

    with st.expander("Real-World Performance Considerations"):
        st.markdown("""
        1. **Memory Allocation:** Linked list nodes may cause heap fragmentation
        2. **Garbage Collection:** Reference counting can be expensive
        3. **Branch Prediction:** Arrays have better branch prediction for loops
        4. **SIMD Operations:** Arrays can leverage SIMD instructions
        5. **Page Faults:** Linked lists may cause more page faults with poor allocation
        """)

# Practice Problems section
def practice_problems():
    st.title("Practice Problems")

    st.header("Problem 1: Reverse a Singly Linked List")
    st.markdown("""
    **Problem Statement:** Given the head of a singly linked list, reverse the list and return the reversed list.

    **Example:**
    - Input: head = [1,2,3,4,5]
    - Output: [5,4,3,2,1]
    """)

    with st.expander("Solution"):
        st.code("""
def reverseList(head):
    prev = None
    current = head

    while current:
        next_temp = current.next  # Store next node
        current.next = prev      # Reverse the link
        prev = current           # Move prev to current
        current = next_temp      # Move to next node

    return prev

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 2: Detect Cycle in Linked List")
    st.markdown("""
    **Problem Statement:** Given head, the head of a linked list, determine if the linked list has a cycle in it.

    **Example:**
    - Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
    - Output: true
    """)

    with st.expander("Solution (Floyd's Cycle Detection)"):
        st.code("""
def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 3: Merge Two Sorted Lists")
    st.markdown("""
    **Problem Statement:** Merge two sorted linked lists and return it as a sorted list.

    **Example:**
    - Input: list1 = [1,2,4], list2 = [1,3,4]
    - Output: [1,1,2,3,4,4]
    """)

    with st.expander("Solution"):
        st.code("""
def mergeTwoLists(list1, list2):
    # Create a dummy node
    dummy = Node(0)
    current = dummy

    # Merge the lists
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

# Time Complexity: O(n + m)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 4: Remove Nth Node From End")
    st.markdown("""
    **Problem Statement:** Given the head of a linked list, remove the nth node from the end of the list and return its head.

    **Example:**
    - Input: head = [1,2,3,4,5], n = 2
    - Output: [1,2,3,5]
    """)

    with st.expander("Solution (Two Pointers)"):
        st.code("""
def removeNthFromEnd(head, n):
    # Create a dummy node
    dummy = Node(0)
    dummy.next = head

    # Use two pointers
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for i in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from end
    second.next = second.next.next

    return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Problem 5: Find Middle of Linked List")
    st.markdown("""
    **Problem Statement:** Given the head of a singly linked list, return the middle node of the linked list.

    **Example:**
    - Input: head = [1,2,3,4,5]
    - Output: [3,4,5]
    """)

    with st.expander("Solution (Fast and Slow Pointers)"):
        st.code("""
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

    st.header("Additional Practice Problems")
    st.markdown("""
    **Easy:**
    6. Remove duplicates from sorted linked list
    7. Check if linked list is palindrome
    8. Find intersection point of two linked lists

    **Medium:**
    9. Add two numbers represented by linked lists
    10. Flatten a multilevel doubly linked list
    11. Sort linked list using merge sort

    **Hard:**
    12. Reverse nodes in k-group
    13. Copy list with random pointer
    14. LRU Cache implementation using doubly linked list
    """)

    st.header("Tips for Solving Linked List Problems")
    st.markdown("""
    - **Dummy Node:** Use a dummy node to handle edge cases (empty list, single node)
    - **Two Pointers:** Fast and slow pointers for cycle detection, finding middle
    - **Recursion:** Natural fit for linked list problems (be mindful of stack space)
    - **Edge Cases:** Always consider empty list, single node, two nodes
    - **Memory Management:** In languages with manual memory management, don't forget to free nodes
    - **Visualization:** Draw the list and pointers on paper to understand the problem
    """)

# References and Resources section
def references_and_resources():
    st.title("References and Resources")

    st.markdown("""
    - [GeeksforGeeks - Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
    - [Wikipedia - Linked List](https://en.wikipedia.org/wiki/Linked_list)
    - [Visualgo - Linked List](https://visualgo.net/en/list)
    - [Streamlit Documentation](https://docs.streamlit.io/)
    """)

# Main app function
def main():
    choice = sidebar()

    if choice == "Introduction":
        introduction()
    elif choice == "Types of Linked Lists":
        types_of_linked_lists()
    elif choice == "Operations and Algorithms":
        operations_and_algorithms()
    elif choice == "Interactive Playground":
        interactive_playground()
    elif choice == "Performance Analysis":
        performance_analysis()
    elif choice == "Practice Problems":
        practice_problems()
    elif choice == "References and Resources":
        references_and_resources()

if __name__ == "__main__":
    main()

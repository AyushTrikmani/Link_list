import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arrow
import numpy as np
import time

# Set page config
st.set_page_config(
    page_title="Interactive Linked Lists",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        font-size: 2rem;
        color: #ff7f0e;
        border-bottom: 3px solid #ff7f0e;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .concept-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .comparison-table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .comparison-table th, .comparison-table td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }
    .comparison-table th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
    }
    .comparison-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .node-structure {
        background: #f0f8ff;
        border: 2px solid #1f77b4;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    .highlight-box {
        background: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    .code-block {
        background: #2d2d2d;
        color: #f8f8f2;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        overflow-x: auto;
    }
    .detail-box {
        background: #e8f4f8;
        border-left: 5px solid #1f77b4;
        padding: 15px;
        margin: 15px 0;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Node and LinkedList classes for implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For doubly linked list

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.size += 1
        return new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1
        return new_node
    
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            return None
        
        if position == 0:
            return self.insert_at_beginning(data)
        
        if position == self.size:
            return self.insert_at_end(data)
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        self.size += 1
        return new_node
    
    def insert_after_node(self, data, target_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                self.size += 1
                return new_node
            current = current.next
        return None
    
    def delete_from_beginning(self):
        if not self.head:
            return None
        
        deleted_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return deleted_node
    
    def delete_from_end(self):
        if not self.head:
            return None
        
        if not self.head.next:
            deleted_node = self.head
            self.head = None
            self.size -= 1
            return deleted_node
        
        current = self.head
        while current.next:
            current = current.next
        
        deleted_node = current
        if current.prev:
            current.prev.next = None
        self.size -= 1
        return deleted_node
    
    def delete_from_position(self, position):
        if position < 0 or position >= self.size:
            return None
        
        if position == 0:
            return self.delete_from_beginning()
        
        if position == self.size - 1:
            return self.delete_from_end()
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        deleted_node = current
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        self.size -= 1
        return deleted_node
    
    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                
                self.size -= 1
                return current
            current = current.next
        return None
    
    def update_at_index(self, index, new_value):
        if index < 0 or index >= self.size:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.data = new_value
        return True
    
    def update_by_value(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def count_nodes(self):
        return self.size
    
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position, current
            current = current.next
            position += 1
        return -1, None
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node  # For doubly linked list
            prev = current
            current = next_node
        self.head = prev
        return self.head
    
    def detect_cycle(self):
        if not self.head or not self.head.next:
            return False
        
        slow = self.head
        fast = self.head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
    
    def find_middle(self):
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def find_nth_from_end(self, n):
        if n <= 0 or not self.head:
            return None
        
        first = self.head
        second = self.head
        
        # Move first pointer n nodes ahead
        for _ in range(n):
            if not first:
                return None
            first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        return second

# Visualization functions
def visualize_linked_list_simple(elements, highlight_index=None, title="Linked List Visualization"):
    """Simple visualization using matplotlib"""
    if not elements:
        fig, ax = plt.subplots(1, 1, figsize=(8, 2))
        ax.text(0.5, 0.5, 'Empty List', ha='center', va='center', fontsize=16)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.title(title, fontsize=14, fontweight='bold')
        return fig
    
    fig, ax = plt.subplots(1, 1, figsize=(max(8, len(elements) * 2), 3))
    ax.set_xlim(0, len(elements) * 2 + 1)
    ax.set_ylim(0, 2)
    ax.axis('off')
    
    for i, element in enumerate(elements):
        x = 1 + i * 2
        y = 1
        
        # Determine color
        color = 'lightgreen' if highlight_index == i else 'lightblue'
        
        # Draw node
        rect = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, 
                             boxstyle="round,pad=0.02",
                             facecolor=color, 
                             edgecolor='blue', 
                             linewidth=2)
        ax.add_patch(rect)
        
        # Add data value
        ax.text(x, y, str(element), ha='center', va='center', 
                fontweight='bold', fontsize=12)
        
        # Draw arrow to next node
        if i < len(elements) - 1:
            arrow = patches.FancyArrowPatch((x+0.4, y), (x+1.6, y),
                                          arrowstyle='->', 
                                          mutation_scale=20,
                                          color='red', 
                                          linewidth=2)
            ax.add_patch(arrow)
    
    # Draw NULL box
    null_x = 1 + len(elements) * 2
    rect = FancyBboxPatch((null_x-0.3, y-0.2), 0.6, 0.4, 
                         boxstyle="round,pad=0.02",
                         facecolor='lightcoral', 
                         edgecolor='red', 
                         linewidth=2)
    ax.add_patch(rect)
    ax.text(null_x, y, 'NULL', ha='center', va='center', 
            fontweight='bold', fontsize=10)
    
    # Add arrow to NULL
    if elements:
        arrow = patches.FancyArrowPatch((1 + (len(elements)-1) * 2 + 0.4, y), 
                                      (null_x-0.3, y),
                                      arrowstyle='->', 
                                      mutation_scale=20,
                                      color='red', 
                                      linewidth=2)
        ax.add_patch(arrow)
    
    # Add HEAD pointer
    ax.text(0.3, 1.5, 'HEAD', fontweight='bold', fontsize=14, color='green')
    if elements:
        arrow_head = patches.FancyArrowPatch((0.5, 1.3), (0.6, 1.1),
                                           arrowstyle='->', 
                                           mutation_scale=15,
                                           color='green', 
                                           linewidth=2)
        ax.add_patch(arrow_head)
    
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    return fig

def draw_linked_list_diagram():
    """Create a visual representation of a basic linked list"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    ax.axis('off')
    
    # Node positions
    nodes = [(1, 1), (3.5, 1), (6, 1), (8.5, 1)]
    data_values = ['10', '20', '30', 'NULL']
    
    for i, (x, y) in enumerate(nodes[:-1]):
        # Draw node rectangle
        rect = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, 
                             boxstyle="round,pad=0.02",
                             facecolor='lightblue', 
                             edgecolor='blue', 
                             linewidth=2)
        ax.add_patch(rect)
        
        # Add data value
        ax.text(x, y, data_values[i], ha='center', va='center', 
                fontweight='bold', fontsize=12)
        
        # Draw arrow to next node
        if i < len(nodes) - 2:
            arrow = patches.FancyArrowPatch((x+0.4, y), (nodes[i+1][0]-0.4, y),
                                          arrowstyle='->', 
                                          mutation_scale=20,
                                          color='red', 
                                          linewidth=2)
            ax.add_patch(arrow)
    
    # Draw NULL box
    null_x, null_y = nodes[-1]
    rect = FancyBboxPatch((null_x-0.3, null_y-0.2), 0.6, 0.4, 
                         boxstyle="round,pad=0.02",
                         facecolor='lightcoral', 
                         edgecolor='red', 
                         linewidth=2)
    ax.add_patch(rect)
    ax.text(null_x, null_y, 'NULL', ha='center', va='center', 
            fontweight='bold', fontsize=10)
    
    # Add arrow to NULL
    arrow = patches.FancyArrowPatch((nodes[-2][0]+0.4, nodes[-2][1]), 
                                  (null_x-0.3, null_y),
                                  arrowstyle='->', 
                                  mutation_scale=20,
                                  color='red', 
                                  linewidth=2)
    ax.add_patch(arrow)
    
    # Add labels
    ax.text(0.5, 0.2, 'HEAD', fontweight='bold', fontsize=14, color='green')
    arrow_head = patches.FancyArrowPatch((0.7, 0.3), (0.9, 0.8),
                                       arrowstyle='->', 
                                       mutation_scale=15,
                                       color='green', 
                                       linewidth=2)
    ax.add_patch(arrow_head)
    
    plt.title('Singly Linked List Structure', fontsize=16, fontweight='bold', pad=20)
    return fig

def draw_array_vs_linkedlist():
    """Create a comparison diagram between array and linked list memory layout"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    
    # Array representation
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 2)
    ax1.axis('off')
    ax1.set_title('Array - Contiguous Memory Layout', fontsize=14, fontweight='bold', pad=20)
    
    # Draw array blocks
    array_values = ['10', '20', '30', '40']
    for i, value in enumerate(array_values):
        x = 2 + i * 1.5
        rect = patches.Rectangle((x, 1), 1.2, 0.6, 
                               facecolor='lightgreen', 
                               edgecolor='darkgreen', 
                               linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x + 0.6, 1.3, value, ha='center', va='center', 
                fontweight='bold', fontsize=12)
        ax1.text(x + 0.6, 0.7, f'[{i}]', ha='center', va='center', 
                fontsize=10, style='italic')
    
    # Memory addresses
    addresses = ['1000', '1004', '1008', '1012']
    for i, addr in enumerate(addresses):
        x = 2 + i * 1.5
        ax1.text(x + 0.6, 0.3, addr, ha='center', va='center', 
                fontsize=9, color='blue')
    
    # Linked List representation
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 2)
    ax2.axis('off')
    ax2.set_title('Linked List - Non-contiguous Memory Layout', fontsize=14, fontweight='bold', pad=20)
    
    # Draw linked list nodes at random positions
    positions = [(1.5, 1.3), (4, 1.3), (7, 1.3), (2.5, 0.4)]
    ll_values = ['10', '20', '30', 'NULL']
    addresses_ll = ['1000', '2048', '3072', 'NULL']
    next_addrs = ['2048', '3072', 'NULL', '']
    
    for i, ((x, y), value, addr, next_addr) in enumerate(zip(positions, ll_values, addresses_ll, next_addrs)):
        if i < 3:  # Not NULL node
            # Data part
            rect1 = patches.Rectangle((x, y), 0.8, 0.4, 
                                    facecolor='lightblue', 
                                    edgecolor='blue', 
                                    linewidth=1)
            ax2.add_patch(rect1)
            ax2.text(x + 0.4, y + 0.2, value, ha='center', va='center', 
                    fontweight='bold', fontsize=10)
            
            # Pointer part
            rect2 = patches.Rectangle((x + 0.8, y), 0.8, 0.4, 
                                    facecolor='lightyellow', 
                                    edgecolor='orange', 
                                    linewidth=1)
            ax2.add_patch(rect2)
            ax2.text(x + 1.2, y + 0.2, next_addr, ha='center', va='center', 
                    fontsize=8)
            
            # Address label
            ax2.text(x + 0.8, y - 0.3, f'@{addr}', ha='center', va='center', 
                    fontsize=8, color='red')
            
            # Draw arrow to next node if not last
            if i < 2:
                next_pos = positions[i + 1]
                arrow = patches.FancyArrowPatch((x + 1.6, y + 0.2), 
                                             (next_pos[0], next_pos[1] + 0.2),
                                             arrowstyle='->', 
                                             mutation_scale=15,
                                             color='red', 
                                             linewidth=1.5,
                                             connectionstyle="arc3,rad=0.3")
                ax2.add_patch(arrow)
    
    plt.tight_layout()
    return fig

def draw_node_structure():
    """Draw detailed node structure"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # Draw main node
    # Data field
    data_rect = patches.Rectangle((2, 2), 1.5, 1, 
                                facecolor='lightblue', 
                                edgecolor='blue', 
                                linewidth=2)
    ax.add_patch(data_rect)
    ax.text(2.75, 2.5, 'DATA\\n42', ha='center', va='center', 
            fontweight='bold', fontsize=12)
    
    # Next pointer field
    next_rect = patches.Rectangle((3.5, 2), 1.5, 1, 
                                facecolor='lightyellow', 
                                edgecolor='orange', 
                                linewidth=2)
    ax.add_patch(next_rect)
    ax.text(4.25, 2.5, 'NEXT\\n→', ha='center', va='center', 
            fontweight='bold', fontsize=12)
    
    # Node boundary
    node_rect = patches.Rectangle((1.8, 1.8), 3.4, 1.4, 
                                fill=False,
                                edgecolor='black', 
                                linewidth=3,
                                linestyle='--')
    ax.add_patch(node_rect)
    
    # Labels
    ax.text(2.75, 3.5, 'Node Structure', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    ax.text(2.75, 1.4, 'Data Field: Stores the actual value', 
            ha='center', va='center', fontsize=10, style='italic')
    ax.text(4.25, 1.4, 'Next Field: Points to the next node', 
            ha='center', va='center', fontsize=10, style='italic')
    
    # Memory address
    ax.text(3, 3.8, 'Memory Address: 0x1A2B', ha='center', va='center', 
            fontsize=10, color='red')
    
    return fig

# Initialize session state for linked list
if 'linked_list' not in st.session_state:
    st.session_state.linked_list = LinkedList()
if 'operation_history' not in st.session_state:
    st.session_state.operation_history = []
if 'step_by_step' not in st.session_state:
    st.session_state.step_by_step = False
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

# Sidebar navigation
st.sidebar.title("🔗 Navigation")
sections = {
    "🏠 Home": "home",
    "📚 Basic Concepts": "basic",
    "🔄 Types of Linked Lists": "types",
    "⚡ Operations & Algorithms": "operations",
    "🛠️ Interactive Operations": "interactive",
    "🎯 Real-world Applications": "applications"
}

selected_section = st.sidebar.selectbox("Choose a section:", list(sections.keys()))
current_section = sections[selected_section]

# Main title
st.markdown('<h1 class="main-header">🔗 Interactive Linked Lists Tutorial</h1>', unsafe_allow_html=True)

# Main content based on selected section
if current_section == "home":
    st.markdown("""
    <div class="concept-box">
        <h2>Welcome to the Interactive Linked Lists Tutorial! 🎓</h2>
        <p>This comprehensive tutorial will help you understand linked lists through interactive visualizations and clear explanations.</p>
        
        <h3>What you'll learn:</h3>
        <ul>
            <li>📚 Basic concepts and differences from arrays</li>
            <li>🔄 Different types of linked lists with visualizations</li>
            <li>⚡ Common operations and algorithms</li>
            <li>🛠️ Interactive operations with real-time visualization</li>
            <li>🎯 Practical applications and use cases</li>
            <li>💻 Implementation examples in Python</li>
        </ul>
        
        <p><strong>Use the navigation sidebar to explore different sections!</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="detail-box">
        <h3>Why Learn About Linked Lists?</h3>
        <p>Linked lists are fundamental data structures in computer science that form the basis for more complex 
        structures like trees, graphs, and hash tables. Understanding linked lists helps you:</p>
        <ul>
            <li>Grasp how dynamic memory allocation works</li>
            <li>Learn about pointers and references</li>
            <li>Understand time and space complexity trade-offs</li>
            <li>Prepare for technical interviews (a common topic!)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif current_section == "basic":
    st.markdown('<h2 class="section-header">📚 Basic Concepts</h2>', unsafe_allow_html=True)
    
    # What is a Linked List?
    st.subheader("🔗 What is a Linked List?")
    
    st.markdown("""
    <div class="concept-box">
        <p><strong>A Linked List</strong> is a linear data structure where elements are stored in nodes, and each node contains:</p>
        <ul>
            <li><strong>Data:</strong> The actual value stored in the node</li>
            <li><strong>Next:</strong> A pointer/reference to the next node in the sequence</li>
        </ul>
        <p>Unlike arrays, linked list elements are not stored in contiguous memory locations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual representation
    st.subheader("📊 Visual Representation")
    fig1 = draw_linked_list_diagram()
    st.pyplot(fig1)
    plt.close(fig1)
    
    # Node Structure
    st.subheader("🏗️ Node Structure")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="node-structure">
            <h4>Node Components:</h4>
            <ul>
                <li><strong>Data Field:</strong> Stores the actual information</li>
                <li><strong>Next Field:</strong> Contains address of next node</li>
            </ul>
            
            <h4>Code Representation:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
class Node:
    def __init__(self, data):
        self.data = data    # Store data
        self.next = None    # Pointer to next node
        # For doubly linked list:
        # self.prev = None  # Pointer to previous node
        """, language="python")
    
    with col2:
        fig_node = draw_node_structure()
        st.pyplot(fig_node)
        plt.close(fig_node)
    
    # Difference between Linked List and Array
    st.subheader("⚖️ Linked List vs Array")
    
    fig2 = draw_array_vs_linkedlist()
    st.pyplot(fig2)
    plt.close(fig2)
    
    # Comparison table
    st.markdown("""
    <table class="comparison-table">
        <tr>
            <th>Aspect</th>
            <th>Array</th>
            <th>Linked List</th>
        </tr>
        <tr>
            <td><strong>Memory Layout</strong></td>
            <td>Contiguous memory blocks</td>
            <td>Non-contiguous, scattered memory</td>
        </tr>
        <tr>
            <td><strong>Access Time</strong></td>
            <td>O(1) - Random access</td>
            <td>O(n) - Sequential access</td>
        </tr>
        <tr>
            <td><strong>Insertion/Deletion</strong></td>
            <td>O(n) - Need to shift elements</td>
            <td>O(1) - At known position</td>
        </tr>
        <tr>
            <td><strong>Memory Overhead</strong></td>
            <td>No extra memory for pointers</td>
            <td>Extra memory for storing pointers</td>
        </tr>
        <tr>
            <td><strong>Cache Performance</strong></td>
            <td>Better - Spatial locality</td>
            <td>Poor - Random memory access</td>
        </tr>
        <tr>
            <td><strong>Size</strong></td>
            <td>Fixed size (static arrays)</td>
            <td>Dynamic size</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

elif current_section == "interactive":
    st.markdown('<h2 class="section-header">🛠️ Interactive Operations</h2>', unsafe_allow_html=True)
    
    # Operation selection
    operation_type = st.selectbox(
        "Select Operation Type:",
        ["Insertion", "Deletion", "Update", "Traversal", "Searching", "Advanced Operations"]
    )
    
    # Initialize variables
    operation_result = None
    highlight_index = None
    
    # Insertion operations
    if operation_type == "Insertion":
        insertion_type = st.selectbox(
            "Select Insertion Type:",
            ["At the beginning", "At the end", "At a specific position", "After a given node"]
        )
        
        data = st.text_input("Enter data to insert:")
        
        if insertion_type == "At a specific position":
            position = st.number_input("Position (0-based):", min_value=0, max_value=st.session_state.linked_list.size, value=0)
        elif insertion_type == "After a given node":
            target_data = st.text_input("Enter node data to insert after:")
        
        if st.button("Perform Insertion"):
            if data:
                if insertion_type == "At the beginning":
                    operation_result = st.session_state.linked_list.insert_at_beginning(data)
                    st.session_state.operation_history.append(f"Inserted '{data}' at beginning")
                    highlight_index = 0
                
                elif insertion_type == "At the end":
                    operation_result = st.session_state.linked_list.insert_at_end(data)
                    st.session_state.operation_history.append(f"Inserted '{data}' at end")
                    highlight_index = st.session_state.linked_list.size - 1
                
                elif insertion_type == "At a specific position":
                    operation_result = st.session_state.linked_list.insert_at_position(data, position)
                    if operation_result:
                        st.session_state.operation_history.append(f"Inserted '{data}' at position {position}")
                        highlight_index = position
                    else:
                        st.error("Invalid position!")
                
                elif insertion_type == "After a given node":
                    if target_data:
                        operation_result = st.session_state.linked_list.insert_after_node(data, target_data)
                        if operation_result:
                            st.session_state.operation_history.append(f"Inserted '{data}' after node '{target_data}'")
                            # Find the index for highlighting
                            elements = st.session_state.linked_list.traverse()
                            try:
                                target_index = elements.index(target_data)
                                highlight_index = target_index + 1
                            except ValueError:
                                pass
                        else:
                            st.error(f"Node with data '{target_data}' not found!")
                    else:
                        st.error("Please enter target node data!")
            else:
                st.error("Please enter data to insert!")
    
    # Deletion operations
    elif operation_type == "Deletion":
        deletion_type = st.selectbox(
            "Select Deletion Type:",
            ["From beginning", "From end", "From specific position", "By value"]
        )
        
        if deletion_type == "From specific position":
            position = st.number_input("Position (0-based):", min_value=0, max_value=max(0, st.session_state.linked_list.size-1), value=0)
        elif deletion_type == "By value":
            value = st.text_input("Enter value to delete:")
        
        if st.button("Perform Deletion"):
            if deletion_type == "From beginning":
                operation_result = st.session_state.linked_list.delete_from_beginning()
                if operation_result:
                    st.session_state.operation_history.append(f"Deleted from beginning: '{operation_result.data}'")
                else:
                    st.error("List is empty!")
            
            elif deletion_type == "From end":
                operation_result = st.session_state.linked_list.delete_from_end()
                if operation_result:
                    st.session_state.operation_history.append(f"Deleted from end: '{operation_result.data}'")
                else:
                    st.error("List is empty!")
            
            elif deletion_type == "From specific position":
                operation_result = st.session_state.linked_list.delete_from_position(position)
                if operation_result:
                    st.session_state.operation_history.append(f"Deleted from position {position}: '{operation_result.data}'")
                else:
                    st.error("Invalid position!")
            
            elif deletion_type == "By value":
                if value:
                    operation_result = st.session_state.linked_list.delete_by_value(value)
                    if operation_result:
                        st.session_state.operation_history.append(f"Deleted by value: '{value}'")
                    else:
                        st.error(f"Value '{value}' not found in list!")
                else:
                    st.error("Please enter a value to delete!")
    
    # Update operations
    elif operation_type == "Update":
        update_type = st.selectbox(
            "Select Update Type:",
            ["Change node value at given index", "Replace node by searching value"]
        )
        
        if update_type == "Change node value at given index":
            position = st.number_input("Position (0-based):", min_value=0, max_value=max(0, st.session_state.linked_list.size-1), value=0)
            new_value = st.text_input("New value:")
        else:
            old_value = st.text_input("Value to replace:")
            new_value = st.text_input("New value:")
        
        if st.button("Perform Update"):
            if update_type == "Change node value at given index":
                if new_value:
                    success = st.session_state.linked_list.update_at_index(position, new_value)
                    if success:
                        st.session_state.operation_history.append(f"Updated position {position} to '{new_value}'")
                        highlight_index = position
                    else:
                        st.error("Invalid position!")
                else:
                    st.error("Please enter a new value!")
            
            else:
                if old_value and new_value:
                    success = st.session_state.linked_list.update_by_value(old_value, new_value)
                    if success:
                        st.session_state.operation_history.append(f"Updated '{old_value}' to '{new_value}'")
                        # Find the index for highlighting
                        elements = st.session_state.linked_list.traverse()
                        try:
                            highlight_index = elements.index(new_value)
                        except ValueError:
                            pass
                    else:
                        st.error(f"Value '{old_value}' not found!")
                else:
                    st.error("Please enter both old and new values!")
    
    # Traversal operations
    elif operation_type == "Traversal":
        if st.button("Display All Elements"):
            elements = st.session_state.linked_list.traverse()
            st.write("List elements:", " → ".join(map(str, elements)) if elements else "Empty list")
            st.session_state.operation_history.append("Displayed all elements")
        
        if st.button("Count Nodes"):
            count = st.session_state.linked_list.count_nodes()
            st.write(f"Number of nodes: {count}")
            st.session_state.operation_history.append(f"Counted nodes: {count}")
    
    # Searching operations
    elif operation_type == "Searching":
        search_value = st.text_input("Enter value to search:")
        
        if st.button("Search"):
            if search_value:
                position, node = st.session_state.linked_list.search(search_value)
                if position != -1:
                    st.success(f"Value '{search_value}' found at position {position}")
                    highlight_index = position
                    st.session_state.operation_history.append(f"Searched for '{search_value}': found at position {position}")
                else:
                    st.error(f"Value '{search_value}' not found!")
                    st.session_state.operation_history.append(f"Searched for '{search_value}': not found")
            else:
                st.error("Please enter a value to search!")
    
    # Advanced operations
    elif operation_type == "Advanced Operations":
        advanced_op = st.selectbox(
            "Select Advanced Operation:",
            ["Reverse the list", "Detect cycle", "Find middle node", "Find Nth node from end"]
        )
        
        if advanced_op == "Find Nth node from end":
            n = st.number_input("Enter N:", min_value=1, max_value=max(1, st.session_state.linked_list.size), value=1)
        
        if st.button("Perform Operation"):
            if advanced_op == "Reverse the list":
                st.session_state.linked_list.reverse()
                st.session_state.operation_history.append("Reversed the list")
                st.success("List reversed successfully!")
            
            elif advanced_op == "Detect cycle":
                has_cycle = st.session_state.linked_list.detect_cycle()
                if has_cycle:
                    st.warning("Cycle detected in the list!")
                else:
                    st.success("No cycle detected in the list.")
                st.session_state.operation_history.append(f"Cycle detection: {'Cycle found' if has_cycle else 'No cycle'}")
            
            elif advanced_op == "Find middle node":
                middle_node = st.session_state.linked_list.find_middle()
                if middle_node:
                    st.success(f"Middle node: {middle_node.data}")
                    # Find the index for highlighting
                    elements = st.session_state.linked_list.traverse()
                    highlight_index = len(elements) // 2
                    st.session_state.operation_history.append(f"Found middle node: {middle_node.data}")
                else:
                    st.error("List is empty!")
            
            elif advanced_op == "Find Nth node from end":
                nth_node = st.session_state.linked_list.find_nth_from_end(n)
                if nth_node:
                    st.success(f"{n}th node from end: {nth_node.data}")
                    # Find the index for highlighting
                    elements = st.session_state.linked_list.traverse()
                    highlight_index = len(elements) - n
                    st.session_state.operation_history.append(f"Found {n}th node from end: {nth_node.data}")
                else:
                    st.error("Invalid position or empty list!")
    
    # Visualization
    st.subheader("📊 Linked List Visualization")
    
    elements = st.session_state.linked_list.traverse()
    if elements:
        fig = visualize_linked_list_simple(elements, highlight_index)
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("The linked list is empty. Add some nodes to see the visualization.")
    
    # List information
    st.subheader("📋 List Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Size:**", st.session_state.linked_list.size)
    
    with col2:
        elements = st.session_state.linked_list.traverse()
        st.write("**Elements:**", " → ".join(map(str, elements)) if elements else "Empty")
    
    with col3:
        if st.button("Clear List"):
            st.session_state.linked_list = LinkedList()
            st.session_state.operation_history = []
            st.session_state.current_step = 0
            st.success("List cleared!")
    
    # Operation history
    if st.session_state.operation_history:
        st.subheader("📜 Operation History")
        for i, op in enumerate(st.session_state.operation_history):
            st.write(f"{i+1}. {op}")

elif current_section == "operations":
    st.markdown('<h2 class="section-header">⚡ Operations & Algorithms</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
        <p>Linked lists support various operations that allow manipulation of the data structure. 
        Understanding these operations is crucial for effective use of linked lists.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Common algorithms
    st.subheader("🧠 Common Algorithms")
    
    tab1, tab2, tab3 = st.tabs(["Reverse List", "Detect Cycle", "Find Middle"])
    
    with tab1:
        st.markdown("""
        <div class="node-structure">
            <h4>Reversing a Linked List</h4>
            <p>This algorithm reverses the direction of pointers in the list.</p>
            
            <p><strong>Steps:</strong></p>
            <ol>
                <li>Initialize three pointers: prev = NULL, current = head, next = NULL</li>
                <li>Traverse the list and for each node:
                    <ul>
                        <li>Store the next node</li>
                        <li>Change next of current to prev</li>
                        <li>Move prev and current one step forward</li>
                    </ul>
                </li>
                <li>Finally, set head = prev</li>
            </ol>
            
            <p><strong>Time Complexity:</strong> O(n)</p>
            <p><strong>Space Complexity:</strong> O(1)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse pointer
        prev = current           # Move prev forward
        current = next_node      # Move current forward
    return prev
        """, language="python")
    
    with tab2:
        st.markdown("""
        <div class="node-structure">
            <h4>Cycle Detection (Floyd's Algorithm)</h4>
            <p>This algorithm detects if a linked list has a cycle using two pointers moving at different speeds.</p>
            
            <p><strong>Steps:</strong></p>
            <ol>
                <li>Initialize two pointers: slow = head, fast = head</li>
                <li>Traverse the list:
                    <ul>
                        <li>Move slow pointer by one node</li>
                        <li>Move fast pointer by two nodes</li>
                        <li>If they meet, cycle exists</li>
                        <li>If fast reaches NULL, no cycle</li>
                    </ul>
                </li>
            </ol>
            
            <p><strong>Time Complexity:</strong> O(n)</p>
            <p><strong>Space Complexity:</strong> O(1)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
        """, language="python")
    
    with tab3:
        st.markdown("""
        <div class="node-structure">
            <h4>Finding the Middle Node</h4>
            <p>This algorithm finds the middle node of a linked list using two pointers.</p>
            
            <p><strong>Steps:</strong></p>
            <ol>
                <li>Initialize two pointers: slow = head, fast = head</li>
                <li>Traverse the list:
                    <ul>
                        <li>Move slow pointer by one node</li>
                        <li>Move fast pointer by two nodes</li>
                        <li>When fast reaches end, slow is at middle</li>
                    </ul>
                </li>
            </ol>
            
            <p><strong>Time Complexity:</strong> O(n)</p>
            <p><strong>Space Complexity:</strong> O(1)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
def find_middle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
        """, language="python")

elif current_section == "types":
    st.markdown('<h2 class="section-header">🔄 Types of Linked Lists</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
        <p>There are several types of linked lists, each with its own characteristics and use cases:</p>
        <ul>
            <li><strong>Singly Linked List:</strong> Each node points to the next node</li>
            <li><strong>Doubly Linked List:</strong> Each node has pointers to both next and previous nodes</li>
            <li><strong>Circular Linked List:</strong> The last node points back to the first node</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Code examples for different types
    st.subheader("💻 Implementation Examples")
    
    tab1, tab2, tab3 = st.tabs(["Singly Linked", "Doubly Linked", "Circular Linked"])
    
    with tab1:
        st.code("""
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        """, language="python")
    
    with tab2:
        st.code("""
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        """, language="python")
    
    with tab3:
        st.code("""
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        """, language="python")

elif current_section == "applications":
    st.markdown('<h2 class="section-header">🎯 Real-world Applications</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
        <p>Linked lists are used in various real-world applications due to their dynamic nature and efficient insertion/deletion capabilities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Applications
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>💾 Memory Management</h4>
            <p>Linked lists are used in memory allocators to maintain free memory blocks. 
            Each node represents a free memory block with its size and location.</p>
            
            <p><strong>Benefits:</strong></p>
            <ul>
                <li>Efficient allocation and deallocation</li>
                <li>Easy to merge adjacent free blocks</li>
                <li>Dynamic memory management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🌐 Web Browsers</h4>
            <p>Doubly linked lists are used to implement browser history and back/forward navigation.</p>
            
            <p><strong>How it works:</strong></p>
            <ul>
                <li>Each page visit adds a new node</li>
                <li>Back button moves to previous node</li>
                <li>Forward button moves to next node</li>
                <li>Efficient navigation in both directions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>📝 Text Editors</h4>
            <p>Linked lists are used to represent text in editors where each character is a node.</p>
            
            <p><strong>Benefits:</strong></p>
            <ul>
                <li>Efficient insertion and deletion of text</li>
                <li>No need to shift entire text after edits</li>
                <li>Better performance for large documents</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🎵 Music Players</h4>
            <p>Circular linked lists are used to implement playlists that loop continuously.</p>
            
            <p><strong>How it works:</strong></p>
            <ul>
                <li>Each song is a node in the list</li>
                <li>Last song points to first song</li>
                <li>Seamless continuous playback</li>
                <li>Easy to add/remove songs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Add footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>🔗 Interactive Linked Lists Tutorial | Made with Streamlit and Matplotlib</p>
    <p>For educational purposes only</p>
</div>
""", unsafe_allow_html=True)

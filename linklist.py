import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arrow
import numpy as np

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

# Sidebar navigation
st.sidebar.title("🔗 Navigation")
sections = {
    "🏠 Home": "home",
    "📚 Basic Concepts": "basic",
    "🔄 Types of Linked Lists": "types",
    "⚡ Operations & Algorithms": "operations",
    "🎯 Real-world Applications": "applications"
}

selected_section = st.sidebar.selectbox("Choose a section:", list(sections.keys()))
current_section = sections[selected_section]

# Main title
st.markdown('<h1 class="main-header">🔗 Interactive Linked Lists Tutorial</h1>', unsafe_allow_html=True)

# Define Node class for code examples
node_class_code = """
class Node:
    def __init__(self, data):
        self.data = data    # Store data
        self.next = None    # Pointer to next node
        # For doubly linked list:
        # self.prev = None  # Pointer to previous node
"""

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
    ax.text(2.75, 2.5, 'DATA\n42', ha='center', va='center', 
            fontweight='bold', fontsize=12)
    
    # Next pointer field
    next_rect = patches.Rectangle((3.5, 2), 1.5, 1, 
                                facecolor='lightyellow', 
                                edgecolor='orange', 
                                linewidth=2)
    ax.add_patch(next_rect)
    ax.text(4.25, 2.5, 'NEXT\n→', ha='center', va='center', 
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

def draw_singly_linked_list():
    """Draw interactive singly linked list"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    nodes_data = ['A', 'B', 'C', 'D']
    x_positions = [2, 4.5, 7, 9.5]
    
    for i, (data, x) in enumerate(zip(nodes_data, x_positions)):
        # Draw node
        node_rect = FancyBboxPatch((x-0.6, 1.2), 1.2, 0.8, 
                                  boxstyle="round,pad=0.05",
                                  facecolor='lightcyan', 
                                  edgecolor='teal', 
                                  linewidth=2)
        ax.add_patch(node_rect)
        
        # Data section
        ax.text(x-0.2, 1.6, data, ha='center', va='center', 
                fontweight='bold', fontsize=14)
        
        # Next pointer
        ax.text(x+0.2, 1.6, '→', ha='center', va='center', 
                fontsize=16, color='red')
        
        # Divider line
        ax.plot([x, x], [1.2, 2.0], color='gray', linewidth=1)
        
        # Draw arrow to next node
        if i < len(nodes_data) - 1:
            next_x = x_positions[i + 1]
            arrow = patches.FancyArrowPatch((x+0.6, 1.6), (next_x-0.6, 1.6),
                                          arrowstyle='->', 
                                          mutation_scale=20,
                                          color='red', 
                                          linewidth=2)
            ax.add_patch(arrow)
    
    # NULL pointer at the end
    null_rect = FancyBboxPatch((10.5, 1.4), 0.8, 0.4, 
                              boxstyle="round,pad=0.02",
                              facecolor='lightcoral', 
                              edgecolor='red', 
                              linewidth=2)
    ax.add_patch(null_rect)
    ax.text(10.9, 1.6, 'NULL', ha='center', va='center', 
            fontweight='bold', fontsize=10)
    
    # Arrow to NULL
    arrow = patches.FancyArrowPatch((x_positions[-1]+0.6, 1.6), (10.5, 1.6),
                                  arrowstyle='->', 
                                  mutation_scale=20,
                                  color='red', 
                                  linewidth=2)
    ax.add_patch(arrow)
    
    # HEAD pointer
    ax.text(1, 2.5, 'HEAD', fontweight='bold', fontsize=14, color='green')
    arrow_head = patches.FancyArrowPatch((1.3, 2.3), (1.4, 1.8),
                                       arrowstyle='->', 
                                       mutation_scale=15,
                                       color='green', 
                                       linewidth=2)
    ax.add_patch(arrow_head)
    
    plt.title('Singly Linked List Visualization', fontsize=16, fontweight='bold', pad=20)
    return fig

def draw_doubly_linked_list():
    """Draw interactive doubly linked list"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    nodes_data = ['X', 'Y', 'Z']
    x_positions = [2.5, 5.5, 8.5]
    
    for i, (data, x) in enumerate(zip(nodes_data, x_positions)):
        # Draw node with three sections
        # Previous pointer
        prev_rect = patches.Rectangle((x-0.8, 1.8), 0.5, 0.8, 
                                    facecolor='lightpink', 
                                    edgecolor='purple', 
                                    linewidth=2)
        ax.add_patch(prev_rect)
        ax.text(x-0.55, 2.2, '←', ha='center', va='center', 
                fontsize=14, color='purple')
        
        # Data section
        data_rect = patches.Rectangle((x-0.3, 1.8), 0.6, 0.8, 
                                    facecolor='lightblue', 
                                    edgecolor='blue', 
                                    linewidth=2)
        ax.add_patch(data_rect)
        ax.text(x, 2.2, data, ha='center', va='center', 
                fontweight='bold', fontsize=14)
        
        # Next pointer
        next_rect = patches.Rectangle((x+0.3, 1.8), 0.5, 0.8, 
                                    facecolor='lightgreen', 
                                    edgecolor='green', 
                                    linewidth=2)
        ax.add_patch(next_rect)
        ax.text(x+0.55, 2.2, '→', ha='center', va='center', 
                fontsize=14, color='green')
        
        # Forward arrows
        if i < len(nodes_data) - 1:
            next_x = x_positions[i + 1]
            arrow = patches.FancyArrowPatch((x+0.8, 2.4), (next_x-0.8, 2.4),
                                          arrowstyle='->', 
                                          mutation_scale=18,
                                          color='green', 
                                          linewidth=2)
            ax.add_patch(arrow)
        
        # Backward arrows
        if i > 0:
            prev_x = x_positions[i - 1]
            arrow = patches.FancyArrowPatch((x-0.8, 1.4), (prev_x+0.8, 1.4),
                                          arrowstyle='->', 
                                          mutation_scale=18,
                                          color='purple', 
                                          linewidth=2)
            ax.add_patch(arrow)
    
    # NULL pointers
    # First node prev = NULL
    null_rect1 = patches.Rectangle((0.5, 1.0), 0.6, 0.3, 
                                 facecolor='lightcoral', 
                                 edgecolor='red', 
                                 linewidth=1)
    ax.add_patch(null_rect1)
    ax.text(0.8, 1.15, 'NULL', ha='center', va='center', 
            fontweight='bold', fontsize=8)
    
    arrow1 = patches.FancyArrowPatch((1.1, 1.2), (1.7, 1.6),
                                   arrowstyle='->', 
                                   mutation_scale=12,
                                   color='purple', 
                                   linewidth=1.5)
    ax.add_patch(arrow1)
    
    # Last node next = NULL
    null_rect2 = patches.Rectangle((10.5, 2.8), 0.6, 0.3, 
                                 facecolor='lightcoral', 
                                 edgecolor='red', 
                                 linewidth=1)
    ax.add_patch(null_rect2)
    ax.text(10.8, 2.95, 'NULL', ha='center', va='center', 
            fontweight='bold', fontsize=8)
    
    arrow2 = patches.FancyArrowPatch((9.3, 2.6), (10.5, 2.9),
                                   arrowstyle='->', 
                                   mutation_scale=12,
                                   color='green', 
                                   linewidth=1.5)
    ax.add_patch(arrow2)
    
    # HEAD pointer
    ax.text(1.5, 3.2, 'HEAD', fontweight='bold', fontsize=14, color='blue')
    arrow_head = patches.FancyArrowPatch((1.8, 3.0), (2.0, 2.8),
                                       arrowstyle='->', 
                                       mutation_scale=15,
                                       color='blue', 
                                       linewidth=2)
    ax.add_patch(arrow_head)
    
    plt.title('Doubly Linked List Visualization', fontsize=16, fontweight='bold', pad=20)
    return fig

def draw_circular_linked_list():
    """Draw circular linked list"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.axis('off')
    
    # Position nodes in a circle
    angles = [0, np.pi/2, np.pi, 3*np.pi/2]
    radius = 2.5
    nodes_data = ['1', '2', '3', '4']
    
    positions = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]
    
    for i, ((x, y), data) in enumerate(zip(positions, nodes_data)):
        # Draw node
        circle = Circle((x, y), 0.4, facecolor='lightgreen', 
                       edgecolor='darkgreen', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, data, ha='center', va='center', 
                fontweight='bold', fontsize=14)
        
        # Draw arrow to next node
        next_i = (i + 1) % len(positions)
        next_x, next_y = positions[next_i]
        
        # Calculate arrow start and end points
        angle_to_next = np.arctan2(next_y - y, next_x - x)
        start_x = x + 0.4 * np.cos(angle_to_next)
        start_y = y + 0.4 * np.sin(angle_to_next)
        end_x = next_x - 0.4 * np.cos(angle_to_next)
        end_y = next_y - 0.4 * np.sin(angle_to_next)
        
        arrow = patches.FancyArrowPatch((start_x, start_y), (end_x, end_y),
                                      arrowstyle='->', 
                                      mutation_scale=20,
                                      color='red', 
                                      linewidth=2,
                                      connectionstyle="arc3,rad=0.1")
        ax.add_patch(arrow)
    
    plt.title('Circular Linked List Visualization', fontsize=16, fontweight='bold', pad=20)
    return fig

def draw_linked_list_operations():
    """Draw common linked list operations"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Common Linked List Operations', fontsize=16, fontweight='bold')
    
    # Insertion at head
    ax1 = axes[0, 0]
    ax1.set_xlim(0, 8)
    ax1.set_ylim(0, 3)
    ax1.axis('off')
    ax1.set_title('Insertion at Head', fontsize=12, fontweight='bold')
    
    # Original list
    ax1.text(2, 2.5, 'HEAD → A → B → NULL', fontsize=10)
    
    # New node
    ax1.text(1, 1.8, 'New Node: X', fontsize=10, color='blue')
    
    # Process
    ax1.text(2, 1.5, '1. X.next = A', fontsize=10)
    ax1.text(2, 1.2, '2. HEAD = X', fontsize=10)
    
    # Result
    ax1.text(2, 0.5, 'Result: HEAD → X → A → B → NULL', fontsize=10, color='green')
    
    # Insertion at tail
    ax2 = axes[0, 1]
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 3)
    ax2.axis('off')
    ax2.set_title('Insertion at Tail', fontsize=12, fontweight='bold')
    
    # Original list
    ax2.text(2, 2.5, 'HEAD → A → B → NULL', fontsize=10)
    
    # New node
    ax2.text(1, 1.8, 'New Node: X', fontsize=10, color='blue')
    
    # Process
    ax2.text(2, 1.5, '1. Traverse to B (last node)', fontsize=10)
    ax2.text(2, 1.2, '2. B.next = X', fontsize=10)
    ax2.text(2, 0.9, '3. X.next = NULL', fontsize=10)
    
    # Result
    ax2.text(2, 0.5, 'Result: HEAD → A → B → X → NULL', fontsize=10, color='green')
    
    # Deletion
    ax3 = axes[1, 0]
    ax3.set_xlim(0, 8)
    ax3.set_ylim(0, 3)
    ax3.axis('off')
    ax3.set_title('Deletion of a Node', fontsize=12, fontweight='bold')
    
    # Original list
    ax3.text(2, 2.5, 'HEAD → A → B → C → NULL', fontsize=10)
    
    # Node to delete
    ax3.text(1, 1.8, 'Delete Node: B', fontsize=10, color='red')
    
    # Process
    ax3.text(2, 1.5, '1. Find A (node before B)', fontsize=10)
    ax3.text(2, 1.2, '2. A.next = B.next (point to C)', fontsize=10)
    ax3.text(2, 0.9, '3. Remove B from memory', fontsize=10)
    
    # Result
    ax3.text(2, 0.5, 'Result: HEAD → A → C → NULL', fontsize=10, color='green')
    
    # Traversal
    ax4 = axes[1, 1]
    ax4.set_xlim(0, 8)
    ax4.set_ylim(0, 3)
    ax4.axis('off')
    ax4.set_title('Traversal', fontsize=12, fontweight='bold')
    
    # List
    ax4.text(2, 2.5, 'HEAD → A → B → C → NULL', fontsize=10)
    
    # Process
    ax4.text(2, 1.8, '1. Start from HEAD', fontsize=10)
    ax4.text(2, 1.5, '2. current = HEAD', fontsize=10)
    ax4.text(2, 1.2, '3. While current != NULL:', fontsize=10)
    ax4.text(3, 0.9, '   print(current.data)', fontsize=10)
    ax4.text(3, 0.6, '   current = current.next', fontsize=10)
    
    # Result
    ax4.text(2, 0.2, 'Output: A, B, C', fontsize=10, color='green')
    
    plt.tight_layout()
    return fig

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
    
    st.markdown("""
    <div class="detail-box">
        <h3>Key Characteristics of Linked Lists:</h3>
        <ul>
            <li><strong>Dynamic Size:</strong> Unlike arrays, linked lists can grow and shrink during runtime</li>
            <li><strong>Memory Efficiency:</strong> Memory is allocated as needed, reducing wasted space</li>
            <li><strong>Insertion/Deletion:</strong> Adding or removing elements is efficient compared to arrays</li>
            <li><strong>Sequential Access:</strong> Elements must be accessed sequentially, starting from the head</li>
            <li><strong>Memory Overhead:</strong> Each node requires extra memory for the pointer/reference</li>
        </ul>
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
        
        st.markdown('<div class="code-block">', unsafe_allow_html=True)
        st.code(node_class_code, language="python")
        st.markdown('</div>', unsafe_allow_html=True)
    
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
    
    st.markdown("""
    <div class="detail-box">
        <h3>When to Use Linked Lists vs Arrays:</h3>
        <p><strong>Use Linked Lists when:</strong></p>
        <ul>
            <li>You need constant-time insertions/deletions from the list</li>
            <li>You don't know how many items will be in the list</li>
            <li>You don't need random access to any elements</li>
            <li>You want to be able to insert items in the middle of the list</li>
        </ul>
        
        <p><strong>Use Arrays when:</strong></p>
        <ul>
            <li>You need index-based/random access to elements</li>
            <li>You know the number of elements in advance</li>
            <li>You need better cache performance for iteration</li>
            <li>Memory is a concern (arrays have less overhead)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Advantages and Disadvantages
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>✅ Linked List Advantages:</h4>
            <ul>
                <li>Dynamic size allocation</li>
                <li>Efficient insertion/deletion</li>
                <li>Memory efficient (no wasted space)</li>
                <li>Easy to implement stacks and queues</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>❌ Linked List Disadvantages:</h4>
            <ul>
                <li>No random access to elements</li>
                <li>Extra memory for storing pointers</li>
                <li>Poor cache locality</li>
                <li>Not suitable for binary search</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "types":
    st.markdown('<h2 class="section-header">🔄 Types of Linked Lists</h2>', unsafe_allow_html=True)
    
    # Tabs for different types
    tab1, tab2, tab3 = st.tabs(["🔗 Singly Linked List", "↔️ Doubly Linked List", "🔄 Circular Linked List"])
    
    with tab1:
        st.subheader("Singly Linked List")
        
        st.markdown("""
        <div class="concept-box">
            <p><strong>Singly Linked List</strong> is the simplest form where each node points to the next node, 
            and the last node points to NULL.</p>
            
            <h4>Characteristics:</h4>
            <ul>
                <li>Each node has one pointer to the next node</li>
                <li>Traversal is possible in only one direction (forward)</li>
                <li>Last node points to NULL</li>
                <li>Memory efficient compared to doubly linked lists</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="detail-box">
            <h3>Detailed Explanation:</h3>
            <p>In a singly linked list, each node contains data and a pointer to the next node in the sequence. 
            The list is traversed starting from the head node, following the next pointers until reaching NULL.</p>
            
            <p><strong>Key Operations:</strong></p>
            <ul>
                <li><strong>Insertion:</strong> Can be done at the beginning, end, or middle of the list</li>
                <li><strong>Deletion:</strong> Removing nodes requires updating the previous node's next pointer</li>
                <li><strong>Traversal:</strong> Visiting each node sequentially from head to tail</li>
                <li><strong>Search:</strong> Finding a node requires traversing the list until found</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        fig_singly = draw_singly_linked_list()
        st.pyplot(fig_singly)
        plt.close(fig_singly)
        
        # Interactive demo
        st.subheader("🎮 Interactive Demo")
        
        # Initialize session state for singly linked list
        if 'singly_list' not in st.session_state:
            st.session_state.singly_list = ['A', 'B', 'C']
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            new_element = st.text_input("Add element:", key="singly_add")
            if st.button("Add to End", key="singly_add_btn"):
                if new_element:
                    st.session_state.singly_list.append(new_element)
                    st.success(f"Added '{new_element}' to the list!")
        
        with col2:
            if st.button("Remove Last", key="singly_remove_btn"):
                if st.session_state.singly_list:
                    removed = st.session_state.singly_list.pop()
                    st.success(f"Removed '{removed}' from the list!")
                else:
                    st.warning("List is empty!")
        
        with col3:
            if st.button("Clear List", key="singly_clear_btn"):
                st.session_state.singly_list = []
                st.success("List cleared!")
        
        if st.session_state.singly_list:
            st.write("**Current List:**", " → ".join(st.session_state.singly_list) + " → NULL")
        else:
            st.write("**Current List:** Empty")
        
        # Code example
        st.subheader("💻 Implementation Example")
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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
        """, language="python")
    
    with tab2:
        st.subheader("Doubly Linked List")
        
        st.markdown("""
        <div class="concept-box">
            <p><strong>Doubly Linked List</strong> is a more complex structure where each node has two pointers: 
            one pointing to the next node and another pointing to the previous node.</p>
            
            <h4>Characteristics:</h4>
            <ul>
                <li>Each node has two pointers: next and previous</li>
                <li>Bidirectional traversal (forward and backward)</li>
                <li>First node's previous pointer is NULL</li>
                <li>Last node's next pointer is NULL</li>
                <li>More memory overhead due to extra pointer</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="detail-box">
            <h3>Detailed Explanation:</h3>
            <p>In a doubly linked list, each node contains data, a pointer to the next node, and a pointer to the previous node. 
            This allows traversal in both directions, making some operations more efficient.</p>
            
            <p><strong>Advantages over Singly Linked List:</strong></p>
            <ul>
                <li>Can be traversed in both directions</li>
                <li>Easier deletion of nodes (don't need to track previous node)</li>
                <li>Better for certain algorithms that require backward traversal</li>
            </ul>
            
            <p><strong>Disadvantages:</strong></p>
            <ul>
                <li>Requires more memory for the extra pointer</li>
                <li>Operations are slightly more complex to implement</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        fig_doubly = draw_doubly_linked_list()
        st.pyplot(fig_doubly)
        plt.close(fig_doubly)
        
        # Interactive demo for doubly linked list
        st.subheader("🎮 Interactive Demo")
        
        if 'doubly_list' not in st.session_state:
            st.session_state.doubly_list = ['X', 'Y', 'Z']
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            new_element_d = st.text_input("Add element:", key="doubly_add")
            if st.button("Add to End", key="doubly_add_btn"):
                if new_element_d:
                    st.session_state.doubly_list.append(new_element_d)
                    st.success(f"Added '{new_element_d}' to the list!")
        
        with col2:
            if st.button("Add to Start", key="doubly_prepend_btn"):
                if new_element_d:
                    st.session_state.doubly_list.insert(0, new_element_d)
                    st.success(f"Added '{new_element_d}' to the start!")
        
        with col3:
            if st.button("Remove Last", key="doubly_remove_btn"):
                if st.session_state.doubly_list:
                    removed = st.session_state.doubly_list.pop()
                    st.success(f"Removed '{removed}' from the list!")
                else:
                    st.warning("List is empty!")
        
        with col4:
            if st.button("Clear List", key="doubly_clear_btn"):
                st.session_state.doubly_list = []
                st.success("List cleared!")
        
        if st.session_state.doubly_list:
            forward = " ⇄ ".join(st.session_state.doubly_list)
            st.write(f"**Forward:** NULL ← {forward} → NULL")
            st.write(f"**Backward:** NULL → {' ← '.join(reversed(st.session_state.doubly_list))} ← NULL")
        else:
            st.write("**Current List:** Empty")
        
        # Code example
        st.subheader("💻 Implementation Example")
        st.code("""
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
    
    def prepend(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
    
    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements
        """, language="python")
    
    with tab3:
        st.subheader("Circular Linked List")
        
        st.markdown("""
        <div class="concept-box">
            <p><strong>Circular Linked List</strong> is a variation where the last node points back to the first node, 
            forming a circle. This can be implemented with both singly and doubly linked structures.</p>
            
            <h4>Characteristics:</h4>
            <ul>
                <li>Last node points to the first node (no NULL at the end)</li>
                <li>Can traverse the entire list from any starting point</li>
                <li>Useful for round-robin scheduling</li>
                <li>Can be singly or doubly circular</li>
                <li>Need to be careful to avoid infinite loops</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="detail-box">
            <h3>Detailed Explanation:</h3>
            <p>In a circular linked list, the last node points back to the first node instead of to NULL. 
            This creates a circular structure that can be traversed indefinitely.</p>
            
            <p><strong>Types of Circular Linked Lists:</strong></p>
            <ul>
                <li><strong>Singly Circular:</strong> Each node has a next pointer, and the last node points to the first</li>
                <li><strong>Doubly Circular:</strong> Each node has next and previous pointers, forming a bidirectional circle</li>
            </ul>
            
            <p><strong>Common Use Cases:</strong></p>
            <ul>
                <li>Round-robin scheduling in operating systems</li>
                <li>Implementing circular buffers</li>
                <li>Multiplayer games where players take turns</li>
                <li>Applications that require repeated cycling through elements</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        fig_circular = draw_circular_linked_list()
        st.pyplot(fig_circular)
        plt.close(fig_circular)
        
        # Interactive demo for circular linked list
        st.subheader("🎮 Interactive Demo")
        
        if 'circular_list' not in st.session_state:
            st.session_state.circular_list = ['1', '2', '3', '4']
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            new_element_c = st.text_input("Add element:", key="circular_add")
            if st.button("Add to Circle", key="circular_add_btn"):
                if new_element_c:
                    st.session_state.circular_list.append(new_element_c)
                    st.success(f"Added '{new_element_c}' to the circle!")
        
        with col2:
            if st.button("Remove Last", key="circular_remove_btn"):
                if st.session_state.circular_list:
                    removed = st.session_state.circular_list.pop()
                    st.success(f"Removed '{removed}' from the circle!")
                else:
                    st.warning("Circle is empty!")
        
        with col3:
            if st.button("Reset Circle", key="circular_reset_btn"):
                st.session_state.circular_list = ['1', '2', '3', '4']
                st.success("Circle reset to default!")
        
        if st.session_state.circular_list:
            circular_display = " → ".join(st.session_state.circular_list)
            st.write(f"**Circular Path:** {circular_display} → {st.session_state.circular_list[0]} → ...")
            st.info(f"💡 The list continues infinitely: {circular_display} → {circular_display} → ...")
        else:
            st.write("**Current Circle:** Empty")
        
        # Traversal demonstration
        if st.session_state.circular_list:
            st.subheader("🔄 Traversal Demo")
            start_from = st.selectbox("Start traversal from:", st.session_state.circular_list)
            steps = st.slider("Number of steps:", 1, 15, 8)
            
            if st.button("Show Traversal Path"):
                start_idx = st.session_state.circular_list.index(start_from)
                path = []
                for i in range(steps):
                    current_idx = (start_idx + i) % len(st.session_state.circular_list)
                    path.append(st.session_state.circular_list[current_idx])
                
                st.write("**Traversal Path:**", " → ".join(path))
        
        # Code example
        st.subheader("💻 Implementation Example")
        st.code("""
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Point to itself
        else:
            # Find the last node (the one pointing to head)
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Insert new node
            current.next = new_node
            new_node.next = self.head
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Update connections
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        
        # If only one node
        if self.head.next == self.head and self.head.data == data:
            self.head = None
            return
        
        # If head needs to be deleted
        if self.head.data == data:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        
        # Delete from middle or end
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self, limit=10):
        if not self.head:
            return []
        
        elements = []
        current = self.head
        count = 0
        while count < limit:
            elements.append(current.data)
            current = current.next
            count += 1
            if current == self.head and count > 1:
                elements.append("...")
                break
        return elements
        """, language="python")
    
    # Summary section
    st.markdown("---")
    st.subheader("📊 Types Comparison Summary")
    
    comparison_data = {
        "Type": ["Singly Linked", "Doubly Linked", "Circular Singly", "Circular Doubly"],
        "Traversal": ["One direction", "Both directions", "One direction (circular)", "Both directions (circular)"],
        "Memory per Node": ["Data + 1 pointer", "Data + 2 pointers", "Data + 1 pointer", "Data + 2 pointers"],
        "Last Node Points To": ["NULL", "NULL", "First node", "First node"],
        "Use Cases": [
            "Simple lists, stacks",
            "Navigation, undo/redo",
            "Round-robin, games",
            "Advanced navigation"
        ]
    }
    
    st.table(comparison_data)
    
    st.markdown("""
    <div class="highlight-box">
        <h4>🎯 When to Use Each Type:</h4>
        <ul>
            <li><strong>Singly Linked:</strong> When you only need forward traversal and want to minimize memory usage</li>
            <li><strong>Doubly Linked:</strong> When you need efficient backward traversal (browsers, text editors)</li>
            <li><strong>Circular:</strong> When you need to cycle through elements continuously (task scheduling, games)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif current_section == "operations":
    st.markdown('<h2 class="section-header">⚡ Operations & Algorithms</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
        <p>Linked lists support various operations that allow manipulation of the data structure. 
        Understanding these operations is crucial for effective use of linked lists.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual representation of operations
    st.subheader("📊 Common Operations Visualization")
    fig_ops = draw_linked_list_operations()
    st.pyplot(fig_ops)
    plt.close(fig_ops)
    
    # Detailed explanations of operations
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>🔍 Search Operation</h4>
            <p><strong>Time Complexity:</strong> O(n)</p>
            <p>To find a node with specific data:</p>
            <ol>
                <li>Start from the head node</li>
                <li>Traverse through each node</li>
                <li>Compare each node's data with target value</li>
                <li>Return node if found, else NULL</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🗑️ Deletion Operation</h4>
            <p><strong>Time Complexity:</strong> O(1) for head, O(n) for arbitrary node</p>
            <p>To delete a node:</p>
            <ol>
                <li>Find the node to delete</li>
                <li>Update the previous node's next pointer</li>
                <li>Free the memory of the deleted node</li>
                <li>Special case: deleting head node</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>📝 Insertion Operation</h4>
            <p><strong>Time Complexity:</strong> O(1) for head, O(n) for arbitrary position</p>
            <p>Three types of insertion:</p>
            <ol>
                <li><strong>At beginning:</strong> Update head pointer</li>
                <li><strong>At end:</strong> Traverse to last node, update its next pointer</li>
                <li><strong>At middle:</strong> Find position, update surrounding pointers</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🔄 Traversal Operation</h4>
            <p><strong>Time Complexity:</strong> O(n)</p>
            <p>To visit all nodes:</p>
            <ol>
                <li>Start from the head node</li>
                <li>Follow next pointers until NULL</li>
                <li>Perform operation on each node</li>
                <li>Stop when NULL is reached</li>
            </ol>
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
        
        st.markdown("""
        <div class="highlight-box">
            <h4>🎵 Music/Video Players</h4>
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
            <h4>🗃️ Hash Tables</h4>
            <p>Linked lists are used to handle collisions in hash table implementations.</p>
            
            <p><strong>How it works:</strong></p>
            <ul>
                <li>Each bucket in hash table is a linked list</li>
                <li>Items with same hash are stored in same list</li>
                <li>Efficient handling of collisions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <h4>⚙️ Operating Systems</h4>
            <p>Linked lists are used in various OS components like process scheduling and file systems.</p>
            
            <p><strong>Applications:</strong></p>
            <ul>
                <li>Process control blocks management</li>
                <li>File directory structures</li>
                <li>Memory page management</li>
                <li>I/O buffer management</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Interview questions section
    st.markdown("---")
    st.subheader("💼 Common Interview Questions")
    
    st.markdown("""
    <div class="node-structure">
        <p>Linked lists are a common topic in technical interviews. Here are some frequently asked questions:</p>
        
        <ol>
            <li>Reverse a linked list</li>
            <li>Detect cycle in a linked list</li>
            <li>Find the middle element of a linked list</li>
            <li>Merge two sorted linked lists</li>
            <li>Remove nth node from end of list</li>
            <li>Add two numbers represented as linked lists</li>
            <li>Intersection point of two linked lists</li>
            <li>Palindrome linked list</li>
            <li>LRU Cache implementation</li>
            <li>Flatten a multilevel doubly linked list</li>
        </ol>
        
        <p><strong>Tips for linked list interviews:</strong></p>
        <ul>
            <li>Always handle edge cases (empty list, single node list)</li>
            <li>Use two-pointer technique for many problems</li>
            <li>Draw diagrams to visualize pointer changes</li>
            <li>Consider recursive solutions for some problems</li>
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

import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx
import io
from PIL import Image
import sys
from io import StringIO
import contextlib
import pandas as pd
import time
import random
import math

try:
    from quiz_config import QUIZ_QUESTIONS, CODING_CHALLENGES, TIME_CHALLENGES
except ImportError:
    # Fallback quiz data if quiz_config.py is not found
    QUIZ_QUESTIONS = [
        {
            "question": "What is the time complexity of inserting an element at the beginning of a singly linked list?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
            "correct": 0,
            "explanation": "Inserting at the beginning requires only updating the head pointer, which is O(1) time.",
            "difficulty": "easy",
            "points": 10
        },
        {
            "question": "In a doubly linked list, each node contains:",
            "options": ["Only data", "Data and one pointer", "Data and two pointers", "Data and three pointers"],
            "correct": 2,
            "explanation": "Doubly linked list nodes contain data, a previous pointer, and a next pointer.",
            "difficulty": "easy",
            "points": 10
        }
    ]
    
    CODING_CHALLENGES = [
        {
            "title": "Reverse a Linked List",
            "difficulty": "easy",
            "points": 50,
            "description": "Write a function to reverse a singly linked list.",
            "starter_code": "def reverse_linked_list(head):\n    # Your code here\n    pass",
            "solution": "def reverse_linked_list(head):\n    prev = None\n    current = head\n    while current:\n        next_node = current.next\n        current.next = prev\n        prev = current\n        current = next_node\n    return prev",
            "test_cases": [{"input": "[1,2,3,4,5]", "expected": "[5,4,3,2,1]"}]
        }
    ]
    
    TIME_CHALLENGES = [
        {
            "title": "Quick Quiz: Basic Operations",
            "time_limit": 60,
            "questions": [0, 1],
            "bonus_points": 20
        }
    ]

try:
    from linked_list_classes import Node, SinglyLinkedList, DoublyLinkedList, CircularLinkedList
except ImportError:
    st.error("linked_list_classes.py not found. Please ensure the file exists.")
    st.stop()

# Set page config
st.set_page_config(
    page_title="Linked List Data Structures",
    layout="wide",
    page_icon="🔗",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS for Modern UI/UX
st.markdown("""
<style>
    :root {
        --primary-blue: #4A90E2;
        --primary-purple: #6A1B9A;
        --success-green: #4CAF50;
        --warning-yellow: #FFC107;
        --error-red: #F44336;
        --text-primary: #2C3E50;
        --text-secondary: #7F8C8D;
        --bg-primary: #FFFFFF;
        --bg-secondary: #F8F9FA;
    }
    
    .stApp {
        background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .section-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .feature-card {
        background: linear-gradient(135deg, #4A90E2 0%, #6A1B9A 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.75rem;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4A90E2 0%, #6A1B9A 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
def initialize_session_state():
    """Initialize all session state variables"""
    defaults = {
        'username': "Guest",
        'user_score': 0,
        'achievements': [],
        'bookmarks': [],
        'notes': {},
        'progress': {},
        'leaderboard': [],
        'quiz_attempts': 0,
        'correct_answers': 0,
        'coding_challenge_score': 0,
        'time_challenge_best': {}
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

# Helper functions
def save_progress(section):
    """Save progress for a section"""
    st.session_state.progress[section] = True

def add_bookmark(section):
    """Add a bookmark for a section"""
    if section not in st.session_state.bookmarks:
        st.session_state.bookmarks.append(section)

def save_note(section, note):
    """Save a note for a section"""
    st.session_state.notes[section] = {
        'text': note,
        'timestamp': pd.Timestamp.now()
    }

def check_achievements():
    """Check for various achievements and update session state"""
    try:
        achievements_to_check = [
            ("🎯 First Correct Answer", st.session_state.correct_answers >= 1),
            ("🔥 5 Correct Answers", st.session_state.correct_answers >= 5),
            ("💯 Perfect Score", st.session_state.quiz_score == len(QUIZ_QUESTIONS)),
            ("⚡ Speed Demon", st.session_state.user_score >= 100),
            ("🧠 Knowledge Seeker", st.session_state.quiz_attempts >= 10),
        ]
        
        for achievement, condition in achievements_to_check:
            if condition and achievement not in st.session_state.achievements:
                st.session_state.achievements.append(achievement)
                st.balloons()
    except Exception as e:
        st.error(f"Error checking achievements: {str(e)}")

# Enhanced Welcome/Dashboard section
def welcome_dashboard():
    """Main welcome dashboard with modern UI"""
    st.markdown('<h1 style="text-align: center; color: #2C3E50; margin-bottom: 2rem;">🔗 Linked List Data Structures</h1>', unsafe_allow_html=True)
    save_progress("Welcome")

    st.markdown("""
    <div class="section-card">
    <h2 style="text-align: center; margin-bottom: 1rem;">Welcome to Your Interactive Learning Journey!</h2>
    <p style="font-size: 1.2em; text-align: center; margin-bottom: 1rem;">
    Master linked lists through interactive visualizations, hands-on practice, and comprehensive analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
        <h3>Learn</h3>
        <p>Comprehensive guide to singly, doubly, and circular linked lists</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🎮</div>
        <h3>Practice</h3>
        <p>Interactive playground with real-time operations</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
        <h3>Analyze</h3>
        <p>Performance comparisons and optimization tips</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
        <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
        <h3>Solve</h3>
        <p>Practice problems with detailed solutions</p>
        </div>
        """, unsafe_allow_html=True)

# Main navigation
def main():
    """Main application function"""
    try:
        initialize_session_state()
        
        # Sidebar navigation
        st.sidebar.markdown("""
        <div style="text-align: center; padding: 2rem 1rem; margin-bottom: 2rem; background: linear-gradient(135deg, #4A90E2 0%, #6A1B9A 100%); border-radius: 15px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔗</div>
            <h2 style="margin: 0; font-size: 1.25rem;">Linked Lists</h2>
            <p style="font-size: 0.875rem; margin: 0.5rem 0;">Interactive Learning Hub</p>
        </div>
        """, unsafe_allow_html=True)
        
        menu_options = [
            "🏠 Welcome",
            "📖 Introduction", 
            "🔗 Types of Lists",
            "⚙️ Operations",
            "🎮 Interactive Playground",
            "📊 Performance Analysis",
            "💡 Practice Problems",
            "🎯 Gamified Quiz",
            "🎨 Advanced Visualizations",
            "📝 Interview Prep",
            "📚 References"
        ]
        
        selected = st.sidebar.selectbox("Navigation Menu", menu_options)
        
        # User profile in sidebar
        with st.sidebar.expander("👤 Profile", expanded=False):
            st.write(f"**Username:** {st.session_state.username}")
            st.write(f"**Score:** {st.session_state.user_score}")
            st.write(f"**Achievements:** {len(st.session_state.achievements)}")
        
        # Route to appropriate section
        if selected == "🏠 Welcome":
            welcome_dashboard()
        elif selected == "📖 Introduction":
            introduction()
        elif selected == "🔗 Types of Lists":
            types_of_linked_lists()
        elif selected == "⚙️ Operations":
            operations_and_algorithms()
        elif selected == "🎮 Interactive Playground":
            interactive_playground()
        elif selected == "📊 Performance Analysis":
            performance_analysis()
        elif selected == "💡 Practice Problems":
            practice_problems()
        elif selected == "🎯 Gamified Quiz":
            interactive_quiz()
        elif selected == "🎨 Advanced Visualizations":
            advanced_visualizations()
        elif selected == "📝 Interview Prep":
            interview_preparation()
        elif selected == "📚 References":
            references_and_resources()
            
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.info("Please refresh the page and try again.")

# Introduction section
def introduction():
    """Introduction to linked lists"""
    st.title("📖 Introduction to Linked Lists")
    save_progress("Introduction")
    
    st.markdown("""
    <div class="section-card">
    <h2>What is a Linked List?</h2>
    <p><strong>A linked list is a fundamental data structure that consists of a sequence of elements called nodes.</strong></p>
    <p>Each node contains two parts:</p>
    <ul>
    <li><strong>Data</strong>: The actual information stored in the node</li>
    <li><strong>Reference/Pointer</strong>: A link to the next node in the sequence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.header("Basic Node Structure")
    st.code("""
class Node:
    def __init__(self, data):
        self.data = data        # The actual data stored in the node
        self.next = None        # Pointer to the next node (None if last node)
    """, language="python")

# Types of Linked Lists section
def types_of_linked_lists():
    """Types of linked lists explanation"""
    st.title("🔗 Types of Linked Lists")
    save_progress("Types")

    st.header("1. Singly Linked List")
    st.markdown("**Overview:** The most basic form of linked list where each node points only to the next node.")
    
    st.code("""
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    """, language="python")

    st.header("2. Doubly Linked List")
    st.markdown("**Overview:** Each node has pointers to both previous and next nodes, enabling bidirectional traversal.")
    
    st.header("3. Circular Linked List")
    st.markdown("**Overview:** The last node points back to the first node, forming a circle.")

# Operations section
def operations_and_algorithms():
    """Operations and algorithms section"""
    st.title("⚙️ Operations and Algorithms")
    save_progress("Operations")

    st.header("1. Insertion Operations")
    st.subheader("Insert at Beginning")
    st.code("""
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # New head
    """, language="python")

    st.header("2. Deletion Operations")
    st.subheader("Delete from Beginning")
    st.code("""
def delete_from_beginning(head):
    if head is None:
        return None, head
    deleted_data = head.data
    new_head = head.next
    return deleted_data, new_head
    """, language="python")

# Interactive Playground section
def interactive_playground():
    """Interactive playground for linked lists"""
    st.title("🎮 Interactive Playground")
    save_progress("Playground")
    
    # Initialize session state for playground
    if 'list_type' not in st.session_state:
        st.session_state.list_type = "Singly Linked List"
    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = SinglyLinkedList()

    # List type selector
    list_types = ["Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    selected_type = st.selectbox("Choose list type:", list_types)

    if selected_type != st.session_state.list_type:
        st.session_state.list_type = selected_type
        if selected_type == "Singly Linked List":
            st.session_state.linked_list = SinglyLinkedList()
        elif selected_type == "Doubly Linked List":
            st.session_state.linked_list = DoublyLinkedList()
        elif selected_type == "Circular Linked List":
            st.session_state.linked_list = CircularLinkedList()

    # Create list interface
    st.header("Create Your Linked List")
    user_input = st.text_input("Enter comma-separated values (e.g., 1, 2, 3, 4)", "")
    
    if st.button("Create List"):
        if user_input:
            try:
                values = [x.strip() for x in user_input.split(",") if x.strip()]
                # Reset the list
                if st.session_state.list_type == "Singly Linked List":
                    st.session_state.linked_list = SinglyLinkedList()
                elif st.session_state.list_type == "Doubly Linked List":
                    st.session_state.linked_list = DoublyLinkedList()
                elif st.session_state.list_type == "Circular Linked List":
                    st.session_state.linked_list = CircularLinkedList()
                
                for val in values:
                    st.session_state.linked_list.insert_at_end(val)
                st.success(f"{st.session_state.list_type} created with {len(values)} elements!")
            except Exception as e:
                st.error(f"Error creating list: {str(e)}")
        else:
            st.warning("Please enter some values.")

    # Display current list
    st.header(f"Current {st.session_state.list_type}")
    if hasattr(st.session_state.linked_list, 'size') and st.session_state.linked_list.size > 0:
        try:
            if st.session_state.list_type == "Doubly Linked List":
                elements = st.session_state.linked_list.traverse_forward()
                st.write("Forward: ", elements)
                st.write("Backward: ", st.session_state.linked_list.traverse_backward())
            else:
                elements = st.session_state.linked_list.traverse()
                st.write("Elements: ", elements)
            st.write(f"Length: {st.session_state.linked_list.size}")
        except Exception as e:
            st.error(f"Error displaying list: {str(e)}")
    else:
        st.info("No list created yet. Use the input above to create one!")

# Performance Analysis section
def performance_analysis():
    """Performance analysis section"""
    st.title("📊 Performance Analysis")
    save_progress("Analysis")

    st.header("Time Complexity Comparison")
    
    # Create comparison data
    operations = [
        'Insert at Beginning',
        'Insert at End',
        'Delete from Beginning',
        'Delete from End',
        'Search by Value',
        'Traversal'
    ]

    complexity_data = {
        'Operation': operations,
        'Singly Linked List': ['O(1)', 'O(n)', 'O(1)', 'O(n)', 'O(n)', 'O(n)'],
        'Doubly Linked List': ['O(1)', 'O(1)*', 'O(1)', 'O(1)*', 'O(n)', 'O(n)'],
        'Array': ['O(n)', 'O(1)', 'O(n)', 'O(1)', 'O(n)', 'O(n)']
    }

    df = pd.DataFrame(complexity_data)
    st.dataframe(df, use_container_width=True)
    st.caption("*Requires tail pointer for O(1) end operations")

# Practice Problems section
def practice_problems():
    """Practice problems section"""
    st.title("💡 Practice Problems")
    save_progress("Practice")

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

# Interactive Quiz section
def interactive_quiz():
    """Interactive quiz section"""
    st.title("🎯 Gamified Quiz")
    save_progress("Quiz")
    
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    if st.session_state.current_question < len(QUIZ_QUESTIONS):
        q = QUIZ_QUESTIONS[st.session_state.current_question]
        
        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(q["question"])
        
        user_answer = st.radio("Select your answer:", q["options"], 
                              key=f"q_{st.session_state.current_question}")
        
        if st.button("Submit Answer"):
            selected_index = q["options"].index(user_answer)
            if selected_index == q["correct"]:
                st.success("✅ Correct!")
                st.session_state.quiz_score += 1
                st.session_state.correct_answers += 1
                check_achievements()
            else:
                st.error(f"❌ Incorrect. The correct answer is: {q['options'][q['correct']]}")
            
            st.info(f"💡 {q['explanation']}")
            st.session_state.quiz_attempts += 1
        
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.success("🎊 Quiz Completed!")
        score_percentage = (st.session_state.quiz_score / len(QUIZ_QUESTIONS)) * 100
        st.write(f"**Final Score:** {st.session_state.quiz_score}/{len(QUIZ_QUESTIONS)} ({score_percentage:.1f}%)")
        
        if st.button("Restart Quiz"):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.rerun()

# Advanced Visualizations section
def advanced_visualizations():
    """Advanced visualizations section"""
    st.title("🎨 Advanced Visualizations")
    save_progress("Advanced Viz")
    
    st.header("3D Linked List Visualization")
    
    # Create a simple 3D visualization
    elements = [10, 20, 30, 40, 50]
    
    fig = go.Figure()
    
    # Add nodes
    node_x = [i * 3 for i in range(len(elements))]
    node_y = [0] * len(elements)
    node_z = [0] * len(elements)
    
    fig.add_trace(go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers+text',
        marker=dict(size=20, color='#4A90E2'),
        text=[str(val) for val in elements],
        textposition="middle center",
        name="Nodes"
    ))
    
    # Add connections
    for i in range(len(elements) - 1):
        fig.add_trace(go.Scatter3d(
            x=[node_x[i], node_x[i+1]],
            y=[node_y[i], node_y[i+1]],
            z=[node_z[i], node_z[i+1]],
            mode='lines',
            line=dict(color='#FF6B6B', width=8),
            showlegend=False
        ))
    
    fig.update_layout(
        title="3D Singly Linked List Visualization",
        scene=dict(
            xaxis_title="Position",
            yaxis_title="Y",
            zaxis_title="Z"
        ),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Interview Preparation section
def interview_preparation():
    """Interview preparation section"""
    st.title("📝 Interview Preparation")
    save_progress("Interview Prep")
    
    st.header("Common Interview Questions")
    
    st.subheader("1. Reverse a Linked List")
    st.markdown("""
    **Question:** How would you reverse a singly linked list?
    
    **Approach:** Use three pointers - previous, current, and next.
    """)
    
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
    """, language="python")
    
    st.subheader("2. Detect Cycle in Linked List")
    st.markdown("""
    **Question:** How do you detect if a linked list has a cycle?
    
    **Approach:** Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    """)
    
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
    """, language="python")

# References section
def references_and_resources():
    """References and resources section"""
    st.title("📚 References and Resources")
    
    st.markdown("""
    ## Learning Resources
    - [GeeksforGeeks - Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
    - [Wikipedia - Linked List](https://en.wikipedia.org/wiki/Linked_list)
    - [Visualgo - Linked List](https://visualgo.net/en/list)
    
    ## Practice Platforms
    - [LeetCode](https://leetcode.com/tag/linked-list/)
    - [HackerRank](https://www.hackerrank.com/domains/data-structures/linked-lists)
    - [CodeChef](https://www.codechef.com/)
    
    ## Books
    - "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
    - "Data Structures and Algorithms in Python" by Goodrich, Tamassia, and Goldwasser
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.info("Please refresh the page and try again.")

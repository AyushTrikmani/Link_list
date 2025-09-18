import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import time
import random

# Set page config
st.set_page_config(
    page_title="Linked List Data Structures",
    layout="wide",
    page_icon="🔗",
    initial_sidebar_state="expanded"
)

# Modern, soft UI/UX CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Remove default padding */
    .main .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
        max-width: 1200px;
    }
    
    /* Global styling */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Dark mode */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 100%);
        }
    }
    
    /* Headers */
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 0 0 2rem 0;
        padding: 1rem 0;
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Cards with glassmorphism */
    .section-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: all 0.3s ease;
    }
    
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 45px 0 rgba(31, 38, 135, 0.5);
    }
    
    @media (prefers-color-scheme: dark) {
        .section-card {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #e2e8f0;
        }
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.75rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    /* Timeline */
    .timeline-content {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .timeline-content:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
    }
    
    @media (prefers-color-scheme: dark) {
        .timeline-content {
            background: rgba(255, 255, 255, 0.1);
            color: #e2e8f0;
            border-left-color: #8b5cf6;
        }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    @media (prefers-color-scheme: dark) {
        .stTextInput > div > div > input {
            background: rgba(255, 255, 255, 0.1);
            color: #e2e8f0;
            border-color: rgba(139, 92, 246, 0.3);
        }
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 12px;
    }
    
    @media (prefers-color-scheme: dark) {
        .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(139, 92, 246, 0.3);
        }
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
        backdrop-filter: blur(10px);
    }
    
    @media (prefers-color-scheme: dark) {
        .css-1d391kg {
            background: linear-gradient(180deg, rgba(26, 32, 44, 0.95) 0%, rgba(45, 55, 72, 0.95) 100%);
        }
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    /* Metrics */
    .metric-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.75rem;
        box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(79, 172, 254, 0.4);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: #2d3748;
        font-weight: 600;
    }
    
    p, li, span {
        color: #4a5568;
        line-height: 1.6;
    }
    
    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 {
            color: #f7fafc;
        }
        
        p, li, span {
            color: #e2e8f0;
        }
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .section-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .feature-card {
            padding: 1rem;
            margin: 0.5rem;
        }
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        border-radius: 12px;
        border: none;
    }
    
    .stError {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        border-radius: 12px;
        border: none;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        border-radius: 12px;
        border: none;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
        border-radius: 12px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'username' not in st.session_state:
    st.session_state.username = "Guest"
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'progress' not in st.session_state:
    st.session_state.progress = {}

def save_progress(section):
    st.session_state.progress[section] = True

def welcome_dashboard():
    st.markdown('<h1 class="main-header">🔗 Linked List Data Structures</h1>', unsafe_allow_html=True)
    save_progress("Welcome")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="text-align: center; margin-bottom: 1.5rem; color: #667eea;">Welcome to Your Interactive Learning Journey!</h2>
    <p style="font-size: 1.2em; text-align: center; margin-bottom: 2rem; opacity: 0.8;">
    Master linked lists through interactive visualizations, hands-on practice, and comprehensive analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>📚 Learn</h3>
        <p>Comprehensive guide to all types of linked lists</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🎮 Practice</h3>
        <p>Interactive playground with real-time visualization</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>📊 Analyze</h3>
        <p>Performance comparisons and optimization tips</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
        <h3>💡 Solve</h3>
        <p>Practice problems with detailed solutions</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #667eea; margin-bottom: 1.5rem;">🎯 Learning Path</h3>
    <div style="margin: 1.5rem 0;">
    <div class="timeline-content">
    <h5 style="color: #667eea;">📖 Introduction</h5>
    <p>Learn the fundamentals of linked lists and their applications</p>
    </div>
    <div class="timeline-content">
    <h5 style="color: #667eea;">🔗 Types</h5>
    <p>Explore singly, doubly, and circular linked lists</p>
    </div>
    <div class="timeline-content">
    <h5 style="color: #667eea;">⚙️ Operations</h5>
    <p>Master insertion, deletion, traversal, and advanced algorithms</p>
    </div>
    <div class="timeline-content">
    <h5 style="color: #667eea;">🎮 Playground</h5>
    <p>Practice with interactive visualizations and live coding</p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h3 style="margin: 0; font-size: 2rem;">3</h3>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Data Structures</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h3 style="margin: 0; font-size: 2rem;">8+</h3>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Operations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h3 style="margin: 0; font-size: 2rem;">10+</h3>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Practice Problems</p>
        </div>
        """, unsafe_allow_html=True)

def introduction():
    st.markdown('<h1 class="main-header">📖 Introduction to Linked Lists</h1>', unsafe_allow_html=True)
    save_progress("Introduction")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">What is a Linked List?</h2>
    <p style="font-size: 1.1em; margin-bottom: 1.5rem;">
    A linked list is a fundamental data structure that consists of a sequence of elements called nodes.
    Unlike arrays, linked lists store elements in non-contiguous memory locations.
    </p>
    <h3 style="color: #764ba2;">Each node contains:</h3>
    <ul style="font-size: 1.05em; line-height: 1.8;">
    <li><strong>Data</strong>: The actual information stored in the node</li>
    <li><strong>Reference/Pointer</strong>: A link to the next node in the sequence</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="section-card">
        <h3 style="color: #48bb78;">✅ Advantages</h3>
        <ul>
        <li>Dynamic size allocation</li>
        <li>Efficient insertion/deletion</li>
        <li>No memory waste</li>
        <li>Flexible structure</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
        <h3 style="color: #f56565;">❌ Disadvantages</h3>
        <ul>
        <li>No random access</li>
        <li>Extra memory for pointers</li>
        <li>Sequential access only</li>
        <li>Poor cache performance</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def types_of_linked_lists():
    st.markdown('<h1 class="main-header">🔗 Types of Linked Lists</h1>', unsafe_allow_html=True)
    save_progress("Types")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">1. Singly Linked List</h2>
    <p>The most basic form where each node points only to the next node.</p>
    <p><strong>Use Cases:</strong> Stacks, simple queues, undo functionality</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">2. Doubly Linked List</h2>
    <p>Each node has pointers to both previous and next nodes, enabling bidirectional traversal.</p>
    <p><strong>Use Cases:</strong> Browser history, LRU cache, deques</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">3. Circular Linked List</h2>
    <p>The last node points back to the first node, forming a circle.</p>
    <p><strong>Use Cases:</strong> Round-robin scheduling, circular buffers, multiplayer games</p>
    </div>
    """, unsafe_allow_html=True)

def operations_and_algorithms():
    st.markdown('<h1 class="main-header">⚙️ Operations and Algorithms</h1>', unsafe_allow_html=True)
    save_progress("Operations")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">Basic Operations</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
    <div style="padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 8px;">
    <h4 style="color: #667eea;">Insertion</h4>
    <p>Add new nodes at beginning, end, or specific position</p>
    </div>
    <div style="padding: 1rem; background: rgba(118, 75, 162, 0.1); border-radius: 8px;">
    <h4 style="color: #764ba2;">Deletion</h4>
    <p>Remove nodes from any position in the list</p>
    </div>
    <div style="padding: 1rem; background: rgba(72, 187, 120, 0.1); border-radius: 8px;">
    <h4 style="color: #48bb78;">Traversal</h4>
    <p>Visit all nodes in sequence</p>
    </div>
    <div style="padding: 1rem; background: rgba(237, 137, 54, 0.1); border-radius: 8px;">
    <h4 style="color: #ed8936;">Searching</h4>
    <p>Find specific values or positions</p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

def interactive_playground():
    st.markdown('<h1 class="main-header">🎮 Interactive Playground</h1>', unsafe_allow_html=True)
    save_progress("Playground")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">Create Your Linked List</h2>
    <p style="font-size: 1.1em; margin-bottom: 1.5rem;">
    Use the controls below to build and manipulate linked lists in real-time.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_input = st.text_input("Enter comma-separated values (e.g., 1, 2, 3, 4)", "")
    
    with col2:
        if st.button("Create List", use_container_width=True):
            if user_input:
                values = [x.strip() for x in user_input.split(",") if x.strip()]
                st.success(f"✅ Created linked list with {len(values)} elements!")
                st.write("**Elements:**", values)
                
                # Simple visualization
                if values:
                    viz_text = " → ".join(values) + " → NULL"
                    st.code(viz_text)

def performance_analysis():
    st.markdown('<h1 class="main-header">📊 Performance Analysis</h1>', unsafe_allow_html=True)
    save_progress("Analysis")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">Time Complexity Comparison</h2>
    <div style="overflow-x: auto; margin-top: 1.5rem;">
    <table style="width: 100%; border-collapse: collapse;">
    <thead>
    <tr style="background: rgba(102, 126, 234, 0.1);">
    <th style="padding: 1rem; text-align: left; border-bottom: 2px solid #667eea;">Operation</th>
    <th style="padding: 1rem; text-align: center; border-bottom: 2px solid #667eea;">Linked List</th>
    <th style="padding: 1rem; text-align: center; border-bottom: 2px solid #667eea;">Array</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="padding: 0.75rem; border-bottom: 1px solid rgba(102, 126, 234, 0.2);">Insert at Beginning</td>
    <td style="padding: 0.75rem; text-align: center; color: #48bb78; font-weight: bold;">O(1)</td>
    <td style="padding: 0.75rem; text-align: center; color: #f56565; font-weight: bold;">O(n)</td>
    </tr>
    <tr>
    <td style="padding: 0.75rem; border-bottom: 1px solid rgba(102, 126, 234, 0.2);">Insert at End</td>
    <td style="padding: 0.75rem; text-align: center; color: #f56565; font-weight: bold;">O(n)</td>
    <td style="padding: 0.75rem; text-align: center; color: #48bb78; font-weight: bold;">O(1)</td>
    </tr>
    <tr>
    <td style="padding: 0.75rem; border-bottom: 1px solid rgba(102, 126, 234, 0.2);">Search</td>
    <td style="padding: 0.75rem; text-align: center; color: #ed8936; font-weight: bold;">O(n)</td>
    <td style="padding: 0.75rem; text-align: center; color: #ed8936; font-weight: bold;">O(n)</td>
    </tr>
    <tr>
    <td style="padding: 0.75rem;">Access by Index</td>
    <td style="padding: 0.75rem; text-align: center; color: #f56565; font-weight: bold;">O(n)</td>
    <td style="padding: 0.75rem; text-align: center; color: #48bb78; font-weight: bold;">O(1)</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    """, unsafe_allow_html=True)

def practice_problems():
    st.markdown('<h1 class="main-header">💡 Practice Problems</h1>', unsafe_allow_html=True)
    save_progress("Practice")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">Problem 1: Reverse a Linked List</h2>
    <p><strong>Problem:</strong> Given the head of a singly linked list, reverse the list and return the reversed list.</p>
    <p><strong>Example:</strong></p>
    <ul>
    <li>Input: [1,2,3,4,5]</li>
    <li>Output: [5,4,3,2,1]</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("💡 Solution"):
        st.code("""
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# Time Complexity: O(n)
# Space Complexity: O(1)
        """, language="python")

def references_and_resources():
    st.markdown('<h1 class="main-header">📚 References and Resources</h1>', unsafe_allow_html=True)
    save_progress("References")
    
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #667eea;">Additional Learning Resources</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
    <div style="padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 8px;">
    <h4>📖 Documentation</h4>
    <ul>
    <li>GeeksforGeeks - Linked List</li>
    <li>Wikipedia - Linked List</li>
    <li>LeetCode Problems</li>
    </ul>
    </div>
    <div style="padding: 1rem; background: rgba(118, 75, 162, 0.1); border-radius: 8px;">
    <h4>🎥 Video Tutorials</h4>
    <ul>
    <li>MIT OpenCourseWare</li>
    <li>Khan Academy</li>
    <li>YouTube Tutorials</li>
    </ul>
    </div>
    <div style="padding: 1rem; background: rgba(72, 187, 120, 0.1); border-radius: 8px;">
    <h4>🛠️ Practice Platforms</h4>
    <ul>
    <li>LeetCode</li>
    <li>HackerRank</li>
    <li>CodeSignal</li>
    </ul>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.markdown('<style>.main .block-container { padding-top: 0 !important; }</style>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem; margin-bottom: 1rem;">
    <h2 style="color: #667eea; margin: 0;">🔗 Navigation</h2>
    <p style="color: #764ba2; font-size: 0.9em; margin: 0.5rem 0;">Interactive Learning Hub</p>
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
        "📚 References"
    ]
    
    selected = st.sidebar.selectbox("Choose a section:", menu_options)
    
    # User profile
    with st.sidebar.expander("👤 Profile"):
        st.write(f"**User:** {st.session_state.username}")
        st.write(f"**Score:** {st.session_state.user_score}")
    
    # Progress tracker
    with st.sidebar.expander("📈 Progress"):
        completed = len(st.session_state.progress)
        total = len(menu_options) - 1
        progress_pct = (completed / total) * 100 if total > 0 else 0
        st.progress(progress_pct / 100)
        st.write(f"{completed}/{total} sections completed ({progress_pct:.0f}%)")
    
    # Route to sections
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
    elif selected == "📚 References":
        references_and_resources()

if __name__ == "__main__":
    main()

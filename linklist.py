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
from quiz_config import QUIZ_QUESTIONS
from linked_list_classes import Node, SinglyLinkedList, DoublyLinkedList, CircularLinkedList

# Set page config
st.set_page_config(
    page_title="Linked List Data Structures",
    layout="wide",
    page_icon="🔗",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS for Modern UI/UX
st.markdown("""
<style>
    /* Modern Typography and Layout */
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out;
    }

    .section-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 2.5rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        border-left: 6px solid #1e3c72;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }

    .section-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #1e3c72, #2a5298, #667eea);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .section-card:hover::before {
        opacity: 1;
    }

    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 0.75rem;
        text-align: center;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }

    .feature-card::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.3s ease;
        opacity: 0;
    }

    .feature-card:hover::after {
        opacity: 1;
        animation: shimmer 1.5s ease-in-out;
    }

    /* Interactive Elements */
    .interactive-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .interactive-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(245, 87, 108, 0.3);
    }

    .code-block {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: #ecf0f1;
        border-left: 4px solid #1e3c72;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border-radius: 10px;
        position: relative;
        font-family: 'Fira Code', 'Monaco', 'Consolas', monospace;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .code-block::before {
        content: '💻';
        position: absolute;
        top: 10px;
        right: 15px;
        font-size: 1.2rem;
        opacity: 0.7;
    }

    .highlight-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border: 2px solid #2196f3;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        position: relative;
        animation: pulse 2s infinite;
    }

    .highlight-box::before {
        content: '💡';
        position: absolute;
        top: -10px;
        left: 20px;
        background: white;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Progress and Metrics */
    .progress-container {
        background: #f8f9fa;
        border-radius: 25px;
        padding: 3px;
        margin: 1rem 0;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .progress-bar {
        background: linear-gradient(90deg, #1e3c72, #667eea);
        height: 20px;
        border-radius: 22px;
        transition: width 1s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    .progress-bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shimmer 2s infinite;
    }

    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.75rem;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        position: relative;
    }

    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }

    .metric-card .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .metric-card .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Tab Enhancements */
    .tab-content {
        padding: 2rem 0;
        animation: fadeIn 0.5s ease-out;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 10px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(30, 60, 114, 0.4);
        transform: translateY(-2px);
    }

    .stTabs [aria-selected="true"]::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    /* Animation Keyframes */
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

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }

    /* Interactive Buttons */
    .modern-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }

    .modern-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }

    .modern-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }

    .modern-button:hover::before {
        left: 100%;
    }

    /* Enhanced Code Blocks */
    .code-container {
        position: relative;
        margin: 1.5rem 0;
    }

    .code-header {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 8px 8px 0 0;
        font-size: 0.9rem;
        font-weight: 600;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .code-content {
        background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
        color: #ecf0f1;
        padding: 1.5rem;
        border-radius: 0 0 8px 8px;
        font-family: 'Fira Code', 'Monaco', 'Consolas', monospace;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        position: relative;
    }

    .copy-button {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .copy-button:hover {
        background: rgba(255,255,255,0.2);
        transform: scale(1.05);
    }

    /* Visual Enhancements */
    .visual-diagram {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        position: relative;
    }

    .visual-diagram::before {
        content: '🎨';
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 1.5rem;
        opacity: 0.6;
    }

    /* Interactive Timeline */
    .timeline {
        position: relative;
        padding-left: 30px;
    }

    .timeline::before {
        content: '';
        position: absolute;
        left: 15px;
        top: 0;
        bottom: 0;
        width: 2px;
        background: linear-gradient(to bottom, #1e3c72, #667eea);
    }

    .timeline-item {
        position: relative;
        margin-bottom: 2rem;
        padding-left: 30px;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -22px;
        top: 8px;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e3c72, #667eea);
        box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.2);
    }

    .timeline-content {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #1e3c72;
    }

    /* Floating Action Elements */
    .floating-element {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        z-index: 1000;
    }

    .floating-element:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }

        .section-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }

        .feature-card {
            padding: 1.5rem;
            margin: 0.5rem;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            font-size: 0.9rem;
        }
    }

    /* Loading Animation */
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        border-top-color: white;
        animation: spin 1s ease-in-out infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* Success Animation */
    .success-checkmark {
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #4CAF50;
        position: relative;
    }

    .success-checkmark::after {
        content: '✓';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-weight: bold;
        animation: checkmark 0.5s ease-in-out;
    }

    @keyframes checkmark {
        0% { transform: translate(-50%, -50%) scale(0); }
        50% { transform: translate(-50%, -50%) scale(1.2); }
        100% { transform: translate(-50%, -50%) scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Welcome/Dashboard section with modern UI/UX
def welcome_dashboard():
    st.markdown('<h1 class="main-header">🔗 Linked List Data Structures</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1rem;">Welcome to Your Interactive Learning Journey!</h2>
    <p style="font-size: 1.2em; text-align: center; color: #666; margin-bottom: 2rem;">
    Master linked lists through interactive visualizations, hands-on practice, and comprehensive analysis.
    </p>
    <div style="text-align: center; margin-top: 2rem;">
    <button class="modern-button" onclick="document.querySelector('.stTabs').scrollIntoView({behavior: 'smooth'})">
    🚀 Start Learning
    </button>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Feature cards with enhanced animations
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.1s;">
        <h3>📚 Learn</h3>
        <p>Comprehensive guide to singly, doubly, and circular linked lists</p>
        <div style="margin-top: 1rem; font-size: 0.9em; opacity: 0.8;">
        <span class="success-checkmark"></span> Interactive Examples
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.2s;">
        <h3>🎮 Practice</h3>
        <p>Interactive playground with real-time operations</p>
        <div style="margin-top: 1rem; font-size: 0.9em; opacity: 0.8;">
        <span class="success-checkmark"></span> Live Visualization
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.3s;">
        <h3>📊 Analyze</h3>
        <p>Performance comparisons and optimization tips</p>
        <div style="margin-top: 1rem; font-size: 0.9em; opacity: 0.8;">
        <span class="success-checkmark"></span> Big O Analysis
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card" style="animation-delay: 0.4s;">
        <h3>💡 Solve</h3>
        <p>Practice problems with detailed solutions</p>
        <div style="margin-top: 1rem; font-size: 0.9em; opacity: 0.8;">
        <span class="success-checkmark"></span> Step-by-Step Solutions
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced Quick stats with metric cards
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🚀 Quick Start Guide")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-value">3</div>
        <div class="metric-label">Data Structures</div>
        <div style="font-size: 0.8em; opacity: 0.7; margin-top: 0.5rem;">Singly, Doubly, Circular</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-value">8+</div>
        <div class="metric-label">Operations</div>
        <div style="font-size: 0.8em; opacity: 0.7; margin-top: 0.5rem;">Insert, Delete, Search, Traverse</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <div class="metric-value">10+</div>
        <div class="metric-label">Practice Problems</div>
        <div style="font-size: 0.8em; opacity: 0.7; margin-top: 0.5rem;">With Detailed Solutions</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced Progress indicator with visual progress bar
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📈 Learning Progress")

    # Progress visualization
    st.markdown("""
    <div style="margin: 2rem 0;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
    <span style="font-weight: 600; color: #1e3c72;">Your Progress</span>
    <span style="font-weight: 600; color: #1e3c72;">0%</span>
    </div>
    <div class="progress-container">
    <div class="progress-bar" style="width: 0%;"></div>
    </div>
    <div style="margin-top: 1rem; font-size: 0.9em; color: #666;">
    Complete sections to track your progress and unlock achievements! 🏆
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive learning path
    st.markdown("""
    <div class="visual-diagram">
    <h4 style="margin-bottom: 1.5rem; color: #1e3c72;">🎯 Learning Path</h4>
    <div class="timeline">
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>📖 Introduction</h5>
    <p>Learn the fundamentals of linked lists</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>🔗 Types</h5>
    <p>Explore singly, doubly, and circular variants</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>⚙️ Operations</h5>
    <p>Master insertion, deletion, and traversal</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>🎮 Playground</h5>
    <p>Practice with interactive visualizations</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>📊 Analysis</h5>
    <p>Understand performance characteristics</p>
    </div>
    </div>
    <div class="timeline-item">
    <div class="timeline-content">
    <h5>💡 Practice</h5>
    <p>Solve challenging problems</p>
    </div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Enhanced Introduction section with modern UI/UX
def introduction():
    st.markdown('<h1 class="main-header">📖 Introduction to Linked Lists</h1>', unsafe_allow_html=True)

    # Interactive concept overview
    st.markdown("""
    <div class="section-card">
    <h2 style="color: #1e3c72; text-align: center; margin-bottom: 1.5rem;">What is a Linked List?</h2>
    <div style="text-align: center; margin-bottom: 2rem;">
    <div class="highlight-box">
    <strong>A linked list is a fundamental data structure that consists of a sequence of elements called nodes.</strong>
    <br><br>
    Each node contains two parts:
    <ul style="text-align: left; display: inline-block; margin-top: 1rem;">
    <li><strong>Data</strong>: The actual information stored in the node</li>
    <li><strong>Reference/Pointer</strong>: A link to the next node in the sequence</li>
    </ul>
    </div>
    </div>
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
    <strong>Key Difference from Arrays:</strong> Unlike arrays, linked lists do not store elements in contiguous memory locations.
    Instead, each node points to the next one, forming a chain-like structure that provides dynamic memory allocation.
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Advantages/Disadvantages with interactive cards
    st.header("Why Use Linked Lists?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="interactive-card" style="border-left: 4px solid #4CAF50;">
        <h3 style="color: #4CAF50; margin-bottom: 1rem;">✅ Advantages</h3>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">🔸</span>
        <strong>Dynamic Size:</strong> Can grow or shrink during runtime
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">⚡</span>
        <strong>Efficient Operations:</strong> O(1) for insertions/deletions at known positions
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">💾</span>
        <strong>No Memory Waste:</strong> Only allocates memory when needed
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #4CAF50; margin-right: 0.5rem;">🔧</span>
        <strong>Flexible Structure:</strong> Easy to implement stacks, queues, and other data structures
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="interactive-card" style="border-left: 4px solid #f44336;">
        <h3 style="color: #f44336; margin-bottom: 1rem;">❌ Disadvantages</h3>
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">🎯</span>
        <strong>Random Access:</strong> O(n) time to access elements by index
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">📊</span>
        <strong>Extra Memory:</strong> Each node requires additional space for pointers
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">➡️</span>
        <strong>Sequential Access:</strong> Must traverse from beginning for most operations
        </div>
        <div style="display: flex; align-items: center;">
        <span style="color: #f44336; margin-right: 0.5rem;">⚡</span>
        <strong>Cache Performance:</strong> Poor locality of reference
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    # Enhanced Node Structure with interactive code block
    st.header("Basic Node Structure")

    st.markdown("""
    <div class="code-container">
    <div class="code-header">
    <span>🔧 Node Implementation</span>
    <button class="copy-button" onclick="navigator.clipboard.writeText(`class Node:\\n    def __init__(self, data):\\n        self.data = data\\n        self.next = None`)">Copy</button>
    </div>
    <div class="code-content">
class Node:
    def __init__(self, data):
        self.data = data        # The actual data stored in the node
        self.next = None        # Pointer to the next node (None if last node)
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive Real-World Applications
    st.header("Real-World Applications")

    applications = [
        {"icon": "🎵", "title": "Music Playlists", "desc": "Songs linked in sequence for easy navigation"},
        {"icon": "🌐", "title": "Browser History", "desc": "Web pages linked for back/forward navigation"},
        {"icon": "↩️", "title": "Undo Functionality", "desc": "Operations stored as linked list in editors"},
        {"icon": "🔗", "title": "Hash Tables", "desc": "Collision resolution using separate chaining"},
        {"icon": "💾", "title": "Memory Management", "desc": "Free memory blocks tracking in OS"},
        {"icon": "📈", "title": "Polynomial Representation", "desc": "Mathematical terms linked by degree"}
    ]

    cols = st.columns(3)
    for i, app in enumerate(applications):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="feature-card" style="animation-delay: {i * 0.1}s; min-height: 120px;">
            <h4 style="margin-bottom: 0.5rem;">{app['icon']} {app['title']}</h4>
            <p style="font-size: 0.9em; opacity: 0.9;">{app['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Enhanced Memory Representation with visual diagram
    st.header("Memory Representation")

    st.markdown("""
    <div class="visual-diagram">
    <h3 style="margin-bottom: 1rem; color: #1e3c72;">🔍 How Linked Lists are Stored in Memory</h3>
    <p style="margin-bottom: 1.5rem;">Visual representation of how linked list nodes are scattered in memory:</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced memory layout visualization
    st.markdown("""
    <div class="section-card">
    <div style="font-family: 'Courier New', monospace; background: #2c3e50; color: #ecf0f1; padding: 1.5rem; border-radius: 8px; margin: 1rem 0;">
    <div style="text-align: center; margin-bottom: 1rem; color: #3498db; font-weight: bold;">Memory Layout Visualization</div>
    <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 1rem;">
    <div style="border: 2px solid #e74c3c; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #e74c3c; font-weight: bold; margin-bottom: 0.5rem;">Node 1</div>
    <div><strong>Data:</strong> 10</div>
    <div><strong>Next:</strong> 0x200 →</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x100</div>
    </div>
    <div style="color: #e74c3c; font-size: 1.5rem;">→</div>
    <div style="border: 2px solid #27ae60; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #27ae60; font-weight: bold; margin-bottom: 0.5rem;">Node 2</div>
    <div><strong>Data:</strong> 20</div>
    <div><strong>Next:</strong> 0x300 →</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x200</div>
    </div>
    <div style="color: #27ae60; font-size: 1.5rem;">→</div>
    <div style="border: 2px solid #f39c12; border-radius: 8px; padding: 1rem; background: #34495e; min-width: 150px;">
    <div style="text-align: center; color: #f39c12; font-weight: bold; margin-bottom: 0.5rem;">Node 3</div>
    <div><strong>Data:</strong> 30</div>
    <div><strong>Next:</strong> NULL</div>
    <div style="text-align: center; margin-top: 0.5rem; color: #95a5a6; font-size: 0.8em;">Address: 0x300</div>
    </div>
    </div>
    <div style="margin-top: 1rem; text-align: center; color: #95a5a6; font-style: italic;">
    Nodes are scattered in memory, connected only by pointers
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Interactive learning checkpoint
    st.markdown("""
    <div class="section-card">
    <h3 style="color: #1e3c72; text-align: center; margin-bottom: 1rem;">🎯 Learning Checkpoint</h3>
    <div style="display: flex; justify-content: space-around; margin: 1.5rem 0;">
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #4CAF50;">✓</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Node Structure</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #4CAF50;">✓</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Memory Layout</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #2196F3;">○</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Types of Lists</div>
    </div>
    <div style="text-align: center;">
    <div style="font-size: 2rem; color: #9E9E9E;">○</div>
    <div style="margin-top: 0.5rem; font-weight: 600;">Operations</div>
    </div>
    </div>
    <div style="text-align: center; margin-top: 2rem;">
    <button class="modern-button" onclick="document.querySelector('.stTabs [aria-selected=true]').nextElementSibling?.click()">
    Continue to Types →
    </button>
    </div>
    </div>
    """, unsafe_allow_html=True)

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

    # Linked list classes are now imported from linked_list_classes module

    # Initialize session state
    if 'list_type' not in st.session_state:
        st.session_state.list_type = "Singly Linked List"
    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = SinglyLinkedList()

    # List type selector
    st.header("Select Linked List Type")
    list_types = ["Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    selected_type = st.selectbox("Choose list type:", list_types, index=list_types.index(st.session_state.list_type))

    if selected_type != st.session_state.list_type:
        st.session_state.list_type = selected_type
        if selected_type == "Singly Linked List":
            st.session_state.linked_list = SinglyLinkedList()
        elif selected_type == "Doubly Linked List":
            st.session_state.linked_list = DoublyLinkedList()
        elif selected_type == "Circular Linked List":
            st.session_state.linked_list = CircularLinkedList()
        st.rerun()

    st.header("Create Your Linked List")
    col1, col2 = st.columns([2, 1])
    with col1:
        user_input = st.text_input("Enter comma-separated values (e.g., 1, 2, 3, 4)", "")
        if st.button("Create List", key="create"):
            if user_input:
                values = [x.strip() for x in user_input.split(",") if x.strip()]
                if st.session_state.list_type == "Singly Linked List":
                    st.session_state.linked_list = SinglyLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                elif st.session_state.list_type == "Doubly Linked List":
                    st.session_state.linked_list = DoublyLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                elif st.session_state.list_type == "Circular Linked List":
                    st.session_state.linked_list = CircularLinkedList()
                    for val in values:
                        st.session_state.linked_list.insert_at_end(val)
                st.success(f"{st.session_state.list_type} created with {len(values)} elements!")
            else:
                st.warning("Please enter some values.")
    with col2:
        if st.button("Clear List", key="clear"):
            if st.session_state.list_type == "Singly Linked List":
                st.session_state.linked_list = SinglyLinkedList()
            elif st.session_state.list_type == "Doubly Linked List":
                st.session_state.linked_list = DoublyLinkedList()
            elif st.session_state.list_type == "Circular Linked List":
                st.session_state.linked_list = CircularLinkedList()
            st.info(f"{st.session_state.list_type} cleared!")

    st.header(f"Current {st.session_state.list_type}")
    if st.session_state.linked_list.size > 0:
        if st.session_state.list_type == "Doubly Linked List":
            st.write("Forward: ", st.session_state.linked_list.traverse_forward())
            st.write("Backward: ", st.session_state.linked_list.traverse_backward())
        else:
            elements = st.session_state.linked_list.traverse() if st.session_state.list_type != "Circular Linked List" else st.session_state.linked_list.traverse(20)
            st.write("Elements: ", elements)
        st.write(f"Length: {st.session_state.linked_list.size}")

        # Enhanced Plotly visualization
        elements = []
        if st.session_state.list_type == "Doubly Linked List":
            elements = st.session_state.linked_list.traverse_forward()
        elif st.session_state.list_type == "Circular Linked List":
            elements = st.session_state.linked_list.traverse(20)
        else:
            elements = st.session_state.linked_list.traverse()

        # Create interactive Plotly visualization
        fig = go.Figure()
        
        # Add nodes
        node_x = [i * 2 for i in range(len(elements))]
        node_y = [0] * len(elements)
        
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            marker=dict(size=50, color='lightblue', line=dict(width=3, color='blue')),
            text=[str(val) for val in elements],
            textposition="middle center",
            textfont=dict(size=14, color='black'),
            name="Nodes",
            hovertemplate="<b>Node %{pointNumber}</b><br>Value: %{text}<extra></extra>"
        ))
        
        # Add arrows based on list type
        for i in range(len(elements)):
            if st.session_state.list_type == "Doubly Linked List":
                if i < len(elements) - 1:
                    fig.add_annotation(
                        x=node_x[i] + 0.5, y=0.2,
                        ax=node_x[i+1] - 0.5, ay=0.2,
                        xref='x', yref='y', axref='x', ayref='y',
                        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='red',
                        text="next", showarrow=True
                    )
                if i > 0:
                    fig.add_annotation(
                        x=node_x[i] - 0.5, y=-0.2,
                        ax=node_x[i-1] + 0.5, ay=-0.2,
                        xref='x', yref='y', axref='x', ayref='y',
                        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='green',
                        text="prev", showarrow=True
                    )
            elif st.session_state.list_type == "Circular Linked List":
                if i < len(elements) - 1:
                    fig.add_annotation(
                        x=node_x[i] + 0.5, y=0,
                        ax=node_x[i+1] - 0.5, ay=0,
                        xref='x', yref='y', axref='x', ayref='y',
                        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='red',
                        showarrow=True
                    )
                elif len(elements) > 1:
                    fig.add_annotation(
                        x=node_x[i] + 0.5, y=0.5,
                        ax=node_x[0] - 0.5, ay=0.5,
                        xref='x', yref='y', axref='x', ayref='y',
                        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='purple',
                        text="circular", showarrow=True
                    )
            else:  # Singly
                if i < len(elements) - 1:
                    fig.add_annotation(
                        x=node_x[i] + 0.5, y=0,
                        ax=node_x[i+1] - 0.5, ay=0,
                        xref='x', yref='y', axref='x', ayref='y',
                        arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='red',
                        showarrow=True
                    )
        
        # Add NULL for non-circular lists
        if st.session_state.list_type != "Circular Linked List" and elements:
            fig.add_trace(go.Scatter(
                x=[node_x[-1] + 2], y=[0],
                mode='markers+text',
                marker=dict(size=40, color='lightgray', line=dict(width=2, color='gray')),
                text=["NULL"],
                textposition="middle center",
                name="NULL",
                showlegend=False
            ))
            fig.add_annotation(
                x=node_x[-1] + 0.5, y=0,
                ax=node_x[-1] + 1.5, ay=0,
                arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='gray',
                showarrow=True
            )
        
        fig.update_layout(
            title=f"{st.session_state.list_type} Visualization",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1, 1]),
            showlegend=False,
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(f"No {st.session_state.list_type.lower()} created yet. Use the input above to create one!")

    st.header(f"Operations on {st.session_state.list_type}")
    if st.session_state.linked_list.size > 0:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Insert Element")
            insert_pos = st.selectbox("Position", ["Beginning", "End", "At Index"])
            insert_val = st.text_input("Value to insert", key="insert_val")

            if insert_pos == "At Index":
                insert_idx = st.number_input("Index", min_value=0, max_value=st.session_state.linked_list.size, value=0, key="insert_idx")

            if st.button("Insert", key="insert_btn"):
                if insert_val:
                    success = False
                    if insert_pos == "Beginning":
                        st.session_state.linked_list.insert_at_beginning(insert_val)
                        success = True
                    elif insert_pos == "End":
                        st.session_state.linked_list.insert_at_end(insert_val)
                        success = True
                    else:  # At Index
                        success = st.session_state.linked_list.insert_at_index(insert_val, insert_idx)

                    if success:
                        st.success(f"Inserted '{insert_val}' at {insert_pos.lower()}!")
                        st.rerun()
                    else:
                        st.warning("Invalid index!")
                else:
                    st.warning("Please enter a value to insert.")

        with col2:
            st.subheader("Delete Element")
            delete_pos = st.selectbox("Delete from", ["Beginning", "End", "By Value"], key="delete_pos")
            if delete_pos == "By Value":
                delete_val = st.text_input("Value to delete", key="delete_val")

            if st.button("Delete", key="delete_btn"):
                if st.session_state.linked_list.size == 0:
                    st.warning("List is empty!")
                else:
                    deleted = None
                    if delete_pos == "Beginning":
                        deleted = st.session_state.linked_list.delete_from_beginning()
                    elif delete_pos == "End":
                        deleted = st.session_state.linked_list.delete_from_end()
                    else:  # By Value
                        if st.session_state.linked_list.delete_by_value(delete_val):
                            deleted = delete_val

                    if deleted is not None:
                        st.success(f"Removed '{deleted}' from {delete_pos.lower()}!")
                        st.rerun()
                    else:
                        st.warning(f"'{delete_val}' not found in list!" if delete_pos == "By Value" else "Operation failed!")

        with col3:
            st.subheader("Search Element")
            search_val = st.text_input("Value to search", key="search_val")

            if st.button("Search", key="search_btn"):
                idx = st.session_state.linked_list.search(search_val)
                if idx != -1:
                    st.success(f"Found '{search_val}' at index {idx}!")
                else:
                    st.warning(f"'{search_val}' not found in list!")

    # Code examples remain the same
    st.header("Code Implementation & Execution")
    st.markdown("Here's how the operations above are implemented in Python. You can also run example code!")

    # Code execution functionality
    st.subheader("🔧 Code Runner")

    # Predefined code examples
    code_examples = {
        "Create Linked List": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create a linked list
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)

print("Linked List:", ll.traverse())
""",
        "Insert at Beginning": """
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

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create and modify linked list
ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)

print("After insertions:", ll.traverse())
""",
        "Search Element": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

# Create linked list and search
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

print("List:", ll.traverse())
print("Position of 20:", ll.search(20))
print("Position of 40:", ll.search(40))
""",
        "Reverse List": """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Create and reverse linked list
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Original:", ll.traverse())
ll.reverse()
print("Reversed:", ll.traverse())
"""
    }

    selected_example = st.selectbox("Choose an example to run:", list(code_examples.keys()))
    
    # Display selected code
    st.code(code_examples[selected_example], language="python")
    
    # Add run button below the code
    if st.button(f"▶️ Run {selected_example}", key="run_selected_code"):
        with st.spinner("Executing code..."):
            try:
                # Capture output
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()
                
                # Execute the code
                exec(code_examples[selected_example])
                
                # Get output
                sys.stdout = old_stdout
                output = captured_output.getvalue()
                
                if output:
                    st.success("Code executed successfully!")
                    st.text("Output:")
                    st.code(output, language="text")
                else:
                    st.success("Code executed successfully (no output)")
                    
            except Exception as e:
                sys.stdout = old_stdout
                st.error(f"Error executing code: {str(e)}")

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

# Advanced Visualizations section
def advanced_visualizations():
    st.title("Advanced Visualizations")

    st.header("Network Graph Visualization")

    # Check if linked list exists and has data
    if 'linked_list' not in st.session_state or st.session_state.linked_list.size == 0:
        st.warning("Please create a linked list in the Playground section first!")
        return

    st.subheader("Linked List as Network Graph")

    # Get list elements based on type
    if hasattr(st.session_state.linked_list, 'traverse_forward'):
        elements = st.session_state.linked_list.traverse_forward()
    else:
        elements = st.session_state.linked_list.traverse()
    
    if not elements:
        st.info("No elements to visualize")
        return

    # Create network graph
    G = nx.DiGraph()

    # Add nodes and edges
    for i, val in enumerate(elements):
        G.add_node(f"Node_{i}", label=str(val), pos=(i, 0))

    for i in range(len(elements) - 1):
        G.add_edge(f"Node_{i}", f"Node_{i+1}")

    # Create positions
    pos = nx.spring_layout(G)

    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')

    # Create node traces
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"{G.nodes[node]['label']}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition="middle center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color='#1e3c72',
            size=40,
            line_width=2))

    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       height=400
                   ))

    st.plotly_chart(fig, use_container_width=True)

    st.header("Memory Layout Animation")

    # Animated memory layout
    st.subheader("Dynamic Memory Allocation")

    animation_placeholder = st.empty()

    if st.button("Animate Memory Allocation"):
        # Get elements for animation
        if hasattr(st.session_state.linked_list, 'traverse_forward'):
            anim_elements = st.session_state.linked_list.traverse_forward()
        else:
            anim_elements = st.session_state.linked_list.traverse()
            
        for i in range(len(anim_elements) + 1):
            with animation_placeholder.container():
                cols = st.columns(min(5, len(anim_elements) + 1))

                for j in range(min(5, i + 1)):
                    if j < len(anim_elements):
                        with cols[j]:
                            st.markdown(f"""
                            <div style="border: 2px solid #1e3c72; border-radius: 10px; padding: 10px; margin: 5px; background: {'#e3f2fd' if j < i else '#f5f5f5'};">
                                <div style="font-weight: bold; color: #1e3c72;">Memory Block {j}</div>
                                <div>Data: {anim_elements[j]}</div>
                                <div style="font-size: 0.8em; color: #666;">Address: 0x{j*100:03X}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    elif j == len(anim_elements):
                        with cols[j]:
                            st.markdown(f"""
                            <div style="border: 2px solid #f44336; border-radius: 10px; padding: 10px; margin: 5px; background: {'#ffebee' if j <= i else '#f5f5f5'};">
                                <div style="font-weight: bold; color: #f44336;">NULL</div>
                                <div>End of List</div>
                                <div style="font-size: 0.8em; color: #666;">Address: 0x{j*100:03X}</div>
                            </div>
                            """, unsafe_allow_html=True)

            import time
            time.sleep(0.5)

# Interactive Quiz section
def interactive_quiz():
    st.title("Interactive Quiz")

    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    questions = QUIZ_QUESTIONS

    st.header("Test Your Knowledge!")

    if st.session_state.current_question < len(questions):
        q = questions[st.session_state.current_question]

        st.subheader(f"Question {st.session_state.current_question + 1} of {len(questions)}")
        st.write(q["question"])

        user_answer = st.radio("Select your answer:", q["options"], key=f"q_{st.session_state.current_question}")

        if st.button("Submit Answer"):
            selected_index = q["options"].index(user_answer)
            if selected_index == q["correct"]:
                st.success("Correct! 🎉")
                st.session_state.quiz_score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {q['options'][q['correct']]}")

            st.info(f"Explanation: {q['explanation']}")

        
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.rerun()
    else:
        # Quiz completed
        st.header("Quiz Completed! 🎊")

        score_percentage = (st.session_state.quiz_score / len(questions)) * 100

        if score_percentage >= 80:
            st.success(f"Excellent! You scored {st.session_state.quiz_score}/{len(questions)} ({score_percentage:.1f}%)")
        elif score_percentage >= 60:
            st.warning(f"Good job! You scored {st.session_state.quiz_score}/{len(questions)} ({score_percentage:.1f}%)")
        else:
            st.error(f"You scored {st.session_state.quiz_score}/{len(questions)} ({score_percentage:.1f}%). Keep studying!")

        if st.button("Restart Quiz"):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.rerun()

# Data Structure Comparison section
def data_structure_comparison():
    st.title("Data Structure Comparison")

    st.header("Linked Lists vs Arrays")

    comparison_data = {
        'Aspect': [
            'Random Access',
            'Insertion at Beginning',
            'Insertion at End',
            'Deletion from Beginning',
            'Deletion from End',
            'Memory Usage',
            'Cache Performance',
            'Implementation Complexity'
        ],
        'Linked List': ['O(n)', 'O(1)', 'O(n)', 'O(1)', 'O(n)', 'Higher', 'Poor', 'Moderate'],
        'Dynamic Array': ['O(1)', 'O(n)', 'O(1)*', 'O(n)', 'O(1)', 'Lower', 'Excellent', 'Simple']
    }

    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)

    st.markdown("*Note: * Amortized O(1) for dynamic arrays")

    # Interactive comparison chart
    st.header("Performance Comparison Chart")

    aspects = ['Random Access', 'Insert Beginning', 'Insert End', 'Delete Beginning', 'Delete End']
    linked_list_scores = [10, 1, 10, 1, 10]  # Lower is better
    array_scores = [1, 10, 1, 10, 1]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Linked List',
        x=aspects,
        y=linked_list_scores,
        marker_color='#1e3c72'
    ))

    fig.add_trace(go.Bar(
        name='Dynamic Array',
        x=aspects,
        y=array_scores,
        marker_color='#667eea'
    ))

    fig.update_layout(
        title="Performance Comparison (Lower is Better)",
        barmode='group',
        yaxis_title="Complexity Score",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.header("When to Use Which?")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Choose Linked List when:")
        st.markdown("""
        - ✅ Frequent insertions/deletions at beginning
        - ✅ Dynamic size requirements
        - ✅ Memory allocation/deallocation is expensive
        - ✅ Implementing stacks, queues, or graphs
        - ✅ Sequential access patterns
        """)

    with col2:
        st.subheader("Choose Array when:")
        st.markdown("""
        - ✅ Need fast random access
        - ✅ Memory efficiency is critical
        - ✅ Most operations are at the end
        - ✅ Simple implementation needed
        - ✅ Cache performance matters
        """)

    st.header("Linked Lists vs Other Data Structures")

    structures = ['Linked List', 'Array', 'Stack', 'Queue', 'Tree', 'Graph']
    use_cases = [
        'Dynamic sequences, undo operations',
        'Static sequences, fast access',
        'LIFO operations, function calls',
        'FIFO operations, scheduling',
        'Hierarchical data, searching',
        'Complex relationships, networks'
    ]

    comparison_df = pd.DataFrame({
        'Data Structure': structures,
        'Primary Use Cases': use_cases
    })

    st.dataframe(comparison_df, use_container_width=True)

# Advanced Algorithms section
def advanced_algorithms():
    st.title("Advanced Algorithms")

    st.header("Merge Sort on Linked Lists")

    st.markdown("""
    **Why Merge Sort for Linked Lists?**
    - Linked lists don't support random access
    - Merge sort is efficient for linked structures
    - No extra space needed for merging
    - Stable sorting algorithm
    """)

    with st.expander("Merge Sort Implementation"):
        st.code("""
def merge_sort(head):
    if not head or not head.next:
        return head

    # Find middle of list
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list
    middle = slow.next
    slow.next = None

    # Recursively sort both halves
    left = merge_sort(head)
    right = merge_sort(middle)

    # Merge the sorted halves
    return merge(left, right)

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

# Time Complexity: O(n log n)
# Space Complexity: O(log n) for recursion stack
        """, language="python")

    st.header("Quick Sort on Linked Lists")

    with st.expander("Quick Sort Implementation"):
        st.code("""
def quick_sort(head):
    if not head or not head.next:
        return head

    # Partition around pivot
    pivot = head
    smaller_head = None
    smaller_tail = None
    greater_head = None
    greater_tail = None

    current = head.next

    while current:
        if current.data < pivot.data:
            if not smaller_head:
                smaller_head = current
                smaller_tail = current
            else:
                smaller_tail.next = current
                smaller_tail = current
        else:
            if not greater_head:
                greater_head = current
                greater_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
        current = current.next

    # Terminate partitions properly
    if smaller_tail:
        smaller_tail.next = None
    if greater_tail:
        greater_tail.next = None
        
    # Recursively sort partitions
    smaller_sorted = quick_sort(smaller_head)
    greater_sorted = quick_sort(greater_head)

    # Connect all parts
    if smaller_tail:
        smaller_tail.next = pivot
    else:
        smaller_head = pivot

    pivot.next = greater_sorted

    return smaller_head if smaller_head else pivot

# Time Complexity: O(n²) worst case, O(n log n) average
# Space Complexity: O(log n) for recursion stack
        """, language="python")

    st.header("Cycle Detection Algorithms")

    st.subheader("Floyd's Cycle Detection Algorithm")

    with st.expander("Implementation"):
        st.code("""
def detect_cycle_floyd(head):
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

    st.subheader("Brent's Cycle Detection Algorithm")

    with st.expander("Implementation"):
        st.code("""
def detect_cycle_brent(head):
    if not head:
        return False

    slow = head
    fast = head.next
    power = 1
    length = 1

    # Find cycle
    while fast and fast != slow:
        if power == length:
            power *= 2
            length = 0
            slow = fast

        fast = fast.next
        length += 1

    return fast is not None

# Time Complexity: O(n)
# Space Complexity: O(1)
# Often faster than Floyd's algorithm in practice
        """, language="python")

    st.header("Advanced Operations")

    st.subheader("Reverse in Groups")

    with st.expander("Reverse k nodes at a time"):
        st.code("""
def reverse_k_groups(head, k):
    if not head or k == 1:
        return head

    # Count total nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    # Create dummy node
    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy

    while count >= k:
        current = prev_group_end.next
        next_group_start = current

        # Reverse k nodes
        for i in range(k - 1):
            temp = current.next
            current.next = temp.next
            temp.next = prev_group_end.next
            prev_group_end.next = temp

        prev_group_end = next_group_start
        count -= k

    return dummy.next

# Example: reverse_k_groups([1,2,3,4,5], 2) -> [2,1,4,3,5]
        """, language="python")

# Memory Layout Visualizations section
def memory_layout_visualizations():
    st.title("Memory Layout Visualizations")

    st.header("How Linked Lists are Stored in Memory")

    st.markdown("""
    **Key Concept:** Unlike arrays that store elements in contiguous memory locations,
    linked list nodes are scattered throughout memory and connected via pointers.
    """)

    # Interactive memory layout demo
    st.subheader("Interactive Memory Layout")

    if 'demo_list' not in st.session_state:
        st.session_state.demo_list = [10, 20, 30, 40]

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Memory Blocks")
        memory_placeholder = st.empty()

    with col2:
        st.markdown("### Controls")
        if st.button("Add Node"):
            st.session_state.demo_list.append(len(st.session_state.demo_list) * 10 + 10)
            st.rerun()

        if st.button("Remove Node") and st.session_state.demo_list:
            st.session_state.demo_list.pop()
            st.rerun()

        if st.button("Shuffle Memory"):
            import random
            random.shuffle(st.session_state.demo_list)
            st.rerun()

    # Display memory layout
    with memory_placeholder.container():
        if st.session_state.demo_list:
            cols = st.columns(min(6, len(st.session_state.demo_list)))

            for i, val in enumerate(st.session_state.demo_list):
                if i < 6:  # Show max 6 blocks
                    with cols[i]:
                        st.markdown(f"""
                        <div style="border: 2px solid #1e3c72; border-radius: 10px; padding: 15px; margin: 5px; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);">
                            <div style="font-weight: bold; color: #1e3c72; text-align: center;">Block {i}</div>
                            <div style="text-align: center; font-size: 1.2em; margin: 10px 0;">{val}</div>
                            <div style="font-size: 0.8em; color: #666; text-align: center;">Addr: 0x{i*100:03X}</div>
                            {'<div style="text-align: center; margin-top: 10px;">→</div>' if i < len(st.session_state.demo_list) - 1 else '<div style="text-align: center; margin-top: 10px; color: #f44336;">NULL</div>'}
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.info("Add some nodes to see the memory layout!")

    st.header("Memory Fragmentation")

    st.markdown("""
    **Memory Fragmentation** occurs when free memory is divided into small, non-contiguous blocks.
    This can happen with frequent insertions and deletions in linked lists.
    """)

    # Fragmentation visualization
    st.subheader("Fragmentation Demo")

    fragmentation_data = [
        {"address": "0x100", "size": 32, "status": "used", "data": "Node A"},
        {"address": "0x120", "size": 16, "status": "free", "data": ""},
        {"address": "0x130", "size": 48, "status": "used", "data": "Node B"},
        {"address": "0x160", "size": 24, "status": "free", "data": ""},
        {"address": "0x184", "size": 40, "status": "used", "data": "Node C"},
    ]

    for block in fragmentation_data:
        color = "#4CAF50" if block["status"] == "used" else "#f44336"
        st.markdown(f"""
        <div style="display: flex; align-items: center; margin: 10px 0; padding: 10px; border-radius: 8px; background: {'#e8f5e8' if block['status'] == 'used' else '#ffebee'};">
            <div style="width: 100px; font-weight: bold;">{block['address']}</div>
            <div style="width: 60px;">{block['size']}B</div>
            <div style="width: 80px; color: {color};">{block['status'].upper()}</div>
            <div style="flex: 1;">{block['data']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    **Impact of Fragmentation:**
    - **Memory Waste:** Small free blocks can't be used for larger allocations
    - **Performance:** Increased time for memory allocation/deallocation
    - **Cache Issues:** Scattered memory access patterns
    """)

    st.header("Cache Performance")

    st.markdown("""
    **Cache Locality** refers to how closely related data elements are stored in memory.
    Arrays have excellent cache locality, while linked lists have poor cache locality.
    """)

    # Cache performance visualization
    st.subheader("Cache Access Patterns")

    cache_demo = st.selectbox("Select data structure:", ["Array", "Linked List"])

    if cache_demo == "Array":
        st.markdown("""
        **Array Access Pattern:**
        - Elements stored contiguously: [10][20][30][40][50]
        - Memory addresses: 0x100, 0x104, 0x108, 0x10C, 0x110
        - **Cache Performance:** Excellent - sequential access
        """)
    else:
        st.markdown("""
        **Linked List Access Pattern:**
        - Elements scattered: 10(0x100) → 20(0x200) → 30(0x150) → 40(0x300)
        - Memory addresses: 0x100, 0x200, 0x150, 0x300
        - **Cache Performance:** Poor - random access, cache misses
        """)

# Performance Benchmarks section
def performance_benchmarks():
    st.title("Performance Benchmarks")

    st.header("Actual Timing Comparisons")

    if st.button("Run Benchmarks"):
        import time

        # Test data sizes
        sizes = [100, 1000, 10000]

        results = {
            'Size': [],
            'Operation': [],
            'Linked List (ms)': [],
            'Array (ms)': []
        }

        for size in sizes:
            # Create test data
            test_data = list(range(size))

            # Linked List Implementation
            class Node:
                def __init__(self, data):
                    self.data = data
                    self.next = None

            class LinkedList:
                def __init__(self):
                    self.head = None

                def insert_at_end(self, data):
                    if not self.head:
                        self.head = Node(data)
                        return
                    current = self.head
                    while current.next:
                        current = current.next
                    current.next = Node(data)

                def search(self, target):
                    current = self.head
                    while current:
                        if current.data == target:
                            return True
                        current = current.next
                    return False

            # Create structures
            ll = LinkedList()
            array = []

            # Insert at end - Linked List
            start_time = time.time()
            for item in test_data:
                ll.insert_at_end(item)
            ll_insert_time = (time.time() - start_time) * 1000

            # Insert at end - Array
            start_time = time.time()
            for item in test_data:
                array.append(item)
            array_insert_time = (time.time() - start_time) * 1000

            # Search - Linked List
            start_time = time.time()
            for _ in range(100):  # Search 100 times
                ll.search(size // 2)
            ll_search_time = (time.time() - start_time) * 1000 / 100

            # Search - Array
            start_time = time.time()
            for _ in range(100):  # Search 100 times
                (size // 2) in array
            array_search_time = (time.time() - start_time) * 1000 / 100

            # Record results
            results['Size'].extend([size, size])
            results['Operation'].extend(['Insert at End', 'Search'])
            results['Linked List (ms)'].extend([ll_insert_time, ll_search_time])
            results['Array (ms)'].extend([array_insert_time, array_search_time])

        # Display results
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)

        # Create comparison chart
        fig = go.Figure()

        for op in ['Insert at End', 'Search']:
            op_data = df[df['Operation'] == op]
            fig.add_trace(go.Bar(
                name=f'Linked List - {op}',
                x=[f"Size {size}" for size in op_data['Size']],
                y=op_data['Linked List (ms)'],
                marker_color='#1e3c72'
            ))
            fig.add_trace(go.Bar(
                name=f'Array - {op}',
                x=[f"Size {size}" for size in op_data['Size']],
                y=op_data['Array (ms)'],
                marker_color='#667eea'
            ))

        fig.update_layout(
            title="Performance Benchmarks",
            barmode='group',
            yaxis_title="Time (milliseconds)",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

    st.header("Memory Usage Analysis")

    st.markdown("""
    **Memory Overhead Comparison:**

    | Data Structure | Element Size | Overhead | Total per Element |
    |----------------|--------------|----------|-------------------|
    | Linked List (Python) | 28 bytes | 8 bytes (pointer) | ~36 bytes |
    | Dynamic Array (Python) | 28 bytes | ~4 bytes (amortized) | ~32 bytes |

    **Note:** Actual memory usage depends on the programming language and implementation.
    """)

# Main app function
def main():
    # Initialize session state for tab navigation
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = 0

    tab_names = [
        "🏠 Welcome",
        "📖 Introduction",
        "🔗 Types",
        "⚙️ Operations",
        "🎮 Playground",
        "📊 Analysis",
        "💡 Practice",
        "🎨 Advanced Viz",
        "🧠 Quiz",
        "⚖️ Comparison"
    ]

    # Navigation selectbox
    selected_tab = st.selectbox("Navigate to:", tab_names, index=st.session_state.current_tab, key="nav_select")
    st.session_state.current_tab = tab_names.index(selected_tab)

    # Render the selected tab content
    if st.session_state.current_tab == 0:
        welcome_dashboard()
    elif st.session_state.current_tab == 1:
        introduction()
    elif st.session_state.current_tab == 2:
        types_of_linked_lists()
    elif st.session_state.current_tab == 3:
        operations_and_algorithms()
    elif st.session_state.current_tab == 4:
        interactive_playground()
    elif st.session_state.current_tab == 5:
        performance_analysis()
    elif st.session_state.current_tab == 6:
        practice_problems()
    elif st.session_state.current_tab == 7:
        advanced_visualizations()
    elif st.session_state.current_tab == 8:
        interactive_quiz()
    elif st.session_state.current_tab == 9:
        data_structure_comparison()

if __name__ == "__main__":
    main()

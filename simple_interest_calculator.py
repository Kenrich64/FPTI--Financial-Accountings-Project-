import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Finance Calculators - FPTI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E4BC7;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #2E4BC7 0%, #7B68EE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-description {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .calculator-header {
        text-align: center;
        color: #2E4BC7;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .calculator-description {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        padding: 0.5rem;
    }
    
    .result-container {
        background: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: linear-gradient(90deg, #2E4BC7 0%, #7B68EE 100%);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 999;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #2E4BC7 0%, #7B68EE 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.95);
    }
</style>
""", unsafe_allow_html=True)

# Main title and description
st.markdown('<h1 class="main-title">📊 Finance Calculators – FPTI</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-description">Your comprehensive toolkit for financial calculations and planning</p>', unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("🔧 Finance Toolkit")
st.sidebar.markdown("---")

menu_option = st.sidebar.selectbox(
    "Choose a Calculator:",
    ["💰 Simple Interest Calculator"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About")
st.sidebar.info("This toolkit provides essential financial calculators to help you make informed financial decisions.")

# Simple Interest Calculator
if menu_option == "💰 Simple Interest Calculator":
    st.markdown('<div class="calculator-header">💰 Simple Interest Calculator</div>', unsafe_allow_html=True)
    st.markdown('<p class="calculator-description">Calculate simple interest and total amount for your investments</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        principal = st.number_input("💵 Principal Amount (₹)", min_value=0.0, value=10000.0, step=1000.0)
    
    with col2:
        rate = st.number_input("📈 Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1)
    
    with col3:
        time = st.number_input("📅 Time Period (years)", min_value=0.0, value=1.0, step=0.5)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🧮 Calculate Interest", key="si_calc"):
            if principal > 0 and rate > 0 and time > 0:
                simple_interest = (principal * rate * time) / 100
                total_amount = principal + simple_interest
                
                st.markdown('<div class="result-container">', unsafe_allow_html=True)
                st.success(f"💰 **Simple Interest:** ₹{simple_interest:,.2f}")
                st.success(f"💸 **Total Amount:** ₹{total_amount:,.2f}")
                st.info(f"📊 **Growth:** Your investment will grow by ₹{simple_interest:,.2f} ({((simple_interest/principal)*100):.2f}%)")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("⚠️ Please enter valid positive values for all fields!")

# -----------------------------------------
# Exercise 2 - Real vs. Nominal Return Calculator (Streamlit Version)
# -----------------------------------------

st.title("📈 Real vs. Nominal Return Calculator")

# Inputs
nominal = st.number_input("Enter the nominal return (as %, e.g., 8 for 8%)", min_value=-100.0, step=0.1) / 100
inflation = st.number_input("Enter the inflation rate (as %, e.g., 3 for 3%)", min_value=-100.0, step=0.1) / 100

def real_return_calculator(nominal_rate, inflation_rate):
    """
    Calculate the real return adjusted for inflation.
    Formula: ((1 + nominal) / (1 + inflation)) - 1
    """
    return ((1 + nominal_rate) / (1 + inflation_rate)) - 1

# Calculate when user provides inputs
if nominal != 0 or inflation != 0:
    real = real_return_calculator(nominal, inflation)
    st.write(f"**Nominal Return:** {nominal * 100:.2f}%")
    st.write(f"**Inflation Rate:** {inflation * 100:.2f}%")
    st.success(f"✅ Real Return: {real * 100:.2f}%")

# Sample Output (when running Streamlit app):
st.markdown("""
### Sample Output
If user enters Nominal = 8% and Inflation = 3%, the app will display:

Nominal Return: 8.00%

Inflation Rate: 3.00%

✅ Real Return: 4.85%
""")

# Learning Outcomes:
st.markdown("""
### Learning Outcomes

**Programming Concepts Learned** → Streamlit inputs (st.number_input), functions, arithmetic operations, formatted output, conditional execution.

**Finance Concepts Learned** → Understanding nominal vs. real return, importance of adjusting investment returns for inflation to measure true purchasing power.
""")

st.markdown("""
### **3. Real vs. Nominal Return Calculator**

* **Python concepts**: Just arithmetic operations and a simple function.
* **Finance concepts**: Difference between nominal return and real return (inflation-adjusted).
* **Task**: Input nominal return and inflation rate, then calculate real return using:

  $
  \\text{Real Return} = \\left(\\frac{1 + \\text{Nominal}}{1 + \\text{Inflation}}\\right) - 1
  $
""")

# Footer
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    Made with ❤️ using Streamlit | FPTI Project
</div>
""", unsafe_allow_html=True)
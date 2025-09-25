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
    ["💰 Simple Interest Calculator", "📈 Real vs. Nominal Return Calculator", "📊 Personal Finance Dashboard"]
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

# Real vs. Nominal Return Calculator
elif menu_option == "📈 Real vs. Nominal Return Calculator":
    st.markdown('<div class="calculator-header">📈 Real vs. Nominal Return Calculator</div>', unsafe_allow_html=True)
    st.markdown('<p class="calculator-description">Calculate real return adjusted for inflation</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        nominal = st.number_input("💰 Nominal Return (%)", min_value=-100.0, value=8.0, step=0.1) / 100
    
    with col2:
        inflation = st.number_input("📉 Inflation Rate (%)", min_value=-100.0, value=3.0, step=0.1) / 100

    def real_return_calculator(nominal_rate, inflation_rate):
        """
        Calculate the real return adjusted for inflation.
        Formula: ((1 + nominal) / (1 + inflation)) - 1
        """
        return ((1 + nominal_rate) / (1 + inflation_rate)) - 1

    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🧮 Calculate Real Return", key="rr_calc"):
            if nominal != 0 or inflation != 0:
                real = real_return_calculator(nominal, inflation)
                
                st.markdown('<div class="result-container">', unsafe_allow_html=True)
                st.info(f"**Nominal Return:** {nominal * 100:.2f}%")
                st.info(f"**Inflation Rate:** {inflation * 100:.2f}%")
                st.success(f"✅ **Real Return:** {real * 100:.2f}%")
                st.warning(f"📊 **Difference:** Your real return is {(nominal - real) * 100:.2f} percentage points lower due to inflation")
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 💡 Understanding Real vs. Nominal Returns")
    st.info("""
    **Nominal Return:** The return on investment without adjusting for inflation.
    
    **Real Return:** The return on investment after adjusting for inflation - shows your actual purchasing power gain.
    
    **Formula:** Real Return = ((1 + Nominal) / (1 + Inflation)) - 1
    
    **Why it matters:** A 10% nominal return with 8% inflation gives you only ~1.85% real return!
    """)

# Personal Finance Dashboard
elif menu_option == "📊 Personal Finance Dashboard":
    st.markdown('<div class="calculator-header">📊 Personal Finance Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<p class="calculator-description">Track your income, expenses, and net worth for better financial planning</p>', unsafe_allow_html=True)
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["💰 Income & Expenses", "📈 Net Worth Calculator", "📊 Financial Summary"])
    
    with tab1:
        st.markdown("### 💰 Monthly Income & Expenses")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📈 Income Sources")
            salary = st.number_input("💼 Salary (₹)", min_value=0.0, value=50000.0, step=1000.0)
            freelance = st.number_input("💻 Freelance Income (₹)", min_value=0.0, value=0.0, step=500.0)
            investments = st.number_input("📊 Investment Returns (₹)", min_value=0.0, value=0.0, step=500.0)
            other_income = st.number_input("💡 Other Income (₹)", min_value=0.0, value=0.0, step=500.0)
            
            total_income = salary + freelance + investments + other_income
            
        with col2:
            st.markdown("#### 📉 Monthly Expenses")
            housing = st.number_input("🏠 Housing/Rent (₹)", min_value=0.0, value=15000.0, step=1000.0)
            food = st.number_input("🍽️ Food & Groceries (₹)", min_value=0.0, value=8000.0, step=500.0)
            transport = st.number_input("🚗 Transportation (₹)", min_value=0.0, value=5000.0, step=500.0)
            utilities = st.number_input("⚡ Utilities (₹)", min_value=0.0, value=3000.0, step=500.0)
            entertainment = st.number_input("🎬 Entertainment (₹)", min_value=0.0, value=4000.0, step=500.0)
            other_expenses = st.number_input("🛍️ Other Expenses (₹)", min_value=0.0, value=5000.0, step=500.0)
            
            total_expenses = housing + food + transport + utilities + entertainment + other_expenses
        
        # Calculate cash flow
        monthly_cash_flow = total_income - total_expenses
        annual_cash_flow = monthly_cash_flow * 12
        
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Income", f"₹{total_income:,.0f}")
        with col2:
            st.metric("Total Expenses", f"₹{total_expenses:,.0f}")
        with col3:
            if monthly_cash_flow >= 0:
                st.metric("Monthly Cash Flow", f"₹{monthly_cash_flow:,.0f}", f"Surplus")
            else:
                st.metric("Monthly Cash Flow", f"₹{monthly_cash_flow:,.0f}", f"Deficit")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Expense breakdown chart
        if total_expenses > 0:
            expense_data = {
                'Category': ['Housing', 'Food', 'Transport', 'Utilities', 'Entertainment', 'Other'],
                'Amount': [housing, food, transport, utilities, entertainment, other_expenses]
            }
            expense_df = pd.DataFrame(expense_data)
            expense_df = expense_df[expense_df['Amount'] > 0]  # Filter out zero expenses
            
            st.markdown("### 📊 Expense Breakdown")
            st.bar_chart(data=expense_df.set_index('Category'))
    
    with tab2:
        st.markdown("### 📈 Net Worth Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💰 Assets")
            cash_savings = st.number_input("💳 Cash & Savings (₹)", min_value=0.0, value=100000.0, step=5000.0)
            investments_assets = st.number_input("📊 Investments (₹)", min_value=0.0, value=50000.0, step=5000.0)
            property_value = st.number_input("🏠 Property Value (₹)", min_value=0.0, value=0.0, step=50000.0)
            vehicle_value = st.number_input("🚗 Vehicle Value (₹)", min_value=0.0, value=0.0, step=10000.0)
            other_assets = st.number_input("💎 Other Assets (₹)", min_value=0.0, value=0.0, step=5000.0)
            
            total_assets = cash_savings + investments_assets + property_value + vehicle_value + other_assets
            
        with col2:
            st.markdown("#### 📉 Liabilities")
            home_loan = st.number_input("🏠 Home Loan (₹)", min_value=0.0, value=0.0, step=10000.0)
            car_loan = st.number_input("🚗 Car Loan (₹)", min_value=0.0, value=0.0, step=5000.0)
            personal_loan = st.number_input("💳 Personal Loan (₹)", min_value=0.0, value=0.0, step=5000.0)
            credit_card_debt = st.number_input("💳 Credit Card Debt (₹)", min_value=0.0, value=0.0, step=1000.0)
            other_debts = st.number_input("📋 Other Debts (₹)", min_value=0.0, value=0.0, step=1000.0)
            
            total_liabilities = home_loan + car_loan + personal_loan + credit_card_debt + other_debts
        
        # Calculate net worth
        net_worth = total_assets - total_liabilities
        
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Assets", f"₹{total_assets:,.0f}")
        with col2:
            st.metric("Total Liabilities", f"₹{total_liabilities:,.0f}")
        with col3:
            if net_worth >= 0:
                st.metric("Net Worth", f"₹{net_worth:,.0f}", f"Positive")
            else:
                st.metric("Net Worth", f"₹{net_worth:,.0f}", f"Negative")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Assets vs Liabilities chart
        if total_assets > 0 or total_liabilities > 0:
            net_worth_data = pd.DataFrame({
                'Category': ['Assets', 'Liabilities'],
                'Amount': [total_assets, total_liabilities]
            })
            st.markdown("### 📊 Assets vs Liabilities")
            st.bar_chart(data=net_worth_data.set_index('Category'))
    
    with tab3:
        st.markdown("### 📊 Financial Summary & Analysis")
        
        # Financial health indicators
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        
        # Calculate financial ratios
        if total_income > 0:
            savings_rate = (monthly_cash_flow / total_income) * 100 if monthly_cash_flow > 0 else 0
            expense_ratio = (total_expenses / total_income) * 100
        else:
            savings_rate = 0
            expense_ratio = 0
            
        if total_assets > 0:
            debt_to_asset_ratio = (total_liabilities / total_assets) * 100
        else:
            debt_to_asset_ratio = 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Savings Rate", f"{savings_rate:.1f}%")
        with col2:
            st.metric("Expense Ratio", f"{expense_ratio:.1f}%")
        with col3:
            st.metric("Debt-to-Asset", f"{debt_to_asset_ratio:.1f}%")
        with col4:
            emergency_fund_months = (cash_savings / total_expenses) if total_expenses > 0 else 0
            st.metric("Emergency Fund", f"{emergency_fund_months:.1f} months")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Financial health assessment
        st.markdown("### 💡 Financial Health Assessment")
        
        health_score = 0
        recommendations = []
        
        if savings_rate >= 20:
            st.success("✅ Excellent savings rate! You're saving 20%+ of income.")
            health_score += 25
        elif savings_rate >= 10:
            st.warning("⚠️ Good savings rate, but try to reach 20%.")
            health_score += 15
            recommendations.append("Increase your savings rate to 20% of income")
        else:
            st.error("❌ Low savings rate. Focus on reducing expenses or increasing income.")
            recommendations.append("Critical: Increase savings rate - aim for at least 10%")
        
        if emergency_fund_months >= 6:
            st.success("✅ Strong emergency fund! You have 6+ months of expenses covered.")
            health_score += 25
        elif emergency_fund_months >= 3:
            st.warning("⚠️ Decent emergency fund, but aim for 6 months of expenses.")
            health_score += 15
            recommendations.append("Build emergency fund to 6 months of expenses")
        else:
            st.error("❌ Insufficient emergency fund. Build at least 3-6 months of expenses.")
            recommendations.append("Priority: Build emergency fund of 3-6 months expenses")
        
        if debt_to_asset_ratio <= 30:
            st.success("✅ Healthy debt levels relative to assets.")
            health_score += 25
        elif debt_to_asset_ratio <= 50:
            st.warning("⚠️ Moderate debt levels. Consider debt reduction.")
            health_score += 15
            recommendations.append("Consider reducing debt-to-asset ratio below 30%")
        else:
            st.error("❌ High debt levels. Focus on debt reduction.")
            recommendations.append("High priority: Reduce debt burden")
        
        if net_worth > 0:
            st.success("✅ Positive net worth - you're building wealth!")
            health_score += 25
        else:
            st.error("❌ Negative net worth. Focus on debt reduction and asset building.")
            recommendations.append("Focus on increasing assets and reducing liabilities")
        
        # Overall score
        st.markdown(f"### 📊 Overall Financial Health Score: {health_score}/100")
        
        if health_score >= 80:
            st.success("🌟 Excellent financial health!")
        elif health_score >= 60:
            st.warning("👍 Good financial health with room for improvement.")
        elif health_score >= 40:
            st.warning("⚠️ Fair financial health. Focus on key areas.")
        else:
            st.error("🚨 Poor financial health. Immediate action needed.")
        
        # Recommendations
        if recommendations:
            st.markdown("### 🎯 Recommendations")
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")
        
        # Future projections
        if monthly_cash_flow > 0:
            st.markdown("### 📈 Future Projections")
            years_ahead = st.slider("Years to project", 1, 20, 5)
            future_savings = monthly_cash_flow * 12 * years_ahead
            projected_net_worth = net_worth + future_savings
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Projected Savings", f"₹{future_savings:,.0f}", f"in {years_ahead} years")
            with col2:
                st.metric("Projected Net Worth", f"₹{projected_net_worth:,.0f}", f"in {years_ahead} years")

# Footer
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    Made with ❤️ using Streamlit | FPTI Project
</div>
""", unsafe_allow_html=True)
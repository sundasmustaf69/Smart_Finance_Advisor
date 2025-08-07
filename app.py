import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Finance Advisor", layout="centered")

st.title("💰 Smart Finance Advisor")
st.subheader("Analyze your income & expenses to get personalized savings advice.")

st.markdown("### 📥 Enter Your Financial Details")

# User inputs
salary = st.number_input("Monthly Salary (PKR)", min_value=0, step=1000, format="%d")
expenses = st.number_input("Monthly Expenses (PKR)", min_value=0, step=1000, format="%d")
target_savings = st.number_input("Target Monthly Savings (PKR)", min_value=0, step=1000, format="%d")

# Predict button
if st.button("🔍 Predict"):
    # Calculate savings
    savings = salary - expenses
    savings_rate = (savings / salary) * 100 if salary > 0 else 0

    # Show summary
    st.markdown("### 📊 Summary")
    st.write(f"**Your Current Savings:** PKR {savings}")
    st.write(f"**Savings Rate:** {savings_rate:.2f}%")

    # Advisor suggestion
    st.markdown("### 💡 Advisor Suggestion")
    if salary == 0:
        st.warning("Please enter a valid salary.")
    elif savings < 0:
        st.error("Your expenses exceed your income. Try to reduce spending.")
    elif savings < target_savings:
        st.warning("You're saving less than your target. Review your budget.")
    else:
        st.success("Great job! You're saving well. Keep it up!")

    # Always show pie chart
    st.markdown("### 📈 Budget Breakdown")

    # Avoid negative values
    labels = ['Expenses', 'Savings'] if savings >= 0 else ['Expenses', 'Overspending']
    sizes = [expenses, abs(savings)]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    st.pyplot(fig)

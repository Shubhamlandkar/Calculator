# multi_tool_app.py

import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Create by Shubh")
st.title("✨ My Multi-Tool Calculator App")

# Sidebar for tool selection
tool = st.sidebar.selectbox(
    "Choose a Tool",
    ["Calculator", "Text Analyzer", "Random Data Chart"]
)

# ---------------- CALCULATOR ----------------
if tool == "Calculator":
    st.header("🧮 Calculator")

    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)

    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "❌ Cannot divide by zero"
        st.success(f"Result: {result}")

# ---------------- TEXT ANALYZER ----------------
elif tool == "Text Analyzer":
    st.header("✍️ Text Analyzer")

    text = st.text_area("Enter your text here:")
    if st.button("Analyze"):
        words = len(text.split())
        characters = len(text)
        st.info(f"📖 Word Count: {words}")
        st.info(f"🔤 Character Count: {characters}")

# ---------------- RANDOM DATA CHART ----------------
elif tool == "Random Data Chart":
    st.header("📊 Random Data Chart")

    rows = st.slider("Select number of rows", 5, 50, 10)
    data = pd.DataFrame(
        np.random.randn(rows, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(data)


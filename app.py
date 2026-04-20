import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="centered")

st.title("🧮 Scientific Calculator")

# Operation selection
operation = st.selectbox(
    "Select Operation",
    [
        "Addition", "Subtraction", "Multiplication", "Division",
        "Power", "Square Root",
        "Sine", "Cosine", "Tangent",
        "Log (base 10)", "Natural Log",
        "Exponential", "Factorial"
    ]
)

# Input fields
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

else:
    num = st.number_input("Enter number")

# Degree / Radian option for trig
angle_mode = st.radio("Angle Mode", ["Degree", "Radian"])

# Calculate button
if st.button("Calculate"):

    try:
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            result = "Error" if num2 == 0 else num1 / num2

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Square Root":
            result = math.sqrt(num) if num >= 0 else "Invalid"

        elif operation == "Sine":
            angle = math.radians(num) if angle_mode == "Degree" else num
            result = math.sin(angle)

        elif operation == "Cosine":
            angle = math.radians(num) if angle_mode == "Degree" else num
            result = math.cos(angle)

        elif operation == "Tangent":
            angle = math.radians(num) if angle_mode == "Degree" else num
            result = math.tan(angle)

        elif operation == "Log (base 10)":
            result = math.log10(num) if num > 0 else "Invalid"

        elif operation == "Natural Log":
            result = math.log(num) if num > 0 else "Invalid"

        elif operation == "Exponential":
            result = math.exp(num)

        elif operation == "Factorial":
            result = math.factorial(int(num)) if num >= 0 and num.is_integer() else "Invalid"

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

# Import necessary libraries
import streamlit as st

# Define basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Streamlit app code
def main():
    st.title("Simple Calculator")

    # Display calculator options
    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Perform the selected operation
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        # Display result
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()

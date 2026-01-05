import streamlit as st

def calculate_results(num1, num2, operation):
    result = None
    error = None
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            if num2 == 0:
                error = "Error: Division by zero is not allowed."
            else:
                result = num1 / num2
        else:
            error = "Invalid Operation selected."
    except Exception as e:
        error = f"An unexpected error occurred: {str(e)}"
    return result, error

def main():
    st.set_page_config(page_title="Streamlit Calculator")
    st.title("Simple Calculator App")
    st.write("Enter two numbers and select an operation.")

    col1, col2 = st.columns(2)
    with col1:
        number1 = st.number_input("First Number", value=0.0, step=1.0)
    with col2:
        number2 = st.number_input("Second Number", value=0.0, step=1.0)

    operation = st.selectbox("Select Operation", 
        ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"))

    if st.button("Calculate"):
        result, error = calculate_results(number1, number2, operation)
        if error:
            st.error(error)
        else:
            st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
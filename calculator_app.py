import streamlit as st

st.set_page_config(
    page_title="Professional Calculator",
    layout="centered" 
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .title-text {
        text-align: center;
        color: #2E86C1;
        font-family: 'Helvetica', sans-serif;
    }
    
    .stApp {
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)

def calculate_results(num1, num2, operation):

    result = None
    error = None

    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (×)":
            result = num1 * num2
        elif operation == "Divide (÷)":
            if num2 == 0:
                error = "Cannot divide by zero"
            else:
                result = num1 / num2
    except Exception as e:
        error = f"Error: {str(e)}"

    return result, error

def main():
    st.markdown("<h1 class='title-text'>Calculator Project</h1>", unsafe_allow_html=True)
    st.write("---")

    with st.container(border=True):
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.caption("Enter first value")
            number1 = st.number_input("Value A", value=0.0, step=10.0, label_visibility="collapsed")
        
        with col2:
            st.caption("Enter second value")
            number2 = st.number_input("Value B", value=0.0, step=10.0, label_visibility="collapsed")

        st.divider() # A nice horizontal line

        st.caption("Select Operation")
        operation = st.radio(
            "Operation",
            ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.write("") # Spacer

        if st.button("Calculate Result", type="primary", use_container_width=True):
            
            result, error = calculate_results(number1, number2, operation)
            
            st.write("") # Spacer
            
            if error:
                st.error(f"{error}")
            else:
                # Use st.metric for a professional "Dashboard" look
                st.markdown("### Output")
                st.metric(label="Calculated Result", value=f"{result:,.2f}")

if __name__ == "__main__":
    main()

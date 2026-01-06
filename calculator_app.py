import streamlit as st

st.set_page_config(page_title="Pro Logic Calc", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }

    .stNumberInput input {
        background-color: #262730;
        color: #00ff41; /* Hacker Green Text */
        border: 1px solid #4B4B4B;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
    }

    div.stButton > button {
        background: linear-gradient(45deg, #2E86C1, #8E44AD);
        color: white;
        border: none;
        border-radius: 25px;
        height: 50px;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(142, 68, 173, 0.6);
    }

    .result-box {
        background-color: #1E1E1E;
        border-left: 5px solid #00ff41;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def calculate_logic(num1, num2, operator):

    result = 0
    error_msg = "" 

    if operator == "Add":
        result = num1 + num2
    elif operator == "Subtract":
        result = num1 - num2
    elif operator == "Multiply":
        result = num1 * num2
    elif operator == "Divide":
        if num2 == 0:
            error_msg = "Cannot divide by zero!"
        else:
            result = num1 / num2
    
    return result, error_msg

def main():
    
    st.markdown("<h1 style='text-align: center;'>Modern Simple Calculator</h1>", unsafe_allow_html=True)
    st.markdown("---")

    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.caption("Enter First Value")
            n1 = st.number_input("Input A", value=0.0, step=10.0, label_visibility="collapsed")
            
        with col2:
            st.caption("Enter Second Value")
            n2 = st.number_input("Input B", value=0.0, step=10.0, label_visibility="collapsed")

        st.write("") 

        st.caption("Choose Operation")
        op_mode = st.radio(
            "Operation",
            ["Add", "Subtract", "Multiply", "Divide"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.write("")

        if st.button("RUN CALCULATION"):
            final_result, error = calculate_logic(n1, n2, op_mode)
            
            if error != "":
                st.error(f"{error}")
            else:
                st.markdown(f"""
                <div class="result-box">
                    <h3 style="margin:0; color:#b3b3b3;">Calculated Result:</h3>
                    <h1 style="margin:0; color:#00ff41; font-family:'Courier New';">{final_result}</h1>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

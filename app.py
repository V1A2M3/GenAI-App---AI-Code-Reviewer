import streamlit as st
import google.generativeai
import os

# Set your OpenAI API key
google.generativeai.configure(api_key=os.getenv("AIzaSyD8_LN6yHSQNPzU5Aeu6NLEDiVt-isDBds"))  # Ensure your API key is set in environment variables

def review_code(code_snippet):
    """Function to send the code to OpenAI for review and receive suggestions."""
    prompt = f"""
    Analyze the following Python code for potential bugs, errors, and improvements. Provide feedback and suggest a fixed version of the code.
    
    Code:
    {code_snippet}
    
    Response format:
    Issues:
    - [List of detected issues]
    
    Fixed Code:
    ```python
    [Fixed version of the code]
    ```
    """
    
    response = google.generativeai.generate_message(
        model="chat-bison-001",
        messages=[{"role": "system", "content": "You are an expert Python code reviewer."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Streamlit UI
st.title("GenAI Code Reviewer")
st.write("Submit your Python code for AI-powered review and feedback.")

code_input = st.text_area("Enter your Python code:", height=200)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Reviewing your code..."):
            feedback = review_code(code_input)
            st.subheader("Review Feedback")
            st.markdown(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")

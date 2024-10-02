import os
from openai import OpenAI
import streamlit as st

# Set your OpenAI API key here
client = OpenAI(
    api_key="" 
)

# Function to call OpenAI's chat API for financial extraction
def extract_financial_info(text):
    try:
        # Call the OpenAI chat API using the client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial assistant."
                },
                {
                    "role": "user",
                    "content": f"Extract key financial data from the following text:\n\n{text}\n\nFinancial Data:"
                }
            ]
        )
        # Extracting the response content properly
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
st.title("Financial Data Extraction Tool")
st.write("Extract key financial details from any text or document using the OpenAI API.")

# Text input box
text_input = st.text_area("Enter text for financial extraction", height=300)

# Button to trigger extraction
if st.button("Extract Financial Data"):
    if text_input:
        # Call the financial extraction function
        financial_data = extract_financial_info(text_input)
        
        # Display extracted financial data
        st.subheader("Extracted Financial Data:")
        st.write(financial_data)
    else:
        st.warning("Please enter some text for extraction.")

# Optional file upload to extract from uploaded documents (text files)
st.subheader("Upload a text file:")
uploaded_file = st.file_uploader("Choose a file", type="txt")

if uploaded_file is not None:
    # Read the uploaded text file
    text_from_file = uploaded_file.read().decode("utf-8")
    
    # Display the uploaded text
    st.write("Uploaded Text:")
    st.write(text_from_file)

    # Extract financial information from the uploaded file
    if st.button("Extract from Uploaded File"):
        financial_data_from_file = extract_financial_info(text_from_file)
        st.subheader("Extracted Financial Data from File:")
        st.write(financial_data_from_file)

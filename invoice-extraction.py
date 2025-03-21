import streamlit as st
from dotenv import load_dotenv
import invoiceutil as iu

# Set page config at the top, before any Streamlit commands
st.set_page_config(page_title="Invoice Extraction Bot", page_icon="📄", layout="wide")

def main():
    load_dotenv()  # Load environment variables

    st.title("Invoice Extraction Bot...💁")  # Header
    st.subheader("I can help you in extracting invoice data")

    # Upload the invoices (PDF files)
    pdf = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)

    # Extract Data Button
    submit = st.button("Extract Data")

    if submit:
        with st.spinner('Wait for it...'):
            df = iu.create_docs(pdf)  # Call function to process PDF
            st.write(df)  # Display extracted data

            st.success("Hope I was able to save your time")

# Invoke main function
if __name__ == '__main__':
    main()

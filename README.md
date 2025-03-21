# Invoice-Parsing-bot


## Overview
This project demonstrates how **Retrieval-Augmented Generation (RAG)** can enhance traditional document parsing by combining the pattern recognition capabilities of **machine learning** with the contextual understanding of **large language models (LLMs)**. This approach can handle variations in invoice formats and extract information with high accuracy.

## Project Structure
The **Invoice Parsing RAG** application consists of two main components:

1. **Driver Program (invoice_extraction.py)** – Handles the UI and user interactions using the **Streamlit** library.
2. **Core Functionality (invoice_util.py)** – Contains the logic for parsing invoices using **LangChain** and a **vector database** for efficient retrieval.

## How It Works
### 1. Running the Application
To start the application, use the following command:
```sh
streamlit run invoice_extraction.py
```
This launches a **Streamlit UI**, allowing users to upload invoices for processing.

### 2. Uploading an Invoice
- Users can upload invoices in **PDF format**.
- The app extracts key details such as **invoice number, description, quantity, date, unit price, amount, etc.**
- Data is also parsed into **JSON format** for structured representation.

## Code Explanation
### **invoice_extraction.py** (Driver Program)
- Uses **Streamlit** for UI creation.
- Provides a file uploader that accepts **PDF invoices**.
- Calls the `create_docs()` function from `invoice_util.py` to process the uploaded invoices.
- Displays extracted information on the UI.

#### **Key Functions in invoice_extraction.py**
```python
st.set_page_config(page_title="Invoice Extraction Bot", page_icon="📄", layout="wide")
```
- Configures the Streamlit UI with a title and page icon.

```python
pdf = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf"], accept_multiple_files=True)
```
- Provides a file uploader control for invoice PDFs.

```python
if submit:
    with st.spinner('Processing...'):
        df = iu.create_docs(pdf)
        st.write(df)
        st.success("Invoice data extracted successfully!")
```
- Triggers document extraction and displays results.

### **invoice_util.py** (Core Functionality)
- Processes uploaded PDF invoices.
- Uses **LangChain's PyPDFLoader** for extracting text.
- Stores extracted information in a **vector database**.
- Constructs a **prompt template** for structured data extraction using **LLMs (GPT-4 or similar)**.

#### **Key Functions in invoice_util.py**
```python
loader = PyPDFLoader(pdf)
documents = loader.load_and_split()
```
- Loads and splits invoice PDFs for processing.

```python
vector_db = FAISS.from_documents(documents, OpenAIEmbeddings())
```
- Creates a **vector database** for efficient retrieval.

```python
retrieval_chain = RetrievalChain(retriever=vector_db, llm=gpt4)
response = retrieval_chain.invoke("Extract invoice details")
```
- Uses **RAG** for extracting invoice details with **GPT-4**.

## Features
✅ Extracts key invoice details automatically.
✅ Supports multiple invoice formats.
✅ Converts invoice data into **structured JSON output**.
✅ Uses **LangChain** for efficient document processing.
✅ Provides a **user-friendly Streamlit UI**.

## Technologies Used
- **Python**
- **Streamlit** (for UI)
- **LangChain** (for document processing)
- **FAISS** (for vector database)
- **OpenAI GPT-4** (for LLM-based data extraction)
- **PyPDFLoader** (for parsing PDFs)

## Installation
To set up and run the project locally:

1. Clone the repository:
```sh
git clone https://github.com/yourusername/invoice-parsing-rag.git
cd invoice-parsing-rag
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Run the Streamlit app:
```sh
streamlit run invoice_extraction.py
```

## Output Example
The extracted invoice data is displayed as structured text and JSON:
```json
{
  "invoice_number": "INV-12345",
  "date": "2024-03-21",
  "items": [
    {"description": "Laptop", "quantity": 1, "unit_price": 1000, "amount": 1000},
    {"description": "Mouse", "quantity": 2, "unit_price": 50, "amount": 100}
  ],
  "total_amount": 1100
}
```

## Conclusion
This project integrates **RAG, vector databases, and LLMs** to efficiently extract structured information from invoices. It showcases the power of **LangChain, FAISS, and OpenAI's GPT models** in intelligent document processing.

Feel free to contribute, suggest improvements, or report issues!

🚀 Happy Coding!


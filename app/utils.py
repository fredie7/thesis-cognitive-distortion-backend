# Information retrieval from the CSV file using the specified columns
import pandas as pd
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_csv_info(file_path):
    df = pd.read_csv(file_path)

    # Concatenate relevant columns into a single text field for each row
    df['combined_text'] = (
        df['Patient Question'].fillna('') + ' ' +
        df['Distorted part'].fillna('') + ' ' +
        df['Dominant Distortion'].fillna('') + ' ' +
        df['Secondary Distortion (Optional)'].fillna('')
    )

    # Convert each row into a Document object
    documents = [Document(page_content=text) for text in df['combined_text'].tolist()]

    split_docs = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20
    )
    return split_docs.split_documents(documents)

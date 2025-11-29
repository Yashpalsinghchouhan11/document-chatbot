from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import os

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    reader = PdfReader(file_path)
    for page_number, page in enumerate(reader.pages):
        text += page.extract_text() + '\n'
    return text


def split_text_into_chunks(text: str) -> list:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 20,
        separators=['\n\n', '\n', ',', ' ', '']
    )
    return text_splitter.split_text(text)

def add_metadata_to_chunks(chunks, file):
    enriched_chunks = []
    file_name = os.path.basename(file)
    for index, chunk in enumerate(chunks):
        enriched_chunks.append({
            'text':chunk,
            'metadata':{
                'document_name':file_name,
                'chunk_index': index
            }
        })
            
    return enriched_chunks
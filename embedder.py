from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv                              
load_dotenv()
class Embedder:
    def __init__(self, model_name="gemini-embedding-001"):
        self.model = GoogleGenerativeAIEmbeddings(model=model_name)

    def embed_text(self, text: str):
        """Create embedding for a text chunk"""
        return self.model.embed_query(text)

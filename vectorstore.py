import chromadb
from embedder import Embedder
from langchain_chroma import Chroma


class VectorStore:
    def __init__(self, collection_name="document_chunks"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)
        self.embedder = Embedder()

    def add_chunks(self, chunks):
        for item in chunks:
            text = item["text"]
            metadata = item["metadata"]
            vector = self.embedder.embed_text(text)

            self.collection.add(
                documents=[text],
                metadatas=[metadata],
                embeddings=[vector],
                ids=[f"{metadata['document_name']}_{metadata['chunk_index']}"]
            )

        # return a LangChain vectorstore
        return Chroma(
            client=self.client,
            collection_name=self.collection.name,
            embedding_function=self.embedder.model
        )

# 📄 Document Chatbot

Chat with your PDF documents using AI! This project implements a Retrieval-Augmented Generation (RAG) system that allows you to have intelligent conversations with your documents.

## 🌟 Overview

Document Chatbot is a learning project built while exploring RAG pipelines and agent development using LangChain and LangGraph. Upload any PDF document and ask questions—the AI will retrieve relevant information and provide accurate, contextual answers.

## 🏗️ Architecture

The system follows a classic RAG pattern with two main workflows:

### Document Processing Pipeline
1. **Upload Document** → User uploads a PDF file
2. **Scrape PDF** → PDFScraper extracts text content
3. **Split Text** → TextSplitter breaks content into chunks
4. **Create Embeddings** → Gemini embedding model converts chunks to vectors
5. **Store** → VectorStore saves embeddings for retrieval

### Query Pipeline
1. **Send Query** → User asks a question
2. **Retrieve Chunks** → VectorStore finds relevant document sections
3. **Generate Response** → LLM uses retrieved context to answer
4. **Return Answer** → User receives the response

![Architecture Diagram](.\docu_chatbot_Diagram.drawio.png)

## 🛠️ Tech Stack

- **Python** - Core programming language
- **LangChain** - Framework for building RAG workflows
- **Google Gemini** - Embedding model and LLM
  - Gemini Embeddings for semantic search
  - Gemini LLM for answer generation
- **Vector Store** - Efficient similarity search and retrieval

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google API key for Gemini

### Installation

1. Clone the repository
```bash
git clone https://github.com/Yashpalsinghchouhan11/document-chatbot.git
cd document-chatbot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
# Create a .env file
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Usage

```python
# Example usage
python main.py
```

1. Upload your PDF document
2. Wait for processing (text extraction, chunking, embedding)
3. Start asking questions about your document
4. Get AI-powered answers based on document content

## 💡 How It Works

**Why RAG?**
Instead of sending entire documents to the LLM (expensive and slow), RAG:
- Only retrieves relevant sections using semantic search
- Sends focused context to the LLM
- Generates accurate, grounded responses
- Reduces costs and improves speed

**The Magic of Embeddings**
Documents are converted to numerical vectors that capture semantic meaning. When you ask a question, the system finds chunks with similar meaning—not just keyword matches!

## 📚 What I Learned

This project helped me understand:
- How RAG systems work in practice
- Building pipelines with LangChain
- Working with embeddings and vector databases
- Integrating Google's Gemini models
- Agent development fundamentals

## 🔮 Future Improvements

- [ ] Add support for multiple document formats (DOCX, TXT, etc.)
- [ ] Implement conversation memory
- [ ] Build a web interface using Streamlit or Gradio
- [ ] Add source citations in responses
- [ ] Optimize chunking strategy
- [ ] Implement LangGraph for complex agent workflows

## 🤝 Contributing

This is a learning project, but contributions and suggestions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Share your ideas and feedback

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- LangChain documentation and community
- Google Gemini API
- The RAG architecture pattern

---

**Note:** This is a learning project built while exploring RAG and agent development. Code may not be production-ready but serves as a solid foundation for understanding these concepts.

⭐ If you find this project helpful, please consider giving it a star!

## 📧 Contact

Yashpal Singh Chouhan
- GitHub: [@Yashpalsinghchouhan11](https://github.com/Yashpalsinghchouhan11)

---

*Happy Learning! 🚀*
import streamlit as st
from extractor import extract_text_from_pdf, split_text_into_chunks, add_metadata_to_chunks
from vectorstore import VectorStore
from retrieval import get_retriever
import tempfile
import time
from chat_history import Chatbot

st.set_page_config(page_title="PDF Q&A", layout="wide")
st.title("📄 PDF Question Answering App")

# Session state to persist vectorstore
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# upload PDF
uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        file_path = tmp.name

    st.success("PDF uploaded successfully!")

    # extract split and chunk
    # st.write("📌 Extracting text...")
    text = extract_text_from_pdf(file_path)

    # st.write("📌 Splitting into chunks...")
    chunks = split_text_into_chunks(text)

    enriched_chunks = add_metadata_to_chunks(chunks, file_path)

    # create vectorstore
    # st.write("📌 Creating vectorstore and embeddings... This may take time ⏳")

    vs = VectorStore()
    vectorstore = vs.add_chunks(enriched_chunks)

    st.session_state.vectorstore = vectorstore

    st.success("Vectorstore created successfully!")


#ask questions
st.success("Ready to ask questions!")


st.subheader("🔍 Ask a question about the PDF")

query = st.text_input("Enter your question")

if st.button("Search") and st.session_state.vectorstore:
    if not st.session_state.vectorstore:
        st.error("Please upload a PDF first.")
    else:
        # Show user message in chat
        st.session_state.chat_history.append(("user", query))


    retriever = get_retriever(st.session_state.vectorstore, k=3)
    # print(query)
    results = retriever.invoke(query)
    print(results[0].page_content)
    best_chunk = results[0].page_content if results else "No relevant information found."

    chat = Chatbot()
    response = chat.generate_response(query, best_chunk)
    print(response)
    st.session_state.chat_history.append(("bot", response))
    # print(results[0].page_content)
    # print(len(results))
    # st.write("### 🔎 Results:")

    # # for i, res in enumerate(results):
    # #     # st.markdown(f"**Result {i+1}:**")
    # #     st.info(res)
    # def stream_text():
    #     for char in results[0].page_content:
    #         yield char
    #         time.sleep(0.01)

    # st.write_stream(stream_text)

# display chat history
st.subheader("Chat History")

for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        # st.markdown(f"🤖 **Bot:** {msg}")
        def stream_text():
            for char in msg:
                yield char
                time.sleep(0.01)
        lable = st.markdown("🤖 **Bot:** ")
        bot_placeholder = st.empty()
        bot_placeholder.write_stream(stream_text)

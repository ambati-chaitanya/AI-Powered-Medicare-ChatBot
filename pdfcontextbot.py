import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/bebe1ee0-b4b6-4e99-8c43-b3d881996b31/GTKVqgNDU8.json"


# Add your API key here directly
GOOGLE_API_KEY = "API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "Answer is not available in the context." Do not provide the wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.3,
        google_api_key=GOOGLE_API_KEY  # Pass the API key here
    )

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )

    print(response)
    st.write("Reply: ", response["output_text"])


def pdfcontextbot():
    st.header("Chat with Medical PDF Context")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Leverage the power of AI to provide medical insights based on the content of uploaded medical reports. By analyzing the text within these documents, our chatbot offers accurate responses to health-related questions, enhancing your understanding of medical information.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Medical PDF Context Chat***")
            st.write("Ask a Question: Enter your question in the text input field to inquire about specific medical topics or seek clarification on information contained within the medical reports.")
            st.markdown("Submit & Process: After typing your question, click the `Submit & Process` button to initiate the analysis of the uploaded medical PDF files. The chatbot will provide a response based on the context found within these documents.")
            st.write("View Response: Once processing is complete, the chatbot will generate a response to your question. The answer will be displayed below the input field, providing relevant medical insights from the document.")
            st.write("Explore Further: Continue asking questions to delve deeper into the medical content. The chatbot is always available to assist you in navigating the context within the medical reports.")
            st.write("With these instructions, you're ready to engage with our Medical PDF Context Chatbot and unlock the medical insights hidden within your documents!")

    with col2:
        st_lottie(l1)
    
    user_question = st.text_input("Ask a Medical Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your Medical PDF Files and Click 'Submit & Process'", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks, GOOGLE_API_KEY)  # Pass the API key
                st.success("Done")

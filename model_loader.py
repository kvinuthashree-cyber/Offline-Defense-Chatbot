from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.prompts import PromptTemplate
from langchain.document_loaders.csv_loader import CSVLoader
import os

def load_qa_chain():
    # Load documents from CSV
    loader = CSVLoader(file_path="defensedata.csv")
    documents = loader.load()

    # Embed and store in Chroma vector store
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents, embedding=embeddings, persist_directory="chroma_db")

    # Load Llama model via LangChain wrapper
    llm = LlamaCpp(
        model_path="models/tinyllama.gguf",
        temperature=0.7,
        max_tokens=512,
        top_p=1,
        n_ctx=2048,
        n_threads=4,
        verbose=False,
    )

    # Custom prompt
    prompt_template = """You are a helpful defense assistant.
Context: {context}
Question: {question}
Helpful Answer:"""

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # Setup Retrieval-based QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain

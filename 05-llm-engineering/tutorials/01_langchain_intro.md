# Tutorial: Building Your First LangChain Application

Build a document question-answering app step by step.

## 📋 What We're Building

A simple Q&A bot that answers questions about a text document using LangChain.

---

## Step 1: Install Dependencies

```bash
pip install langchain langchain-openai faiss-cpu python-dotenv
```

---

## Step 2: Simple LLM Call

```python
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Simple call
response = llm.invoke([
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is LangChain?")
])
print(response.content)
```

---

## Step 3: Prompt Templates

```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {domain} teacher."),
    ("human", "Explain {concept} in simple terms for a beginner.")
])

# Use the template
prompt = template.format_messages(
    domain="machine learning",
    concept="gradient descent"
)
response = llm.invoke(prompt)
print(response.content)
```

---

## Step 4: Chains (LangChain Expression Language - LCEL)

```python
from langchain_core.output_parsers import StrOutputParser

# Build a chain: prompt | llm | output parser
chain = template | llm | StrOutputParser()

result = chain.invoke({
    "domain": "deep learning",
    "concept": "attention mechanism"
})
print(result)
```

---

## Step 5: Document Q&A with RAG

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Sample document
document = """
LangChain is a framework for developing applications powered by large language models.
It provides tools for chaining LLM calls, managing memory, and building agents.
LangChain supports multiple LLM providers including OpenAI, Anthropic, and HuggingFace.
The main components are: Models, Prompts, Chains, Indexes, Memory, and Agents.
"""

# Split document into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.create_documents([document])
print(f"Split into {len(chunks)} chunks")

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# Build Q&A chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# Ask questions
questions = [
    "What is LangChain?",
    "What are the main components of LangChain?",
    "What LLM providers does LangChain support?"
]

for q in questions:
    answer = qa_chain.invoke({"query": q})
    print(f"\nQ: {q}")
    print(f"A: {answer['result']}")
```

---

## ✅ What You Learned

- How to use `ChatOpenAI` for LLM calls
- How to create `ChatPromptTemplate` for reusable prompts
- How to build LCEL chains
- How to build a simple RAG Q&A system

**Next:** Explore [Exercise 02: LangChain Basics](../exercises/02_langchain_basics.ipynb)

# code ref: https://levelup.gitconnected.com/create-your-own-chatbox-and-train-it-in-less-than-30-lines-of-code-in-python-using-openai-and-34b1e9bc5c30

import os
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS, Chroma
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.indexes import VectorstoreIndexCreator

import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

PERSIST = False

if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = TextLoader("data.txt")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

embeddings = OpenAIEmbeddings(openai_api_key="OPEN_API_KEY")
vectors = FAISS.from_documents(loader, embeddings)
chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(temperature=0.0, model_name='text-davinci-003', openai_api_key=api_key), retriever=vectors.as_retriever())
history = []

while True:
    query = input("Enter Your Query:")
    print(chain({"question": query, "chat_history": history})["answer"])

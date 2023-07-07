import os
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import numpy as np

def main():
    #Initialize openAI key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    #Load db
    embedding_function = OpenAIEmbeddings()
    db=Chroma(persist_directory="knowledge/", embedding_function=embedding_function)
    #Ask your questions:
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=db.as_retriever())

    while True:
        query=input('Enter your query and press enter. Press Ctrl+C to exit.\n')
        response=qa.run(query)
        print(response)

if __name__ == '__main__':
    main()


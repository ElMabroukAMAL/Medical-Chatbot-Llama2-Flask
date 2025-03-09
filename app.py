from flask import Flask, render_template, jsonify, request
from src.functions import download_embedding_model
from src.prompt import *
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import os
from dotenv import load_dotenv

app =  Flask(__name__)

# load my api env
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
INDEX_NAME = os.environ.get('INDEX_NAME')

# load my embedding model
embedding_model = download_embedding_model()

# load the index
docsearch=PineconeVectorStore.from_existing_index(INDEX_NAME, embedding_model)

# Create prompt template 
prompt=PromptTemplate(template=prompt_template,input_variables=["context","input"])

# Initialize the llm
llm=CTransformers(model="llama-2-7b-chat.ggmlv3.q2_K.bin",model_type="llama")

# Create a retriever that fetches the top 1 most relevant document for a given question
retriever = docsearch.as_retriever(search_kwargs={'k': 2})

# Set up a chain that combines retrieved documents into a single prompt for the llm
QandA_chain = create_stuff_documents_chain(llm, prompt)

# Combine the retriever and the question-answer chain into a single retrieval pipeline
chain = create_retrieval_chain(retriever, QandA_chain)

@app.route("/")
def index():
    return render_template('mchat.html')


def ask_chat():
    input=request.form["msg"]
    result=chain.invoke({"context":'serious',"input":input})
    print("Response : ", result)
    print('type of result',type(result))
    return str(result['answer'])



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
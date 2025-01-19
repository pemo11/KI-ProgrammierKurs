# file: Langchain.Bsp1.py
# openai.exe ist in diesem Verzeichnis
# C:\Users\pemo24\AppData\Roaming\Python\Python312\Scripts
# pip install langchain
# pip install langchain-openai
# pip install python-dotenv

import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openAIKey = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openAIKey

# PromptTemplate
template = '''
Question: {question}
Answer:
'''
# Define the prompt
prompt = PromptTemplate(
    template=template,
    input_variable=["question"]
)

# Choose the model
model = ChatOpenAI(model="gpt-4o-mini")

# Define the output parser
output_parser = StrOutputParser()

# Build the chain
chain = prompt | model | output_parser

# Ask a question
question = "What is the capital of Germany?"
question = "Who was Steve Jobs?"
question = "Who invented AI?"

# Get the answer
answer = chain.invoke({"question":question})

# Print the answer
print(answer)

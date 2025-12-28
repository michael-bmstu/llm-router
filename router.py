from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv() # load enviroment varibales from .env file

# System prompt
PROMPT = """\
You work on the admissions committee for a Master's program in Artificial Intelligence, \
and students write to you with questions about the program, internships, and entrance exams.

Classify the question into one of the following categories: document submission, entrance examinations, curriculum and courses, internships, other.
Answer format: category name\
"""

# chat template (system prompt + user question)
prompt_template = ChatPromptTemplate([
    ("system", PROMPT),
    ("user", "{question}")
])

llm = init_chat_model(
    model="mistral-medium-latest",
    api_key=os.getenv("MISTRAL_KEY"),
    temperature=0)
chain = prompt_template | llm | StrOutputParser() # object chain for question processing pipeline


if __name__ == "__main__": # Work example (run router.py)
    # question = input("Enter your question: ")
    question = "а на какие стажировки я смогу попасть?"
    ans = chain.invoke({"question": question})
    print(ans)
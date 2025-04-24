# from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain.prompts import PromptTemplate

class MyModel(BaseModel):
    prompt_template: PromptTemplate 

    class Config:
        arbitrary_types_allowed = True
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

def generate_plan(user_query):
    prompt = ChatPromptTemplate.from_template(
        """
        You are a task planning agent.
        Decompose the following query into subtasks:

        Query: {query}

        Respond with a list of tasks.
        """
    )
    chain = prompt | llm
    result = chain.invoke({"query": user_query})
    tasks = result.content.strip().split("\n")
    return [task.strip("- ") for task in tasks if task.strip()]
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

from pydantic import BaseModel
from langchain.prompts import PromptTemplate

class SomeAgentModel(BaseModel):
    prompt: PromptTemplate  

    class Config:
        arbitrary_types_allowed = True

openai_api_key = os.getenv("OPENAI_API_KEY")
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

search = SerpAPIWrapper()
tools = [
    Tool(name="Search", func=search.run, description="useful for answering search queries")
]

def solve_task(task):
    llm = ChatOpenAI()
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    return agent.run(task)
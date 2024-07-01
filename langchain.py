pip install langchain

import getpass
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()

pip install -qU langchain-openai

import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into hindi"),
    HumanMessage(content="good morning"),
]

model.invoke(messages)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

result = model.invoke(messages)

parser.invoke(result)

chain = model | parser

chain.invoke(messages)

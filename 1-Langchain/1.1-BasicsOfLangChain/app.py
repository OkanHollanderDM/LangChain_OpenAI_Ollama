from tarfile import version

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

output_parser = StrOutputParser()
llm = Ollama(model="llama3.1")
chain = prompt_template | llm | output_parser

app = FastAPI(
    title="Langchain API",
    description="API for translating text into different languages",
    version="0.0.1",
)

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


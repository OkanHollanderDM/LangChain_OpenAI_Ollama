from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = Ollama(model="llama3.1")
query = "What is the current time?"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

if query:
    results = chain.invoke({"question": query})
    print(results)

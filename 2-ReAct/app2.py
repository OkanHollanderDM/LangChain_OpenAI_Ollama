from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description

from tools.system_time_tool import check_system_time
from tools.printing_tool import present_result

# Load environment variables
load_dotenv()

# Choose the LLM to use
llm = Ollama(model="llama3.1")

# Set the tools
tools = [check_system_time, present_result]

# Render text descriptions for the tools for inclusion in the prompt
tool_descriptions = render_text_description(tools)

# Set my message (input query)
query = "What is the current time? When you find the time, please present it to me."

# Define the input variables and agent scratchpad
input_variables = ["input", "agent_scratchpad"]

# Improved React prompt template to avoid infinite formatting retries
template = """
You are an intelligent agent with access to the following tools:

{tools}

Please follow these format instructions exactly. Do not retry or reformat responses after reaching the final answer.

Use this format:

Thought: Do I need to use a tool? Yes  
Action: the action to take, should be one of [{tool_names}]  
Action Input: the input to the action  
Observation: the result of the action 

Follow this process step by step and do not reformat the response once the final answer is reached.

**Question**: {input}
**Thought**: {agent_scratchpad}
"""

# Manually format the prompt with tools and tool names
prompt_template = PromptTemplate(
    template=template,
    input_variables=input_variables,
    partial_variables={
        "tools": tool_descriptions,
        "tool_names": ", ".join([t.name for t in tools])
    }
)

# Construct the ReAct agent with the formatted prompt string
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, max_iterations=3)

# Invoke the agent executor to get the current time
agent_executor.invoke({
    "input": query,
    "agent_scratchpad": ""
})

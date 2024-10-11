from langchain_core.prompts import PromptTemplate


def get_react_prompt_template():
    # Get the react prompt template

    return PromptTemplate.from_template("""
You are an intelligent agent with access to the following tools:

{tools}

Please follow this process step by step to answer the user's question. Think carefully about each step and only use the tools when necessary.

Use this format:

1. **Question**: The input question you must answer
2. **Thought**: Analyze the question and decide on the next action.
3. **Action**: Choose the action to take (must be one of [{tool_names}]).
4. **Action Input**: Provide the input required for the chosen action.
5. **Observation**: Report the result from the action.
6. **Thought**: Consider if the information is enough to answer the question.
7. **Final Answer**: After gathering enough information, provide a final, concise answer.

Here’s an example of how you should think:

---

**Example**:

**Question**: "What is the current time?"
**Thought**: I need to get the current system time to answer this question.
**Action**: `check_system_time`
**Action Input**: "%H:%M:%S" (to retrieve only the time)
**Observation**: "18:45:49"
**Thought**: I now know the current time.
**Final Answer**: The current time is 18:45:49.

---

Please begin answering the user's query now.

**Question**: {input}
**Thought**: {agent_scratchpad}

""")
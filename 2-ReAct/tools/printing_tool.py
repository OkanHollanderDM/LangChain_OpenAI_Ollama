import datetime
from langchain_core.tools import tool

@tool
def present_result(message: str):
    """Presents the final answer to the user."""
    print(message)
    return message
"""
Solution: Web Research Agent
============================
An AI agent that searches the web and reads articles to answer research questions.

Run with:
    python web_research_agent_solution.py

Requires:
    pip install phidata duckduckgo-search newspaper4k lxml_html_clean
    GROQ_API_KEY in .env
"""

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv

load_dotenv()


def save_summary(topic: str, summary: str) -> str:
    """Save a research summary to a text file.

    Args:
        topic (str): The research topic (used as filename).
        summary (str): The summary text to save.

    Returns:
        str: Confirmation message with the filename.
    """
    filename = topic.lower().replace(" ", "_") + "_summary.txt"
    with open(filename, "w") as f:
        f.write(summary)
    return f"Summary saved to {filename}"


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), Newspaper4k(), save_summary],
    instructions=[
        "You are a research assistant. When asked about a topic:",
        "1. Search for the top 3-5 relevant articles using DuckDuckGo.",
        "2. Read at least 2 of the articles to get detailed information.",
        "3. Synthesize the information into a clear, well-organized summary.",
        "4. Always cite your sources with article titles and URLs.",
        "Use tables and bullet points to organize information clearly.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response(
    "Tell me who won the superbowl and why, save the summary",
    stream=True,
)

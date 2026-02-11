# Project: Build an AI Agent

## Overview

In the demo, we built a finance agent that uses YFinance tools to fetch stock data. For this project, you will build a **web research agent** that can search the internet and read articles to answer questions on any topic.

You have two options:

- **Option A (Default):** Build a web research agent using DuckDuckGo and Newspaper4k (described below).
- **Option B (Custom):** Build an agent for a use case of your choosing — any tools or APIs you find useful.

If you go with Option B, the same requirements apply — just substitute your own tools.

---

## Option A: Web Research Agent

### The Idea

Build an agent that can:
1. **Search the web** for articles on a topic
2. **Read articles** to extract detailed information
3. **Synthesize** what it finds into a clear summary

This follows the exact same pattern as the finance demo — just with different tools.

---

### Requirements

Your agent must include:

1. **At least 2 tools** — DuckDuckGo for searching + Newspaper4k for reading articles. You can add more (see ideas below).

2. **Instructions** — Tell the agent how to behave (e.g., how many articles to read, how to format output, always cite sources).

3. **A custom function tool** — Write at least one Python function the agent can call. Examples:
   - Save a summary to a file
   - Format results as bullet points
   - Filter results by date or relevance
   - Count words or estimate reading time

4. **A research query** — Choose a topic you're interested in and have the agent research it.

---

### Getting Started

1. **Install dependencies:**
   ```bash
   pip install phidata duckduckgo-search newspaper4k lxml_html_clean
   ```

2. **Make sure your `.env` has your Groq key** (same one from the demo):
   ```
   GROQ_API_KEY=your_key_here
   ```

3. **Create your agent file.** Start from this template — it mirrors the finance demo structure:

   ```python
   from phi.agent import Agent
   from phi.model.groq import Groq
   from phi.tools.duckduckgo import DuckDuckGo
   from phi.tools.newspaper4k import Newspaper4k
   from dotenv import load_dotenv

   load_dotenv()


   # TODO: Write a custom function tool here
   # (look at get_company_symbol from the demo for the pattern)


   agent = Agent(
       model=Groq(id="llama-3.3-70b-versatile"),
       tools=[DuckDuckGo(), Newspaper4k()],  # TODO: add your custom function
       instructions=[
           # TODO: Add 2-3 instructions telling the agent how to research
       ],
       show_tool_calls=True,
       markdown=True,
   )

   agent.print_response(
       "Your research question here",
       stream=True,
   )
   ```

4. **Run it:**
   ```bash
   python your_agent_file.py
   ```

---

### Side-by-Side: Demo vs. Your Agent

| | Finance Demo | Your Research Agent |
|---|---|---|
| **Built-in tools** | `YFinanceTools` | `DuckDuckGo`, `Newspaper4k` |
| **Custom function** | `get_company_symbol()` | Your function (e.g., save summary) |
| **Instructions** | "Use tables", "Use get_company_symbol" | Your instructions (e.g., "Read at least 2 articles") |
| **Query** | Compare TSLA vs MSFT | Your research question |

The code structure is identical — you're just swapping the tools and instructions.

---

## Deliverables

1. Your `.py` file containing the agent code.
2. Run your agent and show the output — either live or as a screenshot. The output should show:
   - The agent searching for articles (tool calls visible)
   - The agent reading at least one article
   - A synthesized answer with sources cited

---

## Rubric

| Criteria | Points |
|---|---|
| 2+ tools (DuckDuckGo + Newspaper4k) | 25 |
| 1+ custom function tool | 25 |
| Clear instructions that shape agent behavior | 15 |
| Interesting research query with good output | 10 |
| Demo / screenshot of working agent | 25 |
| **Total** | **100** |

---

## Option B: Custom Agent

If you want to build something different, go for it. Some ideas:

- **Multi-agent team** — Combine a web search agent with the finance agent from the demo
- **Code explainer** — An agent that reads code files and explains what they do
- **Email drafter** — An agent that researches a topic and drafts a professional email about it
- **Study assistant** — An agent that searches for explanations of concepts and creates flashcard-style summaries

The same rubric applies: 2+ tools, 1+ custom function, instructions, and a demo.

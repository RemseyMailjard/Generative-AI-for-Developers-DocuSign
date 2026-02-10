# Generative AI for Developers Workshop

A hands-on workshop teaching developers how to build applications with Large Language Models (LLMs). Covers prompt engineering, RAG, chatbots, AI agents, and MCP servers using Groq's API and open-source Llama models.

## Access the Virtual Environment

Add your name to the [sign-up sheet](https://docs.google.com/spreadsheets/d/1n_uxwnjiG_R9e86O8ieb5KLzWBok4vQlXhQXV6V80gU/edit?gid=547734190#gid=547734190) to claim your username, then sign in using the instructions included in the sheet.

## Repository Layout

```
.
├── EXTRA NOTES/       # Supplemental reading (PDFs on RAG, Agents, MCP, etc.)
├── LAB EXERCISES/     # Lab exercise instructions and handouts
├── NOTEBOOKS/         # Jupyter notebooks for hands-on labs
├── PDFs/              # Slide decks and lecture reference materials
├── PROJECTS/          # Day 2 project code
│   ├── AI-AGENT/      #   Finance agent using phi + Groq
│   └── MCP-SERVER/    #   Leave management MCP server for Claude Desktop
├── requirements.txt   # Python dependencies for all labs and projects
└── SETUP.md           # Environment setup instructions
```

## Slide Decks (Google Slides)

1) [Generative AI Holistic Perspective](https://docs.google.com/presentation/d/16Kur530IjKau_ldGXsqF_LYisjnePTua/edit?usp=drive_link&ouid=109036277148056682596&rtpof=true&sd=true)

2) [Prompt Engineering](https://docs.google.com/presentation/d/1GrBvkt-BpbIw0fEiPYDaVCNLOf-E7n4D/edit?usp=drive_link&ouid=109036277148056682596&rtpof=true&sd=true)

3) [RAG](https://docs.google.com/presentation/d/1mEdV93GCjAR9sLydqxQZgO_6k3n4rY7q/edit?usp=drive_link&ouid=109036277148056682596&rtpof=true&sd=true)

4) [AI Agents + MCP](https://docs.google.com/presentation/d/18CWz2N2x9VE7qwPLCy5Dokwbq7u5c3P5/edit?usp=drive_link&ouid=109036277148056682596&rtpof=true&sd=true)

5) [AI Ethics and Safety](https://docs.google.com/presentation/d/1mo0IRrU78hI0-vvZs2pJT32MWrZyPAlZ/edit?usp=drive_link&ouid=109036277148056682596&rtpof=true&sd=true)

## Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key
# Create a .env file:
echo "GROQ_API_KEY=your_key_here" > .env

# 4. Register Jupyter kernel
pip install ipykernel
python -m ipykernel install --user --name=genai-workshop

# 5. Launch Jupyter
jupyter notebook
```

See [SETUP.md](SETUP.md) for detailed setup instructions and troubleshooting.

## API Keys

| Provider | Cost | URL |
|----------|------|-----|
| Groq | Free tier | https://console.groq.com |

## Technologies Used

- **Groq API** - Fast LLM inference (Llama 3.3 70B, Llama 3.1 8B)
- **LangChain** - RAG pipeline orchestration
- **FAISS** - Vector similarity search
- **phi (phidata)** - AI agent framework
- **MCP** - Model Context Protocol for tool integration
- **Jupyter** - Interactive notebook environment

## Resources

- [Copilot Skills - How Context Is Managed](https://claude.ai/public/artifacts/c1b84eb3-10d9-41df-8204-43ca8516d826)
- [Instructions vs Agents vs Prompts vs Skills: When to use each?](https://claude.ai/public/artifacts/f9a0c59a-ca44-4383-b7b4-33bb89221645)
- **Create Custom Copilot Customization Files**: [Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) | [Instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) | [Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) | [Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
- [Link for RAG Notebook](https://colab.research.google.com/drive/1I0VsN4F0WLv2wKoZeONcM1xlw3_kuaMM)
- [Glean MCP Information](https://claude.ai/public/artifacts/fe719fb4-66fa-46d4-8ce6-b3e094a03b80)
- [MCP Config File Documentation for VS Code and Copilot](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)

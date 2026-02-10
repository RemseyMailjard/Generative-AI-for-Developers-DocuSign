# Notebooks

Jupyter notebooks for the hands-on labs. All notebooks use the Groq API with Llama models.

## Contents

| Notebook | Day | Topic |
|----------|-----|-------|
| [Prompt_Engineering_with_Groq.ipynb](https://colab.research.google.com/drive/1Bqs9gxZa7HrL2ttn-O_dZ4nxK8KHtvSG) | 1 | Prompt engineering techniques across diverse language tasks |
| [Zero_Shot_Few_Shot_and_Chain_of_Thought_Prompting_with_Groq.ipynb](https://colab.research.google.com/drive/1lmDYIFXUmNsi9l3qtFcs0xM9JMZcBfo7) | 1 | Zero-shot, few-shot, and chain-of-thought prompting patterns |
| [Retrieval_Augmented_Generation_(RAG)_with_Groq.ipynb](https://colab.research.google.com/drive/1I0VsN4F0WLv2wKoZeONcM1xlw3_kuaMM)) | 2 | Building a RAG pipeline with FAISS and Groq |

## Prerequisites

1. Complete the environment setup in [SETUP.md](../SETUP.md)
2. Have a Groq API key set in your `.env` file
3. Select the `genai-workshop` Jupyter kernel

## Running

```bash
# From the workshop root directory
source .venv/bin/activate
jupyter notebook
```

Then navigate to this folder and open any notebook.

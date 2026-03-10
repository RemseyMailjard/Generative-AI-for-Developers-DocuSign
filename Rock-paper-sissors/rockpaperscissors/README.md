
# Rock Paper Scissors Game

A simple, interactive Rock Paper Scissors game where you play against the computer. Features both a command-line and a modern web interface using Streamlit.

---

## Features

- Play classic Rock Paper Scissors against a computer opponent
- Web UI built with [Streamlit](https://streamlit.io/) for a friendly experience
- Score tracking for both player and computer
- Play as many rounds as you like, or reset scores anytime
- Clean, minimal code with clear separation of logic and UI

## Quick Start

### 1. Requirements
- Python 3.7+
- [Streamlit](https://streamlit.io/) (for web UI)

### 2. Installation
```sh
pip install streamlit
```

### 3. Run the Web App
```sh
streamlit run rps.py
```

### 4. Play in the Terminal
Run the classic version:
```sh
python rps_ugly.py
```

---

## Project Structure

```text
rockpaperscissors/
├── rps.py         # Streamlit web app
├── rps_ugly.py    # Minimal terminal version
├── README.md      # Project documentation
```

## How to Play

- **Web App:** Click a button to choose Rock, Paper, or Scissors. The computer picks randomly. Scores update automatically.
- **Terminal:** Type your choice when prompted. Type 'quit' to exit.

> [!TIP]
> Use the web app for a modern, interactive experience. The terminal version is great for quick demos or learning Python basics.

---

## Credits

Created for educational purposes. Inspired by classic coding exercises and modern Python best practices.

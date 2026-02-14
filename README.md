# 🤖 OpenClaw Agents UI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern web interface for managing and chatting with OpenClaw Agents using Streamlit.

## ✨ Features

- 💬 **Interactive Chat** - Modern chat interface with streaming responses
- 🤖 **Agent Management** - Create, delete, and update agent identities
- 🚀 **Auto Terminal Launcher** - Opens terminal automatically to create new agents
- ⚙️ **Advanced Options** - Thinking level, verbose mode, timeout settings
- 🎨 **Modern UI** - Clean Streamlit interface with sidebar controls

## 📋 Requirements

- Python 3.8+
- [OpenClaw CLI](https://github.com/spos/openclaw) installed and configured
- Streamlit:
  ```bash
  pip install streamlit
🚀 Quick Start
bash
# Clone the repository
git clone https://github.com/DrMoRobot/openclaw-web-ui.git
cd openclaw-web-ui

# Run the application
streamlit run streamlit_agent_manager.py
Or use the included script:

bash
./run-openclaw-ui.sh
📁 Project Structure
text
openclaw-web-ui/
├── streamlit_agent_manager.py    # Main application code
├── run-openclaw-ui.sh            # Quick launch script
├── README.md                     # This file
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore rules
🛠️ Usage
Chat Tab
Select your active agent from the sidebar

Type messages in the chat input

View conversation history

Agents Tab
Refresh agents list - Load agents from OpenClaw CLI

Create new agent - Opens terminal to run openclaw agents add <id>

Update identity - Change name, theme, and emoji

Delete agent - Remove agent and its workspace

Advanced Options
Access from the sidebar:

Thinking Level: Control reasoning depth (off, minimal, low, medium, high, xhigh)

Verbose: Output detail level (off, on, full)

Timeout: Request timeout in seconds

Local Mode: Run with local models only

JSON Mode: Return raw JSON responses

🖼️ Screenshots
Coming soon

🤝 Contributing
Contributions are welcome! Please:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
GitHub: @DrMoRobot

Email: muhammadabdulhussien@gmail.com
Telegram Channel: @DrMoRobot_Channel

# 🤖 OpenClaw Agents UI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern web interface for managing and chatting with OpenClaw Agents using Streamlit.

---

## ✨ Features

- 💬 **Interactive Chat** - Modern chat interface with streaming responses
- 🤖 **Agent Management** - Create, delete, and update agent identities
- 🚀 **Auto Terminal Launcher** - Opens terminal automatically to create new agents
- ⚙️ **Advanced Options** - Thinking level, verbose mode, timeout settings
- 🎨 **Modern UI** - Clean Streamlit interface with sidebar controls

---

## 📋 Requirements

Before you start, make sure you have:

- **Python 3.8** or higher
- **OpenClaw CLI** installed and configured
- **pip** (Python package manager)

### Check Your Python Version
```bash
python --version
# or
python3 --version
🚀 Quick Start - Installation Guide
Step 1️⃣: Install Python Dependencies
First, install the required package:

bash
pip install streamlit
If you're on Mac/Linux, you might need:

bash
pip3 install streamlit
Verify Installation:

bash
streamlit --version
Step 2️⃣: Install OpenClaw CLI
Follow the instructions at: https://github.com/spos/openclaw

Or use:

bash
pip install openclaw
Configure OpenClaw:

bash
openclaw configure
Step 3️⃣: Clone the Repository
bash
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui
Step 4️⃣: Run the Application
Option A: Using the Quick Launch Script (Recommended)
On Windows (PowerShell or CMD):

bash
python -m streamlit run streamlit_agent_manager.py
On Mac/Linux:

bash
./run-openclaw-ui.sh
Or manually:

bash
streamlit run streamlit_agent_manager.py
Option B: Manual Execution
bash
streamlit run streamlit_agent_manager.py
🌐 What Happens After You Run It
Local Server Starts: The application will open in your default browser

URL: Usually http://localhost:8501

Dashboard Opens: You'll see the main interface with two tabs:

Chat Tab - Chat with your agents

Agents Tab - Manage your agents

If Port 8501 is Already in Use
Run on a different port:

bash
streamlit run streamlit_agent_manager.py --server.port 8502
📁 Project Structure
text
openclaw-Agents-ui/
├── streamlit_agent_manager.py    # Main application code
├── run-openclaw-ui.sh             # Quick launch script
├── README.md                       # This file
├── LICENSE                         # MIT License
├── .gitignore                      # Git ignore rules
└── screenshots/                    # UI screenshots
🛠️ How to Use the Application
Chat Tab 💬
Select your active agent from the sidebar dropdown

Type your message in the chat input field

Press Enter or click Send

View real-time responses in the conversation history

Agents Tab 🤖
Refresh Agents List
Click "Refresh" to load all available agents from OpenClaw CLI

Create New Agent
Click "Create New Agent"

A terminal window will open automatically

Follow the OpenClaw prompts to create a new agent

Return to the UI and refresh to see your new agent

Update Agent Identity
Select an agent

Click "Update Identity"

Change:

Name: Agent's display name

Theme: Color theme (blue, green, red, etc.)

Emoji: Choose an emoji to represent the agent

Delete Agent
Select an agent

Click "Delete Agent"

Confirm the deletion

Advanced Options ⚙️
Access from the left sidebar:

Option	Description	Values
Thinking Level	Control reasoning depth	off, minimal, low, medium, high, xhigh
Verbose	Output detail level	off, on, full
Timeout	Request timeout (seconds)	1-300
Local Mode	Run with local models only	Toggle On/Off
JSON Mode	Return raw JSON responses	Toggle On/Off
🖼️ Screenshots

🆘 Troubleshooting
Issue: "Command not found: streamlit"
Solution:

bash
pip install --upgrade streamlit
Issue: "OpenClaw CLI not found"
Solution: Install OpenClaw first:

bash
pip install openclaw
openclaw configure
Issue: "Port 8501 already in use"
Solution: Use a different port:

bash
streamlit run streamlit_agent_manager.py --server.port 8502
Issue: "Permission denied" on run-openclaw-ui.sh
Solution: Make it executable (Mac/Linux only):

bash
chmod +x run-openclaw-ui.sh
Issue: "No module named 'streamlit'"
Solution: Install Streamlit:

bash
pip install streamlit
📚 System Requirements
Component	Minimum	Recommended
Python	3.8	3.9+
RAM	2GB	4GB+
Disk Space	500MB	1GB+
OS	Windows/Mac/Linux	Any
🤝 Contributing
Contributions are welcome! Please:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact & Community
GitHub: @DrMoRobot

Email: muhammadabdulhussien@gmail.com

Community: Join our Telegram Channel

🔄 Development Status
Current Version: v0.8-fixed

Recent Updates ✅
✅ Fixed agent ID reading from JSON (id field instead of agentId)

✅ Modern chat interface with st.chat_message & st.chat_input

✅ Auto terminal launcher for agent creation

✅ Advanced agent options (thinking, verbose, timeout)

✅ Agent identity customization

✅ UI Screenshots added

Upcoming Features 🔮
📊 Agent conversation history visualization

💾 Save/Load chat sessions

🔔 Agent notifications

🎯 Skills/Workflows shortcuts

🌍 Multi-language support

📱 Mobile-friendly interface

📖 Complete Installation Walkthrough
For Windows Users 🪟
bash
# 1. Install Python (if not installed)
# Download from https://www.python.org/downloads/

# 2. Open Command Prompt or PowerShell

# 3. Install Streamlit
pip install streamlit

# 4. Install OpenClaw
pip install openclaw
openclaw configure

# 5. Clone the repository
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui

# 6. Run the application
python -m streamlit run streamlit_agent_manager.py

# 7. Open your browser to http://localhost:8501
For Mac/Linux Users 🐧
bash
# 1. Install Python (if not installed)
brew install python3  # Mac
sudo apt-get install python3  # Linux

# 2. Open Terminal

# 3. Install Streamlit
pip3 install streamlit

# 4. Install OpenClaw
pip3 install openclaw
openclaw configure

# 5. Clone the repository
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui

# 6. Make script executable
chmod +x run-openclaw-ui.sh

# 7. Run the application
./run-openclaw-ui.sh

# 8. Open your browser to http://localhost:8501
Made with ❤️ using Streamlit & OpenClaw

⭐ Star this repo • 📝 Report Issue • 💬 Join Community

<div align="center">

  <!-- Animated Logo -->
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Robot.png" alt="OpenClaw Agents UI Logo" width="120" height="120" />

  <h1>🤖 OpenClaw Agents UI</h1>
  
  <p>
    <strong>Next-Generation Web Interface for OpenClaw AI Agents</strong>
  </p>

  <!-- Badges -->
  <p>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"></a>
    <a href="https://streamlit.io"><img src="https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
    <a href="https://github.com/DrMoRobot/openclaw-Agents-ui/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=open-source-initiative&logoColor=white" alt="MIT License"></a>
    <a href="#"><img src="https://img.shields.io/badge/Version-v0.8--fixed-blueviolet?style=for-the-badge&logo=github&logoColor=white" alt="Version"></a>
  </p>

  <p>
    <a href="#-quick-start">🚀 Quick Start</a> •
    <a href="#-features">✨ Features</a> •
    <a href="#-screenshots">📸 Screenshots</a> •
    <a href="#-documentation">📚 Docs</a>
  </p>

  <!-- Animated Divider -->
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="Divider" />

</div>

## 🎯 Overview

**OpenClaw Agents UI** transforms the way you interact with AI agents. Built on top of the powerful OpenClaw CLI and the elegant Streamlit framework, this interface delivers a **seamless, intuitive, and visually stunning** experience for managing and conversing with your AI agents.

> 💡 *"Where powerful AI meets beautiful design"*

### ✨ What Makes Us Different?

- **🚀 Zero-Config Setup** — Get running in under 60 seconds
- **🎨 Modern UI/UX** — Clean, responsive, and dark-mode friendly
- **⚡ Real-Time Streaming** — Watch your agents think in real-time
- **🔧 Fully Customizable** — Tailor every agent to your needs

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 💬 Interactive Chat Experience
- **Streaming responses** — See replies as they generate
- **Rich chat history** — Persistent conversation context
- **Smart suggestions** — Context-aware prompt hints
- **Export conversations** — Save chats as Markdown or JSON

</td>
<td width="50%">

### 🤖 Intelligent Agent Management
- **One-click creation** — Auto-terminal launcher integration
- **Identity customization** — Name, theme, emoji & personality
- **Advanced controls** — Thinking depth, verbosity, timeout settings
- **Multi-agent support** — Switch between agents seamlessly

</td>
</tr>
<tr>
<td width="50%">

### ⚙️ Advanced Configuration
- **Thinking levels:** Off → Minimal → Low → Medium → High → X-High
- **Verbose modes:** Off / On / Full debug output
- **Timeout controls:** 1-300 seconds flexibility
- **Local mode:** Run entirely offline
- **JSON mode:** Raw API responses

</td>
<td width="50%">

### 🎨 Beautiful Interface
- **Streamlit-native** — Fast, responsive, and reliable
- **Sidebar controls** — Non-intrusive settings panel
- **Visual feedback** — Loading states and progress indicators
- **Cross-platform** — Windows, macOS, and Linux

</td>
</tr>
</table>

---

## 🚀 Quick Start

Get up and running in **3 simple steps**:

### Prerequisites

```bash
# ✅ Python 3.8 or higher
python --version

# ✅ OpenClaw CLI installed
pip install openclaw
openclaw configure
Step 1: Install Dependencies
bash
# Install Streamlit
pip install streamlit

# Verify installation
streamlit --version
Step 2: Clone & Launch
bash
# Clone the repository
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui

# Launch the application
./run-openclaw-ui.sh        # Mac/Linux
# OR
python -m streamlit run streamlit_agent_manager.py  # Windows
Step 3: Start Chatting! 🎉
text
🌐 Your browser will open automatically at: http://localhost:8501
<details> <summary>🔧 <strong>Port already in use?</strong></summary>
bash
# Run on a different port
streamlit run streamlit_agent_manager.py --server.port 8502
</details>
📸 Screenshots
<div align="center">
💬 Chat Interface	🤖 Agent Management
<img src="screenshots/chat-tab.png" alt="Chat Interface" width="400" />	<img src="screenshots/agents-tab.png" alt="Agent Management" width="400" />
Seamless conversation flow	Create, customize & manage
⚙️ Advanced Settings	🎨 Identity Customization
<img src="screenshots/settings.png" alt="Settings" width="400" />	<img src="screenshots/identity.png" alt="Identity" width="400" />
Fine-tune your experience	Make it yours
</div>
📚 Documentation
🖥️ Platform-Specific Guides
<details> <summary><strong>🪟 Windows Installation</strong></summary>
powershell
# 1. Install Python from https://python.org/downloads/

# 2. Open PowerShell or CMD as Administrator

# 3. Install dependencies
pip install streamlit openclaw

# 4. Configure OpenClaw
openclaw configure

# 5. Clone and run
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui
python -m streamlit run streamlit_agent_manager.py

# 6. Open http://localhost:8501 in your browser
</details> <details> <summary><strong>🍎 macOS Installation</strong></summary>
bash
# 1. Install Python (if not present)
brew install python3

# 2. Install dependencies
pip3 install streamlit openclaw

# 3. Configure OpenClaw
openclaw configure

# 4. Clone and run
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui
chmod +x run-openclaw-ui.sh
./run-openclaw-ui.sh

# 5. Open http://localhost:8501 in your browser
</details> <details> <summary><strong>🐧 Linux Installation</strong></summary>
bash
# 1. Install Python
sudo apt-get update
sudo apt-get install python3 python3-pip

# 2. Install dependencies
pip3 install streamlit openclaw

# 3. Configure OpenClaw
openclaw configure

# 4. Clone and run
git clone https://github.com/DrMoRobot/openclaw-Agents-ui.git
cd openclaw-Agents-ui
chmod +x run-openclaw-ui.sh
./run-openclaw-ui.sh

# 5. Open http://localhost:8501 in your browser
</details>
🎮 Usage Guide
💬 Chatting with Agents
text
1. Select your agent from the sidebar dropdown
2. Type your message in the chat input
3. Press Enter or click Send
4. Watch the streaming response in real-time
5. Continue the conversation naturally
🤖 Managing Agents
Action	Steps
Create Agent	Click "Create New Agent" → Follow terminal prompts → Refresh list
Update Identity	Select agent → Click "Update Identity" → Modify name/theme/emoji
Delete Agent	Select agent → Click "Delete Agent" → Confirm
Refresh List	Click "Refresh" to sync with OpenClaw CLI
⚙️ Advanced Options
Access these from the left sidebar:

Option	Description	Values
Thinking Level	Control reasoning depth	off → xhigh
Verbose Mode	Output detail level	off / on / full
Timeout	Request timeout (seconds)	1-300
Local Mode	Run with local models only	Toggle On/Off
JSON Mode	Return raw JSON responses	Toggle On/Off
🏗️ Architecture
text
openclaw-Agents-ui/
├── 📄 streamlit_agent_manager.py    # Main application entry point
├── 🔧 run-openclaw-ui.sh            # Quick launch script (Unix)
├── 📖 README.md                      # This beautiful documentation
├── 📜 LICENSE                        # MIT License
├── 🚫 .gitignore                     # Git ignore rules
└── 📸 screenshots/                   # UI screenshots & demos
🔄 Data Flow
text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Streamlit UI  │────▶│  Agent Manager  │────▶│  OpenClaw CLI   │
│                 │     │                 │     │                 │
│  -  Chat Input   │     │  -  Create       │     │  -  Agent API    │
│  -  Sidebar      │     │  -  Delete       │     │  -  LLM Backend  │
│  -  Settings     │     │  -  Update       │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                                               │
         └───────────────────────────────────────────────┘
                            Response Stream
💻 System Requirements
Component	Minimum	Recommended
Python	3.8	3.10+
RAM	2 GB	4 GB+
Disk Space	500 MB	1 GB+
OS	Windows/Mac/Linux	Latest versions
Browser	Chrome/Firefox/Edge	Latest versions
🛠️ Troubleshooting
<details> <summary><strong>❌ "Command not found: streamlit"</strong></summary>
bash
# Solution: Reinstall Streamlit
pip install --upgrade streamlit

# Verify installation
streamlit --version
</details> <details> <summary><strong>❌ "OpenClaw CLI not found"</strong></summary>
bash
# Solution: Install and configure OpenClaw
pip install openclaw
openclaw configure
</details> <details> <summary><strong>❌ "Port 8501 already in use"</strong></summary>
bash
# Solution: Use a different port
streamlit run streamlit_agent_manager.py --server.port 8502
# Or any port: 8503, 8504, etc.
</details> <details> <summary><strong>❌ "Permission denied" on run script</strong></summary>
bash
# Solution: Make script executable (Mac/Linux only)
chmod +x run-openclaw-ui.sh

# Then run again
./run-openclaw-ui.sh
</details> <details> <summary><strong>❌ "No module named 'streamlit'"</strong></summary>
bash
# Solution: Install Streamlit
pip install streamlit

# For Mac/Linux use pip3 if needed
pip3 install streamlit
</details>
🗺️ Roadmap
✅ Completed (v0.8)
 Fixed agent ID reading from JSON

 Modern chat interface with st.chat_message & st.chat_input

 Auto terminal launcher for agent creation

 Advanced agent options (thinking, verbose, timeout)

 Agent identity customization

 UI Screenshots added

🔮 Coming Soon
 📊 Agent conversation history visualization

 💾 Save/Load chat sessions

 🔔 Real-time agent notifications

 🎯 Skills/Workflows shortcuts

 🌍 Multi-language support (Arabic, Chinese, Spanish, etc.)

 📱 Enhanced mobile-friendly interface

 🔐 User authentication system

 🌐 Cloud deployment templates

🤝 Contributing
We welcome contributions from the community! Here's how you can help:

bash
# 1. Fork the repository

# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m '✨ Add amazing feature'

# 4. Push to the branch
git push origin feature/amazing-feature

# 5. Open a Pull Request
📋 Contribution Guidelines
🐛 Bug Reports: Use GitHub Issues with detailed steps

💡 Feature Requests: Open an issue with the enhancement label

🔧 Pull Requests: Ensure code follows existing style

📖 Documentation: Help improve our docs!

📞 Support & Community
<div align="center">
Platform	Link
🐙 GitHub	@DrMoRobot
📧 Email	muhammadabdulhussien@gmail.com
| 💬 **Telegram** | [Join our Community](https://t.me/Aiforeveryone2026) |

</div>
📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

<div align="center"> <h3>⭐ Star this repository if you find it helpful!</h3> <p> <a href="https://github.com/DrMoRobot/openclaw-Agents-ui/stargazers">⭐ Star</a> • <a href="https://github.com/DrMoRobot/openclaw-Agents-ui/issues">🐛 Report Bug</a> • <a href="https://github.com/DrMoRobot/openclaw-Agents-ui/issues">💡 Request Feature</a> </p> <br> <p><strong>Made with ❤️ using Streamlit & OpenClaw</strong></p> <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Robot.png" alt="Robot" width="60" /> <p><sub>© 2024 OpenClaw Agents UI. All rights reserved.</sub></p> </div> ```

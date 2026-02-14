#!/usr/bin/env python3
import streamlit as st
import subprocess
import json
import platform
import shutil

APP_VERSION = "v0.8"

# ---------- BASIC CONFIG ----------
st.set_page_config(
    page_title="OpenClaw Web UI",
    page_icon="🦞",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- HELPERS ----------
def load_agents():
    """Uses: openclaw agents list --json"""
    try:
        result = subprocess.run(
            ["openclaw", "agents", "list", "--json"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            return []
        data = json.loads(result.stdout or "[]")
        # BUG WAS HERE: using "agentId" instead of "id"
        # FIXED: use "id" which is the correct field name
        agents = [a.get("id", "") for a in data if a.get("id")]
        return agents
    except Exception:
        return []

def get_agent_details():
    """Get full agent details including name, emoji, etc."""
    try:
        result = subprocess.run(
            ["openclaw", "agents", "list", "--json"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            return {}
        data = json.loads(result.stdout or "[]")
        # Create dict of id -> details
        details = {}
        for a in data:
            agent_id = a.get("id", "")
            if agent_id:
                details[agent_id] = a
        return details
    except Exception:
        return {}

def call_openclaw_agent(agent_id: str, message: str, opts: dict) -> str:
    """Single-turn agent run"""
    cmd = [
        "openclaw",
        "agent",
        "--agent",
        agent_id,
        "--message",
        message,
    ]
    thinking = opts.get("thinking", "off")
    verbose = opts.get("verbose", "off")
    timeout = int(opts.get("timeout", 120))
    local_mode = bool(opts.get("local", False))
    json_mode = bool(opts.get("json_mode", False))

    if thinking and thinking != "off":
        cmd.extend(["--thinking", thinking])
    if verbose and verbose != "off":
        cmd.extend(["--verbose", verbose])
    if timeout and timeout != 120:
        cmd.extend(["--timeout", str(timeout)])
    if local_mode:
        cmd.append("--local")
    if json_mode:
        cmd.append("--json")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout or 120,
        )
    except subprocess.TimeoutExpired:
        return "Error: timed out while waiting for OpenClaw."
    except FileNotFoundError:
        return "Error: 'openclaw' command not found in PATH."
    except Exception as e:
        return f"Error: {e}"

    if result.returncode == 0:
        output = result.stdout.strip()
        return output if output else "(no output)"
    else:
        err = result.stderr.strip() or "unknown error"
        return f"Error from OpenClaw: {err}"

def run_set_identity(agent_id: str, name: str, theme: str, emoji: str) -> str:
    """Use: openclaw agents set-identity <id> ..."""
    cmd = ["openclaw", "agents", "set-identity", agent_id]
    if name.strip():
        cmd.extend(["--name", name.strip()])
    if theme.strip():
        cmd.extend(["--theme", theme.strip()])
    if emoji.strip():
        cmd.extend(["--emoji", emoji.strip()])

    if len(cmd) == 3:
        return "Nothing to update: please set at least one field."

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except Exception as e:
        return f"Error: {e}"

    if result.returncode == 0:
        return "Identity updated successfully."
    else:
        return f"Error from OpenClaw: {result.stderr.strip() or 'unknown error'}"

def run_delete_agent(agent_id: str) -> str:
    """Delete an agent: openclaw agents delete <id>"""
    try:
        result = subprocess.run(
            ["openclaw", "agents", "delete", agent_id],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except Exception as e:
        return f"Error: {e}"

    if result.returncode == 0:
        return "Agent deleted successfully."
    else:
        return f"Error from OpenClaw: {result.stderr.strip() or 'unknown error'}"

def open_terminal_with_command(command: str) -> bool:
    """Opens a new terminal window and runs the command."""
    system = platform.system()
    
    if system == "Linux":
        terminals = [
            ["gnome-terminal", "--", "bash", "-c", f"{command}; exec bash"],
            ["konsole", "-e", "bash", "-c", f"{command}; exec bash"],
            ["xterm", "-e", f"bash -c '{command}; exec bash'"],
            ["xfce4-terminal", "-e", f"bash -c '{command}; exec bash'"],
            ["lxterminal", "-e", f"bash -c '{command}; exec bash'"],
            ["terminator", "-e", f"bash -c '{command}; exec bash'"],
            ["alacritty", "-e", "bash", "-c", f"{command}; exec bash"],
        ]
        
        for term_cmd in terminals:
            terminal_name = term_cmd[0]
            if shutil.which(terminal_name):
                try:
                    subprocess.Popen(term_cmd)
                    return True
                except Exception:
                    continue
        return False
    
    elif system == "Darwin":
        try:
            script = f'''
            tell application "Terminal"
                do script "{command}"
                activate
            end tell
            '''
            subprocess.Popen(["osascript", "-e", script])
            return True
        except Exception:
            return False
    
    return False

# ---------- SESSION STATE ----------
if "agents" not in st.session_state:
    detected_agents = load_agents()
    st.session_state.agents = detected_agents if detected_agents else []
    # Only use fallback if truly empty
    if not st.session_state.agents:
        st.session_state.agents = ["main"]  # Will refresh on first load

if "current_agent" not in st.session_state:
    st.session_state.current_agent = st.session_state.agents[0] if st.session_state.agents else "main"

if "agent_details" not in st.session_state:
    st.session_state.agent_details = {}

if "messages" not in st.session_state:
    st.session_state.messages = []

if "advanced_opts" not in st.session_state:
    st.session_state.advanced_opts = {
        "thinking": "off",
        "verbose": "off",
        "timeout": 120,
        "local": False,
        "json_mode": False,
    }

def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🦞 OpenClaw")
    st.caption("Local Web UI for your agents")
    st.caption(f"Version: {APP_VERSION}")

    st.session_state.current_agent = st.selectbox(
        "Active agent",
        st.session_state.agents,
        index=st.session_state.agents.index(st.session_state.current_agent)
        if st.session_state.current_agent in st.session_state.agents
        else 0,
    )

    with st.expander("Advanced agent options"):
        thinking = st.selectbox(
            "Thinking level",
            ["off", "minimal", "low", "medium", "high", "xhigh"],
            index=["off", "minimal", "low", "medium", "high", "xhigh"].index(
                st.session_state.advanced_opts.get("thinking", "off")
            ),
        )
        verbose = st.selectbox(
            "Verbose",
            ["off", "on", "full"],
            index=["off", "on", "full"].index(
                st.session_state.advanced_opts.get("verbose", "off")
            ),
        )
        timeout = st.slider("Timeout (seconds)", 30, 600, 120, 10)
        local_mode = st.checkbox("Run locally (--local)", value=False)
        json_mode = st.checkbox("Return JSON (--json)", value=False)

        st.session_state.advanced_opts = {
            "thinking": thinking,
            "verbose": verbose,
            "timeout": timeout,
            "local": local_mode,
            "json_mode": json_mode,
        }

    st.markdown("---")
    st.markdown("**Tips**")
    st.markdown("- Chat with the active agent in the Chat tab.")
    st.markdown("- Create new agents in the Agents tab.")

# ---------- MAIN TABS ----------
tab_chat, tab_agents = st.tabs(["💬 Chat", "🤖 Agents"])

# ===== TAB 1: CHAT =====
with tab_chat:
    st.markdown(
        f"""
        <h2 style="text-align:center; color:#4CAF50;">
            OpenClaw Agent Chat
        </h2>
        <p style="text-align:center; color:#AAAAAA;">
            Chatting with agent: <b>{st.session_state.current_agent}</b>
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "assistant"
        with st.chat_message(role):
            st.markdown(msg["content"])

    prompt = st.chat_input("Type your message for the agent here...")
    if prompt:
        add_message("user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Contacting agent..."):
                reply = call_openclaw_agent(
                    st.session_state.current_agent,
                    prompt,
                    st.session_state.advanced_opts,
                )
                st.markdown(reply)
        add_message("assistant", reply)

# ===== TAB 2: AGENTS =====
with tab_agents:
    st.markdown(
        """
        <h2 style="text-align:center; color:#4CAF50;">
            Agents Overview
        </h2>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("Manage your OpenClaw agents.")

    # --- Refresh List ---
    if st.button("🔄 Refresh agents list"):
        st.session_state.agents = load_agents()
        st.session_state.agent_details = get_agent_details()
        
        if st.session_state.agents:
            st.success(f"✅ Found {len(st.session_state.agents)} agents: {st.session_state.agents}")
            # Update current agent if not valid
            if st.session_state.current_agent not in st.session_state.agents:
                st.session_state.current_agent = st.session_state.agents[0]
        else:
            st.warning("⚠️ No agents found. Create one below.")

    agents_list = st.session_state.agents

    if not agents_list:
        st.warning("No agents detected. Create one below.")
    else:
        # Show agents in a nice table
        st.write(f"**Available Agents ({len(agents_list)}):**")
        
        # Display as cards
        for agent_id in agents_list:
            details = st.session_state.agent_details.get(agent_id, {})
            name = details.get("name", agent_id)
            emoji = details.get("emoji", "🤖")
            model = details.get("model", "Unknown")
            is_default = details.get("isDefault", False)
            
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.write(f"{emoji} **{name}**")
            with col2:
                st.caption(f"ID: `{agent_id}` | Model: `{model}`")
                if is_default:
                    st.caption("⭐ Default agent")
            with col3:
                if agent_id == st.session_state.current_agent:
                    st.success("✓ Active")
            st.markdown("---")

        # Select active agent
        selected_from_tab = st.radio(
            "Set active agent",
            agents_list,
            index=agents_list.index(st.session_state.current_agent)
            if st.session_state.current_agent in agents_list
            else 0,
            key="agent_selector",
        )

        if selected_from_tab != st.session_state.current_agent:
            st.session_state.current_agent = selected_from_tab
            st.success(f"Active agent changed to: {selected_from_tab}")
            st.rerun()

    # --- Create New Agent (Auto Terminal) ---
    st.markdown("---")
    st.markdown("### ➕ Create New Agent")

    new_agent_id = st.text_input(
        "New agent ID (e.g. `sales`, `research`, `marketing`)",
        value="",
        max_chars=40,
        help="Unique ID for the new agent. No spaces.",
        key="new_agent_input",
    )

    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("🚀 Open Terminal & Create Agent", type="primary"):
            if not new_agent_id.strip():
                st.warning("Please enter an agent ID first.")
            else:
                agent_id_clean = new_agent_id.strip()
                if agent_id_clean in st.session_state.agents:
                    st.error(f"Agent '{agent_id_clean}' already exists!")
                else:
                    cmd = f"openclaw agents add {agent_id_clean}"
                    success = open_terminal_with_command(cmd)
                    if success:
                        st.success("""
                        ✅ Terminal opened! 
                        
                        1. Complete the wizard in the new terminal (select model + OAuth)
                        2. Close the terminal when done  
                        3. Click **Refresh agents list** above to see the new agent
                        """)
                        st.balloons()
                    else:
                        st.error("❌ Could not open terminal automatically.")
                        st.info("Please open a terminal manually and run:")
                        st.code(cmd)

    with col2:
        if st.button("📋 Copy Command Only"):
            if not new_agent_id.strip():
                st.warning("Please enter an agent ID first.")
            else:
                cmd = f"openclaw agents add {new_agent_id.strip()}"
                st.code(cmd)
                st.info("Copy the command above and run it in any terminal.")

    # --- Update Identity ---
    st.markdown("---")
    st.markdown("### ✏️ Update Identity")

    with st.form("identity_form"):
        col_n, col_t, col_e = st.columns(3)
        with col_n:
            name = st.text_input("Name", value="", help="Display name")
        with col_t:
            theme = st.text_input("Theme", value="", help="e.g. work/personal")
        with col_e:
            emoji = st.text_input("Emoji", value="", max_chars=4)

        submit_identity = st.form_submit_button("Apply Identity")

    if submit_identity:
        msg = run_set_identity(st.session_state.current_agent, name, theme, emoji)
        if msg.startswith("Error"):
            st.error(msg)
        else:
            st.success(msg)
            # Refresh to get updated details
            st.session_state.agent_details = get_agent_details()

    # --- Delete Agent ---
    st.markdown("---")
    st.markdown("### 🗑️ Delete Agent")

    delete_confirm = st.checkbox(
        "I understand this will permanently delete the agent and its workspace."
    )

    if st.button("Delete Active Agent", type="secondary"):
        if not delete_confirm:
            st.warning("Please confirm deletion by checking the box above.")
        else:
            msg = run_delete_agent(st.session_state.current_agent)
            if msg.startswith("Error"):
                st.error(msg)
            else:
                st.success(msg)
                # Refresh after deletion
                st.session_state.agents = load_agents()
                st.session_state.agent_details = get_agent_details()
                if st.session_state.agents:
                    st.session_state.current_agent = st.session_state.agents[0]
                else:
                    st.session_state.current_agent = "main"
                st.rerun()

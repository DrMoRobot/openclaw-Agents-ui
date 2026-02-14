#!/bin/bash
# تشغيل واجهة OpenClaw Web UI من venv

# 0) إضافة مسار openclaw إلى PATH
export PATH="$HOME/.npm-global/bin:$PATH"

# 1) تفعيل البيئة الافتراضية
source "$HOME/openclaw-ui-venv/bin/activate"

# 2) الدخول إلى مجلد المشروع
cd "$HOME/Desktop/openclaw_tool"

# 3) تشغيل Streamlit عبر run_app.py
python run_app.py

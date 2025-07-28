#!/data/data/com.termux/files/usr/bin/bash
cd $(dirname "$0")
pip install flask > /dev/null 2>&1
FLASK_APP=app.py flask run --host=0.0.0.0 --port=7860

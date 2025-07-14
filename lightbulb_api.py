from flask import Flask, request, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # ✅ loads variables from .env

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "").strip()

# ✅ Use a local directory
EXPORT_FOLDER = "/Users/YOURPATH/DIRECTORY"

@app.route('/createLightbulb', methods=['POST'])
def save_lightbulb():
    auth_header = request.headers.get("X-API-Key", "").strip()
    print("🔐 Header received:", repr(auth_header))
    print("🔐 API key expected:", repr(API_KEY))

    if auth_header != API_KEY:
        print("❌ Unauthorized attempt.")
        return jsonify({"error": "Unauthorized"}), 401

    try:
        lightbulb = request.get_json()
        os.makedirs(EXPORT_FOLDER, exist_ok=True)

        safe_title = lightbulb['title'].replace(" ", "_").replace("/", "-")
        filename = f"{lightbulb['id']}_{safe_title}.md"
        filepath = os.path.join(EXPORT_FOLDER, filename)

        content = f"""---
id: {lightbulb['id']}
title: {lightbulb['title']}
thread_title: {lightbulb['thread_title']}
internal_reference: {lightbulb['internal_reference']}
context: {lightbulb['context']}
tags: {lightbulb['tags']}
somatic_signal: {lightbulb['somatic_signal']}
insight: {lightbulb['insight']}
created: {datetime.today().strftime('%Y-%m-%d')}
---

# {lightbulb['title']}

{lightbulb['insight']}

_Context:_ {lightbulb['context']}

_Somatic signal:_ {lightbulb['somatic_signal']}

_Tags:_ {' '.join(f'#{tag}' for tag in lightbulb['tags'])}
"""
        print("📄 Writing file to:", filepath)
        with open(filepath, 'w') as f:
            f.write(content)

        return jsonify({"success": True}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)

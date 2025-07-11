from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# ✅ Use a local directory that works in Render
EXPORT_FOLDER = "./notes"

@app.route('/createLightbulb', methods=['POST'])
def save_lightbulb():
    try:
        lightbulb = request.get_json()

        # Make sure the export folder exists
        os.makedirs(EXPORT_FOLDER, exist_ok=True)

        # Safe filename
        safe_title = lightbulb['title'].replace(" ", "_").replace("/", "-")
        filename = f"{lightbulb['id']}_{safe_title}.md"
        filepath = os.path.join(EXPORT_FOLDER, filename)

        # Full markdown content with frontmatter
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

        with open(filepath, 'w') as f:
            f.write(content)

        return jsonify({"message": "Lightbulb entry created successfully", "success": True}), 201

    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)

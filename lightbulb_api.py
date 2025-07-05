from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

EXPORT_FOLDER = "/Users/sarahensor/Vaults/Vaultaire/01 ZETTELKASTEN"

@app.route('/lightbulb', methods=['POST'])
def save_lightbulb():
    lightbulb = request.json

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

    with open(filepath, 'w') as f:
        f.write(content)

    return jsonify({"status": "saved", "success"}), 200

if __name__ == '__main__':
    app.run(port=5001)

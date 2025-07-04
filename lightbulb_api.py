from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

EXPORT_FOLDER = "/Users/sarahensor/Vaults/Vaultaire/01 ZETTELKASTEN"

@app.route('/lightbulb', methods=['POST'])
def save_lightbulb():
    lightbulb = request.json

    safe_title = lightbulb['title'].replace(" ", "_").replace("/", "-")
    filename = f"{lightbulb['id']***REMOVED***_{safe_title***REMOVED***.md"
    filepath = os.path.join(EXPORT_FOLDER, filename)

    content = f"""---
id: {lightbulb['id']***REMOVED***
title: {lightbulb['title']***REMOVED***
thread_title: {lightbulb['thread_title']***REMOVED***
internal_reference: {lightbulb['internal_reference']***REMOVED***
context: {lightbulb['context']***REMOVED***
tags: {lightbulb['tags']***REMOVED***
somatic_signal: {lightbulb['somatic_signal']***REMOVED***
insight: {lightbulb['insight']***REMOVED***
created: {datetime.today().strftime('%Y-%m-%d')***REMOVED***
---

# {lightbulb['title']***REMOVED***

{lightbulb['insight']***REMOVED***

_Context:_ {lightbulb['context']***REMOVED***

_Somatic signal:_ {lightbulb['somatic_signal']***REMOVED***

_Tags:_ {' '.join(f'#{tag***REMOVED***' for tag in lightbulb['tags'])***REMOVED***
"""

    with open(filepath, 'w') as f:
        f.write(content)

    return jsonify({"status": "saved", "path": filepath***REMOVED***)

if __name__ == '__main__':
    app.run(port=5001)
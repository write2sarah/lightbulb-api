# 🌟 Lightbulb Tracker API + GPT Companion

Welcome, explorer of sparks! This is the home of the [Lightbulb Tracker API](https://chatgpt.com/g/g-686800dc63fc819192aeb5b8212eb840-lightbulb-tracker-v2), a gentle backend tool that works in tandem with a custom GPT (Lightbulb Tracker V2) to log insights, somatic yeses, and idea flashes directly into your Obsidian vault.

This repo is designed for dreamers, tinkerers, and thought-cartographers who want their GPTs to not only generate—but to *remember, organize,* and *file* the light.

---

## 🧠 What This Is

A local Python API (built with Flask) that:
•	Receives structured insight data from a Custom GPT
•	Writes .md files in Zettelkasten-friendly format
•	Saves them directly into a folder you control—like your Obsidian vault

You host it. You own it. No external deployment required.

---

## 🤖 How It Works With the GPT

You’ll need:
	•	A Custom GPT (like Lightbulb Tracker V2)
	•	This API running on your local machine (using Flask + optional Ngrok)

When a lightbulb strikes in conversation with your GPT, it:
	1.	Gathers your insight’s metadata (title, tags, somatic signal, etc.)
	2.	Sends a POST request to your local API endpoint
	3.	This API writes a .md file with frontmatter into your vault

Voilà—your insight has a home.

---

## 🗂️ File Format

Eash insight is saved like this:

```yaml
---
id: L0001
title: Example Lightbulb
thread_title: Big Thoughts on Tuesday
internal_reference: 2025-07-01_LightbulbThread
context: This came to me while journaling
tags: [insight, identity, metaphor]
somatic_signal: jaw dropped, eyes welled up
insight: I think I just met my true question.
created: 2025-07-01
---
```

And rendered as:

```md
# Example Lightbulb

I think I just met my true question.

_Context:_ This came to me while journaling  
_Somatic signal:_ jaw dropped, eyes welled up  
_Tags:_ #insight #identity #metaphor
```

---

## 🚀 Getting Started (Local)

### 1. Clone the Repo
```bash
git clone https://github.com/write2sarah/lightbulb-api.git
cd lightbulb-api
```
### 2. Set up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Add a .env File
```env
API_KEY=your_secret_key_here
EXPORT_FOLDER=/path/to/your/Obsidian/vault/folder
```
### 4. Run the API

```bash
python lightbulb_api.py
```

### 5. (Optional) Use [ngrok](https://ngrok.com)

```bash
ngrok http 5001
```
Copy the generated https://... URL and plug it into your GPT’s backend endpoint setting.

## 🔐 Security Note

This tool is designed for your vault. To keep your insights safe:
	•	Don’t expose your EXPORT_FOLDER path in public repos
	•	Always use a strong API key in your .env file
	•	Never commit .env to Git

Need to scrub old secrets? Use BFG Repo Cleaner.

---

## 🧾 requirements.txt

```txt
Flask==2.3.2
python-dotenv==1.0.1
```

---

## 🌱 Coming Soon
	•	Metadata templating
	•	Constellation-based tag clustering
	•	Local-first Obsidian Sync Engine
	•	GPT whisperback modes + tag suggestions

⸻

## 🧪 Future Magic
	•	Timestamp-based sorting
	•	Obsidian plugin integration
	•	Google Sheets or SQLite export
	•	AI-summarized Zettel clusters
	•	Fog/fire filtering by state or phase

⸻

## ✨ Created by Sarah Ensor

A writer, strategist, and soul-coded system builder exploring creative collaboration with AI, human rhythms, and poetic infrastructure.

🌐 write2sarah.com

⸻

📖 License

MIT License. Fork it, remix it, make it yours.

⸻

Let me know if you’d like to:
	•	Add screenshots or example .md output
	•	Include the GPT action JSON block
	•	Add a “Troubleshooting” section

---

## ✨ Created by Sarah Ensor

A writer, strategist, and soul-coded system builder exploring creative collaboration with AI, human rhythms, and poetic infrastructure.

More at [write2sarah.com](https://write2sarah.com)

---

## 📖 License

MIT License. Feel free to fork, remix, and evolve.

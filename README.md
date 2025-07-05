# 🌟 Lightbulb Tracker API + GPT Companion

Welcome, explorer of sparks! This is the home of the **Lightbulb Tracker API**, a gentle backend tool that works in tandem with a custom GPT (Lightbulb Tracker V2) to log insights, somatic yeses, and idea flashes directly into your Obsidian vault.

This repo is designed for dreamers, tinkerers, and thought-cartographers who want their GPTs to not only generate—but to *remember, organize,* and *file* the light.

---

## 🧠 What This Is

A Flask-based Python API that:

* Receives structured insight data from a custom GPT
* Writes `.md` files in Zettelkasten-friendly format
* Organizes entries in a local folder (e.g. your Obsidian vault)

Optionally deployable via [Render](https://render.com) or run locally via Flask + Ngrok.

---

## 🤖 How It Works With the GPT

You’ll need:

* A **Custom GPT** (Lightbulb Tracker V2)
* This API, deployed and reachable (e.g., on `https://your-app.onrender.com`)

When a lightbulb strikes in conversation with your GPT, the GPT:

1. Gathers the structured fields (title, tags, somatic signal, etc.)
2. Sends a POST request to this API’s `/lightbulb` endpoint
3. This API writes it to your folder as a `.md` file with YAML frontmatter

You now have a tangible trace of ephemeral insight.

---

## 🗂️ File Format

The markdown files include 8 metadata fields:

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

With friendly rendering below:

```md
# Example Lightbulb

I think I just met my true question.

_Context:_ This came to me while journaling

_Somatic signal:_ jaw dropped, eyes welled up

_Tags:_ #insight #identity #metaphor
```

---

## 🚀 Getting Started

### 📍 Local Use

1. Clone this repo
2. Create a virtual environment
3. Install dependencies

```bash
cd lightbulb-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the server:

```bash
python lightbulb_api.py
```

5. Use [ngrok](https://ngrok.com) to expose your localhost:

```bash
ngrok http 5001
```

Update your GPT’s endpoint to use the ngrok URL.

### 🌐 Deploy to Render (recommended)

1. Fork this repo to your GitHub
2. Create a [Render account](https://render.com)
3. Click "New Web Service", connect your GitHub repo
4. Use these settings:

   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `python lightbulb_api.py`
   * **Runtime**: Python 3.11+
5. Add environment variables if needed (e.g., `EXPORT_FOLDER` path)

---

## 🔐 Security Note

If you're using this for personal insights, keep it private. If you ever put it public:

* Remove your `EXPORT_FOLDER` path or use environment variables
* Scrub API keys from your history (see [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/))
* Consider deploying with GitHub Secrets + `.env` support

---

## 🧾 requirements.txt

```txt
Flask==2.3.2
python-dotenv==1.0.1
```

---

## 🌱 Coming Soon

* Optional OpenAI key integration for GPT-side validation
* Metadata templating
* Tag clustering + constellation visualization
* Obsidian Sync Engine (v2!)

---

## 🪄 Future Ideas
	•	Multi-tag filtering
	•	Timestamp-based sorting
	•	Obsidian plugin integration
	•	Google Sheets export
	•	AI-summarized Zettel clusters

---

## ✨ Created by Sarah Ensor

A writer, strategist, and soul-coded system builder exploring creative collaboration with AI, human rhythms, and poetic infrastructure.

More at [write2sarah.com](https://write2sarah.com)

---

## 📖 License

MIT License. Feel free to fork, remix, and evolve.

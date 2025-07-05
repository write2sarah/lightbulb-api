# 🌟 Lightbulb Tracker — API Companion

Welcome to the API engine for the **Lightbulb Tracker V2**, a creative insights logging system designed to work in tandem with a Custom GPT. This API captures your lightbulb moments—those flashes of insight, clarity, or embodied “yes”—and exports them as Markdown files to your personal vault.

This project is designed for:
- 🧠 Thinkers and creators using a **Zettelkasten** or **Obsidian**-based system
- ✨ People who want their AI-generated insights stored in **human-readable**, versionable files
- 🤖 Builders and tinkerers who use a **Custom GPT** to log creative ideas, somatic signals, or reflections

---

## 🚀 How It Works

The GPT (Lightbulb Tracker V2) sends a POST request to this API with metadata and content from an insight.

The API:
1. Receives the lightbulb entry
2. Formats it into a Markdown file
3. Saves it in a folder inside your Obsidian vault

---

## 📦 What This Repo Contains

- `lightbulb_api.py` — the Flask app that processes and saves insights
- `requirements.txt` — needed Python packages
- `.env` — optional file for storing secrets (see below)
- `README.md` — (this file!)

---

## 🛠️ Setup (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/write2sarah/lightbulb-api.git
cd lightbulb-api
```
### 2. Set Your Export Folder
Edit the line inside lightbulb_api.py:
```python
EXPORT_FOLDER = "/Users/yourname/Vaults/YourVault/01 ZETTELKASTEN"
```
Make sure this folder exists and is writable.
### 3. Create a Virtual Environment (optional but encouraged)
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Run Locally
```bash
python lightbulb_api.py
```
This will launch the server at http://localhost:5001.

---

## 🌐 Deploy to the Web (Optional)

This API was originally deployed using Render, a free web app hosting platform.

To deploy:
	1.	Create a Render account
	2.	Connect to your GitHub repo
	3.	Add your export location as an environment variable (or remove it if you’re not writing to disk)
	4.	Redeploy after updates

---

## 🔐 Secrets & Keys

If you use an API key (e.g., to authorize GPT access), store it in a .env file:
```bash
OPENAI_API_KEY=your-key-here
```
Then, use os.getenv('OPENAI_API_KEY') in your Python code instead of hardcoding it.

---

## 🤝 Connect to the Custom GPT

This API is meant to work with the Lightbulb Tracker V2 Custom GPT. The GPT is configured to POST entries to this endpoint whenever you log a lightbulb.

If you’d like help configuring that GPT, reach out or open an issue.

---

## 🌀 Why Markdown?

Because Markdown
	•	allows for versions
	•	is readable by humans
	•	syncs with Obsidian
	•	is elegant

You get to own your insights in a versatile format.

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

More at write2sarah.com

---

## 📖 License

MIT License. Feel free to fork, remix, and evolve.

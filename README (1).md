# BowBot — Rule-Based AI Chatbot (Flask + HTML/CSS/JS) 🎗️

A web-based rule-based chatbot with a sky-blue, ChatGPT-style interface, built with a **Python (Flask) backend** and an **HTML/CSS/JS frontend**. This is Project 1 of an AI Engineering training track focused on control flow and rule-based logic.

## ✨ Features

- Sky-blue chat-app theme with sidebar, recent chats, and "+ New Chat" button
- Welcome screen with clickable topic cards: AI, Image Generation, Machine Learning, Python, Motivation, Who are you?
- Quick-reply chips below the input box
- Typing indicator animation before bot replies
- Flask backend handles all chatbot logic via a `/chat` API endpoint
- 40+ rule-based responses with a fallback for unrecognized input
- Fully responsive layout

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, vanilla JavaScript (fetch API)

## 📂 Project Structure

```
BowBot/
├── app.py                 # Flask app + chatbot logic (knowledge base, routes)
├── templates/
│   └── index.html         # Chat UI markup
├── static/
│   ├── style.css          # Sky-blue chat UI styling
│   └── script.js          # Frontend chat interactions
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/bowbot-chatbot.git
   cd bowbot-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

5. Click a topic card (AI, Image Generation, Machine Learning, Python, Motivation, Who are you) or type your own message.

## 🧠 How It Works

- The frontend sends the user's message to the `/chat` endpoint via a `fetch()` POST request.
- The Flask backend sanitizes the input (lowercase + strip), looks it up in a Python dictionary (`responses`), and returns a JSON reply.
- If no match is found, a fallback message is returned.
- The frontend renders the conversation, animates a typing indicator, and logs each new conversation in the sidebar.

## 💡 Future Enhancements

- Persist chat history using a database or local storage
- Add keyword/partial matching instead of exact-match only
- Connect a real LLM API as a fallback for unrecognized questions (hybrid architecture)
- Add user authentication for multi-user chat history

## 📄 License

This project is open source and available under the MIT License.

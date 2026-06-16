// script.js — BowBot chat UI logic

const messagesEl = document.getElementById('messages');
const welcomeScreen = document.getElementById('welcomeScreen');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const recentList = document.getElementById('recentList');
const newChatBtn = document.getElementById('newChatBtn');
const quickChips = document.getElementById('quickChips');
const topicCards = document.querySelectorAll('.topic-card');

let chatStarted = false;
let chatCounter = 0;

function showChatView() {
  if (!chatStarted) {
    welcomeScreen.style.display = 'none';
    messagesEl.classList.add('active');
    chatStarted = true;
  }
}

function addMessage(text, sender) {
  const row = document.createElement('div');
  row.className = `msg-row ${sender}`;

  const avatar = document.createElement('div');
  avatar.className = 'msg-avatar';
  avatar.textContent = sender === 'bot' ? '🎗️' : 'Y';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.textContent = text;

  row.appendChild(avatar);
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return bubble;
}

function showTypingIndicator() {
  const row = document.createElement('div');
  row.className = 'msg-row bot';
  row.id = 'typingRow';

  const avatar = document.createElement('div');
  avatar.className = 'msg-avatar';
  avatar.textContent = '🎗️';

  const bubble = document.createElement('div');
  bubble.className = 'msg-bubble';
  bubble.innerHTML = '<span class="typing-dots"><span></span><span></span><span></span></span>';

  row.appendChild(avatar);
  row.appendChild(bubble);
  messagesEl.appendChild(row);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function removeTypingIndicator() {
  const row = document.getElementById('typingRow');
  if (row) row.remove();
}

function addRecentChatEntry(firstMessage) {
  chatCounter += 1;
  const id = `chat-${chatCounter}`;

  document.querySelectorAll('.recent-item').forEach((el) => el.classList.remove('active'));

  const item = document.createElement('div');
  item.className = 'recent-item active';
  item.dataset.id = id;
  item.innerHTML = `<span class="recent-dot">○</span> ${firstMessage}`;
  recentList.prepend(item);
}

async function sendMessage(text) {
  const trimmed = text.trim();
  if (!trimmed) return;

  const isFirstMessage = !chatStarted;
  showChatView();
  addMessage(trimmed, 'user');
  if (isFirstMessage) {
    addRecentChatEntry(trimmed.length > 28 ? trimmed.slice(0, 28) + '…' : trimmed);
  }
  userInput.value = '';

  showTypingIndicator();

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: trimmed }),
    });
    const data = await response.json();

    await new Promise((resolve) => setTimeout(resolve, 500)); // small delay for natural feel
    removeTypingIndicator();
    addMessage(data.reply, 'bot');
  } catch (err) {
    removeTypingIndicator();
    addMessage('Something went wrong connecting to the server. Is Flask running?', 'bot');
  }
}

sendBtn.addEventListener('click', () => sendMessage(userInput.value));

userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    sendMessage(userInput.value);
  }
});

quickChips.addEventListener('click', (e) => {
  const chip = e.target.closest('.chip');
  if (chip) sendMessage(chip.dataset.text);
});

topicCards.forEach((card) => {
  card.addEventListener('click', () => sendMessage(card.dataset.text));
});

newChatBtn.addEventListener('click', () => {
  messagesEl.innerHTML = '';
  messagesEl.classList.remove('active');
  welcomeScreen.style.display = 'flex';
  chatStarted = false;
});

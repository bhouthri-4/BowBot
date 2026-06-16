
# =============================================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -----------------------------
# Knowledge Base
# A dictionary mapping recognized inputs (intents) to fixed responses.
# -----------------------------
responses = {
    # Greetings
    'hello': 'Hi there! How can I help you today?',
    'hi': 'Hello! Nice to see you.',
    'hey': 'Hey! What can I do for you?',
    'good morning': 'Good morning! Hope you have a great day ahead.',
    'good afternoon': 'Good afternoon! Hope your day is going well.',
    'good evening': 'Good evening! How was your day?',
    'good night': 'Good night! Sleep well.',

    # Farewells
    'bye': 'Goodbye! It was nice talking to you.',
    'see you': 'See you soon! Take care.',
    'see you later': 'Catch you later!',

    # Identity & small talk
    'how are you': "I'm running smoothly, all logic gates blue and bright! How about you?",
    'what is your name': 'I am BowBot, your friendly assistant.',
    'who are you': "I'm BowBot, Project 1 of an AI training internship. I was built using Python and HTML!",
    'tell me about yourself': "I'm BowBot, Project 1 of an AI training internship. I was built using Python and HTML!",
    'introduce yourself': "I'm BowBot, Project 1 of an AI training internship. I was built using Python and HTML!",
    'tell me about you': "I'm BowBot, Project 1 of an AI training internship. I was built using Python and HTML!",
    'what are you': "I'm BowBot, Project 1 of an AI training internship. I was built using Python and HTML!",
    'what can you do': 'I can chat about greetings, basic questions, AI concepts, and small talk!',
    'are you human': 'Nope, I am 100% code. No coffee breaks needed.',
    'are you a robot': 'Yes, I am a friendly rule-based chatbot.',
    'who made you': 'I was created as part of an AI engineering training project.',
    'help': 'Try asking me things like "what is AI", "tell me a joke", "what is Python", or just say "hello"!',


    # AI / tech topics (matches the topic cards in the UI)
    'what is ai': 'AI (Artificial Intelligence) is the ability of machines to simulate human-like thinking and decision-making.',
    'what is artificial intelligence': 'Artificial Intelligence is the ability of machines to simulate human-like thinking and decision-making.',
    'what is image generation': 'Image generation is when AI models create brand-new images from text descriptions, using techniques like diffusion models.',
    'what is machine learning': 'Machine Learning is a branch of AI where machines learn patterns from data instead of following fixed rules.',
    'what is deep learning': 'Deep Learning uses layered neural networks to learn complex patterns, inspired by how the human brain works.',
    'what is python': 'Python is a beginner-friendly programming language widely used for AI, web development, and automation.',
    'what is css': 'CSS (Cascading Style Sheets) makes web pages look beautiful, things like colors, spacing, and layout come from CSS!',
    'what is html': 'HTML (HyperText Markup Language) is the structure of every webpage, it defines the content and layout.',
    'what is a loop': 'A loop lets a program repeat a set of instructions automatically until a condition is met.',
    'loop in programming': 'A loop repeats a block of code automatically until a stopping condition is met, like a while or for loop.',

    # Motivation
    'motivation': "Every expert was once a beginner. Keep showing up, and progress will follow.",
    'motivate me': "You don't have to be great to start, but you have to start to be great. Keep going!",
    'i need motivation': "Small steps every day lead to big results. You've got this!",
    'inspire me': "The only way to fail is to stop trying. Keep building, keep learning.",

    # Gratitude
    'thanks': 'You are welcome!',
    'thank you': 'Anytime! Happy to help.',

    # Emotions & feelings
    'i am fine': 'Glad to hear that!',
    'i am good': 'Awesome! That makes me happy.',
    'i am sad': 'I am sorry to hear that. I hope things get better soon.',
    'i am happy': 'That is great to hear!',
    'i am bored': 'How about learning something new? I am always up for a chat.',
    'i am tired': 'Maybe take a short break. You deserve it!',

    # Compliments & reactions
    'you are smart': 'Thank you! I try my best.',
    'you are funny': 'Haha, glad I could make you smile!',
    'i like you': 'Aww, thanks! I like talking to you too.',
    'good job': 'Thank you! I appreciate that.',

    # Fun
    'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs!',
    'more jokes': 'Why did the developer go broke? Because he used up all his cache!',

    # Apology / confusion
    'sorry': 'No worries at all!',
    'oops': 'It happens! No big deal.',

    # Yes/No
    'yes': 'Got it!',
    'no': 'Okay, no problem.',
    'maybe': 'That is fair, take your time deciding.',
}

# Default fallback message for unrecognized input
FALLBACK = "I do not understand that yet. Try asking about AI, Python, or just say hello!"


def get_bot_reply(user_message: str) -> str:
    """Sanitize input and look up a rule-based response with fallback."""
    clean_input = user_message.lower().strip()

    # Nested condition example: catch "name" anywhere in the message
    if 'name' in clean_input and clean_input not in responses:
        return "I'm BowBot, your AI assistant!"

    return responses.get(clean_input, FALLBACK)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get('message', '')

    if not user_message.strip():
        return jsonify({'reply': 'Please type something so I can help!'})

    reply = get_bot_reply(user_message)
    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(debug=True)

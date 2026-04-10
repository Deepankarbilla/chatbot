import random

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "how_are_you": {
        "patterns": ["how are you", "how are you doing"],
        "responses": ["I'm doing great!", "All good!", "Feeling awesome!"]
    },
    "name": {
        "patterns": ["your name", "who are you"],
        "responses": ["I am your AI chatbot 🤖", "You can call me ChatBot!"]
    },
    "help": {
        "patterns": ["help", "what can you do"],
        "responses": ["I can chat with you, answer basic questions, and help you!"]
    },
    "bye": {
        "patterns": ["bye", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!", "Bye! Take care "]
    }
}

def find_intent(user_input):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return None

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        intent = find_intent(user_input)

        if intent:
            response = random.choice(intents[intent]["responses"])
            print("Chatbot:", response)

            if intent == "bye":
                break
        else:
            print("Chatbot:", random.choice([
                "I didn't understand that.",
                "Can you say that differently?",
                "I'm still learning!"
            ]))

chatbot()

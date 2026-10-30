
import json
import re
from pathlib import Path


# Load FAQ data from JSON file
def load_faq_data():
    try:
        file_path = Path(__file__).parent / "sample_faq.json"

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: FAQ dataset file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: FAQ dataset contains invalid JSON.")
        return None

    except OSError as error:
        print(f"Error reading FAQ file: {error}")
        return None


# Clean user messages
def normalize_text(text):
    text = text.lower()
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


# Detect greetings
def is_greeting(message, greetings):
    for greeting in greetings:
        pattern = r"\b" + re.escape(greeting) + r"\b"

        if re.search(pattern, message):
            return True

    return False


# Identify FAQ topics
def find_faq_intents(message):
    patterns = {
        "hours": r"\b(hours?|open|opening|close|closing|operation)\b",
        "submission": r"\b(submit|submission|upload|github|project)\b",
        "certificate": r"\b(certificate|certification|credential)\b"
    }

    matched_intents = []

    for intent, pattern in patterns.items():
        if re.search(pattern, message):
            matched_intents.append(intent)

    return matched_intents


# Retrieve FAQ answers
def get_faq_answers(intents, faq_data):
    answers = []

    faq_mapping = {
        "hours": 0,
        "submission": 1,
        "certificate": 2
    }

    for intent in intents:
        faq_index = faq_mapping[intent]
        answer = faq_data["faqs"][faq_index]["answer"]
        answers.append(answer)

    return answers


# Fallback response
def get_fallback_response():
    return (
        "Sorry, I didn't understand your question. "
        "I can help with business hours, project submission, "
        "and certificate information."
    )


# Generate chatbot response
def get_response(message, faq_data):
    message = normalize_text(message)

    if is_greeting(message, faq_data["greetings"]):
        return "Hello! Welcome to customer support. How can I help you?"

    intents = find_faq_intents(message)

    if intents:
        answers = get_faq_answers(intents, faq_data)
        return "\n".join(answers)

    return get_fallback_response()


# Main chatbot conversation
def main():
    faq_data = load_faq_data()

    if faq_data is None:
        return

    print("Welcome to Customer Support Chatbot!")
    print("Ask me about business hours, projects, or certificates.")
    print("Type 'bye', 'exit', or 'quit' to stop.")

    while True:
        user_message = input("\nYou: ")

        if not user_message.strip():
            print("Bot: Please enter a message.")
            continue

        if normalize_text(user_message) in {"bye", "exit", "quit"}:
            print("Bot: Thank you for chatting. Goodbye!")
            break

        response = get_response(user_message, faq_data)
        print("Bot:", response)


if __name__ == "__main__":
    main()

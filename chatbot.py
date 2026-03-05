def greet():
    print("=" * 60)
    print("            🤖 SMART RULE-BASED CHATBOT 🤖")
    print("=" * 60)
    print(" Ask anything! (Type 'bye' to exit)")
    print("-" * 60)
    print("Chatbot: Hello! I am your assistant.")
    print("-" * 60)


def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 😊"

    elif "how are you" in user_input:
        return "I'm fine! Thanks for asking."

    elif "name" in user_input:
        return "I am a simple rule-based chatbot."

    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"

    elif "help" in user_input:
        return "I can respond to greetings, basic questions and simple chats."

    else:
        return "That's interesting! Tell me more."


def chatbot():
    greet()

    while True:
        print()
        user_input = input("You      : ")
        print("-" * 60)

        response = get_response(user_input)
        print("Chatbot  :", response)
        print("-" * 60)

        if "bye" in user_input.lower():
            print("=" * 60)
            break


chatbot()
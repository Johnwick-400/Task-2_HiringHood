from deepseek_api import get_ai_response

def format_response(response):
    # Add basic formatting (e.g., bullet points for lists)
    if "\n" in response:
        return "\n".join(f"• {line}" for line in response.split("\n"))
    return response

def chat_session():
    print("Welcome to the DEEPSEEK Chatbot! Type 'exit' to end the session.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_ai_response(user_input)
        if response:
            print("\nBot:", format_response(response))
        else:
            print("Bot: Sorry, I couldn't process your request. Please try again.")

if __name__ == "__main__":
    chat_session()
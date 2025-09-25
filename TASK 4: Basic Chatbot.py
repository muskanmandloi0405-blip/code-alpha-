# Basic Chatbot
# A simple rule-based chatbot using if-elif statements

def get_response(user_input):
    """
    Function to generate a response based on user input.
    Uses if-elif to match predefined patterns.
    """
    user_input = user_input.lower().strip()
    
    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you today?"
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

# Main chatbot loop
print("Welcome to the Basic Chatbot!")
print("You can say: 'hello', 'how are you', or 'bye' to interact.")
print("-" * 40)

while True:
    user_input = input("You: ").strip()
    
    if not user_input:  # Skip empty inputs
        continue
    
    response = get_response(user_input)
    print(f"Bot: {response}")
    
    # Exit condition
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break

print("Chat ended. Thanks for chatting!")

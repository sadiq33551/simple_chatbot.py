# ==========================================
# TASK 4: Basic Rule-Based Chatbot
# Author: Syed Muhammad Sadiq
# ==========================================

def chatbot_response(user_input):
    user_input = user_input.lower()  

    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"
    
    else:
        return "Sorry, I don't understand that."


print("🤖 Simple Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break

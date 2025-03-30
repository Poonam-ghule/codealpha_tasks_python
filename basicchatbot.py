import nltk
import random
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!','I am doing great, how about you?']),
    (r'what is your name?',['I am a chatbot created to chat with you!']),
    (r'how old are you?', ['I am ageless, just a bot!']),
    (r'bye|exit|quit', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'what can you do?', ['I can chat with you, answer some basic questions, and have a conversation!']),
    (r'what is your favorite color?',['I dont have preferences, but I think pink is nice!']),
    (r'(.*)your(.*)', ['I am not sure how to respond to that!', 'Lets change the topic.']),
    (r'hi|hello',['Hi!', 'Hello! How can I assist you today?']),
    (r'(.*)', ['I dont understand. Can you ask something else?'])
]
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hi, I am you chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        response = chatbot.respond(user_input)
        print("chatbot:", response)

if __name__ == "__main__":
     start_chat()

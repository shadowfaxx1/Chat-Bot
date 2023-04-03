import nltk
from nltk.chat.util import Chat, reflections
import random
from progress.bar import Bar

# Define the patterns for the chatbot
def chatbot_response(user_input):
    chatbot = Chat(patterns, reflections)
    response = chatbot.respond(user_input)
    return response

def display_menu():
    print("Please select an option from the following menu:")
    print("1. Learn about our electric toothbrushes")
    print("2. Request instructions on how to use our electric toothbrushes")
    print("3. Redeem warranty or report a defective product")
    print("4. Troubleshoot a problem with your electric toothbrush")
    print("5. talk to a customer service executive")
    print("6. Exit the chatbot")
  
def query_response(user_input):
    chatbot = Chat(query, reflections)
    response = chatbot.respond(user_input)
    return response
      
    
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'what.*toothbrush', ['We offer four electric toothbrush models: SB100, SB200, SB300, and SB400. Which one are you interested in?']),
    (r'sb100', ['The SB100 is our basic model. It has a single brushing mode and comes with a two-minute timer. The price is $100.']),
    (r'sb200', ['The SB200 is our mid-range model. It has three brushing modes and comes with a three-minute timer. The price is $200.']),
    (r'sb300', ['The SB300 is our premium model. It has five brushing modes, a pressure sensor, and comes with a four-minute timer. The price is $300.']),
    (r'sb400', ['The SB400 is our top-of-the-line model. It has seven brushing modes, a pressure sensor, Bluetooth connectivity, and comes with a five-minute timer. The price is $500.']),
    (r'warranty|defective', ['I can help you with that. Please provide your name, address, and serial number for the defective toothbrush.']),
    (r'troubleshoot|issue|problem', ['I\'m sorry to hear that. Can you describe the issue you are experiencing with your electric toothbrush?']),
    (r'thank you|thanks', ['You\'re welcome!', 'No problem. Is there anything else I can assist you with?']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!'])
]
query=[(r'dead|not.*work', ['Have you tried charging the toothbrush? If so, please provide more details about the issue.']),
    (r'not.*charging', ['Please make sure the toothbrush is properly connected to the charging dock. If you continue to experience issues, please contact customer support.']),
    (r'brush.*head', ['We recommend replacing the brush head every three months. Would you like to purchase a new one?']),
    (r'pressure|force', ['Our toothbrushes come with pressure sensors to ensure proper brushing technique. If you are experiencing issues, please contact customer support.']),
    (r'toothpaste', ['We recommend using toothpaste formulated for electric toothbrushes. Would you like me to recommend a brand?']),(r'request|demand|provide.*customer|service', ["request you to wait 2 mins our customer service executive will address you shortly "]),
    (r'other.*reason',['type  "no" in the next field and submit your query'])
    ]

  
def start_chatbot():
    print("Welcome to our electric toothbrush company! How may I assist you today?")

    while True:
        display_menu()
        user_input = input("You: ")
        print()
        
        
  
            
        if user_input == '1':
            print("Chatbot: We offer four electric toothbrush models: SB100, SB200, SB300, and SB400. Which one are you interested in?\n")
        elif user_input in ['SB100', 'SB200', 'SB300', 'SB400']:
            response = chatbot_response(user_input)
            print("Chatbot:", response)
            print()
            
        elif user_input == '2':
            print("Chatbot: Our electric toothbrushes come with instructions on how to use them. Would you like me to send you a copy?\n")
        elif user_input == '3':
            print("Chatbot: I can help you with that. Please provide your name, address, and serial number for the toothbrush.\n")
            name = input("You: What is your name? ")
            address = input("You: What is your address?")
            serial=input("You:serial number below the product\n")
            print(f"response has been noted for the respective serial number : {serial} \n 1 year warranty successfully availed thank you {name} ! \n ")
        elif user_input=='4':
            print("Chatbot: I'm sorry to hear that. Can you describe the issue you are experiencing with your electric toothbrush?")
            query=input("Chatbot: choose your query : \n1.charging \n 2.dead brush || head\n 3.pressure || force \n 4.toothpaste\n 5.other\n")
            res=query_response(query)
            print("Chatbot:",res)
            response=input("ChatBot: if not satisfied by the solution type in your query otherwise type 'no'  \n")
            if "no" in response:
                take_response=input("ChatBot: briefly describe your issue and we will revert back to you over email\n")
                print("thank you , your request has been saved with the reference number ", random.randint(244222,4411441))
                print()
        elif user_input=='5':
            bar = Bar('Processing', max=20)
            print("connecting" )
            for i in range(20):
                # Do some work
                print()
                bar.next()
            bar.finish()
            print("sorry for the inconvenience , no support executive is available for the moment ")
                            
                
            
            
                
        elif user_input == '6':
            print("Chatbot: Goodbye! Thank you for chatting with us.\n")
            break
       
        else:
            print("Chatbot: I'm sorry, I didn't understand your selection. Please try again.\n")

if __name__=='__main__':
    start_chatbot()
    
                                   


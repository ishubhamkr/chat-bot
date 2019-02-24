from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
# Create a new chat bot named chaty
chatbot = ChatBot('chaty')
trainer = ListTrainer(chatbot)
# Select File location of the directory of yml file
for files in os.listdir('C:\Users\DELL\Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    data = open ('C:\Users\DELL\Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files , 'r').readlines
    bot.train(data)
while True:
    message = input('User:')
    if meassage.strip()!='Bye':
        reply = chatbot.get_response(meassage)
        print('ChatBot :',reply)
    if meassage.strip()=='Bye':
        print('ChatBot: Bye')
        break
    

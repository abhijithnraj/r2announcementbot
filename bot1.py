#!/usr/bin/python3
from telegram.ext import Updater, CommandHandler

import pickle
f=open("announcement_data.bin","rb")

def start(bot, update):
    update.message.reply_text('Use /about to know more')
    print(update.message.from_user.username+":"+update.message.text)
def hello(bot, update):
    update.message.reply_text('Hello '+update.message.from_user.username)

def about(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="This is the announcement bot of R2 TKMCE")
    bot.send_message(chat_id=update.message.chat_id, text="press /announcements to see details")

def announcements(bot,update):
      bot.send_message(chat_id=update.message.chat_id, text="Announcements is as follows\n")
      f=open("announcement_data.bin","rb")
      l=pickle.load(f)
      for i in range(len(l)):
      	bot.send_message(chat_id=update.message.chat_id, text=str(i+1)+"."+" "+l[i])

def ktu(bot,update):
	import os
	os.system("python get_ktudata.py")
	bot.send_message(chat_id=update.message.chat_id, text="KTU Announcements is as follows\n")
	f=open("ktudata.bin","rb")
	l=pickle.load(f) 	
	for i in range(len(l)):
      		bot.send_message(chat_id=update.message.chat_id, text=str(i+1)+"."+" "+l[i])

	
    
#    update.message.reply_text()
	

key=open("conf.ini",'r').read().strip()

updater = Updater(key)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('announcements', announcements))
updater.dispatcher.add_handler(CommandHandler('about', about))
updater.dispatcher.add_handler(CommandHandler('ktu', ktu))
updater.start_polling()

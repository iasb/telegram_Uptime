#!/usr/bin/python
#coder :- IASB

import sys
import time
import datetime
import telepot
import time, datetime
import os
import random

from telepot.loop import MessageLoop
from re import findall
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

now = datetime.datetime.now()

bot = telepot.Bot('________')

chat_id = ________


output = 'test'
mylist = []

today = datetime.datetime.now()

mylist.append(today)
#print(mylist[0])
#print(today)


out_start = today.strftime('%d/%m/%Y')+' ' + today.strftime('%H:%M')


#print('output ' + output)

while 1:

  today = datetime.datetime.now()

  output2 = today.strftime('%d/%m/%Y')+' ' + today.strftime('%H:%M')

#  print('output2 ' + output2)


  im = bot.sendMessage(chat_id, text='1.18:   '+out_start+'  -->  '+output2)

  MessID = im['message_id']
  time.sleep(600)
  bot.deleteMessage((chat_id,MessID))

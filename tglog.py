#coding:utf-8

import requests
import traceback
import datetime

class logger():
    """Log errors in a log.txt file and receive them by telegram."""
    def __init__(self, chat_id:str=None, bot_token:str=None):
        self.chat_id = str(chat_id) # the telegram chat_id you want to receive the logs on
        self.bot_token = str(bot_token) # the token of the telegram bot which sends you the logs 

    def log_func(self, message):
        try :
            with open('log.txt','a') as f:
                written = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n" + message + "\n"
                f.write('{}\n'.format(written))        
            send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.chat_id + '&text=' + str(message)
            requests.get(send_text)
        except :
            try :
                message = "WARNING : Error in sending log by telegram, {}.\n".format(traceback.format_exc()) + message
                with open('log.txt','a') as f:
                    f.write('{}\n'.format(message)) 
            except : pass

    def debug(self, message) :
        message = "- DEBUG -\n" + message
        self.log_func(message)

    def info(self, message) :
        message = "- INFO -\n" + message
        self.log_func(message)

    def error(self, message) :
        message = "- ERROR -\n" + message
        self.log_func(message)
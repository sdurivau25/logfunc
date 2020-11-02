# tlog

Useful functions to log efficiently into a log.txt file and send you logs by Telegram.

How to use : 

`import tlog

my_chat_id = "12345"            # Your telegram chat_id, usually a chain of integers
my_bot_token = "token123"       # The token of the telegram bot you want to receive logs from

tl = tlog(my_chat_id, 
          my_bot_token)

tl.debug("info for debugging")   # Receive message when checkpoint reached
tl.info("info to be logged")     # Receive some info
tl.error(traceback.format_exc()) # Receive traceback of errors`

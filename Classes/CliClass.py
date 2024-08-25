from pyrogram import Client 
from pyrogram.enums.parse_mode import ParseMode 
from config import API_ID, API_HASH, BOT_TOKEN 
from pyrogram.errors import FloodWait 
from time import sleep 

class Get_Chat(Client): 
    def __init__(self): 
        self.mark_down_parse_mode=ParseMode.HTML 
        
        #---------------------------------------/ 
        super().__init__(                                                                                      #-|
            name=":memory:",                                                                                        #-|
            plugins=dict(root=r'plugins'),                                                                     #-|
            api_id=API_ID,                                                                                     #-|
            api_hash=API_HASH,                                                                                 #-|
            bot_token=BOT_TOKEN,                                                                               #-|
            sleep_threshold=60,                                                                                #-|
            parse_mode=ParseMode.MARKDOWN,                                                                     #-|
            workers=80,                                                                                        #-|
            in_memory=True)
        #--------------------------------------------/
        
    async def send_message(self, *args, **kwargs):
        try:
            return await super().send_message(*args, **kwargs)
        except FloodWait as e:
            if int(e.x) > 5 : raise TimeoutError
            await sleep(e.x)
            return await super().send_message(*args, **kwargs)

    async def edit_message(self, *args, **kwargs):
        try:
            return await super().edit_message_text(*args, **kwargs)
        except FloodWait as e:
            if int(e.x) > 5 : raise TimeoutError
            await sleep(e.x)
            return await super().edit_message_text(*args, **kwargs)
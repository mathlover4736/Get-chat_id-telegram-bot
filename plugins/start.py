from Classes.CliClass import Get_Chat
from pyrogram.types import Message 
from Classes.Helper import helper 


@Get_Chat.on_message() 
def welcome(c: Get_Chat, m: Message): 
    if m.text and m.text == "/start": 
        m.reply(
            text=helper.welcome_text, 
            reply_markup=helper.buttons.init() 
        )
        return 
    elif m.requested_chats: 
        for i in m.requested_chats.chats:
            m.reply(f"id = `{i.id}`" )
    elif m.text and m.text == "contact me": 
        m.reply(helper.contact_text, 
                reply_markup=helper.buttons.contact)
    else: 
        m.reply("Use the menu please!")
        
            

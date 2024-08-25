from pyrogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                            InlineKeyboardButton )
from pyrogram.types import (RequestUserInfo,  RequestChannelInfo,
                            RequestChatInfo)


users_button = KeyboardButton(
            text="User", 
            request_peer=RequestUserInfo(button_id=1,
                                         max_quantity=1,
                                         is_bot=False)
        ) 

bot_button = KeyboardButton(
    text="Bot", 
    request_peer=RequestUserInfo(button_id=2,
                                 is_bot=True)
)
chnl_button = KeyboardButton(
    text="Channel",
    request_peer=RequestChannelInfo(button_id=3)
)

chat_button = KeyboardButton(
    text="Group", 
    request_peer=RequestChatInfo(button_id=4)
)

#---------------------------------------------#/ 
def init() -> ReplyKeyboardMarkup: 
    return ReplyKeyboardMarkup(
        [
            [users_button, bot_button], 
            [chnl_button, chat_button],
            ["contact me"]
        ],
        resize_keyboard=True
    )
    
#-----------------------------------------------#/ 
contact = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Developer", user_id=1463788237)], 
        [InlineKeyboardButton(text="my github", url=r"https://github.com/mathlover4736")]
    ]
)
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ 🖤 ʙᴀʙʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ
๏ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ
๏ ɪᴍᴀɢᴇ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ

ꜱᴇɴᴅ ᴍᴜʟᴛɪᴘʟᴇ ɪᴍᴀɢᴇꜱ ᴏʀ ꜱᴛɪᴄᴋᴇʀꜱ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴛʜᴇ ꜱᴀᴍᴇ

 ๏ ᴍᴀᴅᴇ [🖤]() ʙʏ :[𝗝𝝙𝗬](https://t.me/GJ516_DISCUSS_GROUP)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

1) Send Sticker to get Image
2) Send Image to get Sticker

Note : You can send any amount of images or stickers or both together at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @StarkBots.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StickerToolsBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {},🥀

๏ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
๏ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ
 ➻ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɪᴍᴀɢᴇ
 ➻ ɪᴍᴀɢᴇ ᴛᴏ ꜱᴛɪᴄᴋᴇʀ
๏ ꜱᴇɴᴅ ᴍᴜʟᴛɪᴘʟᴇ ɪᴍᴀɢᴇꜱ ᴏʀ ꜱᴛɪᴄᴋᴇʀꜱ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴛʜᴇ ꜱᴀᴍᴇ
๏ ᴍᴀᴅᴇ [🖤](https://te.legra.ph/file/c45bdbdc46b3f95143e89.jpg) ʙʏ :[𝗝𝝙𝗬](https://t.me/export_gabbar)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="◁", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("ᴊᴏɪɴ ʙᴀʙʏ", url="https://t.me/GJ516_DISCUSS_GROUP")
        ],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/myworldGJ516"),
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/GJ516_DISCUSS_GROUP")
        ],
    ]

    # Help Message
    HELP = """
ʏᴏᴜ ʀᴇᴀʟʟʏ ɴᴇᴇᴅ ʜᴇʟᴘ ?

➻ ꜱᴇɴᴅ ꜱᴛɪᴄᴋᴇʀ ᴛᴏ ɢᴇᴛ ɪᴍᴀɢᴇ
➻ ꜱᴇɴᴅ ɪᴍᴀɢᴇ ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ

ɴᴏᴛᴇ : ʏᴏᴜ ᴄᴀɴ ꜱᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏꜰ ɪᴍᴀɢᴇꜱ ᴏʀ ꜱᴛɪᴄᴋᴇʀꜱ ᴏʀ ʙᴏᴛʜ ᴛᴏɢᴇᴛʜᴇʀ ᴀᴛ ᴏɴᴄᴇ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴡɪᴛʜ ꜱᴀᴍᴇ ꜱᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.

ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ɪɴ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. ᴋᴇᴇᴘ ᴛʀᴀᴄᴋ ʙʏ ᴊᴏɪɴɪɴɢ @GJ516_DISCUSS_GROUP [🥀](https://te.legra.ph/file/050cdb3bc6c92ec2e0741.jpg).
    """

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** 

➢ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ɢɪᴛʜᴜʙ](https://github.com/StarkBotsIndustries/StickerToolsBot)

➢ ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

➢ ʟᴀɴɢᴜᴀɢᴇ  : [ᴘʏᴛʜᴏɴ](www.python.org)

➢ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [ᴊᴀʏ](https://t.me/export_gabbar)
    """

import random

from pyrogram import Client, filters

from VIPMUSIC import app

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

SHAYRI = [
    "**ᴛʜᴇ ᴅᴀʏ ᴡɪʟʟ ᴄᴏᴍᴇ ᴡʜᴇɴ ʏᴏᴜ'ʟʟ ʙᴇ ᴍɪɴᴇ,ʙᴜᴛ ɪ'ʟʟ ᴊᴜꜱᴛ ᴡᴀɪᴛ ᴛɪʟʟ ᴛʜᴀᴛ ᴛɪᴍᴇ ɪꜰ ɪ ʜᴀᴠᴇ ᴛᴏ ᴡᴀɪᴛ ꜰᴏʀᴇᴠᴇʀ,**\n\n**ᴛʜᴀᴛ'ꜱ ᴡʜᴀᴛ ɪ'ʟʟ ʙᴇᴄᴏᴢ...ᴄᴀɴ'ᴛ ʟɪᴠᴇ ᴍʏ ʟɪꜰᴇ ᴡɪᴛʜᴏᴜᴛ ʏᴏᴜ...** ",
]

# Command
SHAYRI_COMMAND = ["gf", "bf", "xuanshang", "sakura", "sasuke", "love"]


@app.on_message(filters.command(SHAYRI_COMMAND) & filters.group)
async def help(client: Client, message: Message):
    await message.reply_text(
        text=random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/seriousvs_version10"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/seriousvs_version20"
                    ),
                ]
            ]
        ),
    )


@app.on_message(filters.command(SHAYRI_COMMAND) & filters.private)
async def help(client: Client, message: Message):
    await message.reply_text(
        text=random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/seriousvs_version10"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/seriousvs_version20"
                    ),
                ]
            ]
        ),
    )


__MODULE__ = "Shayari"
__HELP__ = """
/gf, /bf, /shayri, /sari, /shari, /love: Get a random Shayari.

This command works in both private and group chats. It provides a random piece of Shayari from a predefined list. The reply includes buttons for support and official channels.

Features:
- Provides a random Shayari on command.
- Available in both private and group chats.
- Includes inline keyboard buttons for additional support and official links.

Commands:
- /gf
- /bf
- /shayri
- /sari
- /shari
- /love

Note: This bot provides links to support and official channels for further assistance.
"""

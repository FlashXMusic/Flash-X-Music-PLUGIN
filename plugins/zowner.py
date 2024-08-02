import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from VIPMUSIC import app
from VIPMUSIC.mongo.afkdb import LOGGERS as OWNERS
from VIPMUSIC.utils.database import add_served_chat, get_assistant


@app.on_message(filters.command("repo", "update"))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1e44824e6b8d41def80c.jpg",
        caption=f"""**ᴅᴀɪʟʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/seriousvs_version20"
                    )
                ]
            ]
        ),
    )

@app.on_message(filters.command("dev", "developer"))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1e44824e6b8d41def80c.jpg",
        caption=f"""**ᴛɪᴍᴇꜱ ʏᴏᴜ ᴍᴀᴅᴇ ᴍᴇ ʟᴀᴜɢʜ, ꜰᴏʀ ᴛʜᴇ ᴛɪᴍᴇꜱ ʏᴏᴜ ʟɪꜱᴛᴇɴᴇᴅ ᴛᴏ ᴍᴇ, ᴀɴᴅ ᴛʜᴇ ᴛɪᴍᴇꜱ ʏᴏᴜ ꜱʜᴀʀᴇᴅ ʏᴏᴜʀ ʟɪꜰᴇ ᴡɪᴛʜ ᴍᴇ. ɪ ʜᴏᴘᴇ ᴛʜᴀᴛ ʏᴏᴜ ꜰɪɴᴅ ʏᴏᴜʀ ʜᴀᴘᴘɪɴᴇꜱꜱ ᴇᴠᴇɴ ᴛʜᴏᴜɢʜ ɪᴛ'ꜱ ɴᴏᴛ ᴍᴇ. ᴀʟʟ ɪ ᴡᴀɴᴛ ᴛᴏ ꜱᴀʏ ɪꜱ ᴛʜᴀɴᴋ ʏᴏᴜ ᴀɴᴅ ɢᴏᴏᴅʙʏᴇ.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/Uchihasasuke_is_myLife"
                    )
                ]
            ]
        ),
    )

@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c1e44824e6b8d41def80c.jpg",
        caption=f"""**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ꜱᴜᴅᴏ ᴜꜱᴇʀ ꜱᴏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴄʟᴏɴᴇ ᴍᴇ.**\n**ᴄʟɪᴄᴋ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʜᴏꜱᴛ ᴍᴀɴᴜᴀʟʟʏ ᴏᴛʜᴇʀᴡɪꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ᴏʀ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ꜰᴏʀ ᴄʟᴏɴᴇ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/Uchihasasuke_is_myLife"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio


@app.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @sasukevipmusicbot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001901470191:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")


__MODULE__ = "Repo"
__HELP__ = """
## Repo Module

This module provides utility commands for users to interact with the bot.

### Commands:
- `/repo`: Get the link to the bot's source code repository.
"""

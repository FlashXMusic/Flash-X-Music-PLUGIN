import asyncio

from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(["all", "mention", "mentionall"], prefixes=["@"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"🫧 {m.user.mention} "
            if usernum == 5:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"🫧 {m.user.mention} "
            if usernum == 5:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n{usertxt}\n\n✦ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ ᴄᴀɴᴄᴇʟ✦",
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        [
            "stopmention",
            "offall",
            "cancel",
            "allstop",
            "stopall",
            "cancelmention",
            "offmention",
            "mentionoff",
            "alloff",
            "cancelall",
            "allcancel",
        ],
        prefixes=["/", "@", "#"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


__MODULE__ = "Tag All"
__HELP__ = """
**Tag All Users**

This command allows admins to tag all users in the group or channel.

Commands:
- /all <text>: Tag all users in the group or channel with the provided text.
- /mention <text>: Tag all users in the group or channel with the provided text.
- /mentionall <text>: Tag all users in the group or channel with the provided text.

To stop tagging:
- /stopmention: Stop the tagging process.
- /offall: Stop the tagging process.
- /cancel: Stop the tagging process.
- /allstop: Stop the tagging process.
- /stopall: Stop the tagging process.
- /cancelmention: Stop the tagging process.
- /offmention: Stop the tagging process.
- /mentionoff: Stop the tagging process.
- /alloff: Stop the tagging process.
- /cancelall: Stop the tagging process.
- /allcancel: Stop the tagging process.

Note: Only admins can use these commands.
"""

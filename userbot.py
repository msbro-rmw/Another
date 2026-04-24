import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ─── Config ────────────────────────────────────────────────────────────────────
API_ID   = 38498066          # <-- my.telegram.org se bharo
API_HASH = "c9696114751feacdeb1b4487f5839a1a"         # <-- my.telegram.org se bharo

# ─── Userbot Client ────────────────────────────────────────────────────────────
import os
SESSION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_userbot")

app = Client(
    SESSION_PATH,     # absolute path — session file yahi folder mein banega
    api_id=API_ID,
    api_hash=API_HASH,
)

# ─── Commands ──────────────────────────────────────────────────────────────────

# .ping — alive check
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client: Client, message: Message):
    await message.edit("🏓 Pong!")


# .id — chat/user ID dekho
@app.on_message(filters.command("id", prefixes=".") & filters.me)
async def get_id(client: Client, message: Message):
    reply = message.reply_to_message
    if reply:
        await message.edit(
            f"**User ID:** `{reply.from_user.id if reply.from_user else 'N/A'}`\n"
            f"**Chat ID:** `{message.chat.id}`\n"
            f"**Message ID:** `{reply.id}`"
        )
    else:
        await message.edit(
            f"**Chat ID:** `{message.chat.id}`\n"
            f"**Your ID:** `{message.from_user.id}`"
        )


# .info — user info
@app.on_message(filters.command("info", prefixes=".") & filters.me)
async def get_info(client: Client, message: Message):
    reply = message.reply_to_message
    target = reply.from_user if reply and reply.from_user else message.from_user
    text = (
        f"**Name:** {target.first_name} {target.last_name or ''}\n"
        f"**Username:** @{target.username or 'N/A'}\n"
        f"**ID:** `{target.id}`\n"
        f"**DC:** {target.dc_id or 'N/A'}"
    )
    await message.edit(text)


# .del — replied message delete karo
@app.on_message(filters.command("del", prefixes=".") & filters.me)
async def delete_msg(client: Client, message: Message):
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await message.delete()


# .purge — last N messages delete karo (sirf apne)
@app.on_message(filters.command("purge", prefixes=".") & filters.me)
async def purge_msgs(client: Client, message: Message):
    args = message.text.split()
    n = int(args[1]) if len(args) > 1 and args[1].isdigit() else 10
    count = 0
    async for msg in client.get_chat_history(message.chat.id, limit=n + 1):
        if msg.from_user and msg.from_user.is_self:
            await msg.delete()
            count += 1
    logger.info(f"Purged {count} messages")


# .save — replied message forward karo Saved Messages mein
@app.on_message(filters.command("save", prefixes=".") & filters.me)
async def save_msg(client: Client, message: Message):
    if message.reply_to_message:
        await message.reply_to_message.forward("me")
        await message.edit("✅ Saved to Saved Messages!")
    else:
        await message.edit("❌ Kisi message pe reply karo.")


# .tr <text> — Google Translate (English mein)
@app.on_message(filters.command("tr", prefixes=".") & filters.me)
async def translate(client: Client, message: Message):
    try:
        from deep_translator import GoogleTranslator
        args = message.text.split(None, 1)
        text = args[1] if len(args) > 1 else (
            message.reply_to_message.text if message.reply_to_message else None
        )
        if not text:
            await message.edit("❌ Text ya reply dena zaroori hai.")
            return
        result = GoogleTranslator(source="auto", target="en").translate(text)
        await message.edit(f"🌐 **Translated:**\n{result}")
    except ImportError:
        await message.edit("❌ `deep-translator` install karo: `pip install deep-translator`")
    except Exception as e:
        await message.edit(f"❌ Error: {e}")


# .help — commands list
@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help_cmd(client: Client, message: Message):
    await message.edit(
        "**🤖 Userbot Commands** (prefix: `.`)\n\n"
        "`.ping` — Alive check\n"
        "`.id` — Chat/User ID\n"
        "`.info` — User info\n"
        "`.del` — Message delete\n"
        "`.purge <n>` — Last N apne messages delete\n"
        "`.save` — Saved Messages mein save karo\n"
        "`.tr <text>` — Translate to English\n"
        "`.help` — Ye list"
    )


# ─── Run ───────────────────────────────────────────────────────────────────────
async def main():
    await app.start()
    me = await app.get_me()
    logger.info(f"✅ Userbot started as: {me.first_name} (@{me.username})")
    logger.info("Commands active! Type .help in any chat.")
    await asyncio.get_event_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

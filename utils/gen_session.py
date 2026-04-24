"""
Run this ONCE locally/Termux to generate session string.
python utils/gen_session.py
"""
from pyrogram import Client
import asyncio

API_ID   = 0    # <-- bharo
API_HASH = ""   # <-- bharo

async def main():
    async with Client("gen_temp", api_id=API_ID, api_hash=API_HASH) as app:
        print("\n✅ Session String:\n")
        print(await app.export_session_string())
        print("\nUpar wali string copy kar lo!\n")

asyncio.run(main())

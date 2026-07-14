# (©)Codexbotz
import os
import asyncio
from pyrogram import Client


API_ID = int(os.environ.get("API_ID", 37063855))
API_HASH = os.environ.get("API_HASH", "0419e8626a4ac694ff59f0953c7d089e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8237959420:AAHE0atddUSOCosRnwWxqPNSB6E8We2xjz4")

async def main():
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )
    
    @app.on_message()
    async def hello(client, message):
        await message.reply("ቦቱ እየሰራ ነው!")
    
    print("ቦቱ ተነስቷል!")
    await app.start()
    # ቦቱ እንዳይዘጋ ለዘላለም እንዲቆይ
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

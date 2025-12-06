
import asyncio
from pyrogram import Client, filters
from config import Config

# Initialize bot using config values
app = Client(
    "my_simple_bot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN
)

# Start command handler
@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hi 👋")

# Main function
async def main():
    await app.start()
    
    # Get bot info for logs
    me = await app.get_me()
    print(f"Bot Started Successfully!")
    print(f"Bot Name: {me.first_name}")
    print(f"Bot Username: @{me.username}")
    print("Bot is running...")

    await asyncio.Event().wait()   # Keep bot alive forever

# Run bot
asyncio.run(main())

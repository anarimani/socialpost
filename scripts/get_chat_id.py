
import asyncio
from telegram import Bot

async def main():
    bot_token = '7354614830:AAHBhR5lxYBu7aP-cVS32plicPQ3p5isUdY'
    
    bot = Bot(token=bot_token)
    updates = await bot.get_updates()
    
    if updates:
        chat_id = updates[-1].message.chat_id
        print("Your Chat ID:", chat_id)
    else:
        print("No messages received yet.")

if __name__ == "__main__":
    asyncio.run(main())

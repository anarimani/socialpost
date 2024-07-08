from telegram import Bot
import asyncio

async def post_to_telegram(image_path, text):
    bot = Bot(token='7354614830:AAHBhR5lxYBu7aP-cVS32plicPQ3p5isUdY')
    await bot.send_photo(chat_id='-1002228090246', photo=open(image_path, 'rb'), caption=text)

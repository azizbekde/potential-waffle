from telethon import TelegramClient, events, Button
import os

api_id = 33587202 
api_hash = 'e1da6346fc507ed448d8a7a01694f48b'
bot_token = '8614621930:AAHw0Yhn8626h0_fghHFpbp8G-Rp1HG9CnMU'

bot = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

if not os.path.exists('sessions'):
    os.makedirs('sessions')

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("✅ Bot Render-da ishladi!")

print("Bot ishlamoqda...")
bot.run_until_disconnected()

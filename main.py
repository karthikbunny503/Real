from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

# ✅ Get token securely from environment
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0)

# 🟢 Handle /start command
def start(update, context):
    update.message.reply_text("Hello! Please send me RAT name to get details.")

# 🟢 Handle any text message
def echo(update, context):
    update.message.reply_text("👋 You said: " + update.message.text)

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

@app.route('/')
def home():
    return "🤖 Bot is running!"

# 🔗 Telegram webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# 🌐 Set webhook manually
@app.route('/setwebhook')
def set_webhook():
    webhook_url = 'https://your-app-name.onrender.com/webhook'  # Replace with your live Render URL
    success = bot.set_webhook(url=webhook_url)
    return f"Webhook set: {success}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

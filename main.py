
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8091015409:AAFXSxiUJWBSaP8uENR6tsLkfmQKUq6dxQM"

reply_keyboard = [['🔔 Subscribe', 'ℹ️ Info'], ['📞 Contact', '❌ Exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Welcome to my bot.\nChoose an option below:",
        reply_markup=markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == '🔔 Subscribe':
        await update.message.reply_text("✅ You are now subscribed.")
    elif text == 'ℹ️ Info':
        await update.message.reply_text("ℹ️ This is a sample bot with buttons.")
    elif text == '📞 Contact':
        await update.message.reply_text("📞 Contact us at support@example.com")
    elif text == '❌ Exit':
        await update.message.reply_text("👋 Goodbye!", reply_markup=None)
    else:
        await update.message.reply_text("❓ Please select a button from below.", reply_markup=markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

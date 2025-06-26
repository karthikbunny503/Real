from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# /start command with big buttons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐  CraxsRat v7.6  🔐", callback_data='cr76')],
        [InlineKeyboardButton("🛡️  EagleSpy V4  🛡️", callback_data='esv4')],
        [InlineKeyboardButton("🛡️  EagleSpy V5  🛡️", callback_data='esv5')],
        [InlineKeyboardButton("🔐  CraxsRat v7.4  🔐", callback_data='cr74')],
        [InlineKeyboardButton("📦  More Tools  📦", callback_data='more')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔰 Choose a tool:", reply_markup=reply_markup)

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to see tools with buttons.")

# Handle button presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        'cr76': "✅ You selected: CraxsRat v7.6",
        'esv4': "✅ You selected: EagleSpy V4",
        'esv5': "✅ You selected: EagleSpy V5",
        'cr74': "✅ You selected: CraxsRat v7.4",
        'more': "🔧 More tools coming soon..."
    }

    await query.edit_message_text(text=responses.get(query.data, "❓ Unknown selection."))

# ✅ Your new bot token
BOT_TOKEN = "7240109367:AAG5t8rksmX911DGQYJuFH88SceyL9vIM3Q"

# Build and run the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Your Telegram user ID (to receive forwarded messages)
ADMIN_ID = 6316000882

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔐 CraxsRat v7.6", callback_data='cr76')],
        [InlineKeyboardButton("🛡️ EagleSpy V4", callback_data='esv4')],
        [InlineKeyboardButton("🛡️ EagleSpy V5", callback_data='esv5')],
        [InlineKeyboardButton("🔐 CraxsRat v7.4", callback_data='cr74')],
        [InlineKeyboardButton("📦 More Tools", callback_data='more')],
        [InlineKeyboardButton("🧠 SpyX v3.1", callback_data='spyx')],
        [InlineKeyboardButton("🧰 GhostWare Pro", callback_data='ghost')],
        [InlineKeyboardButton("📲 AndroidHackKit", callback_data='ahk')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔰 Choose a tool:", reply_markup=reply_markup)

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to see tools with buttons.\nYou can also send me any message.")

# Button click handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        'cr76': "✅ You selected: CraxsRat v7.6",
        'esv4': "✅ You selected: EagleSpy V4",
        'esv5': "✅ You selected: EagleSpy V5",
        'cr74': "✅ You selected: CraxsRat v7.4",
        'more': "🔧 More tools coming soon...",
        'spyx': "🧠 You selected: SpyX v3.1",
        'ghost': "🧰 You selected: GhostWare Pro",
        'ahk': "📲 You selected: AndroidHackKit"
    }

    await query.edit_message_text(text=responses.get(query.data, "❓ Unknown selection."))

# Message logger & forwarder
async def log_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = update.message.text or "[non-text message]"
    log = f"📩 Message from {user.first_name or 'Unknown'} (@{user.username}):\n{msg}"

    await update.message.reply_text("✅ Message received. We'll check and reply if needed.")
    await context.bot.send_message(chat_id=ADMIN_ID, text=log)

# ✅ Your updated bot token
BOT_TOKEN = "7240109367:AAHN-WwH8bsSB2_jkg8FuGPhupVckIfzLf0"

# Build and run the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_user_message))

app.run_polling()

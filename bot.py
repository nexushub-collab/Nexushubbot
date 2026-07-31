
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8963771456:AAE1_ssWMG65CHig3yCoWV5ZNFTaB0JuxYA

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut! Sunt NexusHubBot.\nScrie /ajutor."
    )

async def ajutor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
📋 Comenzi

/start
/ajutor
/reguli
/info
"""
    )

async def reguli(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 Regulile grupului:\n1. Fără spam.\n2. Respectă membrii."
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 NexusHubBot versiunea 1."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ajutor", ajutor))
app.add_handler(CommandHandler("reguli", reguli))
app.add_handler(CommandHandler("info", info))

print("Bot pornit!")

app.run_polling()

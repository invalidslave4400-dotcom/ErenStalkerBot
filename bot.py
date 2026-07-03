from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import add_user, get_credits
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = 8525076444

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
add_user(
    user.id,
    user.username if user.username else "NoUsername",
    user.first_name
)

credits = get_credits(user.id)
    if user.id == OWNER_ID:
        text = (
            "👑 WELCOME OWNER!\n\n"
            "🤖 ErenStalkerBot is running successfully."
        )
    else:
        text = (
            "🔥 Welcome to ErenStalkerBot!\n\n"
            "Bot is under development."
        )

    await update.message.reply_text(text)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()

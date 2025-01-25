from telegram import Update
from telegram.ext import Application, CommandHandler
import os

# Optional: Keep the bot alive (if necessary)
from keep_alive import keep_alive
keep_alive()

# Create the bot application with your token
application = Application.builder().token(os.environ.get('token')).build()

# Start command handler
async def welcome(update: Update, context):
    await update.message.reply("Hello! I'm Gunther Bot, Please follow my YT channel")

# Logo command handler
async def logo(update: Update, context):
    await update.message.reply_photo('https://avatars.githubusercontent.com/u/62240649?v=4')

# Set up command handlers
application.add_handler(CommandHandler("start", welcome))
application.add_handler(CommandHandler("help", welcome))
application.add_handler(CommandHandler("logo", logo))

if __name__ == '__main__':
    # Run the bot
    application.run_polling()

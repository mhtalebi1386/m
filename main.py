from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import json
import re
from datetime import datetime

with open('token.json', 'r') as f:
    token_data = json.load(f)
    bot_token = token_data['BOT_TOKEN']

async def delete_links(update: Update, context):
    user_name = update.message.from_user.full_name
    user_id = update.message.from_user.id
    message_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if re.match(r'http[s]?://', update.message.text, re.IGNORECASE) or "مادر جنده" in update.message.text.lower() or re.match(r't.me', update.message.text, re.IGNORECASE):
        await update.message.delete()
        with open('log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"[{message_time}] User: {user_name} (ID: {user_id}) wrote: {update.message.text}\n")

def main():
    application = Application.builder().token(bot_token).build()
    application.add_handler(MessageHandler(filters.TEXT, delete_links))
    application.run_polling()

if __name__ == '__main__':
    main()

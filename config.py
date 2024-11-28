import os
from dotenv import load_dotenv
import telebot


load_dotenv()


tg_bot_token = os.getenv("TG_BOT_TOKEN")
tg_chat_id = os.getenv("TG_CHAT_ID")
bot = telebot.TeleBot(tg_bot_token)

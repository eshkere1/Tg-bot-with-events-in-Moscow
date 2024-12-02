import os
from dotenv import load_dotenv
import telebot


load_dotenv()


tg_bot_token = os.getenv("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)

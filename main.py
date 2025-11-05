import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=["start"])
def start(m, res=False):
  bot.send_message(m.chat.id, 'Я на связи. Напиши мне что нибудь )')

@bot.message_handler(content_types=["text"])
def handle_text(message):
  bot.send_message(m.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=-0)

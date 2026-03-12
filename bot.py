import telebot
from telebot import types
import os
import time

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['menu'])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        is_persistent=True,
        one_time_keyboard=False
    )
    button1 = types.KeyboardButton('ПРОГРАММА')
    button2 = types.KeyboardButton('ТЕХПОДДЕРЖКА')
    markup.row(button1, button2)

    msg = bot.send_message(
        message.chat.id,
        "Для вашего удобства добавили кнопки 😇",
        reply_markup = markup
    )


bot.infinity_polling()

import telebot


TOKEN = "8564271668:AAFhsPGjIUrwTUt3k5fLGjQ_qVRUjJFWsGw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['program'])
def send_program(message):
    bot.send_message(message.chat.id, "ПРОГРАММА")


bot.infinity_polling()
import telebot
import time

from config import TOKEN_1, TOKEN_2, TOKEN_3, TOKEN_4, TOKEN_5, TOKEN_6, TOKEN_7, TOKEN_8, dima, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8

bot_1 = telebot.TeleBot(TOKEN_1)
bot_2 = telebot.TeleBot(TOKEN_2)
bot_3 = telebot.TeleBot(TOKEN_3)
bot_4 = telebot.TeleBot(TOKEN_4)
bot_5 = telebot.TeleBot(TOKEN_5)
bot_6 = telebot.TeleBot(TOKEN_6)
bot_7 = telebot.TeleBot(TOKEN_7)
bot_8 = telebot.TeleBot(TOKEN_8)


time.sleep(10)
bot_1.send_message(dima, text_1)

time.sleep(12)
bot_2.send_message(dima, text_2)

time.sleep(12)
bot_3.send_message(dima, text_3)

time.sleep(15)
bot_4.send_message(dima, text_4)

time.sleep(10)
bot_6.send_message(dima, text_6)

time.sleep(8)
bot_7.send_message(dima, text_7)

time.sleep(10)
bot_8.send_message(dima, text_8)

if __name__ == "__main__":
    bot_1.polling(non_stop=True)
    bot_2.polling(non_stop=True)
    bot_3.polling(non_stop=True)
    bot_4.polling(non_stop=True)
    bot_5.polling(non_stop=True)
    bot_6.polling(non_stop=True)
    bot_7.polling(non_stop=True)
    bot_8.polling(non_stop=True)

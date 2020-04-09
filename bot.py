import telebot
import tokkken
from telebot import types
import COVID19Py
import pprint

bot = telebot.TeleBot(tokkken.tok)
user = bot.get_me()
covid = COVID19Py.COVID19()
@bot.message_handler(commands=['start'])
def srart(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Россия')
    btn2 = types.KeyboardButton('Мир')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Hello", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == "Мир":
        mir = covid.getLatest()
        vuvod = f"Зараженно: {mir['confirmed']},\nСмертей: {mir['deaths']}"
        bot.send_message(message.chat.id, vuvod)
        print('Зараженно: ', vuvod)
    if message.text == "Россия":
        russia = covid.getLocationByCountryCode("RU")
        #print(str(russia[0]))
        rus = dict(russia[0])
        vuvod = f"Зараженно: {rus['latest']['confirmed']},\nСмертей: {rus['latest']['deaths']}"
        bot.send_message(message.chat.id, vuvod)

if __name__ == '__main__':
    bot.polling(none_stop=True)

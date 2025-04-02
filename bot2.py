import telebot
from telebot import types

bot = telebot.TeleBot('7497884487:AAHAkyDch2-q-8vQ2jxcc964J0wvqOfiUTw')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 сиска")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-сосиска!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 сиска':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('хотите стать сосиской?')
        btn2 = types.KeyboardButton('как создавался это бот')
        btn3 = types.KeyboardButton('как готовить сосиски')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'хотите стать сосиской?':
        bot.send_message(message.from_user.id, 'как стать сосиской? хах,сам хз. почитай тут) ' + '[ссылке](https://yandex.ru/q/question/esli_by_vy_byli_chelovekom_sosiskoi_s_vy_c02d1615/)', parse_mode='Markdown')

    elif message.text == 'как создавался это бот':
        bot.send_message(message.from_user.id, 'как делался это бот про сосиски? ' + '[ссылке](https://habr.com/ru/articles/697052/)', parse_mode='Markdown')

    elif message.text == 'как готовить сосиски':
        bot.send_message(message.from_user.id, 'подробная готовка сосисок ' + '[ссылке](https://youtu.be/YTrvmO8fka0)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) 
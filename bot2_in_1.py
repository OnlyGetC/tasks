API_TOKEN = # its a secret)))
from aiogram import types
def fetch_webpage():
    import requests
    webpage = requests.get('https://yandex.ru/')
    return webpage.status_code

def text_analizator(text):
    import collections
    print("Количество предложений в тексте: ", len([i for i in text.split(".")])) # Print в консоль
    words = len([i for i in text.split(".")])
    long = max(text.split(), key = len) # Самое длинное слово работает как-то не так
    print(f'Самое длинное слово в тексте: {long}')
    text = text.split()
    print("Количество слов в тексте:", len(text)) # Print в консоль
    dlina = len(text)
    a = set(text)
    print("Количество уникальных слов: ", len(a)) # Print в консоль
    unic = len(a)
    results = collections.Counter(text).most_common(1)
    print(f'Самое частое слово в тексте: {results[0][0]}') # Print в консоль
    res = results[0][0]
    return words,dlina,unic,res,long

import telebot
bot = telebot.TeleBot(API_TOKEN); #token для бота misis_test_bot
@bot.message_handler(content_types=['text','document','audio'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Здарова, я пажилой-бот, меня завут Валерий Албертович Жмышенко, можно просто ЖМА.(/help)")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Доступные команды: Привет; Яндекс; /help; Можете ввести любой текст для его анализа")
    elif message.text == "Яндекс":
        bot.send_message(message.from_user.id, fetch_webpage())
        bot.send_message(message.from_user.id, "Подсказка: Если ответ 200 - сайт работает, остальное - что-то не так")
    elif message.text == f"Текст":
        bot.send_message(message.from_user.id, "Введите свой текст для его анализа")
    else:
        bot.send_message(message.from_user.id, "Вот смотри, что у тебя за текст такой")
        analys = text_analizator(message.text)
        bot.send_message(message.from_user.id, f'Количество предложений в тексте: {analys[0]}')
        bot.send_message(message.from_user.id, f'Количество слов в тексте: {analys[1]}')
        bot.send_message(message.from_user.id, f'Количество уникальных слов: {analys[2]}')
        bot.send_message(message.from_user.id, f'Самое частое слово в тексте: {analys[3]}')
        bot.send_message(message.from_user.id, f'Самое длинное слово в тексте: {analys[4]}')
bot.polling(none_stop=True, interval=0)
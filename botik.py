import telebot
from telebot import types
import json
import os

bot = telebot.TeleBot('7861103730:AAHfDoR7vVvoFPNOZowI4kIYQ4eFLRGXV5I') 
bot2 = telebot.TeleBot('7815857634:AAGAKxqROT6hFKwx6w9veQJ22xgmPD8_ghM')  

data_file = 'data.json'


def load_data():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Ошибка при декодировании JSON. Файл может быть поврежден.")
            return {}
    return {}


def save_data(data):
    try:
        with open(data_file, 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


user_states = load_data()
print(user_states)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('VBA', callback_data='VBA'))
    markup.add(types.InlineKeyboardButton('C', callback_data='C'))
    markup.add(types.InlineKeyboardButton('Bash', callback_data='Bash'))
    markup.add(types.InlineKeyboardButton('Ваши предложения', callback_data='predlozka'))
    bot.send_message(message.chat.id, 'Спасибо, что выбрали нас, выберите язык:', reply_markup=markup)
    user_states[message.chat.id] = 'main_menu'
    save_data(user_states) 

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    user_id = callback.message.chat.id
    current_state = user_states.get(user_id)  
    
    if current_state is None:
        user_states[user_id] = 'main_menu'
        save_data(user_states)
        current_state = 'main_menu'
        print(current_state)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        start(callback.message)
    if callback.data == 'VBA':
        marcupVBA = types.InlineKeyboardMarkup()
        marcupVBA.add(types.InlineKeyboardButton('Типы данных', url='https://telegra.ph/Tipy-dannyh-12-16-2'))
        marcupVBA.add(types.InlineKeyboardButton('Ввод и вывод данных', url='https://telegra.ph/Vvod-i-vyvod-dannyh-12-16-2'))
        marcupVBA.add(types.InlineKeyboardButton('Функции', url='https://telegra.ph/Funkcii-12-16-3'))
        marcupVBA.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupVBA)
        user_states[user_id] = 'vba_menu'
        save_data(user_states)  

    elif callback.data == 'C':
        marcupC = types.InlineKeyboardMarkup()
        marcupC.add(types.InlineKeyboardButton('Типы данных', url='https://telegra.ph/Osnovnye-tipy-dannyh-12-16'))
        marcupC.add(types.InlineKeyboardButton('Ввод и вывод данных', url='https://telegra.ph/Vvod-dannyh-12-16'))
        marcupC.add(types.InlineKeyboardButton('Функции', url='https://telegra.ph/Funkcii-12-16'))
        marcupC.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupC)
        user_states[user_id] = 'c_menu'
        save_data(user_states) 
    
    elif callback.data == 'Bash':
        marcupBash = types.InlineKeyboardMarkup()
        marcupBash.add(types.InlineKeyboardButton('Типы данных', url='https://telegra.ph/Tipy-dannyh-12-16'))
        marcupBash.add(types.InlineKeyboardButton('Ввод и вывод данных', url='https://telegra.ph/Vvod-i-vyvod-dannyh-12-16'))
        marcupBash.add(types.InlineKeyboardButton('Функции', url='https://telegra.ph/Funkcii-12-16-2'))
        marcupBash.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupBash)
        user_states[user_id] = 'bash_menu'
        save_data(user_states)
    
    elif callback.data == 'back':
        if current_state in ['vba_menu', 'c_menu', 'bash_menu', 'predlozka_menu']:
            bot.delete_message(user_id, callback.message.message_id)
            start(callback.message)
        elif current_state == 'main_menu':
            print("GG")
        else:
            bot.send_message(user_id, "Неизвестное состояние.")

    elif callback.data == 'predlozka': 
        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Напишите своё предложение:')
        user_states[user_id] = 'predlozka_menu'
        save_data(user_states) 

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'predlozka_menu')
def predlozka(message):
    text_predloz = message.text
    bot2.send_message(1088608641, f'Вам поступило предложение: {text_predloz}')
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    start(message)

import atexit
atexit.register(lambda: save_data(user_states))

bot.polling(none_stop=True)



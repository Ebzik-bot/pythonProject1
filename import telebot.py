import telebot
from telebot import types

bot = telebot.TeleBot('7944384802:AAHAn8OOoiyYGvImoKrd-2aJ-oFlYxoRCT4')
bot2 = telebot.TeleBot('7815857634:AAGAKxqROT6hFKwx6w9veQJ22xgmPD8_ghM')
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('VBA', callback_data='VBA'))
    markup.add(types.InlineKeyboardButton('C', callback_data='C'))
    markup.add(types.InlineKeyboardButton('Bash', callback_data='Bash'))
    markup.add(types.InlineKeyboardButton('Ваши предложения', callback_data='predlozka'))
    bot.send_message(message.chat.id, 'Спасибо, что выбрали нас, выберите язык:', reply_markup=markup)
    user_states[message.chat.id] = 'main_menu' 

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    user_id = callback.message.chat.id
    current_state = user_states.get(user_id)
    print(current_state)
    if callback.data == 'VBA':
        marcupVBA = types.InlineKeyboardMarkup()
        marcupVBA.add(types.InlineKeyboardButton('Объявление переменных', url='https://telegra.ph/je-12-04-2'))
        marcupVBA.add(types.InlineKeyboardButton('Вывод данных', callback_data='outVBA'))
        marcupVBA.add(types.InlineKeyboardButton('Массивы', callback_data='matrixVBA'))
        marcupVBA.add(types.InlineKeyboardButton('Следующая страница', callback_data='nextVBA'))
        marcupVBA.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupVBA)
        user_states[user_id] = 'vba_menu'
        print(current_state)

    elif callback.data == 'C':
        marcupC = types.InlineKeyboardMarkup()
        marcupC.add(types.InlineKeyboardButton('Объявление переменных', url='https://www.google.ru/?hl=ru'))
        marcupC.add(types.InlineKeyboardButton('Вывод данных', url='https://www.google.ru/?hl=ru'))
        marcupC.add(types.InlineKeyboardButton('Массивы', url='https://www.google.ru/?hl=ru'))
        marcupC.add(types.InlineKeyboardButton('Следующая страница', callback_data='nextC'))
        marcupC.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupC)
        user_states[user_id] = 'c_menu'
        print(current_state)
    
    elif callback.data == 'Bash':
        marcupBash = types.InlineKeyboardMarkup()
        marcupBash.add(types.InlineKeyboardButton('Объявление переменных', url='https://www.google.ru/?hl=ru'))
        marcupBash.add(types.InlineKeyboardButton('Вывод данных', url='https://www.google.ru/?hl=ru'))
        marcupBash.add(types.InlineKeyboardButton('Массивы', url='https://www.google.ru/?hl=ru'))
        marcupBash.add(types.InlineKeyboardButton('Следующая страница', callback_data='nextC'))
        marcupBash.add(types.InlineKeyboardButton('Назад', callback_data='back'))

        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Выберите опцию:', reply_markup=marcupBash)
        user_states[user_id] = 'bash_menu'
        print(current_state)
    
    elif callback.data == 'back':
        if current_state in ['vba_menu', 'c_menu' , 'bash_menu' , 'predlozka_menu']:
            bot.delete_message(user_id, callback.message.message_id)
            start(callback.message)
        elif current_state == 'c_menu':
            bot.delete_message(user_id, callback.message.message_id)
            start(callback.message)
        elif current_state == 'main_menu':
            bot.send_message(user_id, "Вы уже находитесь в главном меню.")
        else:
            bot.send_message(user_id, "Неизвестное состояние.")

    elif callback.date == 'predlozka':
        bot.delete_message(user_id, callback.message.message_id)
        bot.send_message(user_id, 'Напишите своё предложение:')
        user_states[user_id] = 'predlozka_menu'
@bot.message_handler(func=lambda predloz: True)
def predlozka(predloz):
    text_predloz = predloz.text
    bot2.send_message([1088608641 , 830230755, 1318434794], f'Вам поступило предложение: {text_predloz}')
    bot.delete_message(predloz.message.chat.id, predloz.message.message_id)
    start(predloz.message)
bot.polling(none_stop=True)
bot2.polling(none_stop=True)



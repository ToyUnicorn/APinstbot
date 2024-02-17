import datetime
import time
import telebot
import os
import requests
from telebot import types
from telebot.util import quick_markup
bot = telebot.TeleBot('6784752334:AAG69xQ5xjOQuTZv0Jnxxors0uo8slPYaEw')

d = ''
m = ''
mt = ''
h = ''
mi = ''
user_path = ''
task_path = ''

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я ваш бот-помошник для создания отложенных постов в instagram!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if ((message.text == '👋 Поздороваться') or (message.text == 'Меню')):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Новый пост')
        btn2 = types.KeyboardButton('Запланированные посты')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Выберите нужный пункт меню', reply_markup=markup) #ответ бота

    elif message.text == 'Новый пост':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Меню')
        btn2 = types.KeyboardButton('Фото')
        btn3 = types.KeyboardButton('Видео')
        btn4 = types.KeyboardButton('Карусель')
        btn5 = types.KeyboardButton('Сториз')
        btn6 = types.KeyboardButton('Вызов')
        markup.add(btn2, btn3, btn4, btn5, btn6, btn1)
        bot.send_message(message.from_user.id, 'Выберите тип поста:', reply_markup=markup) #ответ бота
        global user_path
        user_path = 'tasks/'+str(message.from_user.id)
        if not os.path.exists(user_path):
            os.makedirs(user_path)

    elif message.text == 'Фото':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Меню')
        # btn2 = types.KeyboardButton('Назад')
        btn2 = types.KeyboardButton('Заново')
        markup.add(btn2, btn1)
        markup2 = quick_markup({
            '1': {'callback_data': 'day1'},
            '2': {'callback_data': 'day2'},
            '3': {'callback_data': 'day3'},
            '4': {'callback_data': 'day4'},
            '5': {'callback_data': 'day5'},
            '6': {'callback_data': 'day6'},
            '7': {'callback_data': 'day7'},
            '8': {'callback_data': 'day8'},
            '9': {'callback_data': 'day9'},
            '10': {'callback_data': 'day10'},
            '11': {'callback_data': 'day11'},
            '12': {'callback_data': 'day12'},
            '13': {'callback_data': 'day13'},
            '14': {'callback_data': 'day14'},
            '15': {'callback_data': 'day15'},
            '16': {'callback_data': 'day16'},
            '17': {'callback_data': 'day17'},
            '18': {'callback_data': 'day18'},
            '19': {'callback_data': 'day19'},
            '20': {'callback_data': 'day20'},
            '21': {'callback_data': 'day21'},
            '22': {'callback_data': 'day22'},
            '23': {'callback_data': 'day23'},
            '24': {'callback_data': 'day24'},
            '25': {'callback_data': 'day25'},
            '26': {'callback_data': 'day26'},
            '27': {'callback_data': 'day27'},
            '28': {'callback_data': 'day28'},
            '29': {'callback_data': 'day29'},
            '30': {'callback_data': 'day30'},
            '31': {'callback_data': 'day31'},
        }, row_width=5)
        bot.send_message(message.from_user.id, 'Выберите необходимую дату и время отложенного поста для публикации:', reply_markup=markup) #ответ бота
        bot.send_message(message.from_user.id, 'Выберите число:', reply_markup=markup2) #ответ бота

    elif message.text == 'Заново':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Меню')
        btn2 = types.KeyboardButton('Фото')
        btn3 = types.KeyboardButton('Видео')
        btn4 = types.KeyboardButton('Карусель')
        btn5 = types.KeyboardButton('Сториз')
        markup.add(btn2, btn3, btn4, btn5, btn1)
        bot.send_message(message.from_user.id, 'Информация очищена!', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Выберите тип поста:', reply_markup=markup) #ответ бота

    elif message.text == 'Вызов':
        print(requests.post('http://localhost:3000/', params={'test':'1'}).content)

    elif message.text == 'Запланированные посты':
        files = os.listdir(user_path)
        if len(files) > 0:
            bot.send_message(message.from_user.id, 'Постов запланировано: ' + str(len(files)), parse_mode='Markdown')

        else:
            bot.send_message(message.from_user.id, 'У вас еще нет запланированных постов. Самое время создать новый!', parse_mode='Markdown')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    days = ['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10','day11','day12','day13','day14','day15','day16','day17','day18','day19','day20','day21','day22','day23','day24','day25','day26','day27','day28','day29','day30','day31']
    month = ['mon1','mon2','mon3','mon4','mon5','mon6','mon7','mon8','mon9','mon10','mon11','mon12']
    month_list = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
    hour = ['hour1','hour2','hour3','hour4','hour5','hour6','hour7','hour8','hour9','hour10','hour11','hour12','hour13','hour14','hour15','hour16','hour17','hour18','hour19','hour20','hour21','hour22','hour23','hour00']
    minutes = ['min00','min05','min10','min15','min20','min25','min30','min35','min40','min45','min50','min55']
    markup3 = quick_markup({
            'Январь': {'callback_data': 'mon1'},
            'Февраль': {'callback_data': 'mon2'},
            'Март': {'callback_data': 'mon3'},
            'Апрель': {'callback_data': 'mon4'},
            'Май': {'callback_data': 'mon5'},
            'Июнь': {'callback_data': 'mon6'},
            'Июль': {'callback_data': 'mon7'},
            'Август': {'callback_data': 'mon8'},
            'Сентябрь': {'callback_data': 'mon9'},
            'Октябрь': {'callback_data': 'mon10'},
            'Ноябрь': {'callback_data': 'mon11'},
            'Декабрь': {'callback_data': 'mon12'}
        }, row_width=4)
    markup4 = quick_markup({
            '1': {'callback_data': 'hour1'},
            '2': {'callback_data': 'hour2'},
            '3': {'callback_data': 'hour3'},
            '4': {'callback_data': 'hour4'},
            '5': {'callback_data': 'hour5'},
            '6': {'callback_data': 'hour6'},
            '7': {'callback_data': 'hour7'},
            '8': {'callback_data': 'hour8'},
            '9': {'callback_data': 'hour9'},
            '10': {'callback_data': 'hour10'},
            '11': {'callback_data': 'hour11'},
            '12': {'callback_data': 'hour12'},
            '13': {'callback_data': 'hour13'},
            '14': {'callback_data': 'hour14'},
            '15': {'callback_data': 'hour15'},
            '16': {'callback_data': 'hour16'},
            '17': {'callback_data': 'hour17'},
            '18': {'callback_data': 'hour18'},
            '19': {'callback_data': 'hour19'},
            '20': {'callback_data': 'hour20'},
            '21': {'callback_data': 'hour21'},
            '22': {'callback_data': 'hour22'},
            '23': {'callback_data': 'hour23'},
            '00': {'callback_data': 'hour00'}
    }, row_width=4)
    markup5 = quick_markup({
            '00': {'callback_data': 'min00'},
            '05': {'callback_data': 'min05'},
            '10': {'callback_data': 'min10'},
            '15': {'callback_data': 'min15'},
            '20': {'callback_data': 'min20'},
            '25': {'callback_data': 'min25'},
            '30': {'callback_data': 'min30'},
            '35': {'callback_data': 'min35'},
            '40': {'callback_data': 'min40'},
            '45': {'callback_data': 'min45'},
            '50': {'callback_data': 'min50'},
            '55': {'callback_data': 'min55'}
    }, row_width=4)
    if callback.data in days:
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Вы выбрали число: ' + callback.data[3:]) #ответ бота
        bot.send_message(callback.message.chat.id, 'Выберите месяц:', reply_markup=markup3) #ответ бота
        global d
        d = callback.data[3:]

    elif callback.data in month:
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Вы выбрали месяц: ' + month_list[int(callback.data[3:])-1]) #ответ бота
        bot.send_message(callback.message.chat.id, 'Год по умолчанию выбран: 2024') #ответ бота
        bot.send_message(callback.message.chat.id, 'Выберите час:', reply_markup=markup4) #ответ бота
        global m
        m = callback.data[3:]
        global mt
        mt = month_list[int(callback.data[3:])-1]

    elif callback.data in hour:
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Вы выбрали час: ' + callback.data[4:]) #ответ бота
        bot.send_message(callback.message.chat.id, 'Выберите минуты:', reply_markup=markup5) #ответ бота
        global h
        h = callback.data[4:]

    elif callback.data in minutes:
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Вы выбрали: ' + callback.data[3:] + ' минут') #ответ бота
        global mi
        mi = callback.data[3:]
        date = ''
        date = d + ' ' + mt + ' 2024 ' + h + ':' + mi
        # assigned regular string date
        date_time = datetime.datetime(2024, int(m), int(d), int(h), int(mi))
        files = os.listdir(user_path)
        print(files)
        print(len(files))
        task_path = user_path+'/task'+str(len(files)+1)
        if not os.path.exists(task_path):
            os.makedirs(task_path)
        with open(task_path+'/task'+str(len(files)+1)+'.txt', "w") as file:
            file.write(str(time.mktime(date_time.timetuple()))+' \n')
        bot.send_message(callback.message.chat.id, 'Вы выбрали дату: ' + date) #ответ бота
        sent = bot.send_message(callback.message.chat.id, 'Пришлите фото для поста') #ответ бота
        bot.register_next_step_handler(sent, take_photo)

def take_photo(message):
    if message.content_type == 'photo':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Новый пост')
        btn2 = types.KeyboardButton('Запланированные посты')
        markup.add(btn1, btn2)
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        files = os.listdir(user_path)
        print(len(files))
        task_path = user_path+'/task'+str(len(files))
        with open(task_path+'/task'+str(len(files))+'.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Ваш пост запланирован!', reply_markup=markup) #ответ бота)

    else: 
        sent2 = bot.send_message(message.chat.id, 'Это не фото') #ответ бота)
        bot.register_next_step_handler(sent2, take_photo)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
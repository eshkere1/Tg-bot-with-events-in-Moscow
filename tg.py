from telebot import types
from config import bot
from get_weather import get_weather_report
from date_maker import date_maker
import json


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard_start = types.InlineKeyboardMarkup()
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Это наш бот, для получения информации об отдыхе в Москве, самых лучших праздниках и встречах!".format(message.from_user),
        reply_markup=keyboard_start
    )
    bot.send_message(message.chat.id, "Выберите интересующую вас информацию:", reply_markup=keyboard_choose)


@bot.message_handler(content_types=['text'])
def event_type_search(message):
    global keyboard_choose
    global date_keyboard
    global event_types_keyboard
    btn_date = []
    days = date_maker()
    counter = 0
    for day in days:
        counter += 1
        btn_date.append(types.KeyboardButton(day))
    date_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    date_keyboard.add(btn_date[0], btn_date[1], btn_date[2], btn_date[3], btn_date[4], btn_date[5], btn_date[6],
                      btn_date[7], btn_date[8], btn_date[9]).row()

    keyboard_choose = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    search_btn1 = types.KeyboardButton("Поиск мероприятий по датам🔍")
    search_btn2 = types.KeyboardButton("Поиск погоды по датам 🌧")
    keyboard_choose.add(search_btn1).row(search_btn2)

    if message.text == "Поиск мероприятий по датам🔍":  # поиск по типам мероприятий
        event_types_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        event_types_keyboard.add("Кино🍿").row(types.KeyboardButton("Театр🥻"),
                                                 types.KeyboardButton("Елки👦"),
                                                 types.KeyboardButton("Концерты🥳"),
                                                 types.KeyboardButton("Стендап🤭"))
        bot.send_message(message.chat.id, "Выберите тип мероприятия:", reply_markup=event_types_keyboard)
        bot.register_next_step_handler(message, event_date_search)
    elif message.text == "Поиск погоды по датам 🌧":  # поиск погоды
        bot.send_message(message.chat.id, "Выберите дату на которую вы хотите узнать погоду", reply_markup=date_keyboard)
        bot.register_next_step_handler(message, report_message)
    else:
        bot.send_message(message.chat.id, text="На такое я не запрограммирован :(")


def report_message(message):
    try:
        bot.send_message(message.chat.id, get_weather_report(message), reply_markup=keyboard_choose)
    except ValueError:
        bot.send_message(message.chat.id, "Вы неверно ввели дату, попробуйте снова с помощью кнопки",
                         reply_markup=date_keyboard)
        bot.register_next_step_handler(message, report_message)


def event_reader(date):
    try:
        select_day = ""
        with open(file, "r", encoding="utf8") as json_file:
            json_file = json.load(json_file)
            for day in json_file:
                if f"{date.text[8:]}-{months[int(date.text[5:7])-1]}" == day:
                    select_day = day
                    break
            event_list_length = len(json_file[select_day]["prices"])
            if event_list_length == 0:
                bot.send_message(date.chat.id, "Нет событий на этот день", reply_markup=keyboard_choose)
            else:
                for i in range(event_list_length-1):
                    if json_file[select_day]["prices"][i] != "Билеты":
                        price = f"Цена: {json_file[select_day]["prices"][i]}\n"
                    else:
                        price = f"Билеты есть"
                    bot.send_message(date.chat.id, f"Название: {json_file[select_day]["names"][i]}\n{price}Ссылка: {json_file[select_day]["urls"][i]}")
                bot.send_message(date.chat.id, f"Название: {json_file[select_day]["names"][event_list_length-1]}\nЦена: {json_file[select_day]["prices"][event_list_length-1]}\nСсылка: {json_file[select_day]["urls"][event_list_length-1]}", reply_markup=keyboard_choose)
    except ValueError:
        bot.send_message(date.chat.id, "Вы неверно ввели дату, попробуйте снова с помощью кнопки", reply_markup=date_keyboard)
        bot.register_next_step_handler(date, event_reader)


def event_date_search(message):
    global file
    if message.text == "Кино🍿":
        file = "JSON/schedule_cinema.json"
    elif message.text == "Театр🥻":
        file = "JSON/schedule_theatre.json"
    elif message.text == "Елки👦":
        file = "JSON/new-year-for-kids.json"
    elif message.text == "Концерты🥳":
        file = "JSON/schedule_concert.json"
    elif message.text == "Стендап🤭":
        file = "JSON/standup.json"
    else:
        bot.send_message(message.chat.id, "Вы неверно ввели тип мероприятия, выберите его с помощью кнопки", reply_markup=event_types_keyboard)
        bot.register_next_step_handler(message, event_date_search)
    if file != "":
        bot.send_message(message.chat.id, "Выберите дату:", reply_markup=date_keyboard)
        bot.register_next_step_handler(message, event_reader)


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    event_types_keyboard = ""
    keyboard_choose = ""
    date_keyboard = ""
    file = ""
    months = [
        "yanvarya",
        "fevralya",
        "marta",
        "aprelya",
        "maya",
        "iyunya",
        "iyulya",
        "avgusta",
        "sentyabrya",
        "oktyabrya",
        "noyabrya",
        "dekabrya",
    ]
    main()

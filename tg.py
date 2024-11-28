from telebot import types
from config import bot


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Это наш бот, для получения информации об отдыхе в Москве, самых лучших праздниках и встречах!".format(message.from_user),
        reply_markup=markup
    )
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    search_btn1 = types.KeyboardButton("Поиск мероприятий по датам🔍")
    search_btn2 = types.KeyboardButton("Поиск погоды по датам 🌧")
    markup.add(search_btn1).row(search_btn2)
    bot.send_message(message.chat.id, "Выберите интересующую вас информацию:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def type_search(message):
    if message.text == "Поиск мероприятий по датам🔍":  # поиск по типам мероприятий
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn_type_1 = types.KeyboardButton("Кино🍿")
        btn_type_2 = types.KeyboardButton("Театр🥻")
        btn_type_3 = types.KeyboardButton("Елки👦")
        btn_type_4 = types.KeyboardButton("Концерты🥳")
        btn_type_5 = types.KeyboardButton("Стендап🤭")
        markup.add(btn_type_1).row(btn_type_2, btn_type_3, btn_type_4, btn_type_5)
        bot.send_message(message.chat.id, "Выберите тип мероприятий:", reply_markup=markup)
        bot.register_next_step_handler(message, date_search)
    elif message.text == "Поиск погоды по датам 🌧":
        bot.send_message(message.chat.id, text="погода")
    else:
        bot.send_message(message.chat.id, text="На такое я не запрограммирован :(")


def date_search(message):
    types_of_events = [
        "Кино🍿",
        "Театр🥻",
        "Елки👦",
        "Концерты🥳",
        "Стендап🤭"
    ]
    for type_of_event in types_of_events:
        if message.text == type_of_event[0]:
            print("кино")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_date = types.KeyboardButton("Дата")
    markup.add(btn_date).row()
    bot.send_message(message.chat.id, "Выберите дату:", reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling()
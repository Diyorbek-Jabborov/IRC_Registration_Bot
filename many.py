import telebot
from telebot import types


bot_token = '5665978147:AAG8f8i9kpFAH4mY0p-ZKukL-gKlZH2dDXo'
bot = telebot.TeleBot(bot_token, parse_mode=None)


def start_button_markup():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )

    reply_markup.row(
        telebot.types.KeyboardButton(text="🤖IRC Classic")
    )
    buttons = [
        "🤖IRC Robotics"
    ]

    reply_markup.add(*[
       telebot.types.KeyboardButton(text) for text in buttons
    ])
    return reply_markup




def robotics_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    # buttons = [
    #     "⚽️Footbol",
    #     "🕹SUMO"
    # ]
    # reply_markup.add(*[
    #     telebot.types.KeyboardButton(text) for text in buttons
    # ])
    # reply_markup.row(
    #     telebot.types.KeyboardButton(text="orqaga")
    # )
    itembtn1 = types.KeyboardButton("🕹SUMO")
    itembtn2 = types.KeyboardButton("⚽️Footbol")
    itembtn3 = types.KeyboardButton("↩️Orqaga")
    reply_markup.add(itembtn1, itembtn2, itembtn3)

    return reply_markup


def fudbol_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    # reply_markup.row(
    #     telebot.types.KeyboardButton(text="🕹SUMO")
    # )
    # buttons = [
    #     "⚽️Footbol",
    #     "🖲Arqon tortish",
    #     "orqaga"
    # ]
    # reply_markup.add(*[
    #     telebot.types.KeyboardButton(text) for text in buttons
    # ])
    itembtn1 = types.KeyboardButton("🕹SUMO")
    itembtn2 = types.KeyboardButton("⚽️Footbol")
    itembtn3 = types.KeyboardButton("🖲Arqon tortish")
    itembtn4 = types.KeyboardButton("↩️Orqaga")
    reply_markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

    return reply_markup



def all_phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="📞Telefon nomer jo'natish", request_contact=True)
    keyboard.add(button_phone)
    msg3 = bot.send_message(message.chat.id, '📲Telefon nomerizni kiriting ', reply_markup=keyboard)
    bot.register_next_step_handler(msg3, start_button)



@bot.message_handler(commands=['start'])
def start_message(message):
        getname = str(message.from_user.first_name)
        bot.reply_to(message, f"😊Assalomu alaykum! {getname} \n🤖IRC2️⃣0️⃣2️⃣2️⃣ ga Registratsiya botiga xush kelibsiz.",
                         reply_markup=start_button_markup())



@bot.message_handler(func=lambda m: True)
def echo_message(message):

    if message.text == "🤖IRC Classic":
        text = "🗂Sizni qiziqtirgan bo'limni tanlang"
        msg = bot.send_message(message.from_user.id, text, reply_markup=fudbol_button())
        bot.register_next_step_handler(msg, all_footbol)
    elif message.text == "🤖IRC Robotics":
        text = "🗂Sizni qiziqtirgan bo'limni tanlang"
        msg1 = bot.send_message(message.from_user.id, text, reply_markup=robotics_button())
        bot.register_next_step_handler(msg1, all_sumo)


def all_sumo(message):
    if message.text == "🕹SUMO":
        text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting \n" \
               "Guruh a'zolarining ismini vergul(,) bilan ajratib yozing"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_phone)
    elif message.text == "⚽️Footbol":
        text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting \n" \
               "Guruh a'zolarining ismini vergul(,) bilan ajratib yozing"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_phone)
    else:
        bot.send_message(message.from_user.id, "↩️Orqaga qaytdingiz", reply_markup=start_button_markup())

def all_footbol(message):
    if message.text == "🕹SUMO":
        text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting \n" \
               "Guruh a'zolarining ismini vergul(,) bilan ajratib yozing"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_phone)
    elif message.text == "Footbol":
        text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting \n" \
               "Guruh a'zolarining ismini vergul(,) bilan ajratib yozing"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_phone)
    elif message.text == "🖲Arqon tortish":
        text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting \n" \
               "Guruh a'zolarining ismini vergul(,) bilan ajratib yozing"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_phone)
    else:
        bot.send_message(message.from_user.id, "↩️Orqaga qaytdingiz", reply_markup=start_button_markup())




def start_button(message):
    home = str(message.from_user.first_name)
    bot.send_message(message.from_user.id, f"🥳{home} sizni Ro'yxatdan o'tganingiz bilan tabriklaymiz.", reply_markup=start_button_markup())


bot.polling(none_stop=True)


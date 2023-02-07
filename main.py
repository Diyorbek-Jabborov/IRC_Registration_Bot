import telebot
from telebot import types
import sqlite3

bot_token = '5665978147:AAH_DcBogdxL0gjS4fJ5LmToNkBpkwWV4IE'
bot = telebot.TeleBot(bot_token, parse_mode=None)

connection = sqlite3.connect('base.db', check_same_thread=False)
cursor = connection.cursor()

database = """CREATE TABLE "Log" (
	"id"	INTEGER,
	"country" TEXT,
	"names"	TEXT,
	"kontact"	TEXT,
	"email" TEXT,
	"bosilgan_tugma"	TEXT,
	"yonalish"	TEXT,
	"user_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);"""

try:
    cursor.execute(database)
except sqlite3.OperationalError:
    pass


def get_user(user_id):
    sql = f'select * from Log where user_id={user_id}'
    return cursor.execute(sql).fetchone()


def save_information(contact=None, names=None, pressed_btn=None, userr_id=None, yonalish=None, country=None, email=None):
    sql = ''
    if pressed_btn:
        sql = f"""Insert into Log(user_id, bosilgan_tugma) Values({userr_id}, "{pressed_btn}")"""
    elif country:
        sql = f"""Update Log set names="{country}" where user_id={userr_id}"""
    elif names:
        sql = f"""Update Log set names="{names}" where user_id={userr_id}"""
    elif contact:
        sql = f"""Update Log set kontact="{contact}" where user_id={userr_id}"""
    elif email:
        sql = f"""Update Log set email="{email}" where user_id={userr_id}"""
    elif yonalish:
        sql = f"""Update Log set yonalish="{yonalish}" where user_id={userr_id}"""
    cursor.execute(sql)
    connection.commit()


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
        row_width=1,
        resize_keyboard=True
    )
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
    itembtn1 = types.KeyboardButton("🕹SUMO")
    itembtn2 = types.KeyboardButton("⚽️Footbol")
    itembtn3 = types.KeyboardButton("🖲Arqon tortish")
    itembtn4 = types.KeyboardButton("↩️Orqaga")
    reply_markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return reply_markup


def all_phone(message):
    save_information(userr_id=message.from_user.id, names=message.text)
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
    user = get_user(message.from_user.id)
    if user is None:
        save_information(pressed_btn=message.text, userr_id=message.from_user.id)
    if message.text == "🤖IRC Classic":
        text = "🗂Sizni qiziqtirgan bo'limni tanlang"
        msg = bot.send_message(message.from_user.id, text, reply_markup=fudbol_button())
        bot.register_next_step_handler(msg, all_footbol)
    elif message.text == "🤖IRC Robotics":
        text = "🗂Sizni qiziqtirgan bo'limni tanlang"
        msg1 = bot.send_message(message.from_user.id, text, reply_markup=robotics_button())
        bot.register_next_step_handler(msg1, all_sumo)


def all_sumo(message):
    if message.text != '↩️Orqaga':
        save_information(yonalish=message.text, userr_id=message.from_user.id)
    if message.text == "🕹SUMO":
        text = "🇺🇿Iltimos davlatingizni Kiriting"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_name)
    elif message.text == "⚽️Footbol":
        text = "🇺🇿Iltimos davlatingizni Kiriting"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_name)
    else:
        bot.send_message(message.from_user.id, "Orqaga qaytdingiz", reply_markup=start_button_markup())

def all_footbol(message):
    if message.text != '↩️Orqaga':
        save_information(yonalish=message.text, userr_id=message.from_user.id)
    if message.text == "🕹SUMO":
        text = "🇺🇿Iltimos davlatingizni Kiriting"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_name)
    elif message.text == "Footbol":
        text = "🇺🇿Iltimos davlatingizni Kiriting"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_name)
    else:
        text = "🇺🇿Iltimos davlatingizni Kiriting"
        msg = bot.send_message(message.from_user.id, text)
        bot.register_next_step_handler(msg, all_name)

def all_name(message):
    save_information(country=message.text, userr_id=message.from_user.id)
    text = "👥Iltimos guruh a'zolarining Ismi va Familyasini kiriting"
    msg = bot.send_message(message.from_user.id, text)
    bot.register_next_step_handler(msg, all_email)


def all_email(message):
    save_information(email=message.text, userr_id=message.from_user.id)
    text = "📧Email addresingizni kirting"
    msg = bot.send_message(message.from_user.id, text)
    bot.register_next_step_handler(msg, all_phone)


def start_button(message):
    home = str(message.from_user.first_name)
    try:
        save_information(contact=message.contact.phone_number, userr_id=message.from_user.id)
    except:
        save_information(contact=message.text, userr_id=message.from_user.id)
    bot.send_message(message.from_user.id, f"🥳{home} sizni Ro'yxatdan o'tganingiz bilan tabriklaymiz.", reply_markup=start_button_markup())

bot.polling(none_stop=True)






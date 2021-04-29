import telebot;
#import json;
from telebot import types;
#hello asldn
bot = telebot.TeleBot('1747166693:AAHmYjtrQ8M4LtmBU4jWFRDYgH6GMBcxv_A');

name = '';
surname = '';
age = 0;

@bot.message_handler(content_types=['text'])
def start (message):
    if message.text =='/reg':
        message_reg(message)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привіт, чим можу бути корисний?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/help - help \n/love - secret \n/reg - регістрація")
    elif message.text == "/love":
        bot.send_message(message.from_user.id, "А я буль мою Алінку")
    else:
        bot.send_message(message.from_user.id, 'Напиши /help');

def message_reg(message):
    bot.send_message(message.from_user.id, "Назви себе");
    bot.register_next_step_handler(message, get_name);
    #bot.send_message(message.from_user.id, message);
def get_name (message):
    global name;
    name = message.text;

    bot.send_message(message.from_user.id, 'А яке прізвище ?');
    bot.register_next_step_handler(message, get_surn);

def get_surn(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'А скільки років ?');
    bot.register_next_step_handler(message, get_age);

def get_age (message):
    global age;
    try:
        age = int(message.text);
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, будь ласка. Давай заново');
        #bot.send_message(message.from_user.id, "Назви себе");
        return(message_reg(message));
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тобі ' + str(age) + ' років, тебе звуть  ' + name + ' ' + surname + ' ?';
    #bot.send_message(message.from_user.id, 'Тобі ' + str(age) + ' років, тебе звуть ' + name + ' ' + surname + '?');
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_workers(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )');
        result = '\n' + str(call.message.from_user.id) + str(age) + '/' + name + '/' + surname ;
        #bot.send_message(call.message.chat.id, result);
        file = open('Database.txt', 'a');
        file.write(result);
        file.close();
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Ну ладно : )');

bot.polling(none_stop=True, interval=0)






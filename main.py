import telebot;
#import json;
from telebot import types;
#test commit

bot = telebot.TeleBot('1747166693:AAGitUlj7HndObBzAks4OerxwQAuMWJ_wIs');


name = '';
surname = '';
father_name = '';
number = 0;
email = '';
bank = '';
position = '';
age = 0;

@bot.message_handler(content_types=['text'])
def start (message):
    if message.text =='/reg':
        message_reg(message)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привіт, чим можу бути корисний?")
        #bot.send_message(message.from_user.id, message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/help - help \n/love - secret \n/reg - регістрація")
    elif message.text == "/love" and message.from_user.username == "Forewer_Dreamer":
        bot.send_message(message.from_user.id, "А я буль мою Алінку")
    elif message.text == "/file":
        file_read(message)
    else:
        bot.send_message(message.from_user.id, 'Напиши /help');

def file_read(message):
    file = open('Database.txt', 'r')
    text = file.read()
    bot.send_message(message.from_user.id, text)

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
    bot.send_message(message.from_user.id, 'По-батькові ?');
    bot.register_next_step_handler(message, get_father_name);

def get_father_name(message):
    global father_name;
    father_name = message.text;
    bot.send_message(message.from_user.id, 'Назва фінансової установи ?');
    bot.register_next_step_handler(message, get_bank_name);

def get_bank_name(message):
    global bank;
    bank = message.text;
    bot.send_message(message.from_user.id, 'Який номер телефону ?');
    bot.register_next_step_handler(message, get_number);

def get_number(message):
    global number;
    number = message.text;
    bot.send_message(message.from_user.id, 'Яка ваша електронна пошта ?');
    bot.register_next_step_handler(message, get_email);

def get_email(message):
    global email;
    email = message.text;
    bot.send_message(message.from_user.id, 'Яка ваша посада ?');
    bot.register_next_step_handler(message, get_position);

def get_position(message):
    global position;
    position = message.text;
    #bot.send_message(message.from_user.id, 'Яка ваша посада ?');
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Ви ' + name + ' ' + father_name + ' ' + surname + '. '+ '\nВаша електронна пошта: '+ email + '. \nВаш контактний номер: ' + str(number) + '. \nВаша установа: ' + bank + '. \nВаша посада: ' + position + ' ?';
    # bot.send_message(message.from_user.id, 'Тобі ' + str(age) + ' років, тебе звуть ' + name + ' ' + surname + '?');
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



"""
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
"""
@bot.callback_query_handler(func=lambda call: True)
def callback_workers(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )');
        result = '\n' + str(call.message.from_user.id) + '/' + name + '/' + father_name + '/' + surname + '/'+ email + '/' + str(number) + '/' + bank + '/' + position ;
        #bot.send_message(call.message.chat.id, result);
        file = open('Database.txt', 'a');
        file.write(result);
        file.close();
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Ну ладно : )');
        #return (message_reg(call.message));

bot.polling(none_stop=True, interval=0)






import aiogram
import asyncio

import telebot

bot = telebot.TeleBot('1:A')

print(bot.get_me())


@bot.message_handler(commands=['start'])
def point1(message):
    msg = bot.send_message(message.chat.id, 'Введите почту')
    bot.register_next_step_handler(msg, point2)


def point2(message):
    print(f'POINT2: на шаге point1 введено {message.text}')
    msg = bot.send_message(message.chat.id, 'Введите сообщение')
    bot.register_next_step_handler(msg, point3, message.text)


def point3(message, message_point2):
    print(f'POINT3: на шаге point1 введено {message_point2}, на шаге point2 введено {message.text}')
    msg = bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(msg, dw, message_point2, message.text)


def dw(message, message_point2, message_point3):
    print(f'DW: на шаге point1 введено {message_point2}, на шаге point2 введено {message_point3}, '
          f'на шаге point3 введено {message.text}')
    bot.send_message(message.chat.id, f'Ваш ввод:\nпочта: {message_point2}\nсообщение: {message_point3}\n'
                                      f'число: {message.text}')


bot.polling(none_stop=True, interval=0)
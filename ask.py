import telebot
import xlrd
from random import (randint, random)
def rand():
    rb = xlrd.open_workbook('Saved translation.xlsx')
    sheet = rb.sheet_by_index(0)
    rownum = randint(0, sheet.nrows)
    return sheet.cell_value(rownum, 0)+' ----- '+sheet.cell_value(rownum, 1) + '\n' +sheet.cell_value(rownum, 2)+ ' ----- ' + sheet.cell_value(rownum, 3)
token = "1001230120:AAHB5gaj02BOsMTENcNDBGJFgKOzNYm4L70"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, rand())
bot.polling()

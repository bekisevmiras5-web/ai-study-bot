import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я AI помощник 🤖")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

bot.polling()

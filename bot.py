import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7276733157:AAErtnrdBROGkAxgiSTez5j4SyXtSOgtI1A'
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в Финансовый Помощник! Нажмите кнопку ниже, чтобы открыть приложение.")
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://yourdomain.com")
    web_app_button = InlineKeyboardButton(text="Open Financial Assistant", web_app=web_app_info)
    markup.add(web_app_button)
    bot.send_message(message.chat.id, "Откройте приложение", reply_markup=markup)

bot.polling()

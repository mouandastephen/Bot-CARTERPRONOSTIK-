import os
import telebot
from flask import Flask
from threading import Thread

# Récupération du Token configuré sur Render
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def health():
    return "Bot CARTER98 en ligne", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Scanner CARTER98 activé !\nEn attente des analyses Betpawa...")

if __name__ == "__main__":
    # Thread pour Render
    Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))).start()
    bot.infinity_polling()

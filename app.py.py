import os
import telebot
from flask import Flask
from threading import Thread

# Récupère ton Token de Render
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def health():
    return "Bot CARTER98 opérationnel", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 SCANNER CARTER98 ACTIVÉ !\n\nJe suis prêt. Je commence l'analyse de Betpawa...")

if __name__ == "__main__":
    # Thread pour maintenir Render éveillé
    Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))).start()
    bot.infinity_polling()

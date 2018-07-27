import telebot
from flask import Flask, render_template, request
from threading import Thread
app = Flask(__name__)
token = "590872790:AAGQomxTbaFpl9KATP5djOQ6EzyULHJC3XE"

telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

text1 =''
@bot.message_handler(content_types=['text'])
def echo(message):
    global text1
    text = message.text
    user = message.chat.id
    bot.send_message(user, text)
    text1 += message.text
from threading import Thread
@app.route('/')
def index():
    global text1
    return render_template('hello.html', text = text1)
def polling():
    bot.polling(none_stop=True)


def polling2():
    app.run(debug=False, port=8080)
polling_thread = Thread(target=polling)
run_thread = Thread(target=polling2)
polling_thread.start()
run_thread.start()
import telebot
import datetime
from telebot import types
from selenium import webdriver

api = '5450662598:AAGKZ9S1YK45_yk5s5DrTHoFImH8Dlejwus'
bot = telebot.TeleBot(api)

PATH = "D:\KULIAH\SEMESTER 7 (PKL)\Sep_bot\chromedriver.exe"

#memunculkan tanggal
tanggal = datetime.datetime.now()
tanggal = tanggal.strftime('%d-%B-%y')
print(tanggal)

@bot.message_handler(commands=['start'])
def action_start(message):
    nama_depan = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(message, 'Halo, {} {} selamat datang di Sep_Bot' .format(nama_depan,nama_akhir))

@bot.message_handler(commands=['help'])
def action_help(message):
    nama_depan = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    
    bot.reply_to(message, '{} {} Apakah anda butuh bantuan?'.format(nama_depan,nama_akhir))
    markup = types.ReplyKeyboardMarkup()
    itema = types.KeyboardButton('Blimbing')
    itemb = types.KeyboardButton('Sukun')

    #Tambah tombol
    markup.row(itema,itemb)
    bot.send_message(message.chat.id, 'halo apa kabar??' , reply_markup=markup)

@bot.message_handler(regexp="asep")
def action(message):
    driver=webdriver.Chrome(PATH)
    driver.get("http://cctv.malangkota.go.id/cameras_dua")
    time.sleep(10)

print('Bot Sedang berjalan')
bot.polling()




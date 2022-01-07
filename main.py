import telebot
from telebot import types
#modul waktu
import datetime
import time
#modul scrapping web
from urllib.request import urlopen
import urllib

import json
import requests
from bs4 import BeautifulSoup
#modul mengambil data secara random
import random
#
import os
bot = telebot.TeleBot("5049086779:AAGUeZhsHHBT7x250K0Wc1zGzYXjrrDbjv8")


def log(message, perintah):
    global jam, menit
    jam = time.strftime('%H')  # : %M : %S'
    jam = int(jam)+7
    menit = int(time.strftime('%M'))  # : %S')#: %M : %S'
    detik = int(time.strftime('%S'))
    waktu = f"{jam} : {menit} : {detik}"
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime('%d-%B-%Y')
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    #TAMBAHKAN TEXT KE FILE .txt
    text = f"{tanggal} > {waktu} > {nama} {nama_akhir} < {perintah} "
    print(text)

def getData(link):          # dapatkan data dari api 
    url = requests.get(link)
    data = url.json()
    return data

def unduhVideo(video, namaFile):
    page = requests.get(video)
    with open(namaFile, 'wb') as file:
        file.write(page.content)

def unduhMusik(video, namaFile):
    page = requests.get(video)
    with open(namaFile, 'wb') as file:
        file.write(page.content)

def markupVideo(pesan, callback):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
    pesan, callback_data= callback)
    markup.row(item)
    return markup


@bot.message_handler(commands=['start'])
def downloadvidtiktok(message):
    bot.send_message(message.chat.id, 
f'''Halo {message.from_user.first_name}  
Perkenalkan saya Downloader_bot yang akan membantu anda mengunduh konten social media, berikut command yang tersedia :

1️⃣ Tiktok
1. download video tiktok nowm = paste url di chat 
unduh musik click button `Download Musik 🎶`

2️⃣ Instagram
1. download video post/reels/tv = paste url di chat
2. download insta stories = /igs_username
ex : /igs allailqadrillah_
note : 'tidak perlu menggunakan @, dan username harus detail'

3️⃣ Twitter
1. download video twitter = paste url di chat

4️⃣ Youtube
1. download musik youtube = paste url di chat

5️⃣ SoundCloud
1. download musik soundCloud = paste url di chat 

6️⃣ Joox
1. download musik joox = /joox_judulLagu
ex : /joox Alan Walker - Different World
note : 'judul lagunya harus detail'
''') 
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        'Message Developer 🧑🏻‍💻', url='https://telegram.me/Qadrillah')
    markup.row(item)
    bot.send_message(
        message.chat.id, 'jika ada saran fitur ataupun bot terdapat masalah, bisa klik button dibawah', reply_markup=markup)



"""                                      CALLLBACKKK KETIKA BUTTON DI CLICK                                                         """

@bot.callback_query_handler(func=lambda call: True)
def callbacksJoox(call):
# # ketika tombol informasi lagi JOOX click
#     # if call.data == callJoox:
    
#     #     bot.send_chat_action(call.message.chat.id, "upload_photo")
#     #     kirimFoto(f"{laguJoox}.jpg", call.message.chat.id)
#     #     bot.send_chat_action(call.message.chat.id, "typing")
#     #     bot.send_message(call.message.chat.id, f"judul lagu : {laguJoox}\nalbum : {dataJoox['result']['album']}\npenyanyi : {dataJoox['result']['penyanyi']}\npublish : {dataJoox['result']['publish']}" )
#     #     bot.send_message(call.message.chat.id, f"{dataJoox['lirik']['result']}" )
#     #     bot.edit_message_reply_markup()
#     #     log(call.message, f"informasi lagu {laguJoox} ")  


#     if call.data == callTiktok:
#         page = requests.get(musikTiktok)
#         with open(namaFileMusikTiktok, 'wb') as file:
#             file.write(page.content)
#         # kirim musik
#         out = open(namaFileMusikTiktok, 'rb')
#         bot.send_audio(call.message.chat.id, out)
#         out.close()
#         log(call.message, f"Tiktok Music Downloader {namaFileMusikTiktok}")

        if call.data in callbackTiktok:
            bot.send_chat_action(call.from_user.id, "upload_audio")
            print(f"{call.data}.mp3")
            bot.send_audio(call.from_user.id, open(f"{call.data}.mp3", 'rb'))

# key ZENZAPI
api_key = ["b9b38e428d49", "6301bfc9de", "f64a95d64260", "879b62e71cdf"] 
"""                                          TIKTOK DOWNLOADER                                                                  """
callbackTiktok =[]
@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
    # dapatkan data dari api hingga berhasil
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_video")
            link = f"https://zenzapi.xyz/downloader/tiktok?url={message.text}&apikey={api_key[i]}"
            dataTiktok = getData(link)
            if dataTiktok['status'] == False:
                i += 1
            elif dataTiktok['status'] == "OK":
                break
        # ambil url yang diperlukan
        urlNOWM = dataTiktok['result']['nowatermark']
        urlAudio = dataTiktok['result']['audio']
        file = f"{message.from_user.first_name}_{message.text.split('/')[3]}"
        # unduh file
        bot.send_chat_action(message.chat.id, "upload_video")
        unduhVideo(urlNOWM, f"{file}.mp4")
        unduhMusik(urlAudio, f"{file}.mp3")
        markup = markupVideo(f'Download Musik 🎶', file)
        callbackTiktok.append(file)
        # kirim video dan button untuk mendownload musik
        bot.send_video(message.chat.id, open(f"{file}.mp4", 'rb'), reply_markup=markup)

        log(message, f"TIKTOK VID - {i}")
      





print("bot running...!!!")
bot.polling()   

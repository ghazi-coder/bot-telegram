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

def unduhMusik(musik, namaFile):
    page = requests.get(musik)
    with open(namaFile, 'wb') as file:
        file.write(page.content)

def markupVideo(pesan, callback):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
    pesan, callback_data= callback)
    markup.row(item)
    return markup
def markupVideoDuaButtton(pesan1, pesan2, callback1, callback2):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(pesan1, callback_data= callback1)
    item2 = types.InlineKeyboardButton(pesan2, callback_data= callback2)
    markup.row(item1)
    markup.row(item2)
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

import moviepy.editor as mp
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    # TIKTOK BUTTON ACTION
        if call.data in callbackOriTiktok:
            bot.send_chat_action(call.from_user.id, "upload_audio")
            bot.send_audio(call.from_user.id, open(f"{call.data}.mp3", 'rb'))
            log(call.message, f"TIKTOK AUDIO")

        if call.data in callbackVidTiktok:
            bot.send_chat_action(call.from_user.id, "upload_audio")
            # convert video menjadi audio
            clip = mp.VideoFileClip(f"{call.data.split('-')[0]}.mp4")
            clip.audio.write_audiofile(f"{call.data}VID.mp3")
            bot.send_audio(call.from_user.id, open(f"{call.data}VID.mp3", 'rb'))
            log(call.message, f"TIKTOK AUDIO CONVERT")

# key ZENZAPI
api_key = ["b9b38e428d49", "6301bfc9de", "f64a95d64260", "879b62e71cdf"] 
"""                                          TIKTOK DOWNLOADER                                                                  """
callbackOriTiktok =[]
callbackVidTiktok =[]
@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
    # dapatkan data dari api hingga berhasil
    try:
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_video")
            link = f"https://zenzapi.xyz/downloader/musically?url={message.text}&apikey={api_key[i]}"
            dataTiktok = getData(link)
            if dataTiktok['status'] == False:
                i += 1
            elif dataTiktok['status'] == "OK":
                break
        # ambil url yang diperlukan
        urlNOWM = dataTiktok['result']['nowm']
        urlAudio = dataTiktok['result']['audio']
   
        file = f"{message.from_user.first_name}_{message.text.split('/')[3]}"
        file2 = f"{message.from_user.first_name}_{message.text.split('/')[3]}-video"
        # unduh file
        bot.send_chat_action(message.chat.id, "upload_video")
        unduhVideo(urlNOWM, f"{file}.mp4")
        markup = markupVideoDuaButtton('Download Musik Original 🎶', 'Download Musik Video 🎶', file, file2)
        # kirim video dan button untuk mendownload musik
        bot.send_video(message.chat.id, open(f"{file}.mp4", 'rb'), reply_markup=markup)
        callbackOriTiktok.append(file)
        callbackVidTiktok.append(file2)

        log(message, f"TIKTOK VID ZENZ- {i}")
        unduhMusik(urlAudio, f"{file}.mp3")
    except:                                 # API CADANGAN
            bot.send_chat_action(message.chat.id, "upload_video")
            link = f"https://hadi-api.herokuapp.com/api/tiktok?url={message.text}"
            dataTiktok = getData(link)
            # dapatankan link yang diperlukan
            urlNOWM = dataTiktok['result']['video']['nowm']
            urlAudio = dataTiktok['result']['audio_only']['audio1']
    
            file = f"{message.from_user.first_name}_{message.text.split('/')[3]}"
            file2 = f"{message.from_user.first_name}_{message.text.split('/')[3]}-video"
            # unduh file
            bot.send_chat_action(message.chat.id, "upload_video")
            unduhVideo(urlNOWM, f"{file}.mp4")
            markup = markupVideoDuaButtton('Download Musik Original 🎶', 'Download Musik Video 🎶', file, file2)
            # kirim video dan button untuk mendownload musik
            bot.send_video(message.chat.id, open(f"{file}.mp4", 'rb'), reply_markup=markup)
            callbackOriTiktok.append(file)
            callbackVidTiktok.append(file2)

            log(message, f"TIKTOK VID HADI ")
            unduhMusik(urlAudio, f"{file}.mp3")



"""                                                     INSTAGRAM                                                               """

@bot.message_handler(regexp='https://www.instagram.com/')
def downloadvidinstagram(message):

            bot.send_chat_action(message.chat.id, "upload_video")
            url = "https://instagram47.p.rapidapi.com/post_details"
            querystring = {"shortcode": message.text.split('/')[4]} 
            headers = {
            'x-rapidapi-host': "instagram47.p.rapidapi.com",
            'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c" # i
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            
            urlVideo = data['body']['video_url']
             
            unduhVideo(urlVideo, f"{message.text.split('/')[4]}.mp4")
            bot.send_chat_action(message.chat.id, "upload_video")
            bot.send_video(message.chat.id, open(f"{message.text.split('/')[4]}.mp4", 'rb'))

            log(message, f"INSTAGRAM Video {data['body']['owner']['username']}")



print("bot running...!!!")
bot.polling()   

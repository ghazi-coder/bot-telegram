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

def unduhVideo(video, namaFile):
    page = requests.get(video)
    with open(namaFile, 'wb') as file:
        file.write(page.content)


def kirimVideo(namaFile, tujuan):
        while True:
            try:
              out = open(namaFile, 'rb')
              x = bot.send_video(tujuan, out)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
def kirimFoto(namaFile, tujuan):
        while True:
            try:
              out = open(namaFile, 'rb')
              x = bot.send_photo(tujuan, out)
              out.close()
              if x is not EOFError:
                break
            except:
              continue

def kirimMusikMarkup(tujuan, namaFile, markup):
    while True:
        try:
            # kirim musik
            out = open(namaFile, 'rb')
            bot.send_chat_action(tujuan, "upload_audio")
            x = bot.send_audio(tujuan, namaFile, reply_markup=markup)
            out.close()
            if x is not EOFError:
                break
        except:
            continue

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
# tampilkan button 
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        'Message Developer 🧑🏻‍💻', url='https://telegram.me/Qadrillah')
    markup.row(item)
    bot.send_message(
        message.chat.id, 'jika ada saran fitur ataupun bot terdapat masalah, bisa klik button dibawah', reply_markup=markup)

def waktu():
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime('%d-%B-%Y')
    jam = time.strftime('%H')  # : %M : %S'
    menit = int(time.strftime('%M'))  # : %S')#: %M : %S'
    detik = int(time.strftime('%S'))
    return f"{tanggal}{jam}{menit}{detik}"

"""  CALLLBACKKK KETIKA BUTTON DI CLICK"""
@bot.callback_query_handler(func=lambda call: True)
def callbacksJoox(call):
# ketika tombol informasi lagi JOOX click
    if call.data == callJoox:
    
        bot.send_chat_action(call.message.chat.id, "upload_photo")
        kirimFoto(f"{laguJoox}.jpg", call.message.chat.id)
        bot.send_chat_action(call.message.chat.id, "typing")
        bot.send_message(call.message.chat.id, f"judul lagu : {laguJoox}\nalbum : {dataJoox['result']['album']}\npenyanyi : {dataJoox['result']['penyanyi']}\npublish : {dataJoox['result']['publish']}" )
        bot.send_message(call.message.chat.id, f"{dataJoox['lirik']['result']}" )
        bot.edit_message_reply_markup()
        log(call.message, f"informasi lagu {laguJoox} ")  


    if call.data == callTiktok:
        page = requests.get(musikTiktok)
        with open(namaFileMusikTiktok, 'wb') as file:
            file.write(page.content)
        # kirim musik
        out = open(namaFileMusikTiktok, 'rb')
        bot.send_audio(call.message.chat.id, out)
        out.close()
        log(call.message, f"Tiktok Music Downloader {namaFileMusikTiktok}")

"""                                 TIKTOK DOWNLOADER                                                   """

@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
        global callTiktok
        global musikTiktok
        global namaFileMusikTiktok

        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(f"https://api.dapuhy.ga/api/socialmedia/musical?url={message.text}&apikey=qadrillah")
        data = url.json()
        video = data['result']["mp4"]["server_1"]
        musikTiktok = data['result']["mp3"]["server_1"] 
        sumber = message.text.split('/')

        callTiktok  = f'{sumber} {waktu()}'
        namaFile = f"{message.from_user.first_name}_{sumber[3]}.mp4"
        namaFileMusikTiktok = f"{message.from_user.first_name}_{sumber[3]}.mp3"
    # download video
        unduhVideo(video, namaFile)

     # tampilkan button untuk mendownload musik
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(
        'Download Musik 🎶', callback_data=f"download musik tiktok {time}")
        markup.row(item)
     # kirim video
        print(f"download musik tiktok {time}")
        while True:
            try:
              bot.send_chat_action(message.chat.id, "upload_video")
              out = open(namaFile, 'rb')
              x = bot.send_video(message.chat.id, out, reply_markup=markup)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
        
        log(message, f"Tiktok Video Downloader {namaFile}")
    # kirim musik ketika diclick tombol



"""                             INSTAGRAM DOWNLOADER                                    """
# VIDEO POST, REELS and TV downloader
@bot.message_handler(regexp='https://www.instagram.com/')
def downloadPostIG(message):
    try:
        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(f"https://api.dapuhy.ga/api/socialmedia/igdownload?url={message.text}&apikey=qadrillah")
        data = url.json()
        video = data['result']["download_url"]

        sumber = data["user"]["username"]
        namaFile = f"{message.from_user.first_name}_{sumber}.mp4"

    # download video
        unduhVideo(video, namaFile)

    # kirim video
        while True:
            try:
                bot.send_chat_action(message.chat.id, "upload_video")
                out = open(namaFile, 'rb')
                x = bot.send_video(message.chat.id, out)
                out.close()
                if x is not EOFError:
                    break
            except:
                continue
        log(message, "IG DOWNLOADER 1")

    except:
        i = len(api_key-1)
        while True:
            bot.send_chat_action(message.chat.id, "upload_video")
            url = requests.get(f"https://zenzapi.xyz/api/downloader/instagram?url={message.text}&apikey={api_key[i]}")
            data = url.json()

            if data['status'] == False:
                i -= 1
            elif data['status'] == "OK":
                break

        video = data['result']["link"]
        sumber = data["result"]["caption"]["username"]
        namaFile = f"{message.from_user.first_name}_{sumber}.mp4"
    # download video
        unduhVideo(video, namaFile)
    # kirim video
        while True:
            try:
              bot.send_chat_action(message.chat.id, "upload_video")
              out = open(namaFile, 'rb')
              x = bot.send_video(message.chat.id, out)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
        log(message, "IG DOWNLOADER 2")
               


rapidApi_key = ["f355e8c71bmsh2f12c8e8772a755p1aba64jsn14d36932fc37", "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"]
# 
# FULL STORY downloader
@bot.message_handler(commands=['igs'])
def downloadStoriesIG(message):
        
     # cari id dari username
    try:

            url = requests.get(f"https://zenzapi.xyz/api/downloader/ytmp3?url={message.text}&index=2&apikey=6301bfc9de")
            data = url.json()
            url = "https://instagram-stories1.p.rapidapi.com/v1/get_user_id"
            querystring = {"username":message.text[5:]}
            headers = {
                'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
                'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            dataID = json.loads(response.text)
            print(dataID)
            id = dataID["user_id"]


        # cari story
            try:
                url = "https://instagram-stories1.p.rapidapi.com/v2/user_stories"
                querystring = {"userid":id} # cari id dengan API
                headers = {
                    'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
                    'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
                    }
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = json.loads(response.text)

                if data['status'] == 'Fail':
                   bot.send_message(message.chat.id, "user tidak memiliki stories!")
                   
                else:  
                # unduh story
                   data = data['downloadLinks']
                   for i in range(0, int(len(data))):
                        if data[i]["mediaType"] == "video":
                            bot.send_chat_action(message.chat.id, "upload_video")
                            namaFile = f"{message.text[5:]}_{i}.mp4"
                            snap = data[i]["url"]
                            unduhVideo(snap, namaFile)
                            kirimVideo(namaFile, message.chat.id)

                        else:
                            bot.send_chat_action(message.chat.id, "upload_photo")
                            namaFile = f"{message.text[5:]}_{i}.jpg"
                            snap = data[i]["url"]
                            unduhVideo(snap, namaFile)
                            kirimFoto(namaFile, message.chat.id)

                   bot.send_message(message.chat.id, f"total {len(data)} stories")
                   log(message, f"IG STORY {message.text[5:]}")

            except:
                bot.send_message(message.chat.id, "maaf, username tidak ditemukan!")     
    except:
            bot.send_message(message.chat.id, dataID['Warning'])    

api_key = ["b9b38e428d49", "6301bfc9de", "f64a95d64260", "879b62e71cdf"] 
@bot.message_handler(commands=['joox'])
def downloadjoox(message):
# ambil api key yang tidak kadaluarsa 
    i = 0
    global dataJoox
    global laguJoox
    global waktuJoox
    global callJoox

    while True:
        bot.send_chat_action(message.chat.id, "upload_audio")
        url = requests.get(f"https://zenzapi.xyz/api/downloader/joox?query={message.text.split(' ')[1:]}&apikey={api_key[i]}")
        dataJoox = url.json()

        if dataJoox['status'] == False:
            i += 1
        elif dataJoox['status'] == "OK":
            break

    page = requests.get(dataJoox['result']['mp3Link'])
    laguJoox = dataJoox['result']['lagu']
    waktuJoox = waktu()
    callJoox  = f'joox {laguJoox} {waktuJoox}'
    with open(f"{laguJoox}.mp3", 'wb') as file:
        file.write(page.content)

#tampilkan button untuk mendownload musik
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
    f'informasi lagu {laguJoox}', callback_data= callJoox)
    markup.row(item)

    while True:
        try:
            # kirim musik
            out = open(f"{laguJoox}.mp3", 'rb')
            bot.send_chat_action(message.chat.id, "upload_audio")
            x = bot.send_audio(message.chat.id, out, reply_markup=markup)
            out.close()
            if x is not EOFError:
                break
        except:
            continue

    log(message, f"DOWNLOAD MUSIK JOOX {laguJoox} {i}")
    unduhVideo(dataJoox['result']['img'], f"{laguJoox}.jpg")
  



"""
                                   YOUTUBE MUSIK DOWNLOADER                         
"""


@bot.message_handler(regexp='youtu')
def downloadMusikYoutube(message):
    i = 0
    while True:
        bot.send_chat_action(message.chat.id, "upload_audio")
        url = requests.get(f"https://zenzapi.xyz/api/downloader/ytmp3?url={message.text}&index=2&apikey={api_key[i]}")
        data = url.json()

        if data['status'] == False:
            i += 1
        elif data['status'] == "OK":
            break
    url = requests.get(f"https://zenzapi.xyz/api/downloader/ytmp3?url={message.text}&index=2&apikey=6301bfc9de")
    data = url.json()
    
    bot.send_chat_action(message.chat.id, "upload_audio")
        # doenload musik
    page = requests.get(data['result']['url'])
    title = data['result']['title']
    with open(f"{title}.mp3", 'wb') as file:
        file.write(page.content)
    # kirim musik
    out = open(f"{title}.mp3", 'rb')
    bot.send_chat_action(message.chat.id, "upload_audio")
    bot.send_audio(message.chat.id, out)
    out.close()
    log(message,f"DOWNLOAD MUSIK YT {title} {i}")


""" SOUND CLOUND DOWNLOADER
"""
@bot.message_handler(regexp='https://soundcloud.com/')
def downloadjoox(message):
    try:
    # ambil api key yang tidak kadaluarsa 
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(f"https://zenzapi.xyz/api/downloader/soundcloud?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()
            print(message.text.split('?')[0])

            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break
        
            # doenload musik
        page = requests.get(data['result']['url'])
        lagu = data['result']['title']

        with open(f"{lagu}.mp3", 'wb') as file:
            file.write(page.content)
        
        while True:
            try:
                # kirim musik
                out = open(f"{lagu}.mp3", 'rb')
                bot.send_chat_action(message.chat.id, "upload_audio")
                x = bot.send_audio(message.chat.id, out)
                out.close()
                if x is not EOFError:
                    break
            except:
                continue
        log(message, f"SOUND CLOUD DOWNLOADER {i}")
    except:
        bot.send_message(message.chat.id, "musik tidak ditemukan!")
   

"""                             TWITTER DOWNLOADER                                    """
# VIDEO POST, REELS and TV downloader
@bot.message_handler(regexp='https://twitter.com')
def downloadvidtiktok(message):
    try :
        bot.send_chat_action(message.chat.id, "upload_video")
    # ambil apikey satu persatu 
        i = 0
        while True:
            url = requests.get(f"https://zenzapi.xyz/api/downloader/twitter?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()


            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break

        video = data['result']['HD']        

        namaFile = f"{message.from_user.first_name}_twitter.mp4"
    # download video
        unduhVideo(video, namaFile)
    # kirim video
        while True:
            try:
                bot.send_chat_action(message.chat.id, "upload_video")
                out = open(namaFile, 'rb')
                x = bot.send_video(message.chat.id, out)
                out.close()
                if x is not EOFError:
                    break
            except:
                continue
        log(message, f"TWITTER DOWNLOADER {i}")
    except:
        bot.send_message(message.chat.id, "Video tidak ditemukan!")

print("bot running...!!!")
bot.polling()   

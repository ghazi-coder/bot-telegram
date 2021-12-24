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
bot = telebot.TeleBot("1857480052:AAGyNqGpLL7wQ1YiRN313ISiqy4lrcOs49w")


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

def kirimVideoYoutube(message, url, namaFile, action):
        @bot.callback_query_handler(func=lambda call: True)
        def callbacks(call):
            bot.send_chat_action(message.chat.id, "upload_video")
            if call.data == action:
             # doenload video
                unduhVideo(url, namaFile)
                kirimVideo(namaFile, message.chat.id)

"""                                 TIKTOK DOWNLOADER                                                   """

@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(f"https://api.dapuhy.ga/api/socialmedia/musical?url={message.text}&apikey=qadrillah")
        data = url.json()
        video = data['result']["mp4"]["server_1"]
        musik = data['result']["mp3"]["server_1"] 
        sumber = message.text.split('/')

        namaFile = f"{message.from_user.first_name}_{sumber[3]}.mp4"
        namaFileMusik = f"{message.from_user.first_name}_{sumber[3]}.mp3"
    # download video
        unduhVideo(video, namaFile)

     # tampilkan button untuk mendownload musik
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(
        'Download Musik 🎶', callback_data='download musik tiktok')
        markup.row(item)
     # kirim video
        while True:
            try:
              out = open(namaFile, 'rb')
              x = bot.send_video(message.chat.id, out, reply_markup=markup)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
        
        log(message, "Tiktok Video Downloader")
    # kirim musik ketika diclick tombol
        @bot.callback_query_handler(func=lambda call: True)
        def callbacks(call):
            bot.send_chat_action(message.chat.id, "upload_audio")
            if call.data == "download musik tiktok":
             # doenload musik
                page = requests.get(musik)
                with open(namaFileMusik, 'wb') as file:
                    file.write(page.content)
             # kirim musik
                out = open(namaFileMusik, 'rb')
                bot.send_audio(message.chat.id, out)
                out.close()
                log(message, "Tiktok Music Downloader")


"""                             INSTAGRAM DOWNLOADER                                    """
# VIDEO POST, REELS and TV downloader
@bot.message_handler(regexp='https://www.instagram.com/')
def downloadvidtiktok(message):
        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(f"https://zenzapi.xyz/api/downloader/instagram?url={message.text}&apikey=b9b38e428d49")
        data = url.json()
        video = data['result']["link"]
        sumber = data["result"]["caption"]["username"]
        namaFile = f"{message.from_user.first_name}_{sumber}.mp4"

    # download video
        unduhVideo(video, namaFile)

        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(
        'informasi postingan', callback_data='informasi post')
        markup.row(item)

    # kirim video
        while True:
            try:
              out = open(namaFile, 'rb')
              x = bot.send_video(message.chat.id, out, reply_markup=markup)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
        log(message, "IG DOWNLOADER")

        # dapatkan data informasi post
        like = data["result"]["caption"]["total_like"]
        comment = data["result"]["caption"]["total_comment"]
        desc = data["result"]["caption"]["desc"]

        # kirim informasi post ketika diclick tombol
        @bot.callback_query_handler(func=lambda call: True)
        def callbacks(call):
            bot.send_chat_action(message.chat.id, "typing")
            if call.data == "informasi post":
             # download gambar
                page = requests.get(data['result']["link_two"])
                with open(f"{message.from_user.first_name}_{sumber}.jpg", 'wb') as file:
                    file.write(page.content)
             # kirim musik
                out = open(f"{message.from_user.first_name}_{sumber}.jpg", 'rb')
                bot.send_photo(message.chat.id, out)
                out.close()
                bot.send_message(message.chat.id, f"username : {sumber}\nlike : {like}\ncomment : {comment}\ndesc : {desc}")

                log(message, "informasi postingan")



# 
# FULL STORY downloader
@bot.message_handler(commands=['igs'])
def downloadvidtiktok(message):
        
     # cari id dari username
        try:
            url = "https://instagram-stories1.p.rapidapi.com/v1/get_user_id"
            querystring = {"username":message.text[5:]}
            headers = {
                'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
                'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            dataID = json.loads(response.text)
            id = dataID["user_id"]
        except:
            bot.send_message(message.chat.id, "server sedang sibuk, coba beberapa saat lagi!")

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
            data = data['downloadLinks']
        except:
            bot.send_message(message.chat.id, "maaf, username tidak ditemukan!")     

     # unduh story
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



"""
                                   YOUTUBE MUSIK DOWNLOADER                         
"""

@bot.message_handler(regexp='youtu')
def downloadvidtiktok(message):
    url = requests.get(f"https://zenzapi.xyz/api/downloader/ytmp3?url={message.text}&index=2&apikey=b9b38e428d49")
    data = url.json()

    bot.send_chat_action(message.chat.id, "upload_audio")
        # doenload musik
    page = requests.get(data['result']['url'])
    title = data['result']['title']
    with open(f"{title}.mp3", 'wb') as file:
        file.write(page.content)
    # kirim musik
    out = open(f"{title}.mp3", 'rb')
    bot.send_audio(message.chat.id, out)
    out.close()
    log(message, "DOWNLOAD MUSIK YT {title}")






print("bot running...!!!")
bot.polling()       

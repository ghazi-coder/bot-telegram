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
# VIDEO POST dan REELS downloader
@bot.message_handler(regexp='https://www.instagram.com/')
def downloadvidtiktok(message):
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
              out = open(namaFile, 'rb')
              x = bot.send_video(message.chat.id, out)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
        log(message, "IG DOWNLOADER")

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

# # PARTIAL STORY downloader
# @bot.message_handler(commands=['igp'])
# def downloadvidtiktok(message):
        
#      # cari id dari username
#         try:
#             url = "https://instagram-stories1.p.rapidapi.com/v1/get_user_id"
#             querystring = {"username":message.text[5:]}
#             headers = {
#                 'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
#                 'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
#                 }
#             response = requests.request("GET", url, headers=headers, params=querystring)
#             dataID = json.loads(response.text)
#             id = dataID["user_id"]
#         except:
#             bot.send_message(message.chat.id, "server sedang sibuk, coba beberapa saat lagi!")

#      # cari story
#         try:
#             url = "https://instagram-stories1.p.rapidapi.com/v2/user_stories"
#             querystring = {"userid":id} # cari id dengan API
#             headers = {
#                 'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
#                 'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
#                 }
#             response = requests.request("GET", url, headers=headers, params=querystring)
#             data = json.loads(response.text)
#         except:
#             bot.send_message(message.chat.id, "maaf, username tidak ditemukan!")     
        
#      # unduh story
#         partial = ( int(message.text.split(" ")[2]) - 1 )
#         data = data['downloadLinks']
#         jenis = data[partial]["mediaType"]

#         if jenis == "video":
#             bot.send_chat_action(message.chat.id, "upload_video")
#             namaFile = f"{message.text[5:]}_{partial}.mp4"
#             snap = data[partial]["url"]
#             unduhVideo(snap, namaFile)
#             kirimVideo(namaFile, message.chat.id)

#         else:
#             bot.send_chat_action(message.chat.id, "upload_photo")
#             namaFile = f"{message.text[5:]}_{partial}.jpg"
#             snap = data[partial]["url"]
#             unduhVideo(snap, namaFile)
#             kirimFoto(namaFile, message.chat.id)

#         bot.send_message(message.chat.id, f"total {len(data)} stories")
#         log(message, f"IG STORY {message.text[5:]}")

"""
                                   YOUTUBE DOWNLOADER                         
"""

@bot.message_handler(regexp='https://www.youtu')
def downloadvidtiktok(message):
    bot.send_chat_action(message.chat.id, "upload_video")
    print("scrapper")
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
    querystring = {"id":message.text[32:],"geo":"DE"}
    headers = {
        'x-rapidapi-host': "ytstream-download-youtube-videos.p.rapidapi.com",
        'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
 # dapatkan data yang dibutuhkan
    thumb, channel = data['thumb'], data['author']

    unduhVideo(data['link']['22'][0], f"{message.from_user.first_name}_{channel}.mp4") 
    # kirimVideo(f"{message.from_user.first_name}_{channel}.mp4", message.chat.id)
    print("video terunduh")
    # tampilkan button untuk mendownload musik
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
    'Download Sound 🎶', callback_data='download musik youtube')
    markup.row(item)
    # kirim video
    while True:
            try:
              print("mengirim")
              bot.send_chat_action(message.chat.id, "upload_video")
              out = open(f"{message.from_user.first_name}_{channel}.mp4", 'rb')
              x = bot.send_video(message.chat.id, out, reply_markup=markup)
              out.close()
              if x is not EOFError:
                break
            except:
              continue
    log(message, f"DOWNLOAD VIDEO YT {channel}")
 

    url = requests.get(f"https://zenzapi.xyz/api/downloader/ytmp3?url={message.text}&index=2&apikey=b9b38e428d49")
    data = url.json()

 # kirim musik ketika diclick tombol
    @bot.callback_query_handler(func=lambda call: True)
    def callbacks(call):
        bot.send_chat_action(message.chat.id, "upload_audio")
        if call.data == "download musik youtube":
            # doenload musik
            page = requests.get(data['result']['url'])
            with open(f"{message.from_user.first_name}_{channel}.mp3", 'wb') as file:
                file.write(page.content)
            # kirim musik
            out = open(f"{message.from_user.first_name}_{channel}.mp3", 'rb')
            bot.send_audio(message.chat.id, out)
            out.close()
            log(message, "DOWNLOAD SOUND YT {channel}")

    












print("bot running...!!!")
bot.polling()       

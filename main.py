from requests import api
import telebot
from telebot import types
import datetime
import time
from urllib.request import urlopen
import urllib
import json
import requests
import random
import os
from instascrape import *

bot = telebot.TeleBot("5049086779:AAGUeZhsHHBT7x250K0Wc1zGzYXjrrDbjv8")
@bot.message_handler(commands=['tes'])
def downloadvidtiktok(message):
    url = "https://www.instagram.com/p/CYhFuH6hQto/?__a=1"
    SESSIONID = '2135077396%3AcIBHAe6JNABIfo%3A12'
    headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
               "cookie": f"sessionid={SESSIONID};"}
    r = requests.get(url, headers=headers)
    print(r.json())
    
def log(message, perintah):
    global jam, menit
    jam = time.strftime('%H') 
    jam = int(jam)+7
    menit = int(time.strftime('%M'))  
    detik = int(time.strftime('%S'))
    waktu = f"{jam} : {menit} : {detik}"
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime('%d-%B-%Y')
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    #TAMBAHKAN TEXT KE FILE .txt
    text = f"{tanggal} > {waktu} > {nama} {nama_akhir} < {perintah} "
    print(text)
    bot.send_message(-524462976, text)

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
unduh musik click button 

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
    bot.send_message(-515995341, f"{message.from_user.first_name} {message.from_user.last_name} - {message.chat.id}")

@bot.message_handler(commands=['menu'])
def downloadvidtiktok(message):
    bot.send_message(message.chat.id, 
    f'''Halo {message.from_user.first_name}👋
berikut command yang tersedia :

1️⃣ Tiktok
1. download video tiktok nowm = paste url di chat 
unduh musik click button 

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

@bot.message_handler(commands=['tentang'])
def downloadvidtiktok(message):
    bot.send_message(message.chat.id, 
    f'''Halo {message.from_user.first_name}👋 berikut info tentang saya :

- Dibuat menggunakan Python
- Tubuh saya ada di heroku
- Otak saya ada di github''')
    bot.send_message(message.chat.id, 
    f'''
Credits API
- zenzapi.xyz
- hadi-api.herokuapp.com
- instagram47.p.rapidapi.com''')

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
        i = len(api_key) - 1
        while True:
            bot.send_chat_action(message.chat.id, "upload_video")
            link = f"https://zenzapi.xyz/downloader/musically?url={message.text}&apikey={api_key[i]}"
            dataTiktok = getData(link)
            if dataTiktok['status'] == False:
                i -= 1
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



@bot.message_handler(regexp='https://www.instagram.com/') # IG konten/REELS/TV
def downloadvidinstagram(message):
 # scrape konten
    konten = Post(message.text)
    konten.scrape()
    if konten.to_dict()['is_video']: # jika konten adalah video
        bot.send_chat_action(message.chat.id, "upload_video")
        konten.download(f"{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}.mp4")
        bot.send_video(message.chat.id, open(f"{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}.mp4", "rb"))
        log(message, f"IG VIDEO{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}")
    else:  # jika konten adalah image
        bot.send_chat_action(message.chat.id, "upload_photo")
        konten.download(f"{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}.jpg")
        bot.send_video(message.chat.id, open(f"{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}.mp4", "rb"))
        log(message, f"IG IMAGE{konten.to_dict()['username']}_{konten.to_dict()['shortcode']}")



# key rapid api https://rapidapi.com/Prasadbro/api/instagram47/                                                             """
api2 = ["c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c", "f355e8c71bmsh2f12c8e8772a755p1aba64jsn14d36932fc37"]


# FULL STORY downloader
@bot.message_handler(commands=['igs'])
def downloadStoriesIG(message):
     # cari id dari username
        try:   # eror username
            key = 0
            while True: # ambil api key yang masih berlaku
                try:
                    url = "https://instagram47.p.rapidapi.com/get_user_id"
                    querystring = {"username":message.text.split(' ')[1]}
                    headers = {
                        'x-rapidapi-host': "instagram47.p.rapidapi.com",
                        'x-rapidapi-key': api2[key]}
                    response = requests.request("GET", url, headers=headers, params=querystring)
                    dataID = json.loads(response.text)
                    
                    if dataID['status'] == "Success":
                        ID = dataID["user_id"]
                        break
                except:
                    key += 1
                    continue


            try: # dapatkan stories
                url = "https://instagram-stories1.p.rapidapi.com/v1/get_stories"
                querystring = {"userid":ID}
                headers = {
                    'x-rapidapi-host': "instagram-stories1.p.rapidapi.com",
                    'x-rapidapi-key': api2[key] }
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = json.loads(response.text)
    

                if data['status'] == 'Fail': # kirim pesan untuk setiap warning
                    bot.send_message(message.chat.id, data['Warning'])
                elif data['totalStories'] == 0: # kirim pesan jika storiesnya nol
                    bot.send_message(message.chat.id, "user tidak memiliki stories!")

                else:  
                # unduh story
                    data = data['downloadLinks']
                    for i in range(0, int(len(data))): # unduh setiap stories
                        if data[i]["media_type"] == 2: # stories video
                            bot.send_chat_action(message.chat.id, "upload_video")
                            namaFile = f"{message.text[5:]}_{i}.mp4"
                            snap = data[i]["url"]
                            unduhVideo(snap, namaFile)
                            bot.send_video(message.chat.id, open(namaFile, 'rb'))

                        elif data[i]["media_type"] == 1: # stories image
                            bot.send_chat_action(message.chat.id, "upload_photo")
                            namaFile = f"{message.text[5:]}_{i}.jpg"
                            snap = data[i]["url"]
                            unduhVideo(snap, namaFile)
                            bot.send_photo(message.chat.id, open(namaFile, 'rb'))
                            

                    bot.send_message(message.chat.id, f"total {len(data)} stories")
                    log(message, f"IG STORY {key} {message.text[5:]}")
            except: # kirim pesan jika terdapat error
                bot.send_message(message.chat.id, "tidak dapat mengunduh story :(")    
                bot.send_message(message.chat.id, "jika masalah masih berlanjut, hubungi developer yaa")   


        except: # eror username
            bot.send_message(message.chat.id, dataID['Warning'])    


"""                                             JOOX                                                            """
callbackJoox = []
@bot.message_handler(commands=['joox'])
def downloadjoox(message):
# ambil api key yang tidak kadaluarsa 

    try:
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(f"https://zenzapi.xyz/downloader/joox?query={message.text[6:]}&apikey={api_key[i]}")
            dataJoox = url.json()

            if dataJoox['status'] == False:
                i += 1
            elif dataJoox['status'] == "OK":
                break
      
        page = dataJoox['result']['mp3Link']
        laguJoox = dataJoox['result']['lagu']

        unduhMusik(page, f"{laguJoox}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{laguJoox}.mp3", 'rb'))
        log(message, f"JOOX {i} {laguJoox}")
        # buat tombol untuk mendapatkan lirik lagunya
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh musik {message.text.split(' ')[1:]} :(")
      
"""
                                   YOUTUBE MUSIK DOWNLOADER                         
"""
@bot.message_handler(regexp='youtu')
def downloadMusikYoutube(message):
    try:
        i = 0
        while True:
            print(i)
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(f"https://zenzapi.xyz/downloader/ytmp3?url={message.text}&index=2&apikey={api_key[i]}")
            data = url.json()

            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break     

        page = data['result']['url']
        title = data['result']['title'] 

        unduhMusik(page, f"{title}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{title}.mp3", 'rb'))
        log(message, f"YOUTUBE {i} {title}")
    except:
        bot.send_message(message.chat.id, f"tidak dapat mengunduh musik :(")

"""                                 SOUND CLOUND DOWNLOADER                                                                             """
@bot.message_handler(regexp='https://soundcloud.com/')
def downloadjoox(message):
    try:
    # ambil api key yang tidak kadaluarsa 
        i = 0
        while True:
            bot.send_chat_action(message.chat.id, "upload_audio")
            url = requests.get(f"https://zenzapi.xyz/downloader/soundcloud?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()

            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break
        
            # doenload musik    
        page = data['result']['url']
        title = data['result']['title']

        unduhMusik(page, f"{title}.mp3")
        bot.send_chat_action(message.chat.id, "upload_audio")
        bot.send_audio(message.chat.id, open(f"{title}.mp3", 'rb'))
        log(message, f"SOUNDCLOUD {i} {title}")
    except:
         bot.send_message(message.chat.id, f"tidak dapat mengunduh musik :(")


"""                                TWITTER DOWNLOADER                                    """
# VIDEO POST, REELS and TV downloader
@bot.message_handler(regexp='https://twitter.com')
def downloadvidtiktok(message):
    try :
        bot.send_chat_action(message.chat.id, "upload_video")
    # ambil apikey satu persatu 
        i = 0
        while True:
            url = requests.get(f"https://zenzapi.xyz/downloader/twitter?url={message.text.split('?')[0]}&apikey={api_key[i]}")
            data = url.json()
            if data['status'] == False:
                i += 1
            elif data['status'] == "OK":
                break

        video = data['result']['HD']        
        
        unduhVideo(video, f"{message.from_user.first_name}_twitter.mp4")
        bot.send_video(message.chat.id, open(f"{message.from_user.first_name}_twitter.mp4", 'rb'))
        log(message, f"TWITTER {i} ")
    except:
         bot.send_message(message.chat.id, f"tidak dapat mengunduh video :(")

bot.send_message(1214473324, "bot starting!")
print("bot running...!!!")
bot.polling()   

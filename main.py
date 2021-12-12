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

#PERINTAH /MENU =


@bot.message_handler(commands=['menu'])
def menu(message):
    nama = message.from_user.first_name
    bot.send_message(message.chat.id, f'''🤖 Hai {nama} 
🔰/menu        > Perintah yg dapat dilakukan Bot
📨/saran text > mengirimkan pesan kepada developer

1️⃣ ARTIFICIAL INTELIGENCE 🧠
-🗣 Bot dilengkapi dengan auto respon berbahasa inggris

2️⃣ ISLAMIC ✨
/sholat nama kota > Menampilkan jadwal sholat sesuai dengan kota yang diinput
/hadist > Menampilkan 7000+ Hadist dari kitab Bukhari secara random

3️⃣ MEDIA 📺
/cov19 > Melihat update kasus covid🦠 INDONESIA
/cuaca nama kota > Melihat Perkiraan Cuaca Terkini
/news > Update Headline News media Indonesia

4️⃣ MEDSOS 📱
/igVid > Unduh video IG
/tiktokVid > Unduh video TikTok tanpa watermark 
/twitterVid > Unduh Video Twitter

5️⃣ EDUCATION 🏫
/wiki text  > pencarian dengan wikipedia
/tulis text > bot tulis

 O T H E R
/jokes     > Jokes random
/crdGuitar nama lagu > Kunci gitar 

⚠️ WEEBS AREA
/sceanime day > Jadwal rilis anime berdasarkan hari dalam bahasa inggris
Kritik dan Saran ; /masukan
''')
    idP = message.chat.id
    log(message, f"/MENU id : {idP}")

                 #Allail       #Adek       #kakSela    #Fenny
listIdPengguna = [1214473324, 1228610226, 1228610226, 1359785100]
listMenu = ['/','/test','/menu','/addFitur', '/tulis', '/sholat', '/hadist', '/cuaca', '/news', '/igvid', 'https://www.instagram.com/p','/wiki','https://www.instagram.com/tv','https://vt.tiktok.com/', '/tiktokVid', '/sceanime','/jokes', '/crdGuitar'] 
                
           


def kirimPesan(idPengguna):
    out = "DEEKKK, KALAU MAU DOWNLOAD VIDEO IG\nGAUSAH CLICK LAGI MENUNYA YAW\nSEKARANG UDAH BISA LANGSUNG PASTE LINKNYA DI CHAT\n'seperti yang anda inginkan\n\n\n #FROM DEVELOPER'"
    bot.send_message(idPengguna, out)
    print('pesan berhasil terkirim')
#kirimPesan(1228610226)
#START


@bot.message_handler(commands=['start'])
def send_welcome(message):
    nama = message.from_user.first_name
    out = f"Halo {nama} \nLihat apa yang bisa saya lakukan 'click = /menu' "
    markup = types.ReplyKeyboardMarkup()
    item = types.KeyboardButton('/menu')
    markup.row(item)
    idP = message.chat.id
    namaLast = message.from_user.last_name
    bot.send_message(message.chat.id, out, reply_markup=markup)
    bot.send_message(-515995341, f"{nama} {namaLast} : {idP} ")
    #log(message, f"/start id : {idP}")
 
@bot.message_handler(commands=['balasPesan'])
def kirimPesan(message):
  masukan = message.text
  split   = masukan.split(' ')
  idP     = split[1]
  pesan   = split[2:]
  string = ' '.join([str(item) for item in pesan])
  out = f'{string}\n From Developer '
  try:
    bot.send_message(idP, out)
    bot.send_message(1214473324, 'Berhasil Terkirim!')
  except:
    bot.send_message(1214473324, 'Gagal Terkirim!')
idPengguna= [13144391126, ]
@bot.message_handler(commands=['broadCast'])
def kirimPesan(message):
  masukan = message.text
  split   = masukan.split(' ')
  pesan   = split[1:]
  string = ' '.join([str(item) for item in pesan])

  for i in idPengguna:
    bot.send_message(i, string)
   
@bot.message_handler(commands=['saran']) 
def send_pesan(message):
    Pesan = message.text
    split = Pesan.split(' ')
    string = ' '.join([str(item) for item in split[1:]])
    nama = message.from_user.first_name
    bot.send_message(message.chat.id, 'Pesan berhasil disampaikan ke admin') 
    
    idP = message.chat.id
    namaLast = message.from_user.last_name
    out = f"{nama} {namaLast} {idP}\n {string} "
    bot.send_message(1214473324,out)

@bot.message_handler(commands=['masukan'])
def helpp(message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        'Message Developer 🧑🏻‍💻', url='https://telegram.me/Qadrillah')
    markup.row(item)
    bot.send_message(
        message.chat.id, 'Click tombol dibawah ini ya..', reply_markup=markup)
    log(message, "masukan")
    

#RIWAYAT PENGGUNA
def log(message, perintah):
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
    log_bot = open('log_bot.txt', 'a')
    text = f"{tanggal} > {waktu} > {nama} {nama_akhir} < {perintah} "
    log_bot.write(f"{text}\n")
    log_bot.close()
    bot.send_message(-524462976, text)
    print(text)


#                                                                   1️⃣ ISLAMIC ✨

# sumber API : https://aladhan.com/prayer-times-api#GetTimingsByCity
@bot.message_handler(commands=['sholat'])
def send_welcome(message):
    try:
        masukan = message.text
        lis = "%20".join(masukan.split(' '))
        kota = lis[8:]
        pesan = kota.lower()

        url = urlopen(
            f"http://api.aladhan.com/v1/timingsByCity?city={pesan}&country=indonesia&method=8")
        dokumen = url.read().decode("utf-8")
        data = json.loads(dokumen)

        letakData = data['data']  # DATA SHOLAT
        result = letakData['timings']
        out = f"""Jadwal Sholat 🕌
🌑 Imsyak  {result['Imsak']}
🌗 Shubuh  {result['Fajr']}
🌗 Terbit     {result['Sunrise']}
🌞 Dzuhur   {result['Dhuhr']}
🌓 Ashar     {result['Asr']}
🌓 Maghrib {result['Maghrib']}
🌚 Isya        {result['Isha']}
            """
        log(message, f"Jadwal Sholat {pesan}")
        bot.send_message(message.chat.id, out)
    except:
        bot.send_message(message.chat.id, "Kota tidak ditemukan 😭")


@bot.message_handler(commands=['hadist'])
def hadits(message):

    x = random.randint(1, 7008)
    url = urlopen(
        f"http://api.carihadis.com/?kitab=Shahih_Bukhari&id={x}")
    dokumen = url.read().decode("utf-8")
    data = json.loads(dokumen)

    no = data['data']['1']['id']
    nass = data['data']['1']['nass']
    terjemahan = data['data']['1']['terjemah']
    out = f"No Hadist {no}\n{nass}\n{terjemahan}"
    bot.send_message(message.chat.id, out)
    log(message, f"hadist")


#                                       MEDIA

#PERINTAH MELHAT PRAKIRAAN CUACA
@bot.message_handler(commands=['cuaca'])
def send_welcome(message):
    #buka link data
    try:
        masukan = message.text
        pesan = "%20".join(masukan.split(" "))
        cari = pesan[9:]

        url = urlopen(
            f"http://api.openweathermap.org/data/2.5/weather?q={cari}&appid=11a5ba73255cfa55831c342c4a9cceee"
        )
        #baca dokumen
        dokumen = url.read().decode("utf-8")
        data = json.loads(dokumen)

        #akses data yg ingin di scrapp
        #akses data cuaca
        suhu = round(int(data['main']['temp']) - 273.15, 2)
        cuaca = data['weather'][0]['main']
        kelembaban = data['main']['humidity']

        #CETAK OUTPUT
        output = f"{data['name']}\n  Weather: {cuaca}\n  Temperature: {suhu}C\n  Humidity: {kelembaban}"
        bot.send_message(message.chat.id, output)
        log(message, f"Prakiraan Cuaca {cari}")
    except:
        out = "Kota Tidak Ditemukan\n(Bisa jadi kesalahan dalam penulisan nama kota)🤔"
        bot.send_message(message.chat.id, out)
    del(pesan)


@bot.message_handler(commands=['cov19'])
def jadwalRilis(message):
    url = urlopen(
        f"https://covid19.mathdro.id/api/countries/ID"
    )
       #baca dokumen
    dokumen = url.read().decode("utf-8")
    data = json.loads(dokumen)
    positif = int(data['confirmed']['value'])
    sembuh = data['recovered']['value']
    meninggal = data['deaths']['value']
    update = data['lastUpdate']
    time = update[:16]
    out = "Kasus Covid-19 🇲🇨\n\nPositif         : {:,}\nSembuh      : {:,}\nMeninggoi  : {:,}\n\nUpdate pada {}\nJangan lupa pakai masker😷".format(
        positif, sembuh, meninggal, time)
    log(message, "COVID19")
    bot.send_message(message.chat.id, out)


#                                                    M E D S O S
#INSTAGRAMM
@bot.message_handler(commands=['igVid','tiktokVid', 'twitterVid'])
def downloadig(message):
    bot.send_message(message.chat.id, "Paste aja linknya di chat...")
    
def kirim(namaFile, tujuan):
  while True:
    try:
      out = open(namaFile, 'rb')
      x = bot.send_video(tujuan, out)
      out.close()
      
      if x is not EOFError:
        break
    except:
      continue

@bot.message_handler(regexp='https://www.instagram.com/')
def downloadig(message):
        bot.send_chat_action(message.chat.id, "upload_video")
        masukan = message.text
        idP = message.chat.id
        list = masukan.split('/')
        link = list[4]
#Sumber API : https://rapidapi.com/Prasadbro/api/instagram47/
    # OPEN API
        url = "https://instagram47.p.rapidapi.com/post_details"
        querystring = {"shortcode": link}
        bot.send_message(message.chat.id, "Sabarr Boss...")
        headers = {
    'x-rapidapi-host': "instagram47.p.rapidapi.com",
    'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c"
    }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)
        url_video = data['body']['video_url']

        req = requests.get(url_video)
        #nama File
        nama = message.from_user.first_name
        video = data['body']['owner']['username']
        namaFile = f"{nama}_{video}.mp4"
        with open(namaFile, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                f.write(chunk)
            f.close()
        kirim(namaFile, message.chat.id)
        log(message, f"igVID {namaFile}")

        

@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):
        bot.send_chat_action(message.chat.id, "upload_video")
        url = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url=[{message.text}]&key=godownloader.com")
        data = url.json()
        video = data['video_no_watermark'] 
        musik = data['music_url']  
        sumber = data['aweme_id']
    # kirim video
        namaFile = f"{message.from_user.first_name}_{sumber}.mp4"
        namaFileMusik = f"{data['music_author']}.mp3"
        urllib.request.urlretrieve(video, namaFile)
        kirim(namaFile, message.chat.id)
     # tampilkan button untuk mendownload musik
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton(
        'Download Musik 🎶', callback_data='download musik tiktok')
        markup.row(item)
        bot.send_message(message.chat.id,"click tombol dibawah untuk mendownload musik", reply_markup=markup)
    # kirim musik ketika diclick tombol
        @bot.callback_query_handler(func=lambda call: True)
        def callbacks(call):
            bot.send_chat_action(message.chat.id, "upload_audio")
            if call.data == "download musik tiktok":
                urllib.request.urlretrieve(musik, namaFileMusik)
                out = open(namaFileMusik, 'rb')
                bot.send_audio(message.chat.id, out)
                out.close()
        log(message, f"TikTok Vid {namaFile}")
        
# TWITTER
@bot.message_handler(regexp='https://twitter.com/')
def downloadvidtiktok(message):    

    url = requests.get(f"https://dhn-api.herokuapp.com/downloader/twitter/tweet?url={message.text.replace(message.text[len(message.text)-2:], '19')}")
    data = url.json()
    video = data['result']['media_resources']['video_mp4_640x']

    namaFile = f"{message.from_user.first_name}_{data['result']['id']}.mp4"
    urllib.request.urlretrieve(video, namaFile)
        
    kirim(namaFile, message.chat.id)
    log(message, f"Twitter Vid {namaFile}")
        
#PERINTAH BERITA HEADLINE MEDIA INDONESIA
@bot.message_handler(commands=['news'])
def send_welcome(message):
    log(message, "NEWS")

    url = urlopen(
        f"https://newsapi.org/v2/top-headlines?country=id&apiKey=25e3668d7f764829857939ab1fd55c37"
    )
    #baca dokumen
    dokumen = url.read().decode("utf-8")
    data = json.loads(dokumen)

    result = data['articles']
    kya = []
    for i in result:
        kya.append(i)

    list = []
    for i in range(len(kya)):
       berita = data['articles'][i]['title']
       link = data['articles'][i]['url']
     #
       x = f"{berita} {link}\n"
       list.append(x)
    tamp = random.randint(0, len(kya))
    out = list[tamp-1]
    bot.send_message(message.chat.id, out)
    del(list)
    del(kya)


#                                                           ANIME

@bot.message_handler(commands=['sceanime'])
def jadwalRilis(message):
    try:

        pesan = message.text
        perintah = pesan.split(" ")
        masukan = perintah[1]

        url = f"https://jikan1.p.rapidapi.com/schedule/{masukan}"

        headers = {
            'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c",
            'x-rapidapi-host': "jikan1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(response.text)

        anime = data[masukan]
        log(message, f"Jadwal anime rilis {masukan}")

        list = []
        angka = 0
        for i in anime:
            angka += 1
            tulisan = (f"""{angka}. {i['title']}
    Episode :  {i['episodes']}
    Score   :  {i['score']}""")
            list.append(tulisan)

        out = ""
        for a in list:
            out += a + '\n'
        bot.send_message(message.chat.id, out)

    except:
        bot.send_message(message.chat.id, "Anime Tydack ditemukan 🤦🏻 ")


        #                                                                   E D U C A T I O N
#WIKI
@bot.message_handler(commands=['wiki'])
def jokes(message):
    try:
        inputtan = message.text
        list = "%20".join(inputtan.split(' '))
        masukan = list[8:]
        print(masukan)
        url = urlopen(
            f"https://hadi-api.herokuapp.com/api/wiki?query={masukan}")
        dokumen = url.read().decode("utf-8")
        data = json.loads(dokumen)

        link = data['result']
        bot.send_message(message.chat.id, str(link))
        log(message, f'wikiped {masukan}')
    except:
        bot.send_message(message.chat.id, f"'{inputtan[6:]}' tidak ditemukan di wikipedia 🤦🏻")

        
 # BOT TULIS
@bot.message_handler(commands=['tulis'])
def tulis1(message):
    try:
        masukan = message.text
        bot.send_message(message.chat.id, "Sabar wahai orang malass...")
        link = masukan[7:]
        url = f"https://hadi-api.herokuapp.com/api/nulis?teks={link}"
        
        nama = message.from_user.first_name
        namaFile = f'{nama}.jpg'
        img_data = requests.get(url).content
        with open(f'{namaFile}', 'wb') as handler:
            handler.write(img_data)
            handler.close()
        time.sleep(2)
        out = open(namaFile, 'rb')
        bot.send_photo(message.chat.id, out)
        out.close()
        log(message, f"Bot tulis 1")
        os.remove(namaFile)
    except:
        bot.send_message(message.chat.id, "tidak dapat menulis 🤦🏻 ")
        os.remove(namaFile)


        
#                                                                                  O  T  H  E  R

#jokes
@bot.message_handler(commands=['jokes'])
def jokes(message):
    try:
        url = urlopen(f"https://hadi-api.herokuapp.com/api/darkjokes")
        dokumen = url.read().decode("utf-8")
        data = json.loads(dokumen)
        link = data['result']

        nama = message.from_user.first_name
        namaFile = f'{nama}jokes.jpg'
        img_data = requests.get(link).content
        with open(f'{namaFile}', 'wb') as handler:
            handler.write(img_data)
            handler.close()

        time.sleep(0.5)
        out = open(namaFile, 'rb')
        bot.send_photo(message.chat.id, out)
        out.close()
        log(message, f"Jokes")
        os.remove(namaFile)
    except:
        bot.send_message(message.chat.id, "tidak dapat menampilkan jokes 🤦🏻 ")
        os.remove(namaFile)
        
# KUNCI GITAAAAAR
@bot.message_handler(commands=['crdGuitar'])
def chordGuitar(message):
    try:
        inputtan = message.text
        list   = "%20".join(inputtan.split(' '))
        masukan = list[13:]

        url = urlopen(
            f"https://hadi-api.herokuapp.com/api/chord?q={masukan}")
        dokumen = url.read().decode("utf-8")
        data = json.loads(dokumen)
        link = data['result']
        bot.send_message(message.chat.id, str(link))
        log(message, f"Chord {masukan}")
    except:
        bot.send_message(message.chat.id, "tidak dapat menemukan chord gitar 🤦🏻") 

@bot.message_handler(commands=['test'])
def chordGuitar(message):

    url = urlopen(
      "https://sinta.ristekbrin.go.id/authors/detail?id=6022530&view=overview"
    )
    # Ambil/baca dokumen
    dokumen = url.read().decode("utf-8")
    # Buka HTML
    soup = BeautifulSoup(dokumen, "html.parser")
    #temukan data 
    finddata = soup.body.find_all('div', class_="uk-width-1-6 stat-num-pub")

    data = []
    for i in finddata:
      x = i.string
      data.append(x)

    document = data[5]
    citations = data[6]

    rata2Citation = round(int(document)/int(citations),2)

    out = f"Documents: {document}\nCitations: {citations}\nRata-rata Citation: {rata2Citation}"
    bot.send_message(message.chat.id, str(out))

















#                                                           BOT A I

alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'i', 'o', 'p', 'a',
            's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

for i in alphabet:  # API LINK : https://rapidapi.com/farish978/api/ai-chatbot/pricing
    @bot.message_handler(regexp=i)
    def autoRespon(message):
        masukan = message.text
        nama = message.from_user.first_name
        log(message, f'AI-{masukan}')
        if masukan not in listMenu:
            aibot(masukan, nama, message)


def aibot(pesan, name, tujuan):
    try:
        url = "https://ai-chatbot.p.rapidapi.com/chat/free"

        querystring = {"message": pesan, "uid": name}

        headers = {
            'x-rapidapi-key': "c8144b94aamsh08b5fb4cfc6382dp18a232jsn078223838e9c",
            'x-rapidapi-host': "ai-chatbot.p.rapidapi.com"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        
        data = json.loads(response.text)
        out = data['chatbot']['response']
        bot.send_message(tujuan, out)
    except:
        bot.send_message(tujuan, "Sorry, I can't read emoticons 😕")

print("Bot Running...")
bot.polling()

# import os
from bitbot import Robot

bb = Robot()


def listen():
    print("Listening")
    bb.add_emo('Blink')
    bb.audio_open("resources/ding2.wav")
    input("Key to Continue")
    print("During")
    bb.add_emo('During')
    bb.audio_open("resources/ding3.wav")
    bb.add_emo('Smile')


url1 = "https://r5---sn-5np5po4v-c33lk.googlevideo.com/videoplayback?signature=BC61702CB9D4404E6F5046BFBEAB41962993B23A.1701E98764FFE4C4922A3ED9D1B18A4E718E12F3&source=youtube&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&expire=1501089187&mime=video%2Fmp4&ip=171.101.53.191&id=o-AA73OiHudbcMPyWe8-QdGEMYThU-RQ7GBbs56oXmtAqQ&ratebypass=yes&requiressl=yes&mn=sn-5np5po4v-c33lk&mm=31&mt=1501067464&initcwndbps=2266250&ipbits=0&key=yt6&lmt=1497294238992749&dur=4786.956&pl=24&itag=22&mv=m&ms=au&ei=Q3l4WZeMGoLbogPrnKigBg"

url2 = "https://r3---sn-5np5po4v-c33ly.googlevideo.com/videoplayback?ipbits=0&expire=1501089512&mime=video%2Fmp4&itag=18&ratebypass=yes&pl=24&clen=42653730&gir=yes&source=youtube&lmt=1500979284684760&id=o-ACUfOb93Y-YHE3u3oRm-RacPRSQadKAAKdp-9PH-Q36s&ms=au&mt=1501067799&initcwndbps=2315000&mv=m&signature=3228C115466296DD547884F9BCD67CEC41EC8EC2.BBC052721AFBAF583AC443CA1B6BDA664EB8908E&key=yt6&ip=171.101.53.191&mm=31&mn=sn-5np5po4v-c33ly&ei=iHp4WdiiI4LSoAP4ko2QCg&dur=705.654&sparams=clen%2Cdur%2Cei%2Cgcr%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&gcr=th&requiressl=yes"


def youtube():
    print("Youtube")
    bb.speak("ฉันเปิด Youtube แล้ว อยากให้ค้นหาว่าอะไรหรอ")
    input()
    listen()
    bb.add_emo('Loading')
    bb.speak('ฉันขอเวลาไปหา วีดีโอ ให้คุณสักพักนะ อย่าพึ่งไปไหนหละ เดี๋ยวฉันมา')

    k = input(">> video")
    bb.add_emo('During')
    bb.speak('โอเค ฉันเจอวิดีโอของคุณแล้ว')
    if k == 'a':
        bb.hdmi_open(url1, sound=True)
    elif k == 's':
        bb.hdmi_open(url2, sound=True)


def playvideo(num):
    print('resources/videos/A-{}.mp4'.format(num))
    bb.speak("กำลังเปิดวีดีโอที่{0}".format(num))
    input()
    bb.hdmi_open('resources/videos/A-{}.mp4'.format(num), sound=True)


def makefood():
    print("make food")
    bb.speak("ฉันจะสอนคุณทำอาหารเอง")
    bb.hdmi_open('resources/videos/motion_01.mp4')


def makepaper():
    print("make paper")
    bb.speak("ฉันจะสอนคุณพับกระดาษ")
    bb.hdmi_open('resources/videos/motion_02.mp4')


def makedraw():
    print("make draw")
    bb.speak("ฉันจะสอนคุณวาดรูปช้าง")
    bb.hdmi_open('resources/videos/motion_03.mp4')


def main():
    print("Welcome")
    while True:
        key = input(">>>")
        if key == 'l':
            listen()
        elif key == 'y':
            youtube()
        elif key == 'q':
            bb.speak("ฉันฟังไม่เข้าใจ กรุณาพูดใหม่อีกครั้ง")
        elif key == 'c':
            bb.hdmi_close()
        elif key == '1':
            playvideo(int(key))
        elif key == '2':
            playvideo(int(key))
        elif key == '3':
            playvideo(int(key))
        elif key == '4':
            playvideo(int(key))
        elif key == '5':
            playvideo(int(key))
        elif key == '6':
            playvideo(int(key))
        elif key == '7':
            playvideo(int(key))
        elif key == '8':
            playvideo(int(key))
        elif key == '9':
            playvideo(int(key))
        elif key == 'n':
            makefood()
        elif key == 'm':
            makepaper()
        elif key == ',':
            makedraw()
        elif key == 'w':
            txt = input("text >> ")
            bb.speak(txt)


if __name__ == '__main__':
    main()
# from pytube import YouTube
# import os
# from subprocess import PIPE, Popen
# from bitbot import Robot
# # import json
# from utils import Chatty


# def _create_task(cmd):
#     return Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, preexec_fn=os.setsid)


# def speak(text, wait=False, process=False):
#     print("Speak:", text)
#     cmd = ['google_speech', '-l', 'th', text]
#     cmd += ['--sox-effects']
#     if process:
#         cmd += ['pitch', '50']
#         cmd += ['stretch', '2.5', '133.33']
#         cmd += ['lin', '0.2', '0.4']
#         cmd += ['overdrive', '25', '25']
#         cmd += ['echo', '0.4', '0.8', '15', '0.8']
#         cmd += ['synth', 'sine', 'fmod', '30']
#     if process:
#         cmd += ['speed', '3']
#     else:
#         cmd += ['speed', '1.3']
#     speaker = _create_task(cmd=cmd)
#     if wait:
#         speaker.wait()


# text = "สวัสดีครับ"

# chat = Chatty()
# while True:
#     txt = input("<<< ")
#     speak(chat.message(txt))
# print(BB.chatty.message(text))


# import requests

# Make it a bit prettier..
# print("-" * 30)
# print("This will show the Most Popular Videos on YouTube")
# print("-" * 30)

# # Get the feed
# r = requests.get(
#     "http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2.1&alt=jsonc")
# # Convert it to a Python dictionary
# # data = json.loads(r.text)
# # print(data)
# Loop through the result.
# for item in data['data']['items']:

#     print("Video Title: %s" % (item['title']))
#     print("Video Category: %s" % (item['category']))
#     print("Video ID: %s" % (item['id']))
#     print("Video Rating: %f" % (item['rating']))
#     print("Embed URL: %s" % (item['player']['default']))

# import time


# If you don't specify credentials when constructing the client, the
# client library will look for credentials in the environment.


# Make an authenticated API request

# import speech_recognition as sr

# # obtain path to "english.wav" in the same folder as this script
# from os import path
# AUDIO_FILE = "audio.wav"

# # use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

# # recognize speech using Google Cloud Speech
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"Amatar Robotics-8ca65f285ed6.json"

# try:
#     print("Google Cloud Speech thinks you said: " + r.recognize_google_cloud(audio,
#                                                                              credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print(
#         "Could not request results from Google Cloud Speech service; {0}".format(e))
# BB = Robot()
# res = BB.know.wk_search("ภาษาไพทอน")
# BB.speak(res, wait=True)

# yt_list = BB.sight.yt_search("เพลงโดราเอม่อน")
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

# with ydl:
#     result = ydl.extract_info(
#         'http://www.youtube.com' + yt_list[0],
#         download=False  # We just want to extract the info
#     )


# video_url = result.keys()
# print(video_url)

# print(result['url'])
#
# link = "https://www.youtube.com/watch?v=IOYyCHGWJq4"

# print(yt_list)
# url = BB.sight.yt_genstream(yt_list[0])
# # print(url)
# print("OKKKK")
# BB.hdmi_open(url, sound=True)
# time.sleep(10)
# time.sleep(5)
# import requests
# from bs4 import BeautifulSoup

# query = "เพลงสากลใหม่ๆ"
# url = "https://www.youtube.com/results?search_query=" + query

# # print('yxu' in url)
# res = requests.get(url)
# soup = BeautifulSoup(res.content, "html.parser")
# print("OKKKKKKK\n")
# print([vid['href'] for vid in soup.findAll(
#     attrs={'class': 'yt-uix-tile-link'}) if 'list' not in vid['href']])
# for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
#     if 'list' not in vid['href']:
#         print(vid['title'], 'https://www.youtube.com' + vid['href'])

# print(soup)

# BB.loadYoutube(link)
# print("OK")
# time.sleep(5)
# cmd = ['youtube-dl', '-g', link]
# print("Downloading")
# yt = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
#           close_fds=True, preexec_fn=os.setsid).communicate()[0]
#
# url = yt.decode("utf-8").split('\n')[0]
# print(url)
#
# print("Playing")
# cmd = ['omxplayer', '--display', '0', '-o', 'local', url]
# os.system("omxplayer --display 0 -o local \"{0}\"".format(url))
# Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
#      close_fds=True, preexec_fn=os.setsid)
# prin(res)
# print("HI")
# time.sleep(5)

# yt = YouTube("https://www.youtube.com/watch?v=IOg45dmtqPc")

# print(yt.get_videos())
# print(yt.)
# print(yt.filename)
# print(yt.filter('mp4'))
# video = yt.get('mp4', '360p')
# video.download("")
# print(BB.info.age)
# print(BB.info.name)
# print(BB.info.birthday)


# def main():
#     BB.speak("ว่าไงจ๊ะ", wait=False)
#     recog = BB.listen()

# BB.detector_start(["resources/BitBot.pmdl"],[main],[0.5])


# detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
# print("Listening")
# detector.start(detected_callback=callbacks)
# detector.terminate()
# print(".mp3"in"source.mp3")
# cmd = ['google_speech', '-l', 'th',  "สวัสดีทุกๆท่าน", '-e', 'pitch', '100']

# a = subprocess.Popen(cmd)#, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, preexec_fn=os.setsid)

# # os.system("google_speech -l th \'สวัสดีทุกๆคน\' -e pitch 350")
# bitbot.speak("น้อบรับคำสั่ง เจ้าคะ", True)
# bitbot.speak("สวัสดีทุกท่าน", wait=True)
# # time.sleep(0.1)
# bitbot.speak("ฉันก็ไม่รู้เหมือนกัน", True)
# # time.sleep(0.1)
# bitbot.speak("ว่ายังไงรึ", True)
# # time.sleep(0.1)
# bitbot.speak("ไม่บอกหรอก", True)
# time.sleep(0.1)

# emotions = {
#     "Smile" : ['emotions/bit_bot_emotion_1.mp4', 1.85],
#     "Line" : ['emotions/bit_bot_emotion_2.mp4', 3.1],
#     "Angry" : ['emotions/bit_bot_emotion_3.mp4', 4.2]
# }


# BB.add_emo(emotions['Line'])
# BB.add_emo(emotions['Angry'])
# BB.add_emo(emotions['Smile'])
# BB.add_emo(emotions['Angry'])

# while True:
#     print("Hi")
#     time.sleep(1)
# print(emo_queue)
# print(emo_queue.get())
# print(emo_queue)
# # for i in range(5):
# while True:
#     emo, value = random.choice(list(emotions.items()))
#     print(emo)
#     bitbot.dsi_open(value[0])
#     time.sleep(value[1])

# bitbot.dsi_open('emotions/bit_bot_emotion_1.mp4')
# time.sleep(1.85)
# bitbot.dsi_open('emotions/bit_bot_emotion_2.mp4')
# time.sleep(3.1)
# # bitbot.dsi_open('emotions/bit_bot_emotion_1.mp4')
# # time.sleep(1.85)
# bitbot.dsi_open('emotions/bit_bot_emotion_3.mp4')
# time.sleep(4.2)
# print(i)
# print("play \""+"เล่นวีดีโอ ที่ 7.mp3\"")
# bitbot.audio_open("ding.wav", wait=True)
# for i in range(5):
#     bitbot.audio_open("ding2.wav", wait=True)

# print("Hello World {}".format("3"))
# os.system("sox /input/file.mp3 -e mu-law -r 16k /output/file.wav remix 1,2"]
# sox resources/sounds/gtts/สวัสดีทุกท่าน.mp3 resources/sounds/gtts/file.wav


# def voicetick():
#     print("Hello World!")

# def voicetick2():
#     print("Hello World2!")

# model = ["resources/hotwords/BitBot.pmdl", "resources/hotwords/snowboy.umdl"]
# sensitive = [0.5, 0.7]
# callback = [voicetick, voicetick2]

# bitbot = Robot()
# # bitbot.detector_start(model, callback, sensitive)
# print(bitbot.detector_wav("resources/snowboy.wav", model[0]))
# print(bitbot.detector_wav("resources/snowboy.wav", model[1]))

# # for i in range(10):
# #     print("In loop")
# #     time.sleep(1)
# # print("After loop")
# # bitbot.detector_stop()

# # for i in range(10):
# #     print("In loop2")
# #     time.sleep(1)
# # print("After loop2")

# # bitbot.recv("127.0.0.1",5000,hello)

# from pytube import YouTube
<<<<<<< HEAD
from bitbot import Robot
import time

BB = Robot()
yt_list = BB.sight.yt_search("เพลงโดราเอม่อน")
=======
# from bitbot import Robot
# import json


text = "สวัสดีเพื่อนๆของฉันเฟสบุ๊คด้วย"


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
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
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
<<<<<<< HEAD
#link = "https://www.youtube.com/watch?v=IOYyCHGWJq4"

# print(yt_list)
url = BB.sight.yt_genstream(yt_list[0])
# # print(url)
# print("OKKKK")
BB.hdmi_open(url, sound=True)
time.sleep(10)
=======
# link = "https://www.youtube.com/watch?v=IOYyCHGWJq4"

# print(yt_list)
# url = BB.sight.yt_genstream(yt_list[0])
# # print(url)
# print("OKKKK")
# BB.hdmi_open(url, sound=True)
# time.sleep(10)
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
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
<<<<<<< HEAD
#cmd = ['youtube-dl', '-g', link]
=======
# cmd = ['youtube-dl', '-g', link]
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
# print("Downloading")
# yt = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE,
#           close_fds=True, preexec_fn=os.setsid).communicate()[0]
#
<<<<<<< HEAD
#url = yt.decode("utf-8").split('\n')[0]
# print(url)
#
# print("Playing")
#cmd = ['omxplayer', '--display', '0', '-o', 'local', url]
##os.system("omxplayer --display 0 -o local \"{0}\"".format(url))
=======
# url = yt.decode("utf-8").split('\n')[0]
# print(url)
#
# print("Playing")
# cmd = ['omxplayer', '--display', '0', '-o', 'local', url]
# os.system("omxplayer --display 0 -o local \"{0}\"".format(url))
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
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

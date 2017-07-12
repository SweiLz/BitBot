<<<<<<< HEAD
from bitbot import Robot
import threading
import queue
import time
# # import random

BB = Robot()


# print(BB.info.version)
# print(".".join(str(int(x)+1) if i==2 else x for i,x in enumerate(BB.info.version)))
=======
# from bitbot import Robot
# import threading
import queue
# import time
# # # import random

# BB = Robot()

 
from datetime import datetime

q = queue.Queue()
q.put('A')
q.put('B')
q.put('C')
q.put('E')

print(q.get())
while not q.empty():
    q.get()
# q.Clear()
print(q.empty())


# print(BB.info.version)
>>>>>>> 9179167fe60e9673ae374777c967f06910af27f9
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

<<<<<<< HEAD
emotions = {
    "Smile" : ['emotions/bit_bot_emotion_1.mp4', 1.85],
    "Line" : ['emotions/bit_bot_emotion_2.mp4', 3.1],
    "Angry" : ['emotions/bit_bot_emotion_3.mp4', 4.2]
}


BB.add_emo(emotions['Line'])
BB.add_emo(emotions['Angry'])
BB.add_emo(emotions['Smile'])
BB.add_emo(emotions['Angry'])

while True:
    print("Hi")
    time.sleep(1)
=======
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
>>>>>>> 9179167fe60e9673ae374777c967f06910af27f9
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
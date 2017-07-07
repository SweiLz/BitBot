from bitbot import Robot
import time
import random

BB = Robot()

def main():
    BB.speak("ว่าไงจ๊ะ", wait=False)
    recog = BB.listen()
   
BB.detector_start(["resources/BitBot.pmdl"],[main],[0.5])






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

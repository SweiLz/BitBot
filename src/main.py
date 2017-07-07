# !/usr/bin/python
import snowboydecoder
import bitbot_ai
from bitbot import Robot
import random
models = ["resources/BitBot.pmdl"]

BB = Robot()

ans_list = ["น้อมรับคำสั่ง", "ว่ายังไงจ๊ะ", "มาแล้วจ้า", "มีอะไรให้รับใช้", "ขอโทษจ้าฉันมาแล้ว", "มาแล้ว มาแล้ว", "มีอะไรขอให้บอก", "เรียกฉันหรอ"]

def bitbot():
    detector.terminate()
    print("Conversation Started")
    BB.dsi_open('emotions/bit_bot_emotion_3.mp4', loop=True)
    BB.speak(random.choice(ans_list), wait=True)
    BB.speak("ฉันให้คุณถามได้ 5 คำถามเท่านั้นแล้วฉันจะไป", wait=True)
    for i in range(5):
        bitbot_ai.main()
        BB.speak("ถามไปแล้ว {0} เหลืออีก {1}".format(i+1,5-i), wait=True)
    BB.speak("หมดแล้ว ไปแล้วนะ บ้ายบาย มีอะไรก็เรียกใหม่นะ", wait=True)
    print("Conversation Stop")
    print("Listening")
    global detector
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
    BB.dsi_open('emotions/bit_bot_emotion_1.mp4', loop=True)
    detector.start(callbacks)


callbacks = [bitbot]


BB.dsi_open('emotions/bit_bot_emotion_1.mp4', loop=True)
detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
print("Listening")
detector.start(detected_callback=callbacks)
# detector.terminate()

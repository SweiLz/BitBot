# !/usr/bin/python
import snowboydecoder
import bitbot_ai
from bitbot import Robot
models = ["resources/BitBot.pmdl"]

BB = Robot()


def bitbot():
    detector.terminate()
    print("Conversation Started")
    BB.audio_open('ding.wav', wait=True)
    bitbot_ai.main()
    print("Conversation Stop")
    print("Listening")
    global detector
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
    detector.start(callbacks)


callbacks = [bitbot]


detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
print("Listening")
detector.start(detected_callback=callbacks)
# detector.terminate()

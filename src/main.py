# !/usr/bin/python

import bitbot_ai
from bitbot_ai import bb
import snowboydecoder
<<<<<<< HEAD
import speech_recognition as sr
=======

models = ["resources/hotwords/BitBot.pmdl"]
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7


def bitbot():

    detector.terminate()
    bitbot_ai.run_session()
    with sr.Microphone() as source:
        bb.r.adjust_for_ambient_noise(source)
    print("=== Listening Bitbot ===")
    global detector
<<<<<<< HEAD
    detector = snowboydecoder.HotwordDetector(["resources/hotwords/BitBot.pmdl"], sensitivity=0.55)
=======
<<<<<<< HEAD
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
=======
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55 )
>>>>>>> d83b7bea8293017303c68b0b1a5962aee738da0f
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
    detector.start(callbacks)


callbacks = [bitbot]

<<<<<<< HEAD
with sr.Microphone() as source:
    bb.r.adjust_for_ambient_noise(source)
detector = snowboydecoder.HotwordDetector(["resources/hotwords/BitBot.pmdl"], sensitivity=0.55)
=======
detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
print("=== Listening Bitbot ===")
detector.start(callbacks)

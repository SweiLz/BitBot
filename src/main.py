# !/usr/bin/python
import random
from subprocess import PIPE, Popen
import os
import bitbot_ai
import snowboydecoder

models = ["resources/hotwords/BitBot.pmdl"]


def bitbot():
    detector.terminate()
    bitbot_ai.run_session(True)
    print("=== Listening Bitbot ===")
    global detector
<<<<<<< HEAD
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
=======
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55 )
>>>>>>> d83b7bea8293017303c68b0b1a5962aee738da0f
    detector.start(callbacks)


callbacks = [bitbot]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
print("=== Listening Bitbot ===")
detector.start(detected_callback=callbacks)

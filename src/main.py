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
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
    detector.start(callbacks)


callbacks = [bitbot]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.55)
print("=== Listening Bitbot ===")
detector.start(detected_callback=callbacks)

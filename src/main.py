# !/usr/bin/python

import bitbot_ai
from bitbot_ai import bb
import snowboydecoder
import speech_recognition as sr


def bitbot():

    detector.terminate()
    bitbot_ai.run_session()
    with sr.Microphone() as source:
        bb.r.adjust_for_ambient_noise(source)
    print("=== Listening Bitbot ===")
    global detector
    detector = snowboydecoder.HotwordDetector(
        ["resources/hotwords/BitBot_o.pmdl"], sensitivity=0.40)
    detector.start(callbacks)


callbacks = [bitbot]

with sr.Microphone() as source:
    bb.r.adjust_for_ambient_noise(source)
detector = snowboydecoder.HotwordDetector(
    ["resources/hotwords/BitBot_o.pmdl"], sensitivity=0.40)
print("=== Listening Bitbot ===")
detector.start(callbacks)

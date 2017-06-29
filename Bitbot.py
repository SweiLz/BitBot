# !/usr/bin/python
import snowboydecoder

models = ["resources/BitBot.pmdl"]
callbacks = [bitbot]

def bitbot():
    detector.terminate()
    print("Conversation Started")
    snowboydecoder.bot_speak("None", "resources/ding.wav")
    snowboydecoder.main()
    print("Conversation Stop")
    print("Listening")
    global detector
    detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
    detector.start(callbacks)




detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
print("Listening")
detector.start(detected_callback=callbacks)
# detector.terminate()

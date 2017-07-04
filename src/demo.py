import snowboydecoder

model = ["resources/hotwords/BitBot.pmdl"] 

# capture SIGINT signal, e.g., Ctrl+C
# signal.signal(signal.SIGINT, signal_handler)
def speak():
    global detector
    detector.terminate()
    print("Hello")
    snowboydecoder.play_audio_file()
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    detector.start(detected_callback=callback)

print('Listening... Press Ctrl+C to exit')
callback = [speak]

# main loop
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
detector.start(detected_callback=callback)
print("Terminate")
detector.terminate()

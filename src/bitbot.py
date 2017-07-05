import threading
import time
import wave

import pyaudio
from gtts import gTTS
import pyglet
import snowboydecoder


# from omxplayer import OMXPlayer

class Robot:
    def __init__(self):
        print("New Robot")
        self.emotion_thread = threading.Thread()
        print("++++++++++++++++++++++++++++++++++++")

    def _play_audio(self, fname="resources/sounds/ding.wav"):
        # audio = pyaudio.PyAudio()
        pass
        # ding_wav = wave.open(fname, 'rb')
        # ding_data = ding_wav.readframes(ding_wav.getnframes())
        # stream_out = audio.open(
        #     format=audio.get_format_from_width(ding_wav.getsampwidth()),
        #     channels=ding_wav.getnchannels(),
        #     rate=ding_wav.getframerate(), input=False, output=True)
        # stream_out.start_stream()
        # stream_out.write(ding_data)
        # time.sleep(0.2)
        # stream_out.stop_stream()
        # stream_out.close()
        # audio.terminate()
    
    def _emotion(self, fname):
        pass
        # print(fname)
        # media = self.vlc.media_new_path("resources/emotions/"+fname+".mp4")
        # if self.player.is_playing:
        #     self.player.stop()
        # self.player.set_media(media)
        # self.player.play()
        # while self.player.get_state() != vlc.State.Ended:
        #     pass
        # self.player.stop()

    def emotion(self, fname, wait=False):
        if self.emotion_thread.is_alive():
            if wait:
                self.emotion_thread.join()
            else:
                self.emotion_thread.join(0)
        self.emotion_thread = threading.Thread(target=self._emotion, args=(fname,))
        self.emotion_thread.start()

    
    def speak(self, text):
        print("Speak:", text)
        tts = gTTS(text=text, lang="th", slow=False)
        path = "resources/sounds/gtts/"+text+".mp3"
        tts.save(path)
        music = pyglet.media.load(path)
        music.play()
        # pyglet.app.run()
        # self._play_audio(path)
        # self._play_audio()

    def _hdmi(self, fname):
        print("Play video "+fname+" at HDMI")
    
    def _dsi(self, fname):
        print("Play video "+fname+" at DSI")

    

    def start_detect(self, callback=[]):
        print("Start detect")
        # self.detector_thread = threading.Thread(target=self.detector.start, args=(callback,lambda: False,0.03))
        self.detector = snowboydecoder.HotwordDetector(["resources/hotword_models/BitBot.pmdl"], sensitivity=0.5)
        self.detector.start(detected_callback=callback)
        # self.detector.start()


    def checkHotword(self, fwave, fmodel="resources/hotword_models/BitBot.pmdl"):
        f = wave.open(fwave)
        # assert f.getnchannels() == 1,"Error: supports 1 channel only"
        # assert f.getframerate() == 16000, "Error: supports 16K rate only"
        # assert f.getsampwidth() == 2, "Error: supports 16bit per sample"
        data = f.readframes(f.getnframes())
        f.close()
        detection = snowboydecoder.HotwordDetector(fmodel, sensitivity=0.5)
        return detection.detector.RunDetection(data) 

    # def play_wav(self, fname, wait=True):

    #     def play():
    #         audio = pyaudio.PyAudio()
    #         fwav = wave.open(fname, 'rb')
    #         fformat = audio.get_format_from_width(fwav.getsampwidth())
    #         fchannels = fwav.getnchannels()
    #         frate = fwav.getframerate()
    #         fdata = fwav.readframes(fwav.getnframes())
    #         print(fformat,fchannels,frate)
    #         stream = audio.open(format=fformat,channels=fchannels,rate=frate, input=False, output=True)
    #         stream.start_stream()
    #         stream.write(fdata)
    #         stream.stop_stream()
    #         stream.close()
    #         audio.terminate()

    #     if not wait:
    #         threading.Thread(target=play).start()
    #     else:
    #         play()

bitbot = Robot()
# bitbot.speak("resources/ding2.wav")
# print(bitbot.checkHotword("resources/t.wav"))
# print(bitbot.checkHotword("resources/t2.wav"))
# print(bitbot.checkHotword("resources/t3.wav"))

def func():
    bitbot.speak("สวัสดีครับ")
    print("ok")
    bitbot.speak("ได้ยินไหมครับ")
    print("ok2")

models = ["resources/hotwords"]
callbacks = [func]

# func()

player = pyglet.media.Player()
window = pyglet.window.Window()
source = pyglet.media.StreamingSource()
video = pyglet.media.load("resources/emotions/A-1.mp4")
player.queue(video)
# video.play()
player.play()

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

pyglet.app.run()
time.sleep(10)
# time.sleep(10)
# bitbot.start_detect()
# bitbot.stop_detect()

# bitbot.start_detect([bitbot.speak("Hello World")])
# while True:
#     print("hi")
#     time.sleep(1)

# def main():
#     bitbot = Robot()
#     for i in range(4):

#         bitbot.emotion("A-"+str(i+1))
#         time.sleep(1)
#     # bitbot.emotion("A-4")
#     # time.sleep(1)
#     # bitbot.emotion("A-3")
#     # while True:
#         # pass
#     # bitbot.speak("น้อบรับคำสั่ง")
#     # bitbot.play_wav("resources/sounds/accept.wav",False)
#     # bitbot.speak("เล่นแล้ว")
#     # time.sleep(0.25)
#     # bitbot.play_wav("resources/sounds/accept.wav",False)
#     # bitbot.speak("เล่นครั้งที่ 2") 

# if __name__ == '__main__':
#     main()

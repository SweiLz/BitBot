import threading
import time
import wave

import pyaudio
import pygame
import vlc
import snowboydecoder
# from omxplayer import OMXPlayer

class Robot:
    def __init__(self):
        print("New Robot")
        # self.screen = pygame.display.set_mode((800, 480))
        # self.vlc = vlc.Instance("--no-xlib")
        # self.player = self.vlc.media_player_new()
        # self.player.set_xwindow(pygame.display.get_wm_info()["window"])
        self.emotion_thread = threading.Thread()
        self.audio = pyaudio.PyAudio()
        # pygame.display.toggle_fullscreen()

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

    def _play_audio(self, fname):
        ding_wav = wave.open(fname, 'rb')
        ding_data = ding_wav.readframes(ding_wav.getnframes())
        # audio = pyaudio.PyAudio()
        stream_out = self.audio.open(
            format=self.audio.get_format_from_width(ding_wav.getsampwidth()),
            channels=ding_wav.getnchannels(),
            rate=ding_wav.getframerate(), input=False, output=True)
        stream_out.start_stream()
        stream_out.write(ding_data)
        time.sleep(0.2)
        stream_out.stop_stream()
        stream_out.close()
        # audio.terminate()

    def speak(self, text):
        print("Speak:", text)

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
bitbot._play_audio("resources/ding2.wav")

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

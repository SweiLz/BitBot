import glob
import os
import signal
import subprocess
import threading
import time
import wave

import pyaudio
from gtts import gTTS
from omxplayer import OMXPlayer

import snowboydecoder


class Robot:
    def __init__(self):
        print("New Robot")
        self.audio_player = None
        self.dis_layer = [1000, 1000]
        self.dis_player = [[None, None], [None, None]]
        print("++++++++++++++++++++++++++++++++++++")

    def __del__(self):
        try:
            os.system("sudo killall -s 9 omxplayer.bin")
        except Exception:
            pass

    def speak(self, text, wait=False):
        print("Speak:", text)
        path = "resources/sounds/gtts/"+text+".mp3"
        if path in glob.glob("resources/sounds/gtts/*.mp3"):
            print("ok")
            self._audio("sounds/gtts/"+text+".mp3", wait=wait)
        else:
            print("new")
            tts = gTTS(text=text, lang="th")
            tts.save(path)
            self._audio("sounds/gtts/"+text+".mp3", wait=wait)


    def _create_task(self, cmd):
        return subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, preexec_fn=os.setsid)

    def _terminate_task(self, pid):
        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except Exception:
            pass

    def _audio(self, fname, terminate=False, wait=False):
        print("Play audio " + fname)
        ENDPOINT = "resources/" + fname
        # cmd = ['omxplayer', ENDPOINT, '-o', 'local']
        cmd = ['vlc', ENDPOINT, '--play-and-exit']
        if terminate:
            self._terminate_task(self.audio_player.pid)
        self.audio_player = self._create_task(cmd)
        if wait:
            self.audio_player.wait()

    def _display(self, num, fname, sound, wait):
        ENDPOINT = "resources/" + fname
        cmd = ['omxplayer', ENDPOINT, '-b', '--layer',
               str(self.dis_layer[num]), '--display']
        cmd += ['5'] if num else ['0']
        cmd += ['-o', 'local'] if sound else ['-n', '-1']
        dis = self.dis_layer[num] % 3
        self.dis_layer[num] -= 1
        if self.dis_layer[num] < 0:
            self.dis_layer[num] = 1000
        self.dis_player[num][dis] = self._create_task(cmd)
        if self.dis_player[num][1 - dis] != None:
            threading.Timer(0.5, self._terminate_task, args=(
                self.dis_player[num][1 - dis].pid,)).start()
        if wait:
            self.dis_player[num][dis].wait()

    def hdmi(self, fname, sound=False, wait=False):
        print("Play video " + fname + " at HDMI")
        self._display(1, fname, sound, wait)

    def dsi(self, fname, sound=False, wait=False):
        print("Play video " + fname + " at DSI")
        self._display(0, fname, sound, wait)

    def start_detect(self, callback=[]):
        print("Start detect")
        # self.detector_thread = threading.Thread(target=self.detector.start, args=(callback,lambda: False,0.03))
        self.detector = snowboydecoder.HotwordDetector(
            ["resources/hotword_models/BitBot.pmdl"], sensitivity=0.5)
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


bitbot = Robot()
# bitbot._audio("sounds/piano.wav")
bitbot.speak("สวัสดีทุกท่าน", wait=True)
# time.sleep(5)

# for i in range(3):
#     # print("END1")
#     # bitbot._audio("ding.wav",wait=True)
#     # print("END2")
#     # bitbot._dsi("pirate.mp4")
#     # bitbot._hdmi("pirate.mp4")
#     # time.sleep(2)
#     # bitbot._dsi("emotions/A-1.mp4")
#     # time.sleep(1)
#     # bitbot._audio("ding.wav")
#     # bitbot._dsi("emotions/A-1.mp4", sound=True)
#     bitbot._hdmi("emotions/A-3.mp4", wait=True)
#     # time.sleep(2)
#     bitbot._hdmi("emotions/A-2.mp4")
#     time.sleep(1)


# print(bitbot.checkHotword("resources/t.wav"))
# print(bitbot.checkHotword("resources/t2.wav"))
# print(bitbot.checkHotword("resources/t3.wav"))
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

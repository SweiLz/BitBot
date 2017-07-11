import os
import signal
import threading
import time
import queue
# import wave
from subprocess import PIPE, Popen

import speech_recognition as sr
from utils import Personar


# import snowboydecoder
############################### Snowboy Detector ######################
# def _detector(self, models_list, callback_list, sensitive_list):
#     self.detector[0] = snowboydecoder.HotwordDetector(models_list, sensitivity=sensitive_list)
#     self.detector[0].start(detected_callback=callback_list)

# def detector_start(self, models, callbacks, sensitives):
#     print("Start hotword detection")
#     self.detector[1] = threading.Thread(target=self._detector, args=(models, callbacks, sensitives,))
#     self.detector[1].start()

# def detector_stop(self):
#     print("Stop hotword detection")
#     self.detector[0].terminate()
#     self.detector[1].join(0)

# def detector_wav(self, fwave, fmodel):
#     f = wave.open(fwave)
#     # assert f.getnchannels() == 1,"Error: supports 1 channel only"
#     # assert f.getframerate() == 16000, "Error: supports 16K rate only"
#     # assert f.getsampwidth() == 2, "Error: supports 16bit per sample"
#     data = f.readframes(f.getnframes())
#     f.close()
#     return snowboydecoder.HotwordDetector(fmodel).detector.RunDetection(data)
############################### Snowboy Detector ######################
emotions = {
    "Smile": ['emotions/bit_bot_emotion_1.mp4', 1.85],
    "Line": ['emotions/bit_bot_emotion_2.mp4', 3.1],
    "Angry": ['emotions/bit_bot_emotion_3.mp4', 4.2]
}


class Robot:
    def __init__(self):
        print("++++++++++++++++++++++++++++++++++++")
        print("Bitbot, Hello World!")
        print("++++++++++++++++++++++++++++++++++++")
        self.speaker = None
        self.audio_player = None
        self.dis_layer = [1000, 1000]
        self.dis_player = [[None, None], [None, None]]
        # self.detector = [None, None]
        self.info = Personar()
        self.emo_queue = queue.Queue()
        self.emo_flag = True
        threading.Thread(target=self.play_emotions).start()

    def __del__(self):
        try:
            # pass
            os.system("killall -s 9 omxplayer.bin")
        except Exception:
            pass
        print("++++++++++++++++++++++++++++++++++++")
    
    def _close(self):
        try:
             os.system("killall -s 9 omxplayer.bin")
        except Exception:
            pass

    def _create_task(self, cmd):
        return Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, preexec_fn=os.setsid)

    def _terminate_task(self, pid):
        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except Exception:
            pass

    def _audio(self, fname, terminate=False, wait=False):
        ENDPOINT = "resources/" + fname
        cmd = ['omxplayer', ENDPOINT, '-o', 'local']
        if terminate:
            self._terminate_task(self.audio_player.pid)
        self.audio_player = self._create_task(cmd=cmd)
        if wait:
            self.audio_player.wait()

    def audio_open(self, fname, terminate=False, wait=False):
        print("Play audio " + fname)
        self._audio(fname, terminate=terminate, wait=wait)

    def audio_close(self):
        print("Close audio")
        self._terminate_task(self.audio_player.pid)

    def _display(self, num, fname, sound=False, wait=False, loop=False):
        ENDPOINT = "resources/" + fname
        cmd = ['omxplayer', ENDPOINT, '-b', '--no-osd', '--layer',
               str(self.dis_layer[num]), '--display']
        cmd += ['5'] if num else ['0']
        cmd += ['-o', 'local'] if sound else ['-n', '-1']
        if loop:
            cmd += ['--loop']
        if num == 0:
            cmd += ['--win', "\"0 0 799 479\""]
        dis = self.dis_layer[num] % 2
        self.dis_layer[num] -= 1
        if self.dis_layer[num] < 1:
            self.dis_layer[num] = 1000
        self.dis_player[num][dis] = self._create_task(cmd=cmd)
        if self.dis_player[num][1 - dis] != None:
            threading.Timer(0.7, self._terminate_task, args=(
                self.dis_player[num][1 - dis].pid,)).start()
        if wait:
            self.dis_player[num][dis].wait()

    def hdmi_open(self, fname, sound=False, wait=False, loop=False):
        print("Play video " + fname + " at HDMI")
        self._display(1, fname, sound, wait, loop)

    def hdmi_close(self):
        print("Close HDMI")
        if self.dis_player[1][1] != None:
            self._terminate_task(self.dis_player[1][1].pid)
        self._terminate_task(self.dis_player[1][0].pid)

    def dsi_open(self, fname, sound=False, wait=False, loop=False):
        print("Play video " + fname + " at DSI")
        self._display(0, fname, sound, wait, loop)

    def dsi_close(self):
        print("Close DSI")
        if self.dis_player[0][1] != None:
            self._terminate_task(self.dis_player[0][1].pid)
        self._terminate_task(self.dis_player[0][0].pid)

    def speak(self, text, wait=False, process=False):
        print("Speak:", text)
        cmd = ['google_speech', '-l', 'th', text]
        cmd += ['--sox-effects']
        if process:
            cmd += ['pitch', '50']
            cmd += ['stretch', '2.5', '133.33']
            cmd += ['lin', '0.2', '0.4']
            cmd += ['overdrive', '25', '25']
            cmd += ['echo', '0.4', '0.8', '15', '0.8']
            cmd += ['synth', 'sine', 'fmod', '30']
        cmd += ['speed', '1.3']
        self.speaker = self._create_task(cmd=cmd)
        if wait:
            self.speaker.wait()

    def listen(self, timeout=6, lang="th-TH"):
        print("=== Listening ===")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 1500
            audio = r.listen(source, phrase_time_limit=timeout)
        try:
            recog = r.recognize_google(audio, language=lang)
            print("User:", recog)
            return recog
        except sr.UnknownValueError:
            print("--- No Sound ---")
            return 0
        except sr.RequestError:
            print("--- No Service ---")
            return 0

    def add_emo(self, emo, num=1):
        print("### Add Emotions: "+str(num))
        for i in range(num):
            self.emo_queue.put(emo)

    def play_emotions(self):
        while True:
            if self.emo_queue.empty():
                if self.emo_flag:
                    self.dsi_open("emotions/bit_bot_emotion_1.mp4", loop=True)
                    self.emo_flag = False
            else:
                self.emo_flag = True
                p = self.emo_queue.get()
                self.dsi_open(p[0])
                time.sleep(p[1])

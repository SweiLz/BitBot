import os
import queue
import signal
import threading
import time
from subprocess import PIPE, Popen

import speech_recognition as sr

from utils import Personar, Sight


emotions = {
    "Sad": ['emotions/bitbot_sad.m4v', 2.13],
    "Swift": ['emotions/bitbot_swift.m4v', 10.67],
    "Blink": ['emotions/bitbot_blink.m4v', 4.13],
    "Sleepy": ['emotions/bitbot_sleepy.m4v', 4.53],
    "Smile": ['emotions/bitbot_smile.m4v', 2.43],
    "Notification": ['emotions/bitbot_nontification.m4v', 11.03],
    "Bomb": ['emotions/bitbot_bomb.mp4', 5.11],
    "Loading": ['emotions/bitbot_downloading.m4v', 2.23],
    "During": ['emotions/bitbot_during_clip.m4v', 3.73]
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
        self.info = Personar()
        self.sight = Sight()
        self.emo_queue = queue.Queue()
        self.emo_flag = True
        threading.Thread(target=self.play_emotions).start()

    def __del__(self):
        try:
            os.system("killall -s 9 python3 omxplayer.bin")
        except Exception as e:
            print("ERROR => {0} <=".format(e))
        print("++++++++++++++++++++++++++++++++++++")

    def _close(self):
        try:
            os.system("killall -s 9 python3 omxplayer.bin")
        except Exception as e:
            print("ERROR => {0} <=".format(e))

    def _create_task(self, cmd):
        return Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, preexec_fn=os.setsid)

    def _terminate_task(self, pid):
        try:
            os.killpg(os.getpgid(pid), signal.SIGTERM)
        except Exception as e:
            print("ERROR => {0} <=".format(e))

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
        cmd = ['omxplayer', fname, '-b', '--no-osd', '--layer',
               str(self.dis_layer[num]), '--display']
        cmd += ['5', '--orientation', '180'] if num else ['0']
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
        print("Play video at HDMI")
        self._display(1, fname, sound, wait, loop)

    def hdmi_close(self):
        print("Close HDMI")
        if self.dis_player[1][1] != None:
            self._terminate_task(self.dis_player[1][1].pid)
        self._terminate_task(self.dis_player[1][0].pid)

    def dsi_open(self, fname, sound=False, wait=False, loop=False):
         #print("Play video " + fname + " at DSI")
        fname = "resources/" + fname
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
        if process:
            cmd += ['speed', '3']
        else:
            cmd += ['speed', '1.3']
        self.speaker = self._create_task(cmd=cmd)
        if wait:
            self.speaker.wait()

    def listen(self,  lang="th-TH"):
        print("=== Listening Recognition ===")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            '''
            energy_threshold range is 0-4000  , silent room are 0-00 , louder room are 3000-4000
            high value = less sensitive 
            '''
            # r.energy_threshold = 0
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = True
            # r.pause_threshold = 1
            ''' timeout is the maximum number of seconds that this will wait for
            # a phrase to start before giving up
            # The phrase_time_limit parameter is the maximum number of seconds
            # that this will allow a phrase to continue before stopping'''
            audio = r.listen(source, phrase_time_limit=5)
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

    def clear_emo(self):
        print("### Clear Emotions ###")
        while not self.emo_queue.empty():
            self.emo_queue.get()

    def add_emo(self, emo, num=1):
        print("### Add Emotions ###")
        for i in range(num):
            self.emo_queue.put(emotions[emo])

    def play_emotions(self):
        while True:
            if self.emo_queue.empty():
                if self.emo_flag:
                    p = emotions['Smile']
                    print("### Play Emotion {0} ###".format(p[0]))
                    self.dsi_open(p[0], loop=True)
                    self.emo_flag = False
            else:
                self.emo_flag = True
                p = self.emo_queue.get()
                print("### Play Emotion {0} ###".format(p[0]))
                self.dsi_open(p[0])
                time.sleep(p[1] - 0.2)

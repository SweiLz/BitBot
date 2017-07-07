import os
import signal
import threading
import time
import wave
from subprocess import PIPE, Popen

import snowboydecoder


class Robot:
    def __init__(self):
        print("++++++++++++++++++++++++++++++++++++")
        print("Bitbot, Hello World!")
        print("++++++++++++++++++++++++++++++++++++")
        self.speaker = None
        self.audio_player = None
        self.dis_layer = [1000, 1000]
        self.dis_player = [[None, None], [None, None]]
        self.detector = [None, None]

    def __del__(self):
        try:
            # pass
            os.system("killall -s 9 omxplayer.bin > /dev/null 2>&1")
        except Exception:
            pass
        print("++++++++++++++++++++++++++++++++++++")

    def _create_task(self, cmd):
        return Popen(cmd, stdout=PIPE, stderr=PIPE, close_fds=True, preexec_fn=os.setsid)

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

    def _display(self, num, fname, sound=False, wait=False):
        ENDPOINT = "resources/" + fname
        cmd = ['omxplayer', ENDPOINT, '-b', '--layer',
               str(self.dis_layer[num]), '--display']
        cmd += ['5'] if num else ['0']
        cmd += ['-o', 'local'] if sound else ['-n', '-1']
        dis = self.dis_layer[num] % 2
        self.dis_layer[num] -= 1
        if self.dis_layer[num] < 0:
            self.dis_layer[num] = 1000
        self.dis_player[num][dis] = self._create_task(cmd=cmd)
        if self.dis_player[num][1 - dis] != None:
            threading.Timer(0.5, self._terminate_task, args=(self.dis_player[num][1 - dis].pid,)).start()
        if wait:
            self.dis_player[num][dis].wait()
    
    def hdmi_open(self, fname, sound=False, wait=False):
        print("Play video " + fname + " at HDMI")
        self._display(1, fname, sound, wait)

    def hdmi_close(self):
        print("Close HDMI")
        if self.dis_player[1][1] != None:
            self._terminate_task(self.dis_player[1][1].pid)
        self._terminate_task(self.dis_player[1][0].pid)

    def dsi_open(self, fname, sound=False, wait=False):
        print("Play video " + fname + " at DSI")
        self._display(0, fname, sound, wait)

    def dsi_close(self):
        print("Close DSI")
        if self.dis_player[0][1] != None:
            self._terminate_task(self.dis_player[0][1].pid)
        self._terminate_task(self.dis_player[0][0].pid)

    def speak(self, text, wait=False):
        print("Speak:", text)
        cmd = ['google_speech', '-l', 'th', text]
        cmd += ['--sox-effects']
        cmd += ['pitch', '350']
        cmd += ['stretch', '2', '133.33']
        cmd += ['lin', '0.2', '0.4']
        cmd += ['overdrive', '25', '25']
        cmd += ['echo', '0.4', '0.8', '15', '0.8']
        cmd += ['synth', 'sine', 'fmod', '30']
        cmd += ['speed', '3']
        self.speaker = self._create_task(cmd=cmd)
        if wait:
            self.speaker.wait()

    def _detector(self, models_list, callback_list, sensitive_list):
        self.detector[0] = snowboydecoder.HotwordDetector(models_list, sensitivity=sensitive_list)
        self.detector[0].start(detected_callback=callback_list)

    def detector_start(self, models, callbacks, sensitives):
        print("Start hotword detection")
        self.detector[1] = threading.Thread(target=self._detector, args=(models, callbacks, sensitives,))
        self.detector[1].start()

    def detector_stop(self):
        print("Stop hotword detection")
        self.detector[0].terminate()
        self.detector[1].join(0)

    def detector_wav(self, fwave, fmodel):
        f = wave.open(fwave)
        # assert f.getnchannels() == 1,"Error: supports 1 channel only"
        # assert f.getframerate() == 16000, "Error: supports 16K rate only"
        # assert f.getsampwidth() == 2, "Error: supports 16bit per sample"
        data = f.readframes(f.getnframes())
        f.close()
        return snowboydecoder.HotwordDetector(fmodel).detector.RunDetection(data)



# def voicetick():
#     print("Hello World!")

# def voicetick2():
#     print("Hello World2!")

# model = ["resources/hotwords/BitBot.pmdl", "resources/hotwords/snowboy.umdl"]
# sensitive = [0.5, 0.7]
# callback = [voicetick, voicetick2]

# bitbot = Robot()
# # bitbot.detector_start(model, callback, sensitive)
# print(bitbot.detector_wav("resources/snowboy.wav", model[0]))
# print(bitbot.detector_wav("resources/snowboy.wav", model[1]))

# # for i in range(10):
# #     print("In loop")
# #     time.sleep(1)
# # print("After loop")
# # bitbot.detector_stop()

# # for i in range(10):
# #     print("In loop2")
# #     time.sleep(1)
# # print("After loop2")

# # bitbot.recv("127.0.0.1",5000,hello)

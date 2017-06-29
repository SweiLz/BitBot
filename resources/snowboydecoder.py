#!/usr/bin/env python

import collections
import pyaudio
import snowboydetect
import time
import wave
import os
import logging

'''                   sc.py                   '''
import serial
from scipy.interpolate import interp1d
import json
import speech_recognition as sr 
from gtts import gTTS
from googletrans import Translator
import numpy as np
import apiai
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse
import math
import pygame



pygame.mixer.init()
port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)
rift_state = False
CLIENT_ACCESS_TOKEN = '29234bbc7c0c4467ab38edd3ebb6c4f3'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
translator = Translator(service_urls=['translate.google.co.th',
                                      'translate.google.com',])
r = sr.Recognizer()
r.energy_threshold = 1500
# r.dynamic_energy_threshold = True
r.pause_threshold = 0.5
def bot_speak(text, filename = 'temp.mp3',wait = True):
    if filename == 'temp.mp3' :
        print(text)
        tts = gTTS(text=text, lang='th', slow=False)
        tts.save('temp.mp3')


    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()  
    while pygame.mixer.music.get_busy() == True and wait == True:
        pass
    print('[]')
    # pygame.mixer.quit()

def speech_input() :

    with sr.Microphone() as source:
        # r.record(source, duration = 5, offset = None)
        audio = r.listen(source,phrase_time_limit= 6)
        print('**')

    try:
        text_th = r.recognize_google(audio,language = "th-TH")
        text_eng = translator.translate(text_th,dest='en').text
        print(text_th,text_eng)
        return text_th,text_eng
    except sr.UnknownValueError:
        print("I don't understand")
        return 0,0
    except sr.RequestError as e:
        print("Not in service ")
        return 0,0

def kinematic(pitch,roll,H,mode = 'K') :

    if mode == 'K' :
        pitch = np.deg2rad(pitch)
        roll = np.deg2rad(roll)
        Tan_roll = np.tan(roll)
        Tan_pitch = np.tan(pitch)
        l = 80
        L = 138
        A = 50

        R_c = l*Tan_roll + H
        R_a = (L*Tan_pitch + 2*H - l*Tan_roll)/2
        R_b = 3*H - R_a - R_c

    elif mode == 'R' :
        R_a = pitch
        R_b = roll
        R_c = H
    R = [R_a,R_b,R_c]
    if R_a < 0 or R_b < 0 or R_c < 0: 
        R_a += abs(min(R))
        R_b += abs(min(R))
        R_c += abs(min(R))
        print('\n !!  Range error ::> mapping ... \n')   
    if R_a > 50 : R_a = 50
    if R_b > 50 : R_b = 50
    if R_c > 50 : R_c = 50
    R = [R_a,R_b,R_c]

    m01 = interp1d([0,50],[255,0])
    R_a = int(m01(R_a))
    R_b = int(m01(R_b))
    R_c = int(m01(R_c))
    print(R_a,R_b,R_c)
    port.write([64,R_a,35,R_b,36,R_c])

def apiai_do(request,text) :
    global rift_state
    request.query = text
    action = 'None'

    response = json.loads(request.getresponse().read().decode('utf8'))
    try :
        action = response['result']['action']
        print('Action is {}'.format(action))
        if action == 'input.unknown' :
            return 0
    except :
        print("apiai action fail.")
    try :
        print(response['result']['fulfillment']['speech'])
        bot_speak(response['result']['fulfillment']['speech'],wait=False)
    except :
        print("apiai speech fail.")

    if action == 'sound-motion' :
        dreg1 = []
        direction = 'None'
        dreg1 = response['result']['parameters']['dreg1']
        direction = response['result']['parameters']['Direction']
        print(response['result']['parameters'])
        if len(dreg1) == 2 :R = kinematic(dreg1[0],dreg1[1],25)
        elif len(dreg1) == 1 : R = kinematic(dreg1[0],0,25)
        elif direction == 'สมดุล' : R = kinematic(25,25,25,'R')
        elif direction == 'ขึ้น' : R = kinematic(50,50,50,'R')    
        elif direction == 'ลง' : R = kinematic(0,0,0,'R')    
        elif direction == 'ขวา' : R = kinematic(-20,0,25) 
        elif direction == 'ซ้าย' : R = kinematic(20,0,25)
    if action == 'rift-motion' :
        state = False
        state = response['result']['parameters']['Enable-Disable']
        print(state)
        if state == 'เปิด' : rift_state = True
        elif state == 'ยกเลิก' : rift_state = False
    if action == 'play-game' :
        if response['result']['parameters']['Game'] == '21-Game' :
            play = True 
            base = [1,5,9,13,17,21]
            while play == True :
                main()
    if action == '21' :
        
        return ['result']['parameters']['Number']
    if action == 'I-first' :
        return True
    if action == 'You-first' :
        return False
        
def main():
    while True:
        request = ai.text_request()
        # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    
        # bot_speak('เฮ้ย')
        t_th,t_eng= speech_input()
        if t_th != 0 and t_eng != 0 : 
            return apiai_do(request,t_eng)
        else : return 0
    
def print_volume_handler(unused_addr, args, v1,v2,v3):
    m = interp1d([0,1],[0,50])
    v1 = int(m(v1))
    v2 = int(m(v2))
    v3 = int(m(v3))    
    kinematic(v1,v2,v3,'R')

parser = argparse.ArgumentParser()
parser.add_argument("--ip",
                    default="192.168.1.243", help="The ip to listen on")
parser.add_argument("--port",
                    type=int, default=5005, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/p", print)
dispatcher.map("/filter", print_volume_handler, "Volume")
server = osc_server.ThreadingOSCUDPServer(
    (args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
'''                   osc                   '''

logging.basicConfig()
logger = logging.getLogger("snowboy")
logger.setLevel(logging.INFO)
TOP_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCE_FILE = os.path.join(TOP_DIR, "resources/common.res")
DETECT_DING = os.path.join(TOP_DIR, "resources/ding.wav")
DETECT_DONG = os.path.join(TOP_DIR, "resources/dong.wav")


class RingBuffer(object):
    """Ring buffer to hold audio from PortAudio"""
    def __init__(self, size = 4096):
        self._buf = collections.deque(maxlen=size)

    def extend(self, data):
        """Adds data to the end of buffer"""
        self._buf.extend(data)

    def get(self):
        """Retrieves data from the beginning of buffer and clears it"""
        tmp = bytes(bytearray(self._buf))
        self._buf.clear()
        return tmp

def play_audio_file(fname=DETECT_DING):
    os.system("play "+fname)
def play_audio_file2(fname=DETECT_DING):
    """Simple callback function to play a wave file. By default it plays
    a Ding sound.

    :param str fname: wave file name
    :return: None
    """
    ding_wav = wave.open(fname, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(), input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    #time.sleep(0.2)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()


class HotwordDetector(object):
    """
    Snowboy decoder to detect whether a keyword specified by `decoder_model`
    exists in a microphone input stream.

    :param decoder_model: decoder model file path, a string or a list of strings
    :param resource: resource file path.
    :param sensitivity: decoder sensitivity, a float of a list of floats.
                              The bigger the value, the more senstive the
                              decoder. If an empty list is provided, then the
                              default sensitivity in the model will be used.
    :param audio_gain: multiply input volume by this factor.
    """
    def __init__(self, decoder_model,
                 resource=RESOURCE_FILE,
                 sensitivity=[],
                 audio_gain=1):

        def audio_callback(in_data, frame_count, time_info, status):
            self.ring_buffer.extend(in_data)
            play_data = chr(0) * len(in_data)
            return play_data, pyaudio.paContinue

        tm = type(decoder_model)
        ts = type(sensitivity)
        if tm is not list:
            decoder_model = [decoder_model]
        if ts is not list:
            sensitivity = [sensitivity]
        model_str = ",".join(decoder_model)

        self.detector = snowboydetect.SnowboyDetect(
            resource_filename=resource.encode(), model_str=model_str.encode())
        self.detector.SetAudioGain(audio_gain)
        self.num_hotwords = self.detector.NumHotwords()

        if len(decoder_model) > 1 and len(sensitivity) == 1:
            sensitivity = sensitivity*self.num_hotwords
        if len(sensitivity) != 0:
            assert self.num_hotwords == len(sensitivity), \
                "number of hotwords in decoder_model (%d) and sensitivity " \
                "(%d) does not match" % (self.num_hotwords, len(sensitivity))
        sensitivity_str = ",".join([str(t) for t in sensitivity])
        if len(sensitivity) != 0:
            self.detector.SetSensitivity(sensitivity_str.encode())

        self.ring_buffer = RingBuffer(
            self.detector.NumChannels() * self.detector.SampleRate() * 5)
        self.audio = pyaudio.PyAudio()
        self.stream_in = self.audio.open(
            input=True, output=False,
            format=self.audio.get_format_from_width(
                self.detector.BitsPerSample() / 8),
            channels=self.detector.NumChannels(),
            rate=self.detector.SampleRate(),
            frames_per_buffer=2048,
            stream_callback=audio_callback)


    def start(self, detected_callback=play_audio_file,
              interrupt_check=lambda: False,
              sleep_time=0.03):
        """
        Start the voice detector. For every `sleep_time` second it checks the
        audio buffer for triggering keywords. If detected, then call
        corresponding function in `detected_callback`, which can be a single
        function (single model) or a list of callback functions (multiple
        models). Every loop it also calls `interrupt_check` -- if it returns
        True, then breaks from the loop and return.

        :param detected_callback: a function or list of functions. The number of
                                  items must match the number of models in
                                  `decoder_model`.
        :param interrupt_check: a function that returns True if the main loop
                                needs to stop.
        :param float sleep_time: how much time in second every loop waits.
        :return: None
        """
        if interrupt_check():
            logger.debug("detect voice return")
            return

        tc = type(detected_callback)
        if tc is not list:
            detected_callback = [detected_callback]
        if len(detected_callback) == 1 and self.num_hotwords > 1:
            detected_callback *= self.num_hotwords

        assert self.num_hotwords == len(detected_callback), \
            "Error: hotwords in your models (%d) do not match the number of " \
            "callbacks (%d)" % (self.num_hotwords, len(detected_callback))

        logger.debug("detecting...")

        global rift_state
        print('rift_state = ',rift_state)
        server.timeout = 2
        while True:
            if rift_state : server.handle_request()
            
            if interrupt_check():
                logger.debug("detect voice break")
                break
            data = self.ring_buffer.get()
            if len(data) == 0:
                time.sleep(sleep_time)
                continue

            ans = self.detector.RunDetection(data)
            if ans == -1:
                logger.warning("Error initializing streams or reading audio data")
            elif ans > 0:
                message = "Keyword " + str(ans) + " detected at time: "
                message += time.strftime("%Y-%m-%d %H:%M:%S",
                                         time.localtime(time.time()))
                logger.info(message)
                callback = detected_callback[ans-1]
                if callback is not None:
                    callback()

        logger.debug("finished.")

    def terminate(self):
        """
        Terminate audio stream. Users cannot call start() again to detect.
        :return: None
        """
        self.stream_in.stop_stream()
        self.stream_in.close()
        self.audio.terminate()

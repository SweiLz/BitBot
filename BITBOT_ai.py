#from BITBOT_serial import *
from count21 import *
from gtts import gTTS
from googletrans import Translator
import subprocess
import speech_recognition as sr
import numpy as np
import argparse
import math
import pygame
import apiai
import json
from pythonosc import osc_message_builder
from pythonosc import udp_client
OSC_state = True
CLIENT_ACCESS_TOKEN = '29234bbc7c0c4467ab38edd3ebb6c4f3'
pygame.mixer.init()
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
translator = Translator(service_urls=['translate.google.co.th',
                                      'translate.google.com', ])


def bot_speak(text, filename='temp.mp3', wait=True, quit=False):
    try:
        pygame.mixer.init()
    except:
        pass

    if filename == 'temp.mp3':
        print(text)
        tts = gTTS(text=text, lang='th', slow=False)
        tts.save('temp.mp3')
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() and wait:
        pass
    print('[e]')
    if quit:
        pygame.mixer.quit()


r = sr.Recognizer()
# r.energy_threshold = 1500
r.dynamic_energy_threshold = True
# r.pause_threshold = 0.5


def speech_input():
    print('[]')
    try:
        bot_speak("None", "resources/ding2.wav")
    except:
        bot_speak("None", "ding.mp3")
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=6)
        print('**')
    try:
        text_th = r.recognize_google(audio, language="th-TH")
        text_eng = translator.translate(text_th, dest='en').text
        print(text_th, '|', text_eng)
        return text_th, text_eng

    except sr.UnknownValueError:
        print("unknown speech_input!")
        return 0, 0
    except sr.RequestError as e:
        print("Not in service ")
        return 0, 0


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.244",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5001,
                    help="The port the OSC server is listening on")
args = parser.parse_args()
client = [0]
client.append(udp_client.SimpleUDPClient(args.ip, args.port))

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.244",
                    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5002,
                    help="The port the OSC server is listening on")
args = parser.parse_args()
client.append(udp_client.SimpleUDPClient(args.ip, args.port))


def apiai_do(request, text):
    global OSC_state
    request.query = text
    action = 'None'
    response = json.loads(request.getresponse().read().decode('utf8'))
    try:
        action = response['result']['action']
        print('Action is {}'.format(action))
        print('Parameter is ...')
        print(response['result']['parameters'])
        if action == 'input.unknown':
            return 0
    except:
        print("apiai action fail.")
    try:
        print(response['result']['fulfillment']['speech'])
        bot_speak(response['result']['fulfillment']['speech'], wait=True)
    except:
        print("apiai speech fail.")
    if action == 'Video':
        display_number = response['result']['parameters']['Number']  # list
        v_action = response['result']['parameters']['Video-Command']
        if v_action == 'เล่น':
            if len(display_number) == 1:
                client[display_number[0]].send_message("/d", '../../small.mp4')
            elif len(display_number) == 2:
                client[display_number[0]].send_message("/d", '../../small.mp4')
                client[display_number[1]].send_message("/d", '../../small.mp4')
        if v_action == 'หยุดเล่น':
            if len(display_number) == 1:
                client[display_number[0]].send_message("/q", 1)
            elif len(display_number) == 2:
                client[display_number[0]].send_message("/q", 1)
                client[display_number[1]].send_message("/q", 1)

    if action == 'sound-motion':
        dreg1 = []
        direction = 'None'
        dreg1 = response['result']['parameters']['dreg1']
        direction = response['result']['parameters']['Direction']
        print(response['result']['parameters'])
        if len(dreg1) == 2:
            kinematic(dreg1[0], dreg1[1], 25)
        elif len(dreg1) == 1:
            kinematic(dreg1[0], 0, 25)
        elif direction == 'สมดุล':
            kinematic(25, 25, 25, 'R')
        elif direction == 'ขึ้น':
            kinematic(50, 50, 50, 'R')
        elif direction == 'ลง':
            kinematic(0, 0, 0, 'R')
        elif direction == 'ขวา':
            kinematic(-20, 0, 25)
        elif direction == 'ซ้าย':
            kinematic(20, 0, 25)
    if action == 'rift-motion':
        state = False
        state = response['result']['parameters']['Enable-Disable']
        print(state)
        if state == 'เปิด':
            OSC_state = True
        elif state == 'ยกเลิก':
            OSC_state = False
    if action == 'play-game':
        if response['result']['parameters']['Game'] == '21-game':
            print('เข้าสู่เกม 21')
            play = True
            counter = 0
            game = Count21()
            while play:
                x = main()
                print('x :: ', x)
                while x == 'i':
                    n = main()
                    if type(n) == list:
                        x = n

                if x == 'you':
                    counter += 1
                    bot_speak(str(counter))
                if type(x) == list:
                    cheat_ = False
                    if len(x) == 3:
                        if x[0] - counter != 1 or x[1] - x[0] != 1 or x[2] - x[1] != 1:
                            bot_speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if len(x) == 2:
                        if x[0] - counter != 1 or x[1] - x[0] != 1:
                            bot_speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if len(x) == 1:
                        if x[0] - counter != 1:
                            bot_speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if not cheat_:
                        bt = game.user(x)
                        counter = bt[-1]
                        a = ' '
                        for i in bt:
                            a += str(i) + ' '
                        bot_speak(a)
                        if 21 in x:
                            bot_speak('คุณชนะแล้ว เก่งจริงๆเลย')
                            play = False
                        elif counter == 21:
                            bot_speak('ฉันชนะแล้ว คุณอ่อนด้อย')
                            play = False

    if action == '21':
        return list(response['result']['parameters']['number'])
    if action == 'I-first':
        return 'i'
    if action == 'You-first':
        return 'you'


def main():
    # while True:
    request = ai.text_request()
    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    t_th, t_eng = speech_input()
    if t_th != 0 and t_eng != 0:
        do = apiai_do(request, t_eng)
        if do != 0:
            return do


if __name__ == '__main__':
    main()

from bitbot import Robot
import json
import speech_recognition as sr
from googletrans import Translator
from count21 import *
import apiai
CLIENT_ACCESS_TOKEN = '29234bbc7c0c4467ab38edd3ebb6c4f3'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
translator = Translator(service_urls=['translate.google.co.th',
                                      'translate.google.com', ])

r = sr.Recognizer()
r.dynamic_energy_threshold = True

bb = Robot()


def speech_input():
    print('[]')
    bb.audio_open("ding2.wav")
    text_th = bb.listen()
    bb.audio_open("ding3.wav")
    if text_th == 0:
        return 0, 0
    text_en = translator.translate(text_th, dest='en').text
    return text_th,text_en
    # with sr.Microphone() as source:
    #     audio = r.listen(source, phrase_time_limit=6)
    #     print('**')
    #     bb.audio_open("ding3.wav")
    # try:
    #     text_th = r.recognize_google(audio, language="th-TH")
    #     text_eng = translator.translate(text_th, dest='en').text
    #     print(text_th, '|', text_eng)
    #     return text_th, text_eng

    # except sr.UnknownValueError:
    #     print("unknown speech_input!")
    #     return 0, 0
    # except sr.RequestError as e:
    #     print("Not in service ")
    #     return 0, 0


def apiai_do(request, text):
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
    if action == 'ทำลายตัวเอง':
        bb.dsi_open('emotions/A-1.mp4', sound=True)
    if action == 'เล่นวิดีโอตามหมายเลข':
        num_videolist = response['result']['parameters']['Number']  # list
        v_action = response['result']['parameters']['Video-Command']
        if v_action == 'เล่น':
            print('emotions/A-{}.mp4'.format(num_videolist))
            bb.dsi_open('emotions/A-{}.mp4'.format(num_videolist), sound=True)
        if v_action == 'หยุดเล่น':
            print('หยุดเล่นวิดีโอ')
            bb.dsi_close()

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
                while x == 'ฉันเริ่มเล่นก่อน':
                    n = main()
                    if type(n) == list:
                        x = n

                if x == 'บอทเริ่มเล่นก่อน':
                    counter += 1
                    bb.speak(str(counter))
                if type(x) == list:
                    cheat_ = False
                    if len(x) == 3:
                        if x[0] - counter != 1 or x[1] - x[0] != 1 or x[2] - x[1] != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if len(x) == 2:
                        if x[0] - counter != 1 or x[1] - x[0] != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if len(x) == 1:
                        if x[0] - counter != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter))
                            cheat_ = True
                    if not cheat_:
                        bt = game.user(x)
                        counter = bt[-1]
                        a = ' '
                        for i in bt:
                            a += str(i) + ' '
                        bb.speak(a)
                        if 21 in x:
                            bb.speak('คุณชนะแล้ว เก่งจริงๆเลย')
                            play = False
                        elif counter == 21:
                            bb.speak('ฉันชนะแล้ว คุณอ่อนด้อย')
                            play = False

    if action == 'กำลังเล่นเกม21':
        return list(response['result']['parameters']['number'])
    if action in ['ฉันเริ่มเล่นก่อน', 'บอทเริ่มเล่นก่อน']:
        return action
    try:
        print(response['result']['fulfillment']['speech'])
        wait_state = False
        if action == 'play-game':
            wait_state = True
        bb.speak(response['result']['fulfillment']['speech'], wait=wait_state)
    except:
        print("apiai speech fail.")


def main():
    request = ai.text_request()
    t_th, t_eng = speech_input()
    if t_th != 0 and t_eng != 0:
        do = apiai_do(request, t_eng)
        if do != 0:
            return do


if __name__ == '__main__':
    main()

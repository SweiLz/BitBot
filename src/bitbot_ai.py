from bitbot import Robot, emotions
import json
import speech_recognition as sr
from googletrans import Translator
from count21 import *
import apiai
CLIENT_ACCESS_TOKEN = '29234bbc7c0c4467ab38edd3ebb6c4f3'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
translator = Translator(service_urls=['translate.google.co.th',
                                      'translate.google.com', ])

bb = Robot()


def speech_input():
    print('[]')
    bb.audio_open("ding2.wav")
    text_th = bb.listen()
    bb.audio_open("ding3.wav", wait=True)
    if text_th == 0:
        bb.speak("ฉันฟังไม่ค่อยออก")
        return 0, 0
    text_en = translator.translate(text_th, dest='en').text
    print("text_en :", text_en)
    return text_th, text_en


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
            bb.speak("ฉันไม่เข้าใจ")
            return 0
    except:
        bb.speak("ฉันทำไม่ได้")
        print("apiai action fail.")

    try:
        speech = response['result']['fulfillment']['speech']
        # example
        # speech = "โกรธ@ฉันโกรธคุณ"
        # speech.split('@') == ["โกรธ",ฉันโกรธคุณ"]
        splt = speech.split('/')
        print('speech : ', splt)
        bb.clear_emo()
        for order in splt:
            if order[0] == '@':
                try:
                    num = [int(i) for i in order if i.isdigit()][0]
                except:
                    num = 1
                try:
                    order = order.replace('@', '')
                    bb.add_emo(order, num)
                except:
                    pass
            elif order[0] == '!':
                order = order.replace('!', '')
                try:
                    bb.hdmi_open(order)
                except:
                    pass
            elif order[0] == '_':
                try:
                    bb.hdmi_close()
                except:
                    pass
            elif order[0] == '#':
                # do action on some speech
                if speech == '#name':
                    bb.speak("ฉันคือ" + bb.info.name + "เวอร์ชั่น" + bb.info.version)
                elif speech == '#age':
                    bb.speak("ฉันมีอายุ" + bb.info.age)
                elif speech == '#birthdate':
                    bb.speak("ฉันเกิดวันที่" + bb.info.birthday)
            else:
                bb.speak(speech, wait=True)
    except:
        print("apiai speech fail.")

    if action == 'ทำลายตัวเอง':
        bb.clear_emo()
        bb.add_emo(emotions["Bomb"])
        # bb._close()
    if action == 'สอนทำอาหาร':
        bb.hdmi_open('videos/motion_01.mp4', sound=True)
    if action == 'เล่นวิดีโอตามหมายเลข':
        num_videolist = response['result']['parameters']['Number']  # list
        v_action = response['result']['parameters']['Video-Command']
        if v_action == 'เล่น':
            print('videos/A-{}.mp4'.format(num_videolist))
            bb.hdmi_open('videos/A-{}.mp4'.format(num_videolist), sound=True)
        if v_action == 'หยุดเล่น':
            print('หยุดเล่นวิดีโอ')
            bb.hdmi_close()

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
            bb.speak("ใครจะเป็นฝ่ายเริ่มก่อนดีนะ", wait=True)
            play = True
            counter = 0
            game = Count21()
            while play:
                x = run_session()
                print('x :: ', x)
                while x == 'ฉันเริ่มเล่นก่อน':
                    n = run_session()
                    if type(n) == list:
                        x = n

                if x == 'บอทเริ่มเล่นก่อน':
                    counter += 1
                    bb.speak(str(counter), wait=True)
                if type(x) == list:
                    cheat_ = False
                    if len(x) == 3:
                        if x[0] - counter != 1 or x[1] - x[0] != 1 or x[2] - x[1] != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter), wait=True)
                            cheat_ = True
                    if len(x) == 2:
                        if x[0] - counter != 1 or x[1] - x[0] != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter), wait=True)
                            cheat_ = True
                    if len(x) == 1:
                        if x[0] - counter != 1:
                            bb.speak('ฉันลงท้ายด้วย  ' + str(counter), wait=True)
                            cheat_ = True
                    if not cheat_:
                        bt = game.user(x)
                        counter = bt[-1]
                        a = ' '
                        for i in bt:
                            a += str(i) + ' '
                        if a <= 21:
                            bb.speak(a, wait=True)
                        if 21 in x:
                            bb.speak('คุณชนะแล้ว เก่งจริงๆเลย', wait=True)
                            play = False
                        elif counter == 21:
                            bb.speak('ฉันชนะแล้ว', wait=True)
                            play = False

    if action == 'กำลังเล่นเกม21':
        return list(response['result']['parameters']['number'])
    if action in ['ฉันเริ่มเล่นก่อน', 'บอทเริ่มเล่นก่อน']:
        bb.speak(response['result']['fulfillment']['speech'], wait=True)
        return action


def run_session(flag=False):

    # BB.dsi_open('emotions/bit_bot_emotion_1.mp4', loop=True)
    if flag:
        bb.add_emo(emotions['Notification'], 3)
        bb.speak("น้อมรับคำสั่ง", wait=True)
    request = ai.text_request()
    t_th, t_eng = speech_input()
    if t_th != 0 and t_eng != 0:
        do = apiai_do(request, t_eng)
        if do != 0:
            return do


if __name__ == '__main__':
    run_session()

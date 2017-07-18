from bitbot import Robot
import json
import speech_recognition as sr
from googletrans import Translator
from count21 import *
import apiai
import random
CLIENT_ACCESS_TOKEN = '29234bbc7c0c4467ab38edd3ebb6c4f3'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
translator = Translator(service_urls=['translate.google.co.th',
                                      'translate.google.com', ])

bb = Robot()


def speech_input():
    bb.add_emo('Blink', 100)
    print('[]')
    bb.audio_open("resources/soundeffects/BB-8_what" +
                  str(random.randrange(1, 7, 1)) + ".wav", wait=True)
    text_th = bb.listen()
<<<<<<< HEAD
    if text_th == 0:
        # bb.speak("ฉันฟังไม่ค่อยออก")
        bb.audio_open("resources/soundeffects/BB-8_wrong" +
                      str(random.randrange(1, 2, 1)) + ".wav")
=======
    bb.audio_open("ding3.wav")
    if text_th == 0:
        bb.speak("ฉันฟังไม่ค่อยออก")
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
        bb.clear_emo()
        return 0, 0
    else:
        bb.audio_open("resources/soundeffects/BB-8_okay" +
                      str(random.randrange(1, 6, 1)) + ".wav", wait=True)
    text_en = translator.translate(text_th, dest='en').text
    print("text_en :", text_en)
    bb.clear_emo()
    return text_th, text_en


def apiai_processing(request, text):
    request.query = text
    action = 'None'
    response = json.loads(request.getresponse().read().decode('utf8'))
    speech = response['result']['fulfillment']['speech']
<<<<<<< HEAD
    flag_payload_available = True
    # action
=======
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
    try:
        action = response['result']['action']
        print('Action is {}'.format(action))
        print('Parameter is ...')
        if action == 'input.unknown':
<<<<<<< HEAD
            # bb.speak("ฉันไม่เข้าใจ")
            bb.audio_open("resources/soundeffects/BB-8_wrong" +
                          str(random.randrange(1, 2, 1)) + ".wav")
    except:
        # bb.speak("ฉันทำไม่ได้", wait=True)
        bb.audio_open("resources/soundeffects/BB-8_wrong" +
                      str(random.randrange(1, 2, 1)) + ".wav")
        print("apiai action fail.")
    # payload
=======
            bb.speak("ฉันไม่เข้าใจ")
    except:
        bb.speak("ฉันทำไม่ได้", wait=True)
        print("apiai action fail.")
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
    try:
        # print(response['result']['fulfillment']['messages']['payload'])
        payload = response['result']['fulfillment']['messages'][-1]['payload']
        rand = random.choice(list(payload.keys()))
        payload = payload[rand]
        for order in payload:
            if order == 'emotions':
                bb.clear_emo()
                emo_list = payload[order]
                print('emotions list is : ', emo_list)
                for emo in emo_list:
                    try:
                        num = [int(i) for i in emo if i.isdigit()][0]
                    except:
                        num = 1
                    try:
                        emo = emo[:-1]
                        bb.add_emo(emo, num)
                    except:
                        print('add emo error!')
                        pass
            elif order == 'video':
                try:
                    print('hdmi-video :', payload[order])
                    bb.hdmi_open("resources/" + payload[order], sound=True)
                except:
                    pass
            elif order == 'youtube':
<<<<<<< HEAD
                print('****** YOUTUBE ********')
                bb.audio_open("resources/soundeffects/page-flip-" +
                              str(random.randrange(1, 10, 1)) + ".wav", wait=True)
                bb.speak('อยากให้ค้นหาว่าอะไรหรอ', wait=True)
                text_th, _ = speech_input()
                bb.add_emo('Loading', 200)
                # bb.speak('ฉันขอเวลาไปหา' + text_th + 'ให้คุณสักพักนะ อย่าพึ่งไปไหนหละ เดี๋ยวฉันมา')
                bb.audio_open("resources/soundeffects/BB-8_talk" +
                              str(random.randrange(1, 9, 1)) + ".wav")
=======
                bb.speak('อยากให้ค้นหาว่าอะไรหรอ', wait=True)
                text_th, _ = speech_input()
                bb.add_emo('Loading', 200)
                bb.speak('ฉันขอเวลาไปหา' + text_th + 'ให้คุณสักพักนะ อย่าพึ่งไปไหนหละ เดี๋ยวฉันมา')
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
                yt_list = bb.sight.yt_search(text_th)
                url = bb.sight.yt_genstream(yt_list[0])
                bb.clear_emo()
                bb.add_emo('During', 2)
<<<<<<< HEAD
                # bb.speak('โอเค ฉันเจอวิดีโอของคุณแล้ว')
=======
                bb.speak('โอเค ฉันเจอวิดีโอของคุณแล้ว', wait=True)
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
                bb.hdmi_open(url, sound=True)
            elif order == "video_close":
                try:
                    bb.hdmi_close()
                except:
                    pass
<<<<<<< HEAD
            elif order == "speech":
                speech = payload[order]
    except:
        flag_payload_available = False
        pass
    # speech
    try:
        if speech == '#name':
            bb.speak("ฉันคือ" + bb.info.name + "เวอร์ชั่น" + bb.info.version)
        elif speech == '#age':
            bb.speak("ฉันมีอายุ" + bb.info.age)
        elif speech == '#birthdate':
            bb.speak("ฉันเกิดวันที่" + bb.info.birthday)
        elif speech not in [' ', '', [' '], ['']]:
            bb.speak(speech)
        elif not flag_payload_available:
            # bb.speak("ฉันไม่เข้าใจคำสั่งของคุณ")
            bb.audio_open("resources/soundeffects/BB-8_wrong" +
                          str(random.randrange(1, 2, 1)) + ".wav")
    except:
        pass
=======
            elif order == 'speech':
                speech = payload[order]
    except:
        pass
    try:
        if speech == '#name':
            bb.speak("ฉันคือ" + bb.info.name + "เวอร์ชั่น" + bb.info.version)
        elif speech == '#age':
            bb.speak("ฉันมีอายุ" + bb.info.age)
        elif speech == '#birthdate':
            bb.speak("ฉันเกิดวันที่" + bb.info.birthday)
        elif speech not in [' ', '', [' '], ['']]:
            bb.speak(speech)
        else:
            bb.speak("ฉันไม่เข้าใจที่คุณพูด")
    except:
        try:
            speech = response['result']['fulfillment']['speech']
            if speech == '#name':
                bb.speak("ฉันคือ" + bb.info.name + "เวอร์ชั่น" + bb.info.version)
            elif speech == '#age':
                bb.speak("ฉันมีอายุ" + bb.info.age)
            elif speech == '#birthdate':
                bb.speak("ฉันเกิดวันที่" + bb.info.birthday)
            elif order not in [' ', '', [' '], ['']]:
                bb.speak(speech, wait=True)
            else:
                bb.speak("ฉันไม่เข้าใจที่คุณพูด", wait=True)
        except:
            print("apiai speech fail.")

    if action == 'ทำลายตัวเอง':
        bb.clear_emo()
        bb.add_emo("Bomb")
        # bb._close()
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
    if action == 'เล่นวิดีโอตามหมายเลข':
        num_videolist = response['result']['parameters']['Number']  # list
        v_action = response['result']['parameters']['Video-Command']
        if v_action == 'เล่น':
            print('resources/videos/A-{}.mp4'.format(num_videolist))
<<<<<<< HEAD
            bb.hdmi_open(
                'resources/videos/A-{}.mp4'.format(num_videolist), sound=True)
=======
            bb.hdmi_open('resources/videos/A-{}.mp4'.format(num_videolist), sound=True)
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
        if v_action == 'หยุดเล่น':
            print('หยุดเล่นวิดีโอ')
            bb.hdmi_close()

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
                            if i <= 21:
                                a += str(i) + ' '
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
        # bb.speak(response['result']['fulfillment']['speech'], wait=True)
        return action


<<<<<<< HEAD
def run_session():

=======
# ans_list = ["น้อมรับคำสั่ง", "ว่ายังไงจ๊ะ", "มาแล้วจ้า", "มีอะไรให้รับใช้",
        # "ขอโทษจ้าฉันมาแล้ว", "มาแล้ว มาแล้ว", "มีอะไรขอให้บอก", "เรียกฉันหรอ"]


def run_session(flag=False):

    # BB.dsi_open('emotions/bit_bot_emotion_1.mp4', loop=True)
>>>>>>> 6da35e78c2c6d784bfb68dd1999f4fb88d535fd7
    request = ai.text_request()
    t_th, t_eng = speech_input()
    if t_th != 0 and t_eng != 0:
        ans = apiai_processing(request, t_eng)
        if ans != 0:
            return ans


if __name__ == '__main__':
    run_session()

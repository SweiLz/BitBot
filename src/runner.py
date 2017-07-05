# # # !/usr/bin/python
# # import snowboydecoder

# # models = ["resources/BitBot.pmdl"]


# # def bitbot():
# #     detector.terminate()
# #     print("Conversation Started")
# #     # snowboydecoder.play_audio_file()
# #     # snowboydecoder.bot_speak("None", "resources/ding.wav")
# #     # snowboydecoder.main()
# #     print("Conversation Stop")
# #     print("Listening")
# #     global detector
# #     detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
# #     detector.start(callbacks)


# # callbacks = [bitbot]


# # detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
# # print("Listening")
# # detector.start(detected_callback=callbacks)
# # detector.terminate()


# import threading 
# import os
# import time
# # import signal
# import subprocess
# # def process(cmd):
# #     os.system(cmd)
# num = 1
# cmd = ['ok']

# cmd += ['0'] if num else ['1']
# print(cmd) if True else print("no")
import glob

print(glob.glob("resources/*.wav"))
print('resources/t3.wav' in glob.glob("resources/*.wav"))
# try:
#     print(cmd)
# except  :
#     print(e) 
# else:
#     print('else')
# finally:
#     print('final')
# # cmd = 'omxplayer resources/sounds/piano.wav -o local'
# cmd = ["play", "resources/ding.wav"]
# a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
# time.sleep(0.25)
# a.terminate()
# # audio_player = threading.Thread(target=task, args=(cmd,))
# # audio_player.start()

# class task(threading.Thread):
#     def __init__(self, func, cmd):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.cmd = cmd
    
#     def run(self):
#         self.func(self.cmd)
# import threading
# import time
# def hell(text):
#     print("Hello", text)

# threading.Timer(3.0, hell,args=("text",)).start()
# print("hi")
# time.sleep(10)
# audio_player = task(process,cmd)
# audio_player.daemon = True
# audio_player.start()
# # _thread.start_new_thread(task, (cmd,))
# time.sleep(0.2)
# # audio_player.join(0)
# os.kill(os.getpid(audio_player.ident), signal.SIGUSR1)
# for i in range(10):
#     print(i)
# # i =0
# while True:
#     print("ok",i)
#     i +=1
    # pass
import subprocess
import argparse
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
import time
myprocess = 0
myprocess2 = 0

parser = argparse.ArgumentParser()
parser.add_argument("DISPLAY_NUMBER")
args = parser.parse_args()
DISPLAY_NUMBER = args.DISPLAY_NUMBER
if DISPLAY_NUMBER == '2':
    DISPLAY_NUMBER = '5'
elif DISPLAY_NUMBER == '1':
    DISPLAY_NUMBER = '0'


def display(unused_addr, v1='../../small.mp4', v2=''):
    global myprocess
    cmd = ['omxplayer', '-b', '--display', DISPLAY_NUMBER, v1]
    print('command : ', cmd)
    myprocess = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def quit_video(unused_addr, v1):
    global myprocess
    if myprocess != 0:
        print('stop playing')
        myprocess.communicate(bytes('q', 'utf-8'))


def play_new(unused_addr, v1):
    global myprocess, myprocess2
    print('new playing')
    cmd = ['omxplayer', '-b', '--display', DISPLAY_NUMBER, v1]
    print('command : ', cmd)
    myprocess2 = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print('exit old player')
    if myprocess != 0:
        myprocess.communicate(bytes('q', 'utf-8'))
    myprocess = myprocess2


def main():
    dispatcher = Dispatcher()
    dispatcher.map("/d", display)
    dispatcher.map("/q", quit_video)
    dispatcher.map("/n", play_new)
    server = osc_server.ThreadingOSCUDPServer(
        ("192.168.1.244", 4000 + int(args.DISPLAY_NUMBER)), dispatcher)
    print("Display {} Serving on {}".format(args.DISPLAY_NUMBER, server.server_address))
    server.serve_forever()


if __name__ == '__main__':
    main()

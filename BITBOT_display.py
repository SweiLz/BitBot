import subprocess
import argparse
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
import time
import tempfile
import sys
myprocess = 0
myprocess2 = 0
c = 0
i = 9999
parser = argparse.ArgumentParser()
parser.add_argument("DISPLAY_NUMBER")
args = parser.parse_args()
DISPLAY_NUMBER = args.DISPLAY_NUMBER
if DISPLAY_NUMBER == '2':
    DISPLAY_NUMBER = '5'
elif DISPLAY_NUMBER == '1':
    DISPLAY_NUMBER = '0'

pdir = 'resources/emotions/'
play_list = [pdir + 'A-1.mp4', pdir + 'A-2.mp4', pdir +
             'A-3.mp4', pdir + 'A-4.mp4', pdir + 'A-5.mp4']


def display(unused_addr, v1='../../small.mp4', v2=''):
    global myprocess, i
    cmd = ['omxplayer', '--no-osd', '--layer',
           str(i), '-b', '-o', 'alsa', '--display', DISPLAY_NUMBER, v1]
    i -= 1
    print('command : ', cmd)
    myprocess = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def quit_video(unused_addr, v1):
    global myprocess
    if myprocess != 0:
        print('stop playing')
        myprocess.communicate(bytes('q', 'utf-8'))


def play_new(unused_addr, v1):
    global myprocess, myprocess2, c, i
    print('new playing')
    cmd = ['omxplayer', '--no-osd', '--layer', str(i), '--loop', '-b', '-o',
           'alsa', '--display', DISPLAY_NUMBER, play_list[c]]
    c += 1
    i -= 1
    if i >= 0:
        i = 9999
    if c >= 5:
        c = 0
    print('command : ', cmd)
    myprocess2 = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    time.sleep(1.7)
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
        ("192.168.1.243", 4000 + int(args.DISPLAY_NUMBER)), dispatcher)
    print("Display {} Serving on {}".format(args.DISPLAY_NUMBER, server.server_address))
    server.serve_forever()


if __name__ == '__main__':
    main()

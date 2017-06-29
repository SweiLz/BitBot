import subprocess
import argparse
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

myprocess = 0

parser = argparse.ArgumentParser()
parser.add_argument("DISPLAY_NUMBER")
args = parser.parse_args()


def display(unused_addr, v1='../../small.mp4', v2=''):
    global myprocess
    cmd = ['omxplayer', '-b', '--display', args.DISPLAY_NUMBER, v1]
    print('command : ', cmd)
    myprocess = subprocess.Popen(cmd, stdin=subprocess.PIPE)


def quit_video(unused_addr, v1):
    global myprocess
    if myprocess != 0:
        print('stop playing')
        myprocess.communicate(bytes('q', 'utf-8'))


def main():
    dispatcher = Dispatcher()
    dispatcher.map("/d", display)
    dispatcher.map("/q", quit_video)
    server = osc_server.ThreadingOSCUDPServer(
        ("192.168.1.244", 5000 + int(args.DISPLAY_NUMBER)), dispatcher)
    print("Display {} Serving on {}".format(args.DISPLAY_NUMBER, server.server_address))
    server.serve_forever()


if __name__ == '__main__':
    main()

import subprocess
from pythonosc import dispatcher
from pythonosc import osc_server

myprocess = 0


def display(unused_addr, v1='../../small.mp4', v2=''):
    global myprocess
    cmd = ['omxplayer', '-b', '--display', '5', v1]
    print('command : ', cmd)
    myprocess = subprocess.Popen(cmd, stdin=subprocess.PIPE)


def quit_video(unused_addr, v1):
    global myprocess
    if myprocess != 0:
        print('stop playing')
        myprocess.communicate(bytes('q', 'utf-8'))


def main():
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/d", display)
    dispatcher.map("/q", quit_video)
    server = osc_server.ThreadingOSCUDPServer(
        ("192.168.1.244", 5002), dispatcher)
    print("Display 2 Serving on {}".format(server.server_address))
    server.serve_forever()


if __name__ == '__main__':
    main()

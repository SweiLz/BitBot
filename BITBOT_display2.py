import subprocess
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse

myprocess = 0


def display(unused_addr, v1='../../small.mp4', v2=''):
    global myprocess
    cmd = 'omxplayer ' + v2 + '-b --display 5 ' + v1
    print('command : ', cmd)
    myprocess = subprocess.Popen(cmd, stdin=subprocess.PIPE)


def quit(unused_addr, v1):
    global myprocess
    if myprocess != 0:
        myprocess.stdin.write('q')


parser = argparse.ArgumentParser()
parser.add_argument("--ip",
                    default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",
                    type=int, default=5002, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/d", display)
dispatcher.map("/q", quit)
server = osc_server.ThreadingOSCUDPServer(
    (args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()

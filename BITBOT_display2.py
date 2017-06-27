from subprocess import call
from pythonosc import dispatcher
from pythonosc import osc_server
import argparse


def display(unused_addr, v1='../../small.mp4'):
    # cmd = ['omxplayer', '--display', '5', '-o', 'alsa', v1]
    cmd = 'omxplayer --display 5 '+ v1
    print('command : ', cmd)
    call(cmd, shell=True)


parser = argparse.ArgumentParser()
parser.add_argument("--ip",
                    default="127.0.0.1", help="The ip to listen on")
parser.add_argument("--port",
                    type=int, default=5002, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/d", display)
server = osc_server.ThreadingOSCUDPServer(
    (args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()

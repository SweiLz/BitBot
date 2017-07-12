#from bitbot import *
import time
from omxplayer import OMXPlayer
#bb = Robot()
# for i in range(4):
#    bb.emotion("A-"+str(i+1),True)
#    time.sleep(1)
player = OMXPlayer("../resources/emotions/s1.mp4",
                   args=['--no-osd', '-o', 'alsa', '-b'])
player.play()
time.sleep(5)
player.set_position(17)

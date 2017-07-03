# from bitbot import *

# bb = Robot()
# for i in range(4):
#     bb.emotion("A-"+str(i+1),True)
#     time.sleep(1)
from omxplayer import OMXPlayer
import time

player = OMXPlayer("resources/emotions/A-1.mp4")
player.play()

time.sleep(5)
player.pause()
# player.
player.quit()
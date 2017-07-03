from bitbot import *

bb = Robot()
for i in range(4):
    bb.emotion("A-"+str(i+1),True)
    time.sleep(1)

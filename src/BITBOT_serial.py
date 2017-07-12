import serial
import numpy as np
from scipy.interpolate import interp1d

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)

def bitbot_send_serial(a,b,c) :
    port.write([64, a, 35, b, 36, c])

def kinematic(pitch, roll, H, mode='K'):
    if mode == 'K':
        pitch = np.deg2rad(pitch)
        roll = np.deg2rad(roll)
        Tan_roll = np.tan(roll)
        Tan_pitch = np.tan(pitch)
        l = 80
        L = 138
        A = 50
        R_c = l * Tan_roll + H
        R_a = (L * Tan_pitch + 2 * H - l * Tan_roll) / 2
        R_b = 3 * H - R_a - R_c
    elif mode == 'R':
        R_a = pitch
        R_b = roll
        R_c = H
    R = [R_a, R_b, R_c]
    if R_a < 0 or R_b < 0 or R_c < 0:
        R_a += abs(min(R))
        R_b += abs(min(R))

        R_c += abs(min(R))
        print('\n !!  Range error ::> mapping ... \n')

    if R_a > 50:
        R_a = 50
    if R_b > 50:
        R_b = 50
    if R_c > 50:
        R_c = 50

    R = [R_a, R_b, R_c]
    m01 = interp1d([0, 50], [255, 0])
    R_a = int(m01(R_a))
    R_b = int(m01(R_b))
    R_c = int(m01(R_c))
    print(R_a, R_b, R_c)
    
    bitbot_send_serial(R_a,R_b,R_c)
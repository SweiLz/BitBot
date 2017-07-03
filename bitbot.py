import pyaudio
import time
import wave
import threading

class Robot:
    def __init__(self):
        print("New Robot")
        
    
    def speak(self, text):
        print("Speak:", text)
    
    def play_wav(self, fname, wait=True):
    
        def play():
            audio = pyaudio.PyAudio()
            fwav = wave.open(fname, 'rb')
            fformat = audio.get_format_from_width(fwav.getsampwidth())
            fchannels = fwav.getnchannels()
            frate = fwav.getframerate()
            fdata = fwav.readframes(fwav.getnframes())
            print(fformat,fchannels,frate)
            stream = audio.open(format=fformat,channels=fchannels,rate=frate, input=False, output=True)
            stream.start_stream()
            stream.write(fdata)
            stream.stop_stream()
            stream.close()
            audio.terminate()

        if not wait:
            threading.Thread(target=play).start()
        else:
            play()

        

    
def main():
    bitbot = Robot()
    bitbot.speak("น้อบรับคำสั่ง")
    bitbot.play_wav("resources/sounds/accept.wav",False)
    bitbot.speak("เล่นแล้ว")
    time.sleep(0.25)
    bitbot.play_wav("resources/sounds/accept.wav",False)
    bitbot.speak("เล่นครั้งที่ 2") 

if __name__ == '__main__':
    main()
# Bitbot, by BitStudio.

Bitbot ถูกพัฒนาที่ BitStudio

## How to use

Connect to raspberrypi

ip [192.168.1.243]

wifi ssid : bitworkshop

**Connect SSH**
``` shell
sweilz@Liews:~$ ssh pi@192.168.1.243
pi@192.168.1.243's password: raspberry
```

**Run Script**
``` bash
pi@raspberrypi:~ $ cd Documents/BitStudio/BitBot/
pi@raspberrypi:~/Documents/BitStudio/BitBot $ python3 src/main.py
```

**Test Script**

ใช้สำหรับทดสอบฟังก์ชั่นการทำงานของ Bitbot

``` bash
pi@raspberrypi:~/Documents/BitStudio/BitBot $ python3 src/runner.py
```

### Bitbot features:

* [x] Generate speech from text
* [x] Play audio file
* [x] Dual display [HDMI, DSI]
* [x] Change voice pitch to robot
* [x] Voice active Snowboy
* [x] Play game [Count21]
* [x] Understand what user say [api.ai]
* [x] Translate Thai <-> English
* [x] Stream Video from Youtube
* [x] Search infomation from Wikipedia
* [x] Emotion display
* [x] Basic Conversation bot from RiveScript
* [ ] Control motion platform
* [ ] Auto train Snowboy to hotword
* [ ] Camera Capture
* [ ] Face Recognition

### To-Do
* [ ] แสดงอารมณ์ (หน้าตาแสดงอารมณ์ เสียง)
* [ ] เรียกร้องความสนใจ (บ่น)

### Requirements:
* Raspberry Pi3 with Raspbian
* Python 3.4 or later
* Snowboy Hotword Detector

## Installation

``` 
$ sudo apt-get install sox libatlas-base-dev python3-pyaudio python3-dev
$ sudo apt-get install autoconf automake libtool bison libpcre3 libpcre3-dev 
```

## Train Hotword Model

**Personal model**

Create your personal hotword model [Snowboy](https://snowboy.kitt.ai) 

Replace the hotword model in `resources/hotwords` with your personal model.
and rename to `Bitbot.pmdl`

## Example Command

* เล่นวิดีโอที่ [1-9] 
* หยุดเล่นวิดีโอ / ปิดวิดีโอ
* สอนฉันทำอาหารหน่อย
* สอนฉันพับกระดาษหน่อย
* สอนฉันวาดรูปหน่อย
* เปิดยูทูป
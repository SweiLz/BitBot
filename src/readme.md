# Bitbot Documents

## Features

* พูดข้อความที่ต้องการ
* ฟังเสียงที่เราพูดแล้วแปลงเป็นข้อความ
* เล่นไฟล์เสียง wav
* เล่นไฟล์วีดีโอ หน้าจอ
* เล่นไฟล์วีดีโอ โปรเจคเตอร์
* เล่นหน้าตามอารมรมณ์ต่างๆ
* Stream วีดีโอจาก Youtube
* ค้นหาข้อมูลจาก Wikipedia
* เขียนคำถามคำตอบจาก RiveScript

### Bitbot object initialize
``` python
from bitbot import Robot

bitbot = Robot()
```
___

### พูดจากข้อความที่เราให้

#### Text to Speech
``` python
self.speak(text, wait=False, process=False)
```

Arguments :
``` markdown
<string> text : ข้อความที่เราต้องการจะให้หุ่นยนต์พูด
<boolean> wait : ต้องการรอให้พูดจบก่อนแล้วถึงทำฟังก์ชั่นถัดไปหรือไม่
<boolean> process : แปลงเสียงให้เหมือน Wall-E
```

Example :
``` python
bitbot.speak("สวัสดีค่ะ")
#พูดสวัสดีค่ะแล้วรันคำสั่งต่อไปโดยไม่ต้องรอจบ
bitbot.speak("ยินดีที่ได้รู้จักค่ะ", wait=True)
#รอให้พูดยินดีที่ได้รู้จักเสร็จก่อน
bitbot.speak("ฉันชื่อ วอล์อี", wait=True,process=True)
#แปลงเสียงพูดและรอให้พูดจบ
```
___

### ฟังเสียงที่เราพูดแล้วแปลงเป็นข้อความ

#### Voice Recognition 
``` python
self.listen(lang="th-TH")
```

Arguments :
``` markdown
<string> lang : ภาษาที่เราต้องการให้หุ่นยนต์ฟัง
```

Return :
``` markdown 
<string> text : ข้อความที่ฟังได้
<int> 0 : หากอินเทอร์เน็ตขัดข้องหรือไม่ได้ยินคำพูด
```

Example :
``` python
recognize_th = bitbot.listen()
print(recognize_th)
#ฟังคำพูดภาษาไทยแล้ว print ออกมา
recognize_en = bitbot.listen(lang="en-US")
print(recognize_en)
#ฟังคำพูดภาษาอังกฤษแล้ว print ออกมา
```
___

### เล่นไฟล์เสียง

#### เปิดไฟล์เสียง
``` python
self.audio_open(fname, terminate=False, wait=False)
```
#### ปิดไฟล์เสียง
``` python
self.audio_close()
```

Arguments :
``` markdown
<string> fname : ที่อยู่ของไฟล์เสียง
<boolean> terminate : ปิดเสียงที่เล่นค้างเอาไว้อยู่ทั้งหมด
<boolean> wait : ต้องการรอให้เล่นจบก่อนแล้วถึงทำฟังก์ชั่นถัดไปหรือไม่
```

Example :
``` python
bitbot.audio_open("resources/sounds/ding.wav")
#เล่นไฟล์เสียง ding.wav
bitbot.audio_open("resources/sounds/dong.wav", terminate=True, wait=True)
#ปิดเสียงที่เล่นอยู่ทั้งหมดแล้วเล่นไฟล์ dong.wav และรอให้เล่นจบ
bitbot.audio_open("resources/sounds/piano.wav", wait=True)
#เปิดไฟล์เสียง piano.wav และรอให้เล่นจบ
bitbot.audio_close()
#ปิดไฟล์เสียงที่เล่นอยู่ทั้งหมด
```
___

### เล่นไฟล์วีดีโอ

#### เล่นวีดีโอบนหน้าจอ
``` python
self.dsi_open(fname, sound=False, wait=False, loop=False)
```
#### หยุดเล่นวีดีโอบนหน้าจอ
``` python
self.dsi_close()
```
#### เล่นวีดีโอบนโปรเจคเตอร์
``` python
self.hdmi_open(fname, sound=False, wait=False, loop=False)
```
#### หยุดเล่นวีดีโอบนโปรเจคเตอร์
``` python
self.hdmi_close()
```

Arguments :
``` markdown
<string> fname : ที่อยู่ของไฟล์วีดีโอ หรือ URL ของวีดีโอ
<boolean> sound : ต้องการเปิดเสียงวีดีโอที่กำลังจะเล่นหรือไม่
<boolean> wait : ต้องการรอให้เล่นจบหรือไม่
<boolean> loop : ต้องการให้วีดีโอเล่นซ้ำไปเรื่อยๆหรือไม่
```

Example :
``` python
bitbot.dsi_open("resources/videos/A-0.mp4")
#เล่นวีดีโอไม่มีเสียง
bitbot.dsi_open("resources/videos/A-1.mp4", sound=True)
#เล่นวีดีโอพร้อมเปิดเสียง
bitbot.dsi_open("resources/videos/A-2.mp4", wait=True)
#เล่นวีดีโอและรอจนกว่าวีดีโอจะเล่นจบ
bitbot.dsi_open("resources/videos/A-3.mp4", sound=True, loop=True)
#เล่นวีดีโอโดยเปิดเสียง และเป็น Loop 
time.sleep(2)
bitbot.dsi_close()
#หน่วงเวลา 2 วินาทีแล้วปิดวีดีโอทั้งหมดบนหน้าจอ

bitbot.hdmi_open("resources/videos/spiderman.mp4")
#เล่นวีดีโอไม่มีเสียงผ่านโปรเจคเตอร์
bitbot.hdmi_open("resources/videos/pirate.mp4", sound=True)
#เล่นวีดีโอพร้อมเสียง
time.sleep(60)
bitbot.hdmi_close()
#หน่วงเวลา 1 นาทีและปิดไฟล์วีดีโอทั้งหมด
```
___

### Stream Video จาก Youtube

#### ค้นหาวีดีโอที่ต้องการ
``` python
self.sight.yt_search(query)
```
Arguments :
``` markdown
<string> query : คำที่ต้องการค้นหาใน youtube
```
Return :
``` markdown
<list> res : ลิสของลิ้งค์วีดีโอที่หาเจอ
```
Example :
``` python
yt_list = bitbot.sight.yt_search("โดเรม่อน")
print(yt_list)
#ค้นหาคำว่า โดเรม่อน ใน Youtube และ print ออกมา
```

#### สร้างลิ้งค์ Stram วีดีโอ
``` python
self.sight.yt_getstream(link)
```
Arguments :
``` markdown
<string> link : ลิ้งค์วีดีโอจาก Youtube
```
Return :
``` markdown
<string> url : ลิ้งค์ stream 
```
Example :
``` python
yt_list = bitbot.sight.yt_search("โดเรม่อน")
yt_url = bitbit.sight.yt_genstream(yt_link[0])
print(yt_url)
#สร้างลิ้งค์ Stram วีดีโอและ print ออกมา

bitbot.hdmi_open(yt_url, sound=True)
#แสดงวีดีโอที่สร้างมาผ่านโปรเจคเตอร์พร้อมเปิดเสียงวีดีโอ
```
___

### ค้นหาข้อมูลจาก Wikipedia

#### หาจาก wiki
``` python
self.knowledge.wk_search(title)
```
Arguments :
``` markdown
<string> title : คำที่ต้องการจะค้นหา
```
Return :
``` markdown
<string> res : ข้อมูลคำตอบจาก Wikipedia
```
Example :
``` python
doremon_txt = bitbot.knowledge.wk_search("โดเรม่อน")
print(doremon_txt)
#ค้นหาข้อมูลที่เกี่ยวกับ Doremon และ print ออกมา
```
___

### สร้าง bot คุยเล่น

#### bot พูดคุยด้วย Rivescript
``` python
self.chatty.message(text)
```
Arguments :
``` markdown
<string> text : ข้อความจาก user ไปให้หุ่นยนต์
```
Return :
``` markdown
<string> res : ข้อความคำตอบจากหุ่นยนต์
```
Example :
``` rivescript
+ สวัสดี (ครับ | คะ | จ้า | เจ้า)
- สวัสดีค่ะ
- ว่ายังไงหรอ
- เรียกเค้าหรอ
- เค้ามาแล้วมีอะไร
```
``` python
res_txt = bitbot.chatty.message("สวัสดีครับ")
print(res_txt) # สวัสดีค่ะ

res_text = bitbot.chatty.message("สวัสดี")
print(res_txt) #เค้ามาแล้วมีอะไร
```
___
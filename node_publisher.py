import time
from node_class import NodePub

def main():
    stock_data = {
        'symbol': 'ABB',
        'price' : 230
    }
    stock_data2 = [10,20,30,40,50] 

    fb_bot = NodePub("tcp://127.0.0.1:5000")

    while True:
        fb_bot.send('speaker_hdmi',stock_data)
        time.sleep(1)

if __name__ == '__main__':
    main()
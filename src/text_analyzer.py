
def _text_analysis(HOT, text_th):
    text = text_th
    t_ = {"เล่นวิดีโอ": ["เล่นวิดีโอ", "เปิดวิดีโอ"],
          0: ['0', 'ศูนย์'], 1: ['1', 'หนึ่ง'], 2: ['2', 'สอง'], 3: ['3', 'สาม'], 4: ['4', 'สี่'],
          5: ['5', 'ห้า'], 6: ['6', 'หก'], 7: ['7', 'เจ็ด'], 8: ['8', 'แปด'], 9: ['9', 'เก้า']
          }
    for key in t_:
        for word in t_[key]:
            if word in text:
                print('word :', word)
                HOT[key] = text.index(word)
                _text_analysis(HOT, text.replace(word, ''))
                return HOT


def text_sort(text_th):
    HOT = {}
    HOT = _text_analysis(HOT, text_th)
    HOT = {v: k for k, v in HOT.items()}  # swap dict key|value
    HOT_sorted = {}
    sort_temp = []
    for i in HOT:
        sort_temp.append(i)
    sort_temp.sort()
    for k in range(len(sort_temp)):
        HOT_sorted[k] = HOT[sort_temp[k]]
    return HOT_sorted

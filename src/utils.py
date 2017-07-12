import json
from datetime import datetime

class Experience(object):
    pass

class Personar(object):
    def __init__(self):
        self.data = self._load()
        self._up_version()

    def _load(self):
        print("::: Load Personar :::")
        with open('resources/personar.json', 'r') as f:
            return json.load(f)

    def _overwrite(self):
        # print("::: Write Personar :::")
        with open('resources/personar.json', 'w') as f:
            json.dump(self.data, f)

    def update(self, key, value):
        print("::: Update {0} to {1}".format(key, value))
        self.data[key] = value
        self._overwrite()

    @property
    def name(self):
        return self.data['name']

    @property
    def birthday(self):
        d = datetime.strptime(self.data['birthday'], '%Y-%m-%d %H:%M:%S')
<<<<<<< HEAD
        return "วันที่ {0} เดือน {1} ปี {2}".format(d.day, d.month, d.year)
=======
        return "{0} เดือน {1} ปี {2}".format(d.day, d.month, d.year)
>>>>>>> 8024d7458773fe9252b3259f40e1d3711f00ccf0

    @property
    def age(self):
        d = datetime.now() - datetime.strptime(self.data['birthday'], '%Y-%m-%d %H:%M:%S')
        h, s = divmod(d.seconds, 3600)
        m, s = divmod(s, 60)
<<<<<<< HEAD
        return "{0} วัน {1} ชั่วโมง {2} นาที".format(d.days, h, m)

    @property
    def version(self):
        return list(map(int, self.data['version'].split('.')))

    def _up_version(self):
        ver = self.version
=======
        return "{0} วัน {1} ชั่วโมง {2} นาที {3} วินาที".format(d.days, h, m, s)

    @property
    def version(self):
        # return list(map(int, self.data['version'].split('.')))
        return self.data['version']

    def _up_version(self):
        ver = list(map(int, self.data['version'].split('.')))
>>>>>>> 8024d7458773fe9252b3259f40e1d3711f00ccf0
        ver[2] += 1
        if ver[2] == 100:
            ver[2] = 0
            ver[1] += 1
            if ver[1] == 100:
                ver[1] = 0
                ver[0] += 1
        self.update('version', ".".join(map(str, ver)))

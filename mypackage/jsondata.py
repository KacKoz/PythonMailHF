import json

class jsondata:
    def __init__(self, filename):
        self.file = open(filename)
        self.data = json.load(self.file)




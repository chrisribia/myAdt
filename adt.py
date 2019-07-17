import sys

class student:

    def __init__(self,filename):
        self.filename = filename

    def get_each_line(self):
        a = open(self.filename, mode = "rt", encoding = "utf-8")
        for line in a:
            sys.stdout.write(line)
        a.close()
        
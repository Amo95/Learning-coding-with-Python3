class Colors(object):
    def __init__(self):
        self.red = "\033[91m"
        self.magenta = "\033[1;35m"

class Red(Colors):
    def color2(self):
        super(Red, self).__init__()

class Magenta(Colors):
    def color2(self):
        super(Magenta, self).__init__()


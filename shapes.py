class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.length

    def parameter(self):
        return 2 * self.width + 2 * self.length

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return self

    def parameter(self):
        return 4 * self.length

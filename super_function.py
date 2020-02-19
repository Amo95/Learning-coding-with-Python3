# super explained

class Base:
    def __init__(self):
        print("Base.__init__")

class Child1(Base):
    def __init__(self):
        Base.__init__(self)
        print("Child1.__init__")

class Child2(Base):
    def __init__(self):
        Base.__init__(self)
        print("Child2.__init__")

class Child3(Child1, Child2):
    def __init__(self):
        Child1.__init__(self)
        Child2.__init__(self)
        print("Child3.__init__")

c3 = Child3()

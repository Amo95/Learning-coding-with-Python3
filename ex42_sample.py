class sample(object):
    # Static variable for object Number
    ObjNum = 0

    def __init__(self, name):
        self.name = name

        # Increment static variable for each object
        sample.ObjNum += 1

        # each objects's unique number than can
        # can be considered as a Unique number
        self.objectNo = sample.ObjNum

    def myFunc(self):
        print("My name is ", self.name,
            "from object ", self.objectNo)


    def alterIt(self, newName):
        self.name = newName

    @staticmethod
    def myFunc2():
        print("I'm not a bound method")

# creating first instance of class sample
test1 = sample("James")
test1.myFunc()

# unhode the line below to see the error
sample.myFunc2() #------------> error line (TypeError)

# creatinf second instances pf class sa,ples
test2 = sample("Amo")
test2.myFunc()
test2.alterIt("Eric")
test2.myFunc()
test1.myFunc()

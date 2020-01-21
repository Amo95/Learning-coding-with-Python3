#SOLUTION
class Thing(object):
    def test(a, message):
        print(message)

a = Thing()
a.test("Hello")


#ERROR ~ TypeError (python takes a.test("Hello") as test(a, "Hello")
#hence two arguments were given instead of one
class Thing(object):
    def test(message):
        print(message)

a = Thing()
a.test("Hello")

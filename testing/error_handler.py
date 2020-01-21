try:
    class Thing(object):
        def test(message):
            print(message)

    a = Thing()
    a.test("Hello")

except TypeError as e:
    class Person(object):
        def test(var, message):
            print(message)

    x = Person()
    x.test("Hello")

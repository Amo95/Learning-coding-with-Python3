
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)

class D(C):

    def __init__(self):
        print("Initializing: class D")
        super().__init__()

    def sub_method(self, b):
        print("Printing from class D:", b)
        super().sub_method(b + 1)




if __name__ == '__main__':
    d = D()
    d.sub_method(1)

class MyStuff(object):
  """docstring for ClassName"""
  def __init__(self, name):
    self.name = name

  def apple(self):
    print(self.name + " said 'OOP is rocking well!'")

  def code(self):
    print(self.name + ' says he love coding')

def main():
  thing = MyStuff("Amo James")
  thing.apple()
  thing.code()

if __name__ == "__main__":
  main()

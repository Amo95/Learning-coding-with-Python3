# dict style
mystuff = {
  "avocado": "hello",
  "apple": "This is a dictionary",
  "orange": "hi"
}
mystuff['apple']

# module style
def apple():
  print("This is a module with function")
tangerine = ""
mystuff.apple()
print(mystuff.tangerine)

# class style
class MyStuff(object):
  """docstring for MyStuff"""
  def __init__(self):
    self.tangerine = "I love tangerine"

  def apple():
    print("I love apples")

def main():
  thing = MyStuff()
  thing.apple
  print(thing.tangerine)

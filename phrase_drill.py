class Names(object):
  def __init__(self, name):
    self.name = name

  def question(self):
    for line in self.name:
      print("My name is " + line)

thing = Names([
  "DummyCod3R",
  "Amo",
  "James"
  ])

thing.question()
print(thing.name)

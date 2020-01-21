from sys import argv

script, filename = argv

# target = open(filename)
# target.close()

with open(filename) as target:
  output = target.read()

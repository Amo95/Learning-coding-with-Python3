def add(a, b):
  print(f"The sum of {a} and {b} is equal", end=" ")
  return a + b

print("Enter first digit", end=' ')
fnum = int(input("? "))
print("Enter second digit", end=' ')
snum = int(input("? "))

print(add(fnum, snum))

def id(name, age= 23):
  return ("Your name is {} and you are {} years old".format(name, age))

print("Enter your Name here:", end=" ")
id_name = input("? ")
# print("Enter your Age here:", end=" ")
# id_age = input("? ")

print(id(id_name))

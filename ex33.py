i = 0
inc = int(input("Enter number of increment > "))
numbers = []

def loop(i, incr):
  num = int(input("Enter value here > "))
  while i < num:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += incr
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

loop(i, inc)

print("The numbers: ")

for num in numbers:
  print(num)

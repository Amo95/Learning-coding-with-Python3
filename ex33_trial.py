i = 0
inc = int(input("Enter number of increment > "))
numbers = []

def loop(i, incr):
  num = int(input("Enter first range value > "))
  num2 = int(input("Enter second range value > "))
  for i in range(num, num2):
    print(f"At the top i is {i}")
    numbers.append(i)

    i += inc
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

loop(i, inc)

print("The numbers: ")

for num in numbers:
  print(num)

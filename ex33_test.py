import ex33_test_func

i = 0
inc = int(input("Enter number of increment > "))
numbers = []

ex33_test_func.loop(i, inc)

print("The numbers: ")

for num in numbers:
  print(num)

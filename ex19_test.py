def adding(first, second):
  print("You first number is {}".format(first))
  print(f"Your second number is {second}")
  add = first + second
  print(f"The sum of {first} and {second} is {add}")

# 1
adding(1000, 20)

# 2
fnum = 4 + 5
snum = 200 - 45
adding(fnum, snum)

# 3
adding(fnum + 2, snum - 5)

# 4
adding(fnum + snum, snum)

# 5
adding(fnum, 10)

# 6
adding(50 - 3, 7)

# 7
adding(fnum / 2, snum % 2)

# 8
adding('hello', 'world')

# 9
adding('hello' * 2, 'world')

# 10
adding((10 * 4 + 5)/ 3 + 4, snum)

# 11
print("Enter first digit here:", end=" ")
digit_1 = int(input())
digit_2 = int(input("Enter second digit here: "))

adding(digit_1, digit_2)

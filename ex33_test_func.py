def loop(i, incr):
  numbers = []
  num = int(input("Enter value here > "))
  while i < num:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += incr
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

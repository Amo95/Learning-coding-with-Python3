# loop row
for row in range(6):
  # loop column
    for col in range(7):
      # condition
        if (row == 1 and col % 3 != 0) or (row == 2 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()
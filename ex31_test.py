print("""You enter a dark room with two doors.
  Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    else:
        print("The bear eats your legs off, Good job!")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.\n2. Yellow jacket clothespins.\n3. Understanding revolvers yelling melodies.")

    body = input("> ")

    if body == "1":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    elif body == "2":
        print("Your body survives powered bya mind of jello. \nGood Job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
  print("You stumble around and fall on a knife and die. Good job!")

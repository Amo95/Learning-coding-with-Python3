from sys import exit #import the feature exit from the sys package (simply putting)
from os import system #importing a os.system module to use it features

def gold_room():
  system("clear")
    print(""""This is room is full of gold. How much do you take?

  Hints: Enter a value""")

  choice = input("> ")
  if choice > "0":
    how_much = int(choice)
  else:
    dead("Man, learn to type a number.")

  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    print("Do want to play again? Type Yes/No")
    select = input("> ")

    if select == "Yes" or select == "yes":
      start()
    elif select == "No" or select == "no":
      print("Thanks for playing my game...")
      exit(0)
    else:
      print("Type the correct value (Yes or No)")

  else:
    dead("You greedy bastard!")
    print("try again!!\n\n\n")
    bear_room()

def bear_room():

  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("""How are you going to move the bear?
    1. Take Honey
    2. Taunt bear when it moves
    3. Taunt bear when it has already moved
    4. Open Door
    5. Quit
    6. Back

  Hints: Enter 2 options here""")
  bear_moved = False
  test = True

  while test:
    choice = int(input("> "))

    if choice == 1:
      dead("The bear looks at you then slaps your face off.")
    elif choice == 2 and not bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == 3 and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif choice == 4 and bear_moved:
      gold_room()
    elif choice == 5:
      def stop():
        system("clear")
        print("Aagh! Are you sure you want to quit? Yes or No")
        take_in = input("> ")

        if take_in == "Yes":
          exit(0)
        elif take_in == "No":
          bear_room()
        elif take_in == "":
          print("Please i'm being polite to tell to enter something!!!!!!!")
        else:
          print("Goosssssssh!! It's 'Yes' or 'No'")
          exit(0)

      stop()

    elif choice == 6:
      start()
    else:
      print("I got no idea what that means.")

def cthulhu_room():
  system("clear")
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.")
  print("""Do you flee for your life or eat your head?
    1. Flee for my life
    2. Eat my head""")

  choice = int(input("> "))

  if choice == 1:
    start()
  elif choice == 2:
    def now():
      dead("Well that was tasty!")
      print("""Game Over!!! Do you want try again?
        1. Yes
        2. No""")
      selects = int(input("> "))

      if selects == 1:
        start()
      elif selects == 2:
        quit("Thanks for playing. It was fun")
      else:
        print("Please select an option!!\n\n")
        now()

    now()

  else:
    cthulhu_room()

def dead(why):
  print(why, "Good job!")
  exit(0)

def quit(entry):
  print(entry)
  exit(0)

# first function i.e preceding of code

def start():
  system("clear") # clearing screen with the os.system module

  # using the escape string \033 to change font color, background color and font size i.e ([3; 37; 40m respectively)

  print("\033[3;37;40mYou are in a dark room.")
  print("There is a door to your right and left.")
  print("""Which one do you take?
    1. Left
    2. Right
    3. Quit""")

  choice = int(input("> ")) # user input accept int values

  if choice == 1:
    system("clear")
    bear_room()
  elif choice == 2:
    cthulhu_room()
  elif choice == 3:
    system("clear")
    print("""Are you sure you want to quit?
      1. Yes
      2. No""")
    pick = int(input("> "))

    if pick == 1:
      print("Hope to see you play again")
      exit(0)
    elif pick == 2:
      start()
    else:
      dead("Well, wrong entry")

  else:
    dead("You stumble around the room until you starve.")

# calling function to start the code right from the start() method
start()


# Select rooms
# ROOM 1 hints
# if room 1 is selected
# select options to proceed
# if you start game in room 1, then type enter to open door
# after door is open, you are acknowledged
#  then you solve a puzzle to skip a monster or get killed

# starting the aclose here
from os import system
import ex36_mod
import os, sys, subprocess
from sys import exit, argv


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

if not os.geteuid() == 0:
    sys.exit("Evolution must be run as root")

def now():
  system("clear")
  print("Oh Maaaan, that was bad a$$")
  print("""So you wanna show you good huh? then bring it on!!

    How many animals did Moses sent to the ark?
    1. 300
    2. 3000
    3. pairs
    4. Enter your number if its not provide""")
  accept = input("> ")

  if accept == "1":
    print("I'm sorry, LOSER looooooooool!, start all over")
    use()
  elif accept == "2":
    print("Did you just choose that, you suck huh!, start all over")
    use()
  elif accept == "3":
    print("OMG, just stop playing")
    use()
  elif accept == "4":
    def right():
      take = input("Enter number here > ")

      if take != "none" or take != "nothing" or take != "wrong":
        print("you LOSER, start all over")
        use()
      else:
        print("Oh boy, you are genius!!!")
    right()

  else:
    exit(0)

def use():
    clear()
    logo()
    print("OOPS LOOOOOOOOOOSSSER ^_^")
    print("Why would you avoid all these values")
    print(GREEN + """888888888888888a88888888888888888888883458888888888888888888888888
8880988888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888588888888888888888888888888888888888
8888888888888888m88888888888888888888888888888888888881888888888888
8888888888888888888888888888888288888888888888888888888888888888888""" + END)
    user = input("Enter username > ")

    if user == "amo95":
      password()
    elif user == "Q" or user == "q":
      print(GREEN + '''
Thank You for using Evolution, Don't work hard, work smart!  \n''' + END)
      exit(0)
    else:
      print("oh really, You are not the admin!!")
      use()

def pas():
    passwd = input("Enter password > ")

    if passwd == "12345":
      start()
    else:
      while True:
        print("oh wrong password, retry")
        pas()


def room_one():
  clear()
  print(MAGENTA + """An ex-policeman lost his house and wife. What did he
first lost?""" + YELLOW + """
Press Ctrl^C to quit""" + END)
  choose = input(RED + "\n\nEnter answer here >> " + END)

  if choose == "house" or choose == "House" or choose == "HOUSE":
    def option():
      clear()
      print("""Enter {0}[{1}n{0}]{1} to move to the next puzzle or enter {0}[{1}b{0}]{1} to go back""".format(RED, END))
      accept = input("> ")

      while True:
        if accept == "n":
          now()
        elif accept == "b":
          room_one()
        else:
          option()


  elif   choose == "wife" or choose == "WIFE" or choose == "Wife":
    print("JOKES ON YOU. I WIN, YOU LOSE!!")
    use()
  elif choose == "job" or choose == "Job" or choose == "JOB":
    print("I'm sorry PUNK. YOU LOSE!!")
    use()
  else:
    room_one()

  option()


def easy():
  clear()
  ex36_mod.need()
  print(GREEN + """

Oh you a newbie... Welcome once again to evolution ^_^
To become a professional treasure hunter, kill the bear and get a treasure...""" + YELLOW + """

Select a room of your choice

1. Room 1
2. Room 2
3. Room 3
[B] Back""" + END)

  info = input("> ")

  if info == "1":
    room_one()
  elif info == "2":
    room_two()

  elif info == "3":
    room_three()
  elif info == "B" or info == "b":
    start()
  else:
    easy()

def clear():
    system("clear")

def start():
  clear()
  ex36_mod.need()
  print(GREEN + """


Welcome to Evolution. An amazing CLI game to test if you are
genius enough to find your way through to finding the hidden treasure!! hahahaaahaa!
Lets Play s^cker!

Hint: There are 3 levels and 3 rooms in each level

Select a level to start

[E] Easy
[A] Average
[D] Difficult
[L] Logout""" + END)

  select = (input("> "))

  if select == "E" or select == "e":
    def next():
        clear()
        print(GREEN + "You selected easy. Do you want to stay? Select " + END + """
1. Yes
2. No""")
        select = input("> ")

        if select == "1":
          easy()
        elif select == "2":
          start()
        elif select != "1" or select != "2":
          system("clear")
          print("Please enter something!!")
          next()
        else:
          pass

    next()
  elif select == "A" or select == "a":
    average()
  elif select == "D" or select == "d":
    difficult()
  elif select == "L" or select == "l":
    username()
  else:
    dead("Oops")

def close():
    sys.stdout.write(GREEN + '''
Thank You for using Evolution, Don't work hard, work smart!  \n''' + END)

def logo():
  sys.stdout.write(MAGENTA + """
                .' '. WE BEEZ U  __
       .        .   .          \(__\_/             Beta Version: 0.1
        .         .         . -{{#(|8)
          ' .  . ' ' .  . '    /(__/ \      by:""" + WHITE + ' Amo James (' + MAGENTA + '@hackAfrique' + WHITE + ')' + '\n' + '\n' + END)
  print("{0}[{1}Q{0}]{1} Quit or control^c ".format(MAGENTA, WHITE) + "\n")

def dead(entry):
  print(entry, "Enter something!!")
  close()

def username():
    clear()
    logo()
    print("WELL DONE mate ^<>^")
    print("Why would you avoid all these values")
    print(GREEN + """8888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888
88888888888888888888888User888888am09588888888888888888888888888888
88888888888888888888888888888888888888pass8888888888881234588888888
8888888888888888888888888888888888888888888888888888888888888888888""" + END)
    user = input("Enter username > ")

    if user == "amo95":
      password()
    elif user == "Q" or user == "q":
      close()
    else:
      exec('print("oh really, You are not the admin!!")')
      username()

def password():
    passwd = input("Enter password > ")

    if passwd == "12345":
      start()
    else:
      while True:
        exec('print("oh wrong password, retry")')
        password()

def puzzle():

  if sys.platform == "linux" or sys.platform == "linux2":
    subprocess.call("clear", shell=True)
    logo()
  else:
    subprocess.call("cls", shell=True)
    logo()

  print(BLUE + "Solve the following puzzles to earn the username and password to start" + END)
  print("""

    An electronic train from the west is moving to east. The train poduces smoke.
    Which direction would the smoke go
    1. West
    2. East
    3. North-West
    4. None
    """)

  puzz = input("Answer > ")

  if puzz == "1":
    print("Oh no!! You are wrong")
    close()
  elif puzz == "2":
    print("Oh shoot!! You are wrong")
    close()
  elif puzz == "3":
    print("Oh shut the front door! You almost there")
    close()
  elif puzz == "4":
    print("You are right!! How did you get that!!")
    username()
  elif puzz == "Q" or puzz == "q":
    close()
  else:
    print("Enter something please re-enter")
    puzzle()

def main():
  try:
    puzzle()

  except KeyboardInterrupt:
    close()

main()

import ex31_function
import os

os.system("clear")

def start():
  print("""This game is created by @DummyCod3r.
It is a simple question and answer questions.""")
  print("""Are you:\n
    1. A student
    2. An employee
    3. An employer
    4. quit""")

  options = input("> ")

  if options == "1":
    os.system("clear")
    print("Amazing to know you are a student!")

    def back():
      print("""What is your level of education:\n
        1. Basic Education
        2. Senior High School
        3. University
        4. Back""")

      options2 = input("> ")
      if options2 == "1":
          os.system("clear")
          print("What is your name? ", end=" ")
          name = input()
          os.system("clear")
          print(f"""\033[1;32;40m Hello {name}\033[1;37;40m, solve the following
Use the calculator to perform some calculation:\n""")
          print("\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Back")

          select = input("> ")
          if select == "1":
            num1 = int(input("Enter first value: "))
            num2 = int(input("Enter second value: "))
            final = int(num1 + num2)
            total = ex31_function.addition(num1, num2)
            print(final)

            if total == final:
              os.system("clear")
              print("You are brilliant!!")
              back()

            else:
              print("You are dumb!!")

          elif select == "2":
            num1 = int(input("Enter first value: "))
            num2 = int(input("Enter second value: "))
            final = int(num1 - num2)
            total = ex31_function.sub(num1, num2)
            print(final)

            if total == final:
              print("You are a genius!!")

            else:
              print("You are dumb!!")

          elif select == "3":
            num1 = int(input("Enter first value: "))
            num2 = int(input("Enter second value: "))
            final = int(num1 * num2)
            total = ex31_function.multiple(num1, num2)
            print(final)

            if total == final:
              print("Maaan you're doing it right!!")

            else:
              print("You are dumb!!")

          elif select == "4":
            print("Enter first value: ", end=" ")
            num1 = float(input())
            print("Enter second value: ", end=" ")
            num2 = float(input())
            final = int(num1 / num2)
            total = ex31_function.divide(num1, num2)
            print(final)

            if total == final:
              print("Awesome, let's hack more!!")

            else:
              print("You are dumb!!")

          elif select == "5":
            os.system("clear")
            back()

          else:
            print("You typed a wrong number... exiting...")

      elif options2 == "2":
          print("Hello SHS swag kid, can you tell me more about yourself?")
          print("yes/no ")

          entry = input("> ")

          if entry == "yes":
            print("Thank you for admitting to this!")
            name = input("What is you name? > ")
            age = input(int(f"Hi {name}, How old are you? > "))
            color = input("what is your favorite color? > ")
            course = input("what course do you offer? > ")
            form = input(int("Enter your form here? > "))
            fav_uni = input("Enter your favorite university? > ")

            print("Thank You {} for answering. We now know you are {} years old".format(name, age))
            print("""Also your favorite color is {}. {} is the course you offer while
            you are in form {} and your favorite university is {}""".format(color, course, form, fav_uni))
            print(f"We hope you get admission to {fav_uni}")

          elif entry == "no":
            print("Its unfortunate you can't make it. Thanks for your time!!")

          else:
            print("WRONG ENTRY!!!")

      elif options2 == "3":
          print("""1. Koforidua Technical University
            2. University of Ghana
            3. University of Cape Coast
            4. KNUST""")

          print("Select the University you attend > ", end=" ")
          choose = input()

          if choose == "1":
            print("You lucky to be admitted!")

          elif choose == "2":
            print("Leg fuo ne guyguy")

          elif choose == "3":
            print("The math alone...")

          elif choose == "4":
            print("The technicians of Kumasi")

          else:
            print("Please type the write thing!!!")

      else:
          os.system("clear")
          start()

    back()

  elif options == "2":
    print("hi")

  elif options == "3":
    print("hello")

  elif options == "4":
    os.system("clear")
    print("Are you sure you want to quit?")
    print("1. Yes\n2. No\n>", end=" ")
    enter = input()
    try:
      if enter == "1":
        print("Thanks for using this game!")
        os.system("exit")

      else:
        os.system("clear")
        start()

    except:
      print("quitting...")


  else:
    print("you are wrong")

start()



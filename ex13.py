from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#WYSS
prompt = "> "
print("Enter your name ")
input(prompt)

print("Enter your age ", end= "> ")
entry = int(input())

enter = input("Enter your surname > ")
print(enter)

print(f"Hello my name is James {enter}")
print("I am {} years old".format(entry))

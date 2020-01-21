from sys import argv # importing modules or packages

script, input_file = argv # unpacking and assigning values

# a function with a single argument
# and also reads contents
def print_all(f):
  print(f.read())

# a function with a single paramete
# this function rewind content to the beginning or default
# switches to the current position at offset
def rewind(f):
  f.seek(0)

# a function with a double argument
# in this function we print a line count on each content
def print_a_line(line_count, f):
  print(line_count, f.readline())

# we use an open function to open file objects before reading contents
current_file = open(input_file)

print("First let's print the whole file:\n") # output a simple string value

print_all(current_file) # calling a function to use the function for its purpose in line 8

print("Now let's rewind, kind of like a tape.") # output a simple string value

rewind(current_file) # calling functions initialize it tendency which rewinds contents

print("Let's print three lines:") # output a simple string value

# create a var called current_line and assigning a value to it
# after that we call the function passing parameters to it
# in other words we're passing variables as parameters
current_line = 1 # equals to 1
print_a_line(current_line, current_file)

current_line += 1 # equals to 2
print_a_line(current_line, current_file)

current_line +=  1 # equals to 3
print_a_line(current_line, current_file)

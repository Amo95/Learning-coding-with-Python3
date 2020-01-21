# line 2 through 4 simply assigns values to a variable
people = 30
cars = 40
trucks = 15
'''The ff. lines compares the boolean expressions to either True or False
then prints the branch or block of code beneath the expression if
the expression is true. Eg. line 12 compares complex expression.
The if statement is used to provide a condition to run a block of code

elif is an alternative condition to the first expression
whilst the else is a default'''
if cars > people or trucks > cars:
  print("We should take the cars.")

elif cars < people:
  print("We should not take the cars.")
else:
  print("We can't decide.")

if trucks > cars:
  print("That's cool many trucks.")
elif trucks < cars:
  print("Maybe we could take the trucks.")
else:
  print("We still can't decide.")

if people > trucks:
  print("Alright, let's just take the trucks.")
else:
  print("Fine, let's stay home then.")

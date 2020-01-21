types_of_people = 10 # we create a variable and assign a value of 10 to it
x = f"There are {types_of_people} types of people." # we create a variable and assigned a value involving
# a string format f"" to add variables to it

binary = "binary" # assign a string value to a var
do_not = "don't" # assign a string value to a var
y = f"Those who know {binary} and those who {do_not}." # assing the variable y with a formatted string value

print(x) # output the result of the var x
print(y) # output the result of the var y

print(f"I said: {x}") # output the ff string values and also values in the var x
print(f"I also said: '{y}'") # output the ff string values and also values in the var y

hilarious = False # assign a boolean value to the var hilarious
joke_evaluation = "Isn't that joke so funny?! {}" # assign values in the ff var and with a template {}

print(joke_evaluation.format(hilarious)) # using another form of string format .format(), we can run variables within a print function (output)

w = "This is the left side of ..." # assign a string value to a var w
e = "a string with a right side." # assign a string value to a var e

print(w + e) # concatenate the values in the variables w and e NOTE: can also use ',' comma
print("This is the left side of ..." + "a string with a right side.")
print("This is the left side of ...", "a string with a right side.")

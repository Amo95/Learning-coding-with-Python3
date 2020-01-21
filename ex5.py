name = 'Zed A. Shaw'
age = 24 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"his teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

centimeters = 2.54
conversion0 = height * centimeters
print(f"If {height} is multiplied by {centimeters} then the final value is {conversion0} cm.")

kilogram = 0.45
conversion1 = weight * kilogram
print(f"If {weight} is multiplied by {kilogram} then the final value is {conversion1} kg.")
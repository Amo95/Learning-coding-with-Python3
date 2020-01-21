ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are mot things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Songs", "Frisbee",
        "Corn", "Bnana","Girl", "Boy"]
while len(stuff) != 10:
    next_stuff = more_stuff.pop(-1)
    print("Adding: {}".format(next_stuff))
    stuff.append(next_stuff)
    print(f"There are {len(stuff)} items now.")

print(f"There we go: {stuff}")

print("Let's do some stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)
print("#".join(stuff[3:5]))

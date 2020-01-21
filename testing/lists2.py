elements = "Apple Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that")

stuff = elements.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
        "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_stuff = more_stuff.pop()
    print("Adding: ", next_stuff)
    stuff.append(next_stuff)
    print(f"There are {len(stuff)} items now.")
    
print(f"There we go: {stuff}")

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

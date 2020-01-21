elements = "James Emmanuel Godwin Gideon Joseph Jonas Joseph Nelson"
print("Wait! we need 15 elements or things in the list")

lists = elements.split(' ')
add_lists = ["Peter"," Andrew", "Albert", "Alfred", "Frederick",
        "Patrick", "Gabriel", "Michael", "Evans", "Jim", "Matthew",
        "Theophilus"]
while len(lists) != 15:
    remove_one = add_lists.pop()
    print(f"You are adding {remove_one} to you list")
    lists.append(remove_one)
   
    print(f"You have {len(lists)} here")

print(lists[1])
print(lists[-1])
print(lists.pop())
print(' '.join(lists))
print(' *'.join(lists[5:10]))

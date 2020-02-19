#!usr/bin/env python3

# using count() method
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = " ".join(aList[1:4])
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))
print("COunt for 'a' in bList: ", bList.count("a", 3, 10))

print("\n\n")
str = "this is string example....wow!!!"
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))

print(str.count('i'))
sub = 'ring'
print(str.count(sub))

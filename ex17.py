# importing libraries or modules
# i.e. from sys package or os.path package
# we import the following features argv & exists
from sys import argv
from os.path import exists

# creating, unpacking and assigning values from
# argv to the respective variables
script, from_file, to_file = argv

# using string formats on this line
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

# create a variable called 'in_file' and open and assign
# the contents in the 'from_file' to it
# then we also created an indata variable which
# reads the content of the file we just opened
# what happens here is we are reading from the source
# in order to transfer its content to our destination
in_file = open(from_file)
indata = in_file.read()

# we are still using string formatting here
# also observe a new function called 'len'
# len() prints the length of a value
print(f"The input file is {len(indata)} bytes long")

# here, we're using 'exists' function
# personally presume that this is a boolean function
# since it outputs a true or false value
# so we are trying to tell if our destination file exists?
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# this is our usual input function
# which accepts entries from users
input()

# now, we're done reading 'from_file' and also can tell
# whether the to_file exist or not, with the assumption that
# it exists, we create a variable called out_file
# this we open our to_file with the 'w' mode which represents
# write mode, hence we don't need to truncate the contents
out_file = open(to_file, 'w')
out_file.write(indata) # then we write the contents read from from_file to
# the to_file

print("Alright, all done.") # a simple print string value

# we close the following files after opening and reading to prevent the
# from running from the background
out_file.close()
in_file.close()

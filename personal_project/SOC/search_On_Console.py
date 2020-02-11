'''
name: Amo James
app: search_On_console
twitter: @hackAfrique
github: amo95
'''

# import libraries
import os, glob # glob is used to create a list of the define items in the path
import sys

# add and locate files
path = input("Enter path here>> ")
extent = input("Add extention>> ")
os.chdir(path)

# add an argument variable with condition
try: # handling error on console
    if sys.argv[1] == "print":
        # loop of the items in the list of images generated
        for file in glob.glob(f"*.{extent}"):
            print(file)

except IndexError:
    sys.stdout.write("\nan argument is missing. add \"print\"...\n")
    exit(1)

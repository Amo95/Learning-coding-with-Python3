import sys

script, filename = sys.argv
input_file = input("Reenter file name> ")

try:
    txt = open(input_file).read()
    print(txt)    

except Exception as e:
    print(" [!] unable to open input file: {0}".format(input_file))

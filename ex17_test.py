from sys import argv
from os.path import exists

script, source, destination = argv

out_file = open(source).read()
# indata = out_file.read()

print(f"Does the output file exists? {exists(destination)}")

in_file = open(destination, 'w').write(out_file)
# in_file.write(indata)

# print("Alright, all done.")

# out_file.close()
# in_file.close()

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())
txt.close()
# another way
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

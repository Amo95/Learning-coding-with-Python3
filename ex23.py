import sys # we import the package sys for additional features
# here we unpack values in sys.argv and assign them to each var in the line below
script, input_encoding, error = sys.argv

# the function main() takes three arguments
# and read a line the of the first argument
def main(language_file, encoding, errors):
  line = language_file.readline()
# we add a condition on the line var
  if line:
    # then, we call the function and pass in its three arguments
    print_line(line, encoding, errors)
    # then we return the main() as well
    return main(language_file, encoding, errors)
# we create a second function with three args
def print_line(line, encoding, errors):
  # we used a method called the strip()
  # its used to remove whitespaces character at the beginning and the end of a string
  # so what is happening here is, we remove white spaces chars in the language file
  # and also assigned the result to a variable called next_lang.
  next_lang = line.strip()
  # we create a new variable on the line called raw_bytes
  # and also deployed an encode() method
  # the encode() method is used to return the encoded version of a string.
  # on the next line we decode the encoded result using the decode() method
  raw_bytes = next_lang.encode(encoding, errors=errors)
  cooked_string = raw_bytes.decode(encoding, errors=errors)
# we print the encoded and decoded values in this line
  print(raw_bytes,"<===>", cooked_string)
# on this line we open the argument variables using the open() method
languages = open("languages.txt", encoding="utf-8")
# on this last line we call the main() function
main(languages, input_encoding, error)

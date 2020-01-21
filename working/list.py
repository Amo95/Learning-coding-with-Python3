# 10 examples of things in real life that would fit in a list.
'''
1. Menu list in in a restaurant
2. List of hairstyle at a salon
3. List of female students in class
4. List of absentees
5. List of Cards
6. List of price tags on items
7. List of Senior Secondary schools to select for placement
8. List of airtime to purchase
9. List of options to select on an ATM
10. Selection of a chapter from a content
'''
import sys, os
from os.path import exists

try:
  print("""shs placement selection list
    """.upper())

  schools = []

  while len(schools) != 5:
    entry = input(f"Enter school number {len(schools)} here > ")
    entry = entry.upper() # not necessary

    if entry == "":
      print("WARNING: No list, quitting...")
      exit(0)

    if " SHS" not in entry:
      print("""end your list with \"SHS\"!!!
        Eg. New Juabeng SHS""")

      exit(0)

    schools.append(entry)

  print("\n\"Your selected schools are:\"")
  num = ["1st", "2nd", "3rd", "4th", "5th"]
  num.reverse()

  while len(num) != 0:
    rem = num.pop()
    print(f"\n{rem} choice: {schools.pop(0)}")

except KeyboardInterrupt:
  sys.stdout.write("\nQuitting...\n")

# Usual printing to console (not necessary)
# print("\n#".join(schools[0:6]))

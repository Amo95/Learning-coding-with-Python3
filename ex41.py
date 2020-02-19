# ex41: Learning To Speak Object Oriented

import random
from urllib.request import urlopen
import sys
import subprocess

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

# WORD_URL = "http://learncodethehardway.org/words.txt"
WORD_URL = "file:///media/james/80BEBF1EBEBF0C22/Users/A.J/Desktop/programming/python3/lpthw/ex41_words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	  "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip().decode("utf-8"))

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	if sys.platform == "linux" or sys.platform == "linux2":
		subprocess.call("clear", shell=True)
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(MAGENTA + question + END)

			input("> ")
			print(RED + "ANSWER:   {}".format(answer) + END)
			print("\n\n\nPress CTRL-D to close session")

except EOFError:
	print("\nBye")

# Prints any dictionary to command line.
from dictionary import Lexicon
import argparse

ki = Lexicon()

parser = argparse.ArgumentParser(description="Print a dictionary to the command line.")
parser.add_argument("dict")
args = parser.parse_args()

ki.set_dictionary(args.dict)

for i in range(0, len(ki.dictionary)):
    print(ki.format_term(find_term(i)))
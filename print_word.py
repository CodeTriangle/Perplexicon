# Prints any dictionary to command line.
from dictionary import Lexicon
from dictionary import format_term
import argparse

ki = Lexicon()

parser = argparse.ArgumentParser(description="Print a single term's definitions to the command line.")
parser.add_argument("dict")
parser.add_argument("term")
parser.add_argument("-m", "--method", nargs=1)
args = parser.parse_args()

ki.set_dictionary(args.dict)

if args.method == None or args.method[0].lower() == "index":
    print(format_term(ki.find_term(int(args.term))))
elif args.method[0].lower() == "word":
    print(format_term(ki.find_term(args.term, "word")))
elif args.method[0].lower() == "word-part":
    terms = ki.find_term(args.term, "word-part")
    for i in range(0, len(terms)):
        print(format_term(terms[i]))
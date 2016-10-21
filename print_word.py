# Prints any dictionary to command line.
from dictionary import Lexicon
import argparse

ki = Lexicon()

parser = argparse.ArgumentParser(description="Print a single term's definitions to the command line.")
parser.add_argument("dict")
parser.add_argument("term")
parser.add_argument("-m", "--method", nargs=1)
args = parser.parse_args()

ki.set_dictionary(args.dict)

if args.method == None or args.method[0].lower() == "index":
    print(ki.format_term(ki.find_term(int(args.term))))
elif args.method[0].lower() == "word":
    print(ki.format_term(ki.find_term(args.term, "word")))
# Prints any definition to command line.
from dictionary import Lexicon
from dictionary import format_term
import argparse
import sys

ki = Lexicon()

parser = argparse.ArgumentParser(description="Print a single term's definitions to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
parser.add_argument("term", help="the term you are searching for (changes when the -m tag is active)")
parser.add_argument("-m", "--method", nargs=1, help="the search method to be used. 'index' searches in the lexicon for a numerical index corresponding to where it is placed. 'word' shows the word called whatever query is. 'word-part is a list of all words that contain query.")
args = parser.parse_args()

ki.set_dictionary(args.lex)

try:
    if args.method == None or args.method[0].lower() == "word-part":
        terms = ki.find_term(args.term, "word-part")
        for i in range(0, len(terms)):
            print(format_term(terms[i]))
    elif args.method[0].lower() == "word":
        print(format_term(ki.find_term(args.term, "word")))
    elif args.method[0].lower() == "index":
        print(format_term(ki.find_term(int(args.term))))
except TypeError:
    print("TypeError: No definition found for '%s'" % (args.term))
    sys.exit()
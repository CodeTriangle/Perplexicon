# Prints any lexicon to command line.
import lexicon
import template
import argparse

ki = lexicon.Lexicon()

parser = argparse.ArgumentParser(description="Print an entire lexicon or a single term's definitions to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
parser.add_argument("-q", "--query", nargs=1, help="allows you to enter a query to search. Type the term you are searching for.")
parser.add_argument("-m", "--method", nargs=1, help="the search method to use.", choices=["index","term","term-part"])
args = parser.parse_args()

ki.set_lexicon_file(args.lex)

if args.query == None:
    for i in range(0, len(ki.lexicon)):
        print(lexicon.format_term(ki.find_term(i)))
else:
    if args.method == None or args.method[0].lower() == "term-part":
        terms = ki.find_term(args.query[0], "term-part")
        for i in range(0, len(terms)):
            print(lexicon.format_term(terms[i]))
    elif args.method[0].lower() == "term":
        print(lexicon.format_term(ki.find_term(args.query[0], "term")))
    elif args.method[0].lower() == "index":
        print(lexicon.format_term(ki.find_term(int(args.query[0]))))
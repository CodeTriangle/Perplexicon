# Prints any dictionary to command line.
import dictionary
import template
import argparse

ki = dictionary.Lexicon()

parser = argparse.ArgumentParser(description="Print an entire lexicon or a single term's definitions to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
parser.add_argument("-q", "--query", nargs=1, help="allows you to enter a query to search. Type the term you are searching for.")
parser.add_argument("-m", "--method", nargs=1, help="the search method to use.", choices=["index","word","word-part"])
args = parser.parse_args()

ki.set_dictionary(args.lex)

if args.query == None:
    for i in range(0, len(ki.dictionary)):
        print(dictionary.format_term(ki.find_term(i)))
else:
    if args.method == None or args.method[0].lower() == "word-part":
        terms = ki.find_term(args.query[0], "word-part")
        for i in range(0, len(terms)):
            print(dictionary.format_term(terms[i]))
    elif args.method[0].lower() == "word":
        print(dictionary.format_term(ki.find_term(args.query[0], "word")))
    elif args.method[0].lower() == "index":
        print(dictionary.format_term(ki.find_term(int(args.query[0]))))
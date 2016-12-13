# Prints any lexicon to command line.
import lexicon
from template import *
import argparse
import sys

lx = lexicon.Lexicon()

parser = argparse.ArgumentParser(description="Print an entire lexicon or a single term's definitions to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
parser.add_argument("-q", "--query", nargs=1, help="allows you to enter a query to search. Type the term you are searching for.")
parser.add_argument("-m", "--method", nargs=1, help="the search method to use.", choices=["index", "term", "term-part"])
parser.add_argument("-t", "--template", nargs=1, help="which template to use.", choices=["normal", "multiline", "html"])
parser.add_argument("-o", "--output", nargs=1, help="file to output to.")
args = parser.parse_args()

lx.set_lexicon_file(args.lex)

fl = "";

if args.query == None:
    for i in range(0, len(l.lexicon)):
        if args.template != None:
            fl = fl + lexicon.format_term(lx.find_term(i), temp=template_list[args.template[0]])
        else:
            fl = fl + print(lexicon.format_term(lx.find_term(i))
else:
    if args.method == None or args.method[0].lower() == "term-part":
        terms = lx.find_term(args.query[0], "term-part")
        for i in range(0, len(terms)):
            fl = fl + lexicon.format_term(terms[i])
    elif args.method[0].lower() == "term":
        fl = fl + lexicon.format_term(lx.find_term(args.query[0], "term"))
    elif args.method[0].lower() == "index":
        fl = fl + lexicon.format_term(lx.find_term(int(args.query[0])))
    else:
        print("Invalid search method")
        sys.exit()
if args.output == None:
    print(fl)
else:
    f = open(args.output[0], "w")
    f.write(fl)
    f.close()

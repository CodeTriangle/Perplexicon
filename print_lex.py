# Prints any lexicon to command line.
from lexicon import *
from template import *
import argparse
import sys

lx = lexicon()

parser = argparse.ArgumentParser(description="Print an entire lexicon or a single term's definitions to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
parser.add_argument("-q", "--query", nargs=1, help="allows you to enter a query to search. Type the term you are searching for.")
parser.add_argument("-m", "--method", nargs=1, help="the search method to use.", choices=["index", "term", "term-part"])
parser.add_argument("-t", "--template", nargs=1, help="which template to use.", default=["default"])
parser.add_argument("-o", "--output", nargs=1, help="file to output to.")
args = parser.parse_args()

lx.set_lexicon_file(args.lex)

fl = "";

if args.query == None:
    for i in range(0, len(lx.lexicon["terms"])):
        fl = fl + lx.get_formatted_term(i, "index", temp=template_list[args.template[0]])
else:
    if args.method == None or args.method[0].lower() == "term-part":
        terms = lx.find_term(args.query[0], "term-part", temp=template_list[args.template[0]])
        for i in terms:
            fl = fl + lx.format_term(i)
    elif args.method[0].lower() == "term":
        fl = lx.get_formatted_term(lx.find_term(args.query[0], "term", temp=template_list[args.template[0]]))
    elif args.method[0].lower() == "index":
        fl = lx.format_term(lx.find_term(int(args.query[0]), "index"), temp=template_list[args.template[0]])
    else:
        print("Invalid search method")
        sys.exit()

if args.output == None:
    print(fl)
else:
    f = open(args.output[0], "w")
    f.write(fl)
    f.close()
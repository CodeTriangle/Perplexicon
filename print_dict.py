# Prints any dictionary to command line.
import dictionary
import template
import argparse

ki = dictionary.Lexicon()

parser = argparse.ArgumentParser(description="Print a dictionary to the command line.")
parser.add_argument("lex", help="the lexicon file that should be used (pass a valid JSON filename).")
args = parser.parse_args()

ki.set_dictionary(args.lex)

for i in range(0, len(ki.dictionary)):
    print(dictionary.format_term(ki.find_term(i)))
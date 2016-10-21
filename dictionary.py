import json
import sys

# Class that handles most of the dictionary stuff.
class Lexicon:
    def set_dictionary(self, filename="dictionary.json"):
        try:
            f = open(filename)
            self.dictionary = json.load(f)
            f.close()
        except IOError:
            print("IOError: Lexicon file can't be read")
            sys.exit()

    def find_term(self, query, method="index"):
        if method == "index":
            return self.dictionary[query]
        elif method == "word":
            for i in self.dictionary:
                if i[0] == query:
                    return i
            return None
        elif method == "word-part":
            results = []
            for i in self.dictionary:
                if i[0].find(query) != -1:
                    results.append(i)
            return results
            
def format_term(term):
    ret = str(term[0]) + " -- "
    for i in range(1, len(term)):
        ret += "(" + (term[i][0]) + ") "
        for j in range(1, len(term[i])):
            ret += str(j) + ". " + term[i][j] + " "
    return ret
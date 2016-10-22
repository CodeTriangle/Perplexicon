from template import Template
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
            
def format_term(term, temp=Template()):
    ret = temp.before_term + str(term[0]) + temp.before_defs
    for i in range(1, len(term)):
        ret += temp.before_pos + (term[i][0]) + temp.before_list
        for j in range(1, len(term[i])):
            if temp.use_numbers == True:
                ret += str(j)
            ret += temp.before_def + term[i][j] + temp.after_def
        ret += temp.after_list
    ret += temp.after
    return ret
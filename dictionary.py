import json

# Class that handles most of the dictionary stuff.
class Lexicon:
    def set_dictionary(self, filename="dictionary.json"):
        f = open(filename)
        self.dictionary = json.load(f)
        f.close()

    def find_term(self, term, method="index"):
        if method == "index":
            return self.dictionary[term]
        elif method == "word":
            for i in self.dictionary:
                if i[0] == term:
                    return i
            return None
            
    def format_term(self, term):
        ret = str(term[0]) + " -- "
        for i in range(1, len(term)):
            ret += "(" + (term[i][0]) + ") "
            for j in range(1, len(term[i])):
                ret += str(j) + ". " + term[i][j] + " "
        return ret
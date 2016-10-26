from template import Template
import json
import sys

# Class that handles most of the dictionary stuff.
class Lexicon:
    # Set which file a Lexicon object will read from.
    def set_lexicon_file(self, filename):
        # Open requested lexicon file.
        try:
            f = open(filename)
            self.lexicon = json.load(f)
            f.close()
        # Throw error if file doesn't exist.
        except IOError:
            print("IOError: Lexicon file can't be read")
            sys.exit()
            
    # Find a specific term and its definitions utilizing different methods
    def find_term(self, query, method="index"):
        try:
            # Return one term using a list index.
            if method == "index":
                return self.lexicon[query]
            # Return one term with query's value.
            elif method == "term":
                for i in self.lexicon:
                    if i[0] == query:
                        return i
                return None
            # Return all terms where the term contains the query's value.
            elif method == "term-part":
                results = []
                for i in self.lexicon:
                    if i[0].find(query) != -1:
                        results.append(i)
                return results
        # Throw error if definition not found.
        except TypeError:
            print("TypeError: No definition found for '%s'" % (args.term))
            sys.exit()
            
# Format a term list into something readable.
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
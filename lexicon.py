from template import *
import json
import sys

# Class that handles most of the dictionary stuff.
class lexicon:
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

    def pos_abbr(self, query):
        ret = query
        for i in self.lexicon["poses"]:
            if i["pos"] == query:
                ret = i["abbr"]
        return ret
            
    # Find a specific term and its definitions utilizing different methods
    def find_term(self, query, method):
        try:
            # Return one term using a list index.
            if method == "index":
                return self.lexicon["terms"][query]
            # Return one term with query's value.
            elif method == "term":
                for i in self.lexicon["terms"]:
                    if i["term"] == query:
                        return i
                return None
            # Return all terms where the term contains the query's value.
            elif method == "term-part":
                results = []
                for i in self.lexicon["terms"]:
                    if i["term"].find(query) != -1:
                        results.append(i)
                return results
        # Throw error if definition not found.
        except TypeError:
            print("TypeError: No definition found for '%s'" % (query))
            sys.exit()

    # Format a term list into something readable.
    def format_term(self, term, temp="default"):
        if str(type(temp)) == "<class 'str'>":
            template = template_list[temp]
        elif str(type(temp)) == "<class 'template.template'>":
            template = temp
        ret = template.before_term + str(term["term"]) + template.before_defs
        for i in range(0, len(term["defs"])):
            ret += template.before_pos + (self.pos_abbr(term["defs"][i][0])) + template.before_list
            for j in range(1, len(term["defs"][i])):
                if template.use_numbers == True:
                    ret += str(j)
                ret += template.before_def + term["defs"][i][j] + template.after_def
            ret += template.after_list
        ret += template.after
        return ret

    def get_formatted_term(self, query, method, temp="default"):
        return self.format_term(self.find_term(query, method), temp=temp)
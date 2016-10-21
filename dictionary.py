import json

class Dictionary:
    def set_dictionary(self, filename="dictionary.json"):
        f = open(filename)
        self.dictionary = json.load(f)
        f.close()

    def find_term(self, term, method="index"):
        return self.dictionary[term]

    def format_term(self, term):
        data = self.find_term(term)
        ret = str(data[0]) + " -- "
        for i in range(1, len(data)):
            ret += "(" + (data[i][0]) + ") "
            for j in range(1, len(data[i])):
                ret += str(j) + ". " + data[i][j] + " "
        return ret
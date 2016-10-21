import json

f = open("dictionary.json")
words = json.load(f)
f.close()

def get_defs(idx):
  data = words[idx]
  ret = str(data[0]) + " -- "
  for i in range(1, len(data)):
    ret += "(" + (data[i][0]) + ") "
    for j in range(1, len(data[i])):
      ret += str(j) + ". " + data[i][j] + " "
  return ret
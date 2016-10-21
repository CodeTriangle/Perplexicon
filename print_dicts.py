# Prints Ki*iul dictionary to command line.

from dictionary import Dictionary

ki = Dictionary()

ki.set_dictionary("kiiul.json")

for i in range(0, len(ki.dictionary)):
  print(ki.format_term(i))
# Perplexicon

*Perplex*icon / Perp*lexicon*

A simple but capable system for making conlang lexicons. 

The way Perplexicon will function is so easy that anyone could figure it out. Simply update a single JSON file with new words and you will immediately be able to export them to as many filetypes as you want.

## Implimented Features:

- [x] Ability to specify more than one definition and part of speech for a word/term.
- [x] Command line interface for opening lexicons.
- [x] Command line interface for looking up certain definitions.
- [x] Messy Python code!

## Planned Features:

- [ ] Command line interface for editing lexicons.
- [ ] Graphical interface for opening and editing lexicons.
- [ ] Multiple styles for definitions.
- [ ] Export to multiple formats.
- [ ] Clean Python code!

## How It Works

I'll have a better documentation later, but for now, here's how it works.

### Lexicon Files

You'll need to make yourself a lexicon file. The way you do this is by copying this simple template:

    [
        ["term 1", ["part of speech 1", "definition 1", "definition 2"], ["part of speech 2", "definition 3", "definition 4"]],
        ["term 2", ["part of speech 1", "definition 1", "definition 2"], ["part of speech 2", "definition 3", "definition 4"]]
    ]

If the term can't function as more than one part of speech, get rid of the second chunk. If it has five parts of speech that it can function as, add a few more blocks. If the term only has one definition, get rid of one of them. If it has ten, add more. It's super easy to make a lexicon file that is both readable and extensible.

### Command Line

Open up a command window in your working directory. Different parameters change what happens.

| You type: | What happens: |
|--|--|
| `python print_dict.py` | Error telling you that you need a lexicon file. |
| `python print_dict.py lexicon.json` | Prints every entry in lexicon.json. |
| `python print_dict.py lexicon -q uk` | Prints every entry in lexicon.json where the term contains "uk". |
| `python print_dict.py lexicon -q uk -m word` | Prints the entry in lexicon.json that the term is "uk". |
| `python print_dict.py lexicon -q 1 -m index` | Prints the entry that is found in lexicon.json at that index. |
| `python print_dict.py lexicon -q uk -m word-part` | Prints every entry in lexicon.json where the term contains "uk" |

That's basically everything you need to know for Perplexicon.
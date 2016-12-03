# Perplexicon

*Perplex*icon / Perp*lexicon*

A simple but capable system for making conlang lexicons. 

## What Makes it Special

The way Perplexicon will function is so easy that anyone could figure it out. Simply update a single YAML file with new words and you will immediately be able to export them to as many filetypes as you want. Perplexicon is built with languages where one word can function as multiple parts of speech and/or has different meanings in different contexts in mind, but that doesn't have to be the case -- Perplexicon works just as well with languages where there is one word for every meaning.

I have included two sample lexicons from conlangs I've made before. Sajem Tan ([sajem_tan.yaml](https://github.com/CodeTriangle/Perplexicon/blob/master/sajem_tan.yaml)) is a language that has all of the traits listed above. In this dictionary are three words that have several different definitions. Some of them need context to make sense due to them being inside jokes, but it's really just a technical demo to test whether the multiple definitions system works. Ki\*iul ([kiiul.yaml](https://github.com/CodeTriangle/Perplexicon/blob/master/kiiul.yaml)) is a language where none of these features apply. It's just to show that it works with languages that have one definition per word too.

## Dependencies

You'll need `ruamel.yaml` to parse YAML files. 

    pip install ruamel.yaml

## Implemented Features:

- [x] Ability to specify more than one definition and part of speech for a word/term.
- [x] Command line interface for opening lexicons.
- [x] Command line interface for looking up certain definitions.
- [x] Multiple styles for definitions.
- [x] Messy Python code!

## Planned Features:

- [ ] Command line interface for editing lexicons.
- [ ] Graphical interface for opening and editing lexicons.
- [ ] IPA Support
- [ ] Export to multiple formats.
- [ ] Clean Python code!

## How It Works

I'll have a better documentation later, but for now, here's how it works.

### Lexicon Files

You'll need to make yourself a lexicon file. The way you do this is by copying this simple template:

    - term: <TERM>
      ipa: <IPA TRANSCRIPTION>
      defs:
      - - <PART OF SPEECH 1>
        - <DEFINITION 1>
        - <DEFINITION 2>
      - - <PART OF SPEECH 2>
        - <DEFINITION 3>
        - <DEFINITION 4>

If the term can't function as more than one part of speech, get rid of the second chunk. If it has five parts of speech that it can function as, add a few more blocks. If the term only has one definition, get rid of one of them. If it has ten, add more. It's super easy to make a lexicon file that is both readable and extensible.

### Command Line

Open up a command window in your working directory. Different parameters change what happens.

| You type: | What happens: |
|-----------|---------------|
| `python print_lex.py` | Error telling you that you need a lexicon file. |
| `python print_lex.py lexicon.yaml` | Prints every entry in lexicon.json. |
| `python print_lex.py lexicon.yaml -q uk` | Prints every entry in lexicon.json where the term contains "uk". |
| `python print_lex.py lexicon.yaml -q uk -m word` | Prints the entry in lexicon.json that the term is "uk". |
| `python print_lex.py lexicon.yaml -q 1 -m index` | Prints the entry that is found in lexicon.json at that index. |
| `python print_lex.py lexicon.yaml -q uk -m word-part` | Prints every entry in lexicon.json where the term contains "uk". |
| `python print_lex.py lexicon.yaml -q uk -m word-part -t html` | Prints every entry in lexicon.json where the term contains "uk" using template HTML. |

That's basically everything you need to know for Perplexicon.

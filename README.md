*Perplex*icon / Perp*lexicon*

A simple but capable system for making conlang lexicons. 

# What Makes it Special

The way Perplexicon will function is so easy that anyone could figure it out. Simply update a single JSON file with new words and you will immediately be able to export them to as many filetypes as you want. Perplexicon is built with languages where one word can function as multiple parts of speech and/or has different meanings in different contexts in mind, but that doesn't have to be the case -- Perplexicon works just as well with languages where there is one word for every meaning.

I have included two sample lexicons from conlangs I've made before. Sajem Tan ([sajem_tan.json](https://github.com/CodeTriangle/Perplexicon/blob/master/sajem_tan.json)) is a language that has all of the traits listed above. In this dictionary are three words that have several different definitions. Some of them need context to make sense due to them being inside jokes, but it's really just a technical demo to test whether the multiple definitions system works. Ki\*iul ([kiiul.json](https://github.com/CodeTriangle/Perplexicon/blob/master/kiiul.json)) is a language where none of these features apply. It's just to show that it works with languages that have one definition per word too.

# List of Features:

- [x] Ability to specify more than one definition and part of speech for a word/term
- [x] Command line interface
    - [x] Opens lexicons
    - [x] Looks up certain definitions
    - [ ] Edits lexicons
    - [x] Outputs to file
- [ ] Graphical interface
- [x] Multiple styles for definitions
- [x] Abbreviations for parts of speech
- [ ] Alphabetizing lexicons
- [ ] IPA Support
- [ ] Clean Python code

# How It Works

I'll have a better documentation later, but for now, here's how it works.

## Lexicon Files

You'll need to make yourself a lexicon file. The way you do this is by copying this simple template:

    {
        "poses": [

        ]
        "terms": [

        ]
    }

### Adding Parts of Speech

Within the `pos` array, you can define different parts of speech and how to abbreviate them. For each part of speech add:

    {"pos": "PART OF SPEECH", "abbr": "ABBREVIATION"}

For example, if you want to abbreviate "noun" to "n.", type:

    {"pos": "noun", "abbr": "n."}

### Adding Terms

Terms are any morpheme that can be used. Put these in the `terms` array. Add:

    {"term":"TERM", "defs":[["PART OF SPEECH 1", "DEFINITION 1", "DEFINITION 2"], ["PART OF SPEECH 2", "DEFINITION 3", "DEFINITION 4"]]}

If the term can't function as more than one part of speech, get rid of the second chunk. If it has five parts of speech that it can function as, add a few more blocks. If the term only has one definition, get rid of one of them. If it has ten, add more. It's super easy to make a lexicon file that is both readable and extensible.

For example, if [*parecer*](http://www.spanishdict.com/translate/parecer) is the verb for "to seem", you'd add this:

    {"term":"parecer", "defs":[["verb", "to seem"]]}

But, if it can also mean "to look" and "to appear" you would add them as such.

   {"term":"parecer", "defs":[["verb", "to seem", "to look", "to appear"]]}

If it can also be used to mean "opinion", then:

   {"term":"parecer", "defs":[["verb", "to seem", "to look", "to appear"], ["noun", "opinion"]]}

## Command Line

Open up a command window in your working directory. Different parameters change what happens.

| You type: | What happens: |
|-----------|---------------|
| `python print_lex.py` | Error telling you that you need a lexicon file. |
| `python print_lex.py lexicon.json` | Prints every entry in lexicon.json. |
| `python print_lex.py lexicon.json -q uk` | Prints every entry in lexicon.json where the term contains "uk". |
| `python print_lex.py lexicon.json -q uk -m term` | Prints the entry in lexicon.json that the term is "uk" (See [Search Methods](#search-methods) below. |
| `python print_lex.py lexicon.json -t html` | Prints every entry in lexicon.json using template HTML (See [Templates](#templates) below. |
| `python print_lex.py lexicon.json -o output.txt` | Prints every entry in lexicon.json to the file output.txt |

## Search Methods

When searching for specific terms, there are different ways to get that information.

| Method | Explanation |
|--------|-------------|
| `term` | Returns the entry where the term *exactly* matches the query. |
| `index` | Returns the entry at the specified position. |
| `term-part` | Returns any entry where the term contains the query. |

## Templates

Perplexicon comes with several different templates from which to choose. These have no functional purpose, but they are useful when exporting to other filetypes.

| Template | Explanation |
|----------|-------------|
| `default` | Completely normal template. |
| `html` | Adds HTML tags to the default template. |
| `latex` | Uses same styling as `html`, but for LaTeX. |
| `multiline` | Prints each definition on a separate line. |
| `multiline-html` | Prints each definition on a separate line in HTML. |
| `webster` | Built to mimic the style Merriam-Webster uses for their dictionaries. |
| `webster-html` | Like `webster` but with HTML tags. |
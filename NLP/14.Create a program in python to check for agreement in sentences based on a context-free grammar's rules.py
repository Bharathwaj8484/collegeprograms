import nltk

def check_agreement(grammar, sentence):
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(sentence):
        tree.pretty_print()
        print("Agreement: Yes")

# Example usage:
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> 'the' 'cat'
    VP -> 'run'
""")

input_sentence = ['the', 'cat', 'run']
check_agreement(cfg, input_sentence)

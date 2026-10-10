import nltk
def earley_parser(grammar, sentence):
    parser = nltk.EarleyChartParser(grammar)
    for tree in parser.parse(sentence):
        tree.pretty_print()
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> 'the' 'cat'
    VP -> 'runs'
""")
sentence = ['the', 'cat', 'runs']
earley_parser(cfg, sentence)

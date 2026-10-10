import nltk
def top_down_parser(grammar, sentence):
    parser = nltk.ChartParser(grammar)
    
    for tree in parser.parse(sentence):
        
        tree.pretty_print()
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> 'the' 'cat'
    VP -> 'runs'
""")
input_sentence = ['the', 'cat', 'runs']
top_down_parser(cfg, input_sentence)

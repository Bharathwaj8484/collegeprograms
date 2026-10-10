import nltk

def pcfg_parser(grammar, sentence):
    parser = nltk.ViterbiParser(grammar)
    for tree, prob in parser.parse(sentence):
        print("Probability:", prob)
        tree.pretty_print()

# Example usage:
pcfg = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> 'the' 'cat' [0.7] | 'a' 'dog' [0.3]
    VP -> 'runs' [0.5] | 'jumps' [0.5]
""")

input_sentence = ['the', 'cat', 'runs']
pcfg_parser(pcfg, input_sentence)

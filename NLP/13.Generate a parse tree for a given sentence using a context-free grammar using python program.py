import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> 'John'
    VP -> V NP
    V -> 'likes'
    NP -> 'pizza'
""")
parser = nltk.ChartParser(grammar)
text = "John likes pizza"
for tree in parser.parse(text.split()):
    tree.pretty_print()

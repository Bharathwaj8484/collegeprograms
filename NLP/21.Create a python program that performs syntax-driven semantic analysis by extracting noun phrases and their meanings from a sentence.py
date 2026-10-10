from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
def extract_noun_phrases(sentence):
    return [(word, get_word_meaning(word)) for word, pos in pos_tag(word_tokenize(sentence)) if pos.startswith('NN')]
def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    return synsets[0].definition() if synsets else "No meaning found"
sentence = "The cat are playing in the garden."
noun_phrases = extract_noun_phrases(sentence)
print("Noun Phrases and Meanings:", noun_phrases)

from nltk.corpus import wordnet

def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    for synset in synsets:
        print(f"Synset: {synset.name()}, Definition: {synset.definition()}")

# Example usage:
word_to_explore = "happy"
explore_word_meanings(word_to_explore)

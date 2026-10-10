from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
def lesk_algorithm(sentence, target_word):
    tokens = word_tokenize(sentence)
    sense = lesk(tokens, target_word)
    if sense:
        return sense.definition()
    else:
        return "No sense found."
sentence = "The bank is on the river bank."
target_word = "bank"
result = lesk_algorithm(sentence, target_word)
print(result)

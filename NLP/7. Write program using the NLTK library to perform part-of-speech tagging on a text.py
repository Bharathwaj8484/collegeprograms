import nltk
from nltk import pos_tag, word_tokenize
text = "NLTK is a powerful library for natural language processing."
words = word_tokenize(text)
tagged_words = pos_tag(words)
print("Original Text:", text)
print("Part-of-Speech Tagging Result:", tagged_words)

from nltk import pos_tag, word_tokenize
text = "This is a simple stochastic POS tagging example."
words = word_tokenize(text)
tagged_words = pos_tag(words)
print("Original Text:", text)
print("Part-of-Speech Tagging Result:", tagged_words)

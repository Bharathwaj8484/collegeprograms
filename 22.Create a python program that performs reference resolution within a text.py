import nltk
from nltk import pos_tag, word_tokenize

def resolve_references(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    resolved_sentence = []

    for word, pos in tagged_words:
        if pos == 'PRP':
            resolved_sentence.append('he' if word.lower() == 'it' else 'she')
        else:
            resolved_sentence.append(word)

    return ' '.join(resolved_sentence)

# Example sentence
sentence = "The cat is chasing the mouse. It is very fast."

# Resolve references
resolved_sentence = resolve_references(sentence)

# Print results
print("Original Sentence:", sentence)
print("Resolved Sentence:", resolved_sentence)

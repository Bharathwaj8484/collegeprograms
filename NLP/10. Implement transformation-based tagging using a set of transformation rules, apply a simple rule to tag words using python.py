import nltk
def transform_based_tagging(text):
    words = nltk.word_tokenize(text)
    tags = nltk.pos_tag(words)
    return tags
text =  "NLTK is a powerful library for natural language processing."
transformed_tags = transform_based_tagging(text)
print(transformed_tags)

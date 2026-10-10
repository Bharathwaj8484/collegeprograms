from nltk.stem import PorterStemmer
text = "Running and played are both verb forms of the word run and play."
words = text.split()
ps = PorterStemmer()
stemed =[ps.stem(word) for word in words]
print("Original Text:")
print(text)
print("\nMorphological Analysis:")
print(stemed)

from nltk.stem import PorterStemmer
words = ["running", "jumps", "happily", "dogs", "cats", "better"]
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stemmed)

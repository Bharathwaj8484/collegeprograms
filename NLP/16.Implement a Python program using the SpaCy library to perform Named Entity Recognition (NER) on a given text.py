import spacy
text = "Apple is looking at buying U.K. startup for $1 billion"
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
for ent in doc.ents:
    print(f"Entity: {ent.text}, Type: {ent.label_}")


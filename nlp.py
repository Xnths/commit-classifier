import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love designing and building software")

for token in doc:
    print(token.text, token.pos_)

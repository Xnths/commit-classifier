import spacy

try:
    spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError(
        "spaCy model not found. Run: python -m spacy download en_core_web_sm"
    )


nlp = spacy.load("en_core_web_sm")
doc = nlp("I love designing and building software")

for token in doc:
    print(token.text, token.pos_)

import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

def extract_concepts(text: str):
    doc = nlp(text)
    concepts = set()
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN']:
            concepts.add(token.lemma_.lower())
            
    return list(concepts)
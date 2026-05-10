import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

def clean_phrase(phrase: str) -> str:
    phrase = phrase.lower().strip()
    
    removable_words = {"the", "a", "an", "this", "that", "these", "those", "strong", "weak", "potential", "reported"}
    
    words = [word for word in phrase.split() if word not in removable_words]
    return ' '.join(words).strip()

def extract_concepts(text: str):
    doc = nlp(text)
    concepts = set()
    
    # Extract noun chunks first, because these capture multi-word concepts
    for chunk in doc.noun_chunks:
        phrase = clean_phrase(chunk.text)
        if phrase and len(phrase.split()) <= 4:  # Limit to reasonably short phrases
            concepts.add(phrase)
    
    # Add important single-word nouns as fallback
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN']:
            lemma = token.lemma_.lower().strip()
            
            if len(lemma) > 2:  # Filter out very short words
                concepts.add(lemma)
                
    return list(concepts)

# extracts complex terms like "profit growth", "inflation risk", -> keeps single terms like "profit", "growth", "risk"
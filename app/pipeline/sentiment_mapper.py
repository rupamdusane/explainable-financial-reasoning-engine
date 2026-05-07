from app.knowledge.concept_polarity import CONCEPT_POLARITY

def map_sentiment(concepts):
    results = []
    
    for c in concepts:
        polarity = CONCEPT_POLARITY.get(c, 0.0)
        is_known = c in CONCEPT_POLARITY
        
        results.append({
            "term": c,
            "polarity": polarity,
            "known_concept": is_known,
        })
        
    return results
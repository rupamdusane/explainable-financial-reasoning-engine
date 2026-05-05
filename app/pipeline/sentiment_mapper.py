from app.knowledge.concept_polarity import CONCEPT_POLARITY

def map_sentiment(concepts):
    results = []
    
    for c in concepts:
        polarity = CONCEPT_POLARITY.get(c, 0.0)
        
        results.append({
            "term": c,
            "polarity": polarity
        })
        
    return results
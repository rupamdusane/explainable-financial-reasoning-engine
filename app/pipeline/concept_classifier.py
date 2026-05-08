# Here, it adds categories to each concept.

from app.knowledge.concept_categories import CONCEPT_CATEGORIES

def classify_concepts(sentiment_data):
    classified = []
    
    for item in sentiment_data:
        term = item["term"]
        category = CONCEPT_CATEGORIES.get(term, "unknown")
        
        item["category"] = category
        classified.append(item)
        
    return classified
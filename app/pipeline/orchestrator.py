from app.pipeline.concept_extractor import extract_concepts
from app.pipeline.sentiment_mapper import map_sentiment


def analyze_text(text: str):
    # Step 1: Extract concepts
    concepts = extract_concepts(text)
    
    # Step 2: Map concepts to sentiment
    sentiment_data = map_sentiment(concepts)
    
    # Step 3: Calculate overall sentiment
    if sentiment_data:
        overall = sum([c['polarity'] for c in sentiment_data]) / len(sentiment_data)
    else:
        overall = 0.0
           
    return {
        "original_text": text,
        "concepts": sentiment_data,
        "overall_sentiment": overall,
    }
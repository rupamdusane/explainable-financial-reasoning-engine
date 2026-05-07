from app.pipeline.concept_extractor import extract_concepts
from app.pipeline.sentiment_mapper import map_sentiment


def analyze_text(text: str):
    # Step 1: Extract concepts
    concepts = extract_concepts(text)
    
    # Step 2: Map concepts to sentiment
    sentiment_data = map_sentiment(concepts)
    
    known_concepts = [c for c in sentiment_data if c["known_concept"]]
    
    # Step 3: Calculate overall sentiment
    if known_concepts:
        overall = sum([c['polarity'] for c in known_concepts]) / len(known_concepts)
    else:
        overall = 0.0
        
    if overall > 0.2:
        sentiment_label = "positive"
        market_signal = "bullish"
    elif overall < -0.2:
        sentiment_label = "negative"
        market_signal = "bearish"
    else:
        sentiment_label = "mixed"
        market_signal = "uncertain"
           
    return {
        "original_text": text,
        "concepts": sentiment_data,
        "overall_sentiment": round(overall, 3),
        "sentiment_label": sentiment_label,
        "market_signal": market_signal
    }
    
from app.pipeline.concept_extractor import extract_concepts
from app.pipeline.sentiment_mapper import map_sentiment
from app.pipeline.concept_classifier import classify_concepts
from app.pipeline.interaction_engine import detect_interactions
from app.pipeline.reasoning_engine import build_reasoning
from app.pipeline.summary_generator import generate_summary
from app.pipeline.concept_normalizer import normalize_concepts


def analyze_text(text: str):
    # Step 1: Extract raw concepts
    raw_concepts = extract_concepts(text)
    
    # Step 2: Normalize concepts
    concepts = normalize_concepts(raw_concepts)
    
    # Step 3: Map polarity to concepts
    sentiment_data = map_sentiment(concepts)
    
    # Step 4: Add concept categories
    classified_concepts = classify_concepts(sentiment_data)
    
    # Step 5: Use only known concepts for base score
    known_concepts = [c for c in classified_concepts if c["known_concept"]]
    
    if known_concepts:
        base_score = sum([c['polarity'] for c in known_concepts]) / len(known_concepts)
    else:
        base_score = 0.0
        
    # Step 6: Detect interactions between concepts
    interactions = detect_interactions(classified_concepts)
    
    # Step 7: Add interaction effect
    interaction_score = sum(item["weight"] for item in interactions)
    
    final_score = base_score + interaction_score

    # Step 8: Decide final label
    if final_score > 0.2:
        sentiment_label = "positive"
        market_signal = "bullish"
    elif final_score < -0.2:
        sentiment_label = "negative"
        market_signal = "bearish"
    else:
        sentiment_label = "mixed"
        market_signal = "uncertain"
        
    # Step 9: Build reasoning path
    reasoning_path = build_reasoning(classified_concepts, interactions)
    
    # Step 10: Generate summary
    summary = generate_summary(
        sentiment_label,
        market_signal,
        classified_concepts,
        interactions
    )       
    
    return {
        "original_text": text,
        "raw_concepts": raw_concepts,
        "normalized_concepts": concepts,
        "concepts": classified_concepts,
        "base_sentiment_score": round(base_score, 3),
        "interaction_score": round(interaction_score, 3),
        "final_sentiment_score": round(final_score, 3),
        "sentiment_label": sentiment_label,
        "market_signal": market_signal,
        "interactions": interactions,
        "reasoning_path": reasoning_path,
        "summary": summary,
    }
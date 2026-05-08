from app.pipeline.orchestrator import analyze_text

if __name__ == "__main__":
    text = "The company reported strong profit growth but faces inflation risk and potential layoffs."
    
    result = analyze_text(text)
    
    print("\nINPUT:")
    print(text)
    
    print("\nCONCEPT ANALYSIS:")
    for c in result["concepts"]:
        status = "known" if c["known_concept"] else "unknown"
        print(
            f"{c['term']}: {c['polarity']} ({status}),"
            f" category: {c['category']} ({status})"
            )
        
    print("\nINTERACTIONS:")
    if result["interactions"]:
        for item in result["interactions"]:
            print(f"- {', '.join(item['concepts'])}: {item['effect']}")
    else:
        print("No interaction rules triggered.")
        
    print("\nREASONING PATH:")
    for step in result["reasoning_path"]:
        print(f"- {step}")

    print("\nOVERALL:")
    print("Base Sentiment:", result["base_sentiment_score"])
    print("Interaction Score:", result["interaction_score"])
    print("Final Sentiment Score:", result["final_sentiment_score"])
    print("Sentiment Label:", result["sentiment_label"])
    print("Market Signal:", result["market_signal"])
    
    print("\nSUMMARY:")
    print(result["summary"])
from app.pipeline.orchestrator import analyze_text

if __name__ == "__main__":
    text = "The company reported strong profit growth but faces inflation risk and potential layoffs."
    
    result = analyze_text(text)
    
    print("\nINPUT:")
    print(text)
    
    print("\nCONCEPT ANALYSIS:")
    for c in result["concepts"]:
        status = "known" if c["known_concept"] else "unknown"
        print(f"{c['term']}: {c['polarity']} ({status})")

    print("\nOVERALL:")
    print("Sentiment Score:", result["overall_sentiment"])
    print("Sentiment Label:", result["sentiment_label"])
    print("Market Signal:", result["market_signal"])
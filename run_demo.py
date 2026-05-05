from app.pipeline.orchestrator import analyze_text

if __name__ == "__main__":
    text = "The company reported strong profit growth but faces inflation risk and potential layoffs."
    
    result = analyze_text(text)
    
    print("\nINPUT:")
    print(text)
    
    print("\nOUTPUT:")
    for c in result["concepts"]:
        print(f"{c['term']}: {c['polarity']}")
        
    print("\nOverall Sentiment:", result["overall_sentiment"])
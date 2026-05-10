import json
from app.pipeline.orchestrator import analyze_text

def print_result(example_id, result):
    print("\n" + "=" * 80)
    print(f"Example ID: {example_id}")
    print("=" * 80)
    
    print("\nINPUT:")
    print(result["original_text"])
    
    print("\nRAW CONCEPTS:")
    print(result["raw_concepts"])
    
    print("\nNORMALIZED CONCEPTS:")
    print(result["normalized_concepts"])

    print("\nCONCEPT ANALYSIS:")
    for c in result["concepts"]:
        status = "known" if c["known_concept"] else "unknown"
        print(
            f"- {c['term']}: polarity={c['polarity']}, "
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
    
if __name__ == "__main__":
    with open("data/sample_inputs.json", "r", encoding="utf-8") as file:
        examples = json.load(file)
        
    for example in examples:
        result = analyze_text(example["text"])
        print_result(example["id"], result)
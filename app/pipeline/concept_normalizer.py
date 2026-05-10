NORMALIZATION_RULES = {
    # Company performance
    "profit growth": "profit growth",
    "strong profit growth": "profit growth",
    "revenue growth": "revenue growth",
    "earnings growth": "earnings growth",
    "earnings decline": "earnings decline",
    "revenue decline": "revenue decline",
    "profit decline": "profit decline",

    # Macroeconomic pressure
    "inflation risk": "inflation risk",
    "rising inflation": "inflation",
    "interest rate hike": "interest rate hike",
    "rate hike": "interest rate hike",
    "market volatility": "market volatility",
    "economic slowdown": "economic slowdown",

    # Employment
    "potential layoffs": "layoff",
    "layoffs": "layoff",
    "layoff": "layoff",
    "job cuts": "layoff",

    # Market psychology
    "investor confidence": "investor confidence",
    "market confidence": "investor confidence",
    "market uncertainty": "market uncertainty",

    # Policy / regulation
    "regulatory pressure": "regulatory pressure",
    "regulation pressure": "regulatory pressure",
}

def remove_subconcepts(concepts):
    concept_set = set(concepts)
    final_concepts = set(concepts)
    
    multi_word_concepts = [c for c in concept_set if len(c.split()) > 1]
    
    for multi in multi_word_concepts:
        parts = multi.split()
        
        for part in parts:
            if part in final_concepts:
                final_concepts.remove(part)
                
    return list(final_concepts)


def normalize_concepts(concepts):
    normalized = set()

    for concept in concepts:
        clean = concept.lower().strip()

        if clean in NORMALIZATION_RULES:
            normalized.add(NORMALIZATION_RULES[clean])
        else:
            normalized.add(clean)

    return remove_subconcepts(normalized)
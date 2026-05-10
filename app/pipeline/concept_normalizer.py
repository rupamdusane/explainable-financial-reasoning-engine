NORMALIZATION_RULES = {
    # Company performance
    "profit growth": "profit growth",
    "strong profit growth": "profit growth",
    "revenue growth": "revenue growth",
    "earnings growth": "earnings growth",
    "earnings decline": "earnings decline",
    "revenue decline": "revenue decline",
    "profit decline": "profit decline",
    "strong earnings": "strong earnings",
    "earnings": "earnings",
    "earning": "earnings",
    
    # New market entry
    "new market": "new markets",
    "new markets": "new market",
    "acquisition": "acquisition",
    
    # Company Financial Signals
    "rising debt": "debt",

    # Macroeconomic pressure
    "inflation risk": "inflation risk",
    "rising inflation": "inflation",
    "interest rate hike": "interest rate hike",
    "interest rate hikes": "interest rate hike",
    "interest rate increases": "interest rate hike",
    "interest rate increase": "interest rate hike",
    "rate hike": "interest rate hike",
    "rate hikes": "interest rate hike",
    "rate increase": "interest rate hike",
    "market volatility": "market volatility",
    "economic slowdown": "economic slowdown",

    # Employment
    "potential layoffs": "layoff",
    "layoffs": "layoff",
    "layoff": "layoff",
    "job cuts": "layoff",

    # Market psychology
    "investor confidence": "investor confidence",
    "rising investor confidence": "investor confidence",
    "market confidence": "investor confidence",
    "market uncertainty": "market uncertainty",
    "concern": "market concern",
    "concerns": "market concern",
    "raising concerns": "market concern",
    "investor concern": "market concern",

    # Policy / regulation
    "regulatory pressure": "regulatory pressure",
    "regulation pressure": "regulatory pressure",
}

IGNORE_CONCEPTS = {
    "company", "firm", "market", "investor", "investors", "markets",
    }


def split_compound_concept(concepts):
    expanded = set()
    
    for concept in concepts:
        concept = concept.lower().strip()
        
        if " and " in concept:
            parts = [part.strip() for part in concept.split(" and ") if part.strip()]
            expanded.update(parts)
        else:
            expanded.add(concept)

    return list(expanded)


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

def normalize_single_concept(concept):
    clean = concept.lower().strip()
    
    if clean in NORMALIZATION_RULES:
        return NORMALIZATION_RULES[clean]
    
    return clean


def normalize_concepts(concepts):
    expanded_concepts = split_compound_concept(concepts)
    normalized = set()

    for concept in expanded_concepts:
        normalized_concept = normalize_single_concept(concept)

        # Important: split again after normalization attempt if compound phrase survived
        if " and " in normalized_concept:
            parts = [
                normalize_single_concept(part.strip())
                for part in normalized_concept.split(" and ")
                if part.strip()
            ]
            normalized.update(parts)
        else:
            normalized.add(normalized_concept)

    cleaned = {
        concept for concept in normalized
        if concept not in IGNORE_CONCEPTS
    }
    
    return remove_subconcepts(cleaned)
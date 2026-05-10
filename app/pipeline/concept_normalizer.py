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


def normalize_concepts(concepts):
    normalized = set()

    for concept in concepts:
        clean = concept.lower().strip()

        if clean in NORMALIZATION_RULES:
            normalized.add(NORMALIZATION_RULES[clean])
        else:
            normalized.add(clean)

    return list(normalized)
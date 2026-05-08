INTERACTION_RULES = [
    {
        "required_concepts": ["inflation", "risk"],
        "effect": "macroeconomic pressure is creating uncertainty",
        "impact": "negative",
        "weight": -0.2,
    },
    {
        "required_concepts": ["profit", "growth"],
        "effect": "strong company performance supports positive investor sentiment",
        "impact": "positive",
        "weight": 0.2,
    },
    {
        "required_concepts": ["layoff", "risk"],
        "effect": "employment concerns may increase perceived business risk",
        "impact": "negative",
        "weight": -0.2,
    },
    {
        "required_concepts": ["growth", "inflation"],
        "effect": "business growth is being balanced by macroeconomic pressure",
        "impact": "mixed",
        "weight": 0.0,
    },
]
INTERACTION_RULES = [
    {
        "required_concepts": ["inflation", "risk"],
        "effect": "macroeconomic pressure is creating uncertainty",
        "impact": "negative",
        "weight": -0.2,
    },
    {
        "required_concepts": ["inflation risk"],
        "effect": "inflation-related uncertainty may pressure market expectations",
        "impact": "negative",
        "weight": -0.15,
    },
    {
        "required_concepts": ["profit", "growth"],
        "effect": "strong company performance supports positive investor sentiment",
        "impact": "positive",
        "weight": 0.2,
    },
    {
        "required_concepts": ["profit growth"],
        "effect": "profit growth indicates improving company performance",
        "impact": "positive",
        "weight": 0.15,
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
    {
        "required_concepts": ["profit growth", "inflation risk"],
        "effect": "positive company performance is being challenged by inflation-related risk",
        "impact": "mixed",
        "weight": -0.05,
    },
    {
        "required_concepts": ["interest rate hike", "market volatility"],
        "effect": "tightening monetary conditions may amplify market volatility",
        "impact": "negative",
        "weight": -0.25,
    },
    {
        "required_concepts": ["earnings decline", "layoff"],
        "effect": "weak earnings and workforce reduction indicate structural company weakness",
        "impact": "negative",
        "weight": -0.25,
    },
    {
        "required_concepts": ["acquisition", "revenue growth"],
        "effect": "corporate expansion and revenue growth support positive business momentum",
        "impact": "positive",
        "weight": 0.2,
    },
    {
        "required_concepts": ["inflation risk", "interest rate hike"],
        "effect": "inflation risk and interest rate pressure may tighten financial conditions",
        "impact": "negative",
        "weight": -0.25,
    },
    {
        "required_concepts": ["economic slowdown", "interest rate hike"],
        "effect": "economic slowdown under higher interest rates may weaken market confidence",
        "impact": "negative",
        "weight": -0.25,
    },
]
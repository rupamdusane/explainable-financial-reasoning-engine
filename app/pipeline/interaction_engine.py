from app.knowledge.interaction_rules import INTERACTION_RULES

def detect_interactions(concepts):
    detected = []

    known_terms = {item["term"] for item in concepts}

    for rule in INTERACTION_RULES:
        required = set(rule["required_concepts"])

        if required.issubset(known_terms):
            detected.append({
                "concepts": rule["required_concepts"],
                "effect": rule["effect"],
                "impact": rule["impact"],
                "weight": rule["weight"],
            })

    return detected
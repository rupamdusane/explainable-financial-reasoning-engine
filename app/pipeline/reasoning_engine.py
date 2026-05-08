def build_reasoning(concepts, interactions):
    reasoning_path = []

    positive_concepts = []
    negative_concepts = []

    for item in concepts:
        if not item["known_concept"]:
            continue

        term = item["term"]
        category = item["category"]
        polarity = item["polarity"]

        if polarity > 0:
            positive_concepts.append(term)
            reasoning_path.append(
                f"{term} is a positive signal linked to {category.replace('_', ' ')}."
            )

        elif polarity < 0:
            negative_concepts.append(term)
            reasoning_path.append(
                f"{term} is a negative signal linked to {category.replace('_', ' ')}."
            )

    for interaction in interactions:
        reasoning_path.append(
            f"The combination of {', '.join(interaction['concepts'])} suggests that {interaction['effect']}."
        )

    return reasoning_path
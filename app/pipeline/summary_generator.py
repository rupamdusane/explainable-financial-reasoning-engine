def generate_summary(sentiment_label, market_signal, concepts, interactions):
    known = [c for c in concepts if c["known_concept"]]

    positive = [c["term"] for c in known if c["polarity"] > 0]
    negative = [c["term"] for c in known if c["polarity"] < 0]

    positive_interactions = [
        item["effect"] for item in interactions if item["impact"] == "positive"
    ]

    negative_interactions = [
        item["effect"] for item in interactions if item["impact"] == "negative"
    ]

    mixed_interactions = [
        item["effect"] for item in interactions if item["impact"] == "mixed"
    ]

    if sentiment_label == "positive":
        summary = (
            f"The text suggests a {market_signal} market signal, mainly supported by "
            f"positive concepts such as {', '.join(positive[:3])}."
        )

        if positive_interactions:
            summary += (
                " The reasoning layer reinforces this through interactions such as "
                f"{'; '.join(positive_interactions[:2])}."
            )

        return summary

    if sentiment_label == "negative":
        summary = (
            f"The text suggests a {market_signal} market signal, mainly driven by "
            f"negative concepts such as {', '.join(negative[:3])}."
        )

        if positive:
            summary += (
                f" Although positive signals such as {', '.join(positive[:2])} are present, "
                "they are outweighed by stronger risk-related signals."
            )

        if negative_interactions:
            summary += (
                " The reasoning layer supports this through interactions such as "
                f"{'; '.join(negative_interactions[:2])}."
            )

        return summary

    summary = (
        f"The text shows mixed sentiment. Positive signals such as "
        f"{', '.join(positive[:3]) if positive else 'none'} are balanced against "
        f"negative signals such as {', '.join(negative[:3]) if negative else 'none'}."
    )

    useful_interactions = (
        positive_interactions[:1]
        + negative_interactions[:1]
        + mixed_interactions[:1]
    )

    if useful_interactions:
        summary += (
            " The reasoning layer highlights this tension through interactions such as "
            f"{'; '.join(useful_interactions)}."
        )

    return summary
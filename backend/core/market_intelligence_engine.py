from dataclasses import dataclass


@dataclass
class MarketIntelligence:

    title: str

    market_state: str

    confidence: int

    summary: str

    strengths: list

    weaknesses: list


def analyze_market_intelligence(

    market_story,

    timeline,

    checklist,

    decision

):

    strengths = []

    weaknesses = []

    for item in checklist.items:

        if item.completed:

            strengths.append(item.name)

        else:

            weaknesses.append(item.name)

    return MarketIntelligence(

        title="Market Intelligence",

        market_state=decision.direction,

        confidence=decision.confidence,

        summary=market_story.summary,

        strengths=strengths,

        weaknesses=weaknesses

    )
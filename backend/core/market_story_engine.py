from dataclasses import dataclass

from core.session_engine import analyze_session


@dataclass
class MarketStory:

    greeting: str
    session: str

    bias: str
    phase: str
    objective: str
    expectation: str

    confidence: int

    summary: str

    waiting_for: list[str]

    warnings: list[str]

    opinion: str


def analyze_market_story():

    session = analyze_session()

    return MarketStory(

        greeting=session.greeting,

        session=session.name,

        bias="Bullish",

        phase="Expansion",

        objective="Weekly Buy Side Liquidity",

        expectation="GBPUSD Bearish",

        confidence=92,

        summary=(
            "Daily imbalance continues to hold. "
            "Asia manipulation completed. "
            "Strong bullish displacement remains intact."
        ),

        waiting_for=[
            "London Manipulation",
            "3m CISD",
            "Fresh FVG Retest"
        ],

        warnings=[
            "No High Impact News"
        ],

        opinion=(
            "The market story is very clear. "
            "Do not enter early. "
            "Allow the execution model to complete."
        )

    )
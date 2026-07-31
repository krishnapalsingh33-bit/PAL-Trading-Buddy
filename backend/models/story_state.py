from dataclasses import dataclass


@dataclass
class StoryState:

    direction: str = "NONE"

    market_story: str = ""

    description: str = ""

    next_step: str = "Observe"

    confidence: int = 0

    # Future fields
    weekly_trend: str = ""

    daily_trend: str = ""

    h4_trend: str = ""

    weekly_external = None

    daily_external = None

    h4_external = None
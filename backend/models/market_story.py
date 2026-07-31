from dataclasses import dataclass

from models.trend_analysis import TrendAnalysis


@dataclass
class MarketStory:
    """
    Higher timeframe market narrative.
    """

    weekly: TrendAnalysis | None = None

    daily: TrendAnalysis | None = None

    h4: TrendAnalysis | None = None

    overall_bias: str = "RANGE"

    confidence: int = 0

    objective: str = ""

    story: str = ""
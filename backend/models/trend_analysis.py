from dataclasses import dataclass


@dataclass
class TrendAnalysis:
    """
    PAL Trend Analysis
    """

    timeframe: str = ""

    direction: str = "NEUTRAL"

    delivery: str = "UNKNOWN"

    liquidity_objective: str = "UNKNOWN"

    displacement: str = "UNKNOWN"

    candle_closes: str = "UNKNOWN"

    score: int = 0

    confidence: int = 0

    reason: str = ""
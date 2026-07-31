from dataclasses import dataclass

from models.trend_analysis import TrendAnalysis


@dataclass
class TradingPlan:
    """
    PAL Trading Plan
    """

    h1: TrendAnalysis | None = None

    m30: TrendAnalysis | None = None

    m15: TrendAnalysis | None = None

    mission: str = ""

    trading_focus: str = ""

    ready: bool = False
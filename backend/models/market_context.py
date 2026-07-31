from dataclasses import dataclass, field
from typing import List


@dataclass
class Candle:
    time: str = ""

    open: float = 0.0
    high: float = 0.0
    low: float = 0.0
    close: float = 0.0

    volume: float = 0.0


@dataclass
class TimeframeData:
    timeframe: str = ""
    candles: List[Candle] = field(default_factory=list)


@dataclass
class MarketContext:

    symbol: str = ""

    weekly: TimeframeData = field(
        default_factory=lambda: TimeframeData("W1")
    )

    daily: TimeframeData = field(
        default_factory=lambda: TimeframeData("D1")
    )

    h4: TimeframeData = field(
        default_factory=lambda: TimeframeData("H4")
    )

    h1: TimeframeData = field(
        default_factory=lambda: TimeframeData("H1")
    )

    m30: TimeframeData = field(
        default_factory=lambda: TimeframeData("M30")
    )

    m15: TimeframeData = field(
        default_factory=lambda: TimeframeData("M15")
    )

    m5: TimeframeData = field(
        default_factory=lambda: TimeframeData("M5")
    )

    m3: TimeframeData = field(
        default_factory=lambda: TimeframeData("M3")
    )

    m1: TimeframeData = field(
        default_factory=lambda: TimeframeData("M1")
    )
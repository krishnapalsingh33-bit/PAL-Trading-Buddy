from dataclasses import dataclass, field

from models.candle import Candle


@dataclass
class MarketData:
    """
    Contains all timeframe data for one symbol.
    """

    symbol: str

    monthly: list[Candle] = field(default_factory=list)
    weekly: list[Candle] = field(default_factory=list)
    daily: list[Candle] = field(default_factory=list)

    h4: list[Candle] = field(default_factory=list)
    h1: list[Candle] = field(default_factory=list)

    m30: list[Candle] = field(default_factory=list)
    m15: list[Candle] = field(default_factory=list)
    m5: list[Candle] = field(default_factory=list)
    m3: list[Candle] = field(default_factory=list)
    m1: list[Candle] = field(default_factory=list)
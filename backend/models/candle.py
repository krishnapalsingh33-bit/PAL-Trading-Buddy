from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    datetime: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float | None = None

    @property
    def bullish(self):
        return self.close > self.open

    @property
    def bearish(self):
        return self.close < self.open

    @property
    def body_size(self):
        return abs(self.close - self.open)

    @property
    def range(self):
        return self.high - self.low

    @property
    def upper_wick(self):
        return self.high - max(
            self.open,
            self.close
        )

    @property
    def lower_wick(self):
        return min(
            self.open,
            self.close
        ) - self.low

    @property
    def midpoint(self) -> float:
        return (self.high + self.low) / 2
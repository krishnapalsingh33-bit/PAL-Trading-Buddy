from dataclasses import dataclass


@dataclass
class TradingFocus:

    direction: str = "NONE"

    timeframe: str = ""

    objective: str = ""

    waiting_for: str = ""

    confidence: int = 0
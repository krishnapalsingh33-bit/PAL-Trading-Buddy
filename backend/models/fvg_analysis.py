from dataclasses import dataclass, field

from models.candle import Candle


@dataclass
class FairValueGap:

    direction: str = "None"

    top: float = 0.0

    bottom: float = 0.0

    midpoint: float = 0.0

    creation_candle: Candle | None = None

    mitigated: bool = False

    mitigation_candle: Candle | None = None

    valid: bool = True

    reason: str = ""


@dataclass
class FVGAnalysis:

    bullish: list[FairValueGap] = field(default_factory=list)

    bearish: list[FairValueGap] = field(default_factory=list)

    active_bullish: FairValueGap | None = None

    active_bearish: FairValueGap | None = None

    total: int = 0

    story: str = ""
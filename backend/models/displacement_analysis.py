from dataclasses import dataclass, field

from models.candle import Candle


@dataclass
class DisplacementAnalysis:
    """
    PAL Displacement Analysis

    A displacement is the complete momentum sequence that
    follows manipulation and demonstrates aggressive delivery.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str = ""

    # ----------------------------------
    # Detection
    # ----------------------------------

    confirmed: bool = False

    direction: str = "NONE"      # Bullish / Bearish

    # ----------------------------------
    # Momentum Sequence
    # ----------------------------------

    start_candle: Candle | None = None

    end_candle: Candle | None = None

    candles: list[Candle] = field(default_factory=list)

    candle_count: int = 0

    # ----------------------------------
    # Momentum Quality
    # ----------------------------------

    body_ratio: float = 0.0

    opposite_wick_ratio: float = 0.0

    strong_body: bool = False

    small_opposite_wick: bool = False

    # ----------------------------------
    # Summary
    # ----------------------------------

    reason: str = ""

    summary: str = ""
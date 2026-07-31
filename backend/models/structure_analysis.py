from dataclasses import dataclass
from typing import Optional

from models.candle import Candle


@dataclass
class StructureAnalysis:
    """
    PAL Structure Analysis

    This model represents the current structural state of a timeframe.
    It is consumed by:
        - LiquidityEngine
        - PremiumDiscountEngine
        - StoryEngine
        - ExecutionEngine
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str

    # ----------------------------------
    # Swing Information
    # ----------------------------------

    swing_highs: list[Candle]

    swing_lows: list[Candle]

    latest_swing_high: Optional[Candle] = None

    latest_swing_low: Optional[Candle] = None

    # ----------------------------------
    # Market Structure
    # ----------------------------------

    trend: str = "UNKNOWN"      # BULLISH / BEARISH / TRANSITION / RANGE / UNKNOWN

    active_side: str = "NONE"   # BUY / SELL / NONE

    # ----------------------------------
    # External Structure
    # ----------------------------------

    external_high: Optional[Candle] = None

    external_low: Optional[Candle] = None

    # ----------------------------------
    # Protected Levels
    # ----------------------------------

    protected_high: Optional[Candle] = None

    protected_low: Optional[Candle] = None

    # ----------------------------------
    # Summary
    # ----------------------------------

    story: str = ""

    summary: str = ""
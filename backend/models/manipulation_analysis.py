from dataclasses import dataclass

from models.candle import Candle
from models.liquidity_level import LiquidityLevel


@dataclass
class ManipulationAnalysis:
    """
    PAL Manipulation Analysis

    Represents a liquidity sweep prior to displacement.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str = ""

    # ----------------------------------
    # Detection
    # ----------------------------------

    exists: bool = False

    direction: str = "NONE"      # Bullish / Bearish

    liquidity: LiquidityLevel | None = None

    # ----------------------------------
    # Sweep Information
    # ----------------------------------

    sweep_candle: Candle | None = None

    sweep_price: float | None = None

    rejection: bool = False

    wick_ratio: float = 0.0

    # ----------------------------------
    # Summary
    # ----------------------------------

    reason: str = ""

    summary: str = ""
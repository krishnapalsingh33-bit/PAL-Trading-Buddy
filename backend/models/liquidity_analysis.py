from dataclasses import dataclass, field

from models.candle import Candle
from models.liquidity_level import LiquidityLevel


@dataclass
class LiquidityAnalysis:
    """
    PAL Liquidity Analysis

    Stores all liquidity objectives for the timeframe and
    the currently active market objective.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str

    # ----------------------------------
    # Active Objectives
    # ----------------------------------

    remaining_buy: list[LiquidityLevel] = field(default_factory=list)

    remaining_sell: list[LiquidityLevel] = field(default_factory=list)

    current_objective: LiquidityLevel | None = None

    next_objective: LiquidityLevel | None = None

    # ----------------------------------
    # Statistics
    # ----------------------------------

    total_remaining: int = 0

    # ----------------------------------
    # Last Sweep
    # ----------------------------------

    last_sweep_side: str = "NONE"

    last_sweep_price: float | None = None

    last_sweep_candle: Candle | None = None

    # ----------------------------------
    # Summary
    # ----------------------------------

    story: str = ""

    summary: str = ""
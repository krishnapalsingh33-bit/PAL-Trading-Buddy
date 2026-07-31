from dataclasses import dataclass, field
from typing import Any


@dataclass
class TradingResult:

    # ----------------------------------
    # Trading Timeframes
    # ----------------------------------

    h1_trend: str = ""
    m30_trend: str = ""
    m15_trend: str = ""

    # ----------------------------------
    # Alignment
    # ----------------------------------

    timeframe_alignment: bool = False
    htf_alignment: bool = False

    # ----------------------------------
    # Liquidity
    # ----------------------------------

    current_objective: Any = None
    next_objective: Any = None

    # ----------------------------------
    # Entry Filters
    # ----------------------------------

    dxy_alignment: bool = False
    manipulation_confirmed: bool = False
    displacement_confirmed: bool = False
    cisd_confirmed: bool = False
    premium_discount_ok: bool = False

    # ----------------------------------
    # Trading Decision
    # ----------------------------------

    setup_grade: str = ""
    execute: bool = False

    # ----------------------------------
    # Mission
    # ----------------------------------

    current_mission: str = ""
    next_event: str = ""
    trading_focus: str = ""

    # ----------------------------------
    # Summary
    # ----------------------------------

    summary: list[str] = field(default_factory=list)

    # ----------------------------------
    # Confidence
    # ----------------------------------

    confidence: int = 0
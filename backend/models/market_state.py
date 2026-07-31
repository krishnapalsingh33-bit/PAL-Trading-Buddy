from dataclasses import dataclass, field

from models.liquidity_level import LiquidityLevel
from models.trading_focus import TradingFocus


@dataclass
class MarketState:

    # ----------------------------------
    # Current Price
    # ----------------------------------

    current_price: float = 0.0

    # ----------------------------------
    # Story
    # ----------------------------------

    current_objective: LiquidityLevel | None = None

    next_objective: LiquidityLevel | None = None

    # ----------------------------------
    # Trading Focus
    # ----------------------------------

    trading_focus: TradingFocus | None = None

    # ----------------------------------
    # Liquidity
    # ----------------------------------

    remaining_liquidity: list[LiquidityLevel] = field(default_factory=list)

    completed_liquidity: list[LiquidityLevel] = field(default_factory=list)

    # ----------------------------------
    # Information
    # ----------------------------------

    summary: list[str] = field(default_factory=list)
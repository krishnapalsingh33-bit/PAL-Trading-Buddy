from dataclasses import dataclass, field


@dataclass
class ExecutionDecision:
    """
    Final execution decision produced by the PAL Engine.
    """

    # BUY / SELL / WAIT / PREPARE / NO TRADE
    action: str = "WAIT"

    # M5 / M15 / M30
    timeframe: str = ""

    # Overall market trend
    trend: str = "UNKNOWN"

    # Workflow stage
    stage: str = ""

    # Why this decision was made
    reason: str = ""

    # Optional execution levels
    entry_price: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None
    risk_reward: float | None = None

    # Evidence collected by PAL
    confirmations: list[str] = field(default_factory=list)

    # Any warnings for the trader
    warnings: list[str] = field(default_factory=list)

    # Human-readable summary
    summary: str = ""
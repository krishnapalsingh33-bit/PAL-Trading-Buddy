from dataclasses import dataclass

from models.liquidity_level import LiquidityLevel


@dataclass
class MarketMission:

    # ----------------------------------
    # Story
    # ----------------------------------

    story_direction: str = ""

    story_objective: LiquidityLevel | None = None

    # ----------------------------------
    # Trading Mission
    # ----------------------------------

    direction: str = "NONE"

    objective: LiquidityLevel | None = None

    session: str = ""

    confidence: int = 0

    status: str = "OBSERVE"

    reason: list[str] = None

    def __post_init__(self):

        if self.reason is None:

            self.reason = []
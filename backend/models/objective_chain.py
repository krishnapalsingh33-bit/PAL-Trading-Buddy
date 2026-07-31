from dataclasses import dataclass, field

from models.liquidity_level import LiquidityLevel


@dataclass
class ObjectiveChain:

    # Destination

    external: LiquidityLevel | None = None

    # Checkpoints

    internals: list[LiquidityLevel] = field(default_factory=list)

    # Current position

    current_internal: LiquidityLevel | None = None

    # Journey status

    completed: bool = False

    story: str = ""
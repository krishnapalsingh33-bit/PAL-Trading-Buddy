from dataclasses import dataclass, field


@dataclass
class Mission:

    # --------------------------------
    # Current Mission
    # --------------------------------

    direction: str

    target_timeframe: str

    target_liquidity: str

    # --------------------------------
    # Planner State
    # --------------------------------

    current_stage: str = "Planning"

    confidence: int = 0

    # --------------------------------
    # Market Story
    # --------------------------------

    current_story: str = ""

    current_objective: str = ""

    next_objective: str = ""

    # --------------------------------
    # Evidence
    # --------------------------------

    reason: list[str] = field(default_factory=list)
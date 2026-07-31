from dataclasses import dataclass, field


@dataclass
class SwingAnalysis:

    timeframe: str = ""

    # --------------------------------------------------
    # All detected swings
    # --------------------------------------------------

    swing_highs: list = field(default_factory=list)

    swing_lows: list = field(default_factory=list)

    # --------------------------------------------------
    # Meaningful swings
    # (Filtered by PAL)
    # --------------------------------------------------

    meaningful_highs: list = field(default_factory=list)

    meaningful_lows: list = field(default_factory=list)

    # --------------------------------------------------
    # External Structure
    # --------------------------------------------------

    external_high = None

    external_low = None

    # --------------------------------------------------
    # Protected Levels
    # --------------------------------------------------

    protected_high = None

    protected_low = None

    # --------------------------------------------------
    # Internal Liquidity
    # --------------------------------------------------

    internal_highs: list = field(default_factory=list)

    internal_lows: list = field(default_factory=list)

    # --------------------------------------------------
    # Completed Liquidity
    # --------------------------------------------------

    completed_highs: list = field(default_factory=list)

    completed_lows: list = field(default_factory=list)

    # --------------------------------------------------
    # Story
    # --------------------------------------------------

    story_valid: bool = True
from dataclasses import dataclass, field


@dataclass
class StoryAnalysis:
    """
    PAL Story Analysis

    Represents the complete workflow state for a single timeframe.
    This object is shared across:

    - StoryEngine
    - GradeEngine
    - PALEngine
    - ExecutionEngine
    - ReportEngine
    """

    # ==================================================
    # Identity
    # ==================================================

    timeframe: str = ""

    trend: str = "UNKNOWN"

    liquidity: str = "UNKNOWN"

    # ==================================================
    # Workflow Components
    # ==================================================

    manipulation: bool = False

    displacement: bool = False

    delivery: bool = False

    cisd: bool = False

    premium: bool = False

    discount: bool = False

    bullish_fvg: bool = False

    bearish_fvg: bool = False

    # ==================================================
    # Workflow State
    # ==================================================

    stage: str = "WAIT_STRUCTURE"

    next_step: str = ""

    ready_for_entry: bool = False

    # ==================================================
    # Progress
    # ==================================================

    progress: dict = field(
        default_factory=lambda: {
            "completed": 0,
            "total": 8,
            "percentage": 0.0
        }
    )

    # ==================================================
    # Explanation
    # ==================================================

    entry_reason: str = ""

    completed_steps: list[str] = field(default_factory=list)

    missing_steps: list[str] = field(default_factory=list)

    confirmations: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    # ==================================================
    # Summary
    # ==================================================

    summary: str = ""
from dataclasses import dataclass, field


@dataclass
class GradeAnalysis:
    """
    PAL Grade Analysis
    """

    grade: str = "NO TRADE"

    score: int = 0

    trade_allowed: bool = False

    stage: str = ""

    decision: str = "WAIT"

    reasons: list[str] = field(default_factory=list)

    summary: str = ""
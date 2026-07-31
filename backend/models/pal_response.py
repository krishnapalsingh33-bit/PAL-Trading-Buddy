from dataclasses import dataclass, field

from models.execution_decision import ExecutionDecision
from models.timeframe_analysis import TimeframeAnalysis


@dataclass
class PALResponse:

    symbol: str = ""

    overall_bias: str = "UNKNOWN"

    execution: ExecutionDecision | None = None

    timeframes: list[TimeframeAnalysis] = field(default_factory=list)

    dxy_summary: str = ""

    confidence: int = 0

    summary: str = ""

    warnings: list[str] = field(default_factory=list)

    confirmations: list[str] = field(default_factory=list)
from dataclasses import dataclass, field
from typing import Any

from models.market_context import MarketContext
from models.story_analysis import StoryAnalysis
from models.grade_analysis import GradeAnalysis


@dataclass
class TimeframeAnalysis:
    """
    Stores every analysis result for a single timeframe.

    Every engine writes its output here.
    Nothing should be recalculated inside ReportEngine.
    """

    timeframe: str

    # Engine Results
    structure: Any = None
    liquidity: Any = None
    manipulation: Any = None
    displacement: Any = None
    delivery: Any = None
    cisd: Any = None
    premium_discount: Any = None
    fvg: Any = None

    # Human-readable analysis
    story: StoryAnalysis | None = None
    grade: GradeAnalysis | None = None


@dataclass
class PALAnalysis:
    """
    Complete PAL analysis returned by the PAL Engine.
    """

    context: MarketContext

    timeframes: list[TimeframeAnalysis] = field(default_factory=list)

    overall_bias: str = "UNKNOWN"

    execution_timeframe: str = ""

    ready_for_entry: bool = False

    summary: str = ""
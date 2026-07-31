from dataclasses import dataclass, field

from models.story_result import StoryResult
from models.trading_result import TradingResult
from models.execution_result import ExecutionResult


@dataclass
class DashboardResult:

    session: str = ""

    mission: str = ""

    story: str = ""

    execution: str = ""

    confidence: int = 0

    evidence: list[str] = field(default_factory=list)


class DashboardEngine:

    def build(

        self,

        story: StoryResult,

        trading: TradingResult,

        execution: ExecutionResult

    ) -> DashboardResult:

        result = DashboardResult()

        # -------------------------------
        # Mission
        # -------------------------------

        result.mission = trading.current_mission

        # -------------------------------
        # Story
        # -------------------------------

        result.story = story.market_story

        # -------------------------------
        # Execution
        # -------------------------------

        result.execution = execution.stage

        # -------------------------------
        # Confidence
        # -------------------------------

        result.confidence = execution.confidence

        # -------------------------------
        # Evidence
        # -------------------------------

        result.evidence.extend(execution.reason)

        return result
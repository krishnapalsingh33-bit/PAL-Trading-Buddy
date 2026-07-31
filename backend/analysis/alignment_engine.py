from models.story_result import StoryResult
from models.trading_result import TradingResult


class AlignmentEngine:

    def build(
        self,
        story: StoryResult,
        trading: TradingResult
    ) -> tuple[bool, bool]:

        return (
            self.check_htf_alignment(story),
            self.check_timeframe_alignment(story, trading)
        )

    # ----------------------------------
    # Higher Timeframe Alignment
    # ----------------------------------

    def check_htf_alignment(
        self,
        story: StoryResult
    ) -> bool:

        return story.htf_bias != "MIXED"

    # ----------------------------------
    # Trading Timeframe Alignment
    # ----------------------------------

    def check_timeframe_alignment(
        self,
        story: StoryResult,
        trading: TradingResult
    ) -> bool:

        bias = story.htf_bias

        if bias == "MIXED":
            return False

        return (
            trading.h1_trend == bias
            and trading.m30_trend == bias
        )
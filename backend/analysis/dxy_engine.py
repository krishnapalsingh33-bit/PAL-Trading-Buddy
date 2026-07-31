from analysis.context_builder import ContextBuilder
from analysis.story_engine import StoryEngine
from analysis.grade_engine import GradeEngine

from models.dxy_analysis import DXYAnalysis


class DXYEngine:
    """
    PAL DXY Engine

    Builds the DXY narrative and converts it into the
    expected GBP direction.
    """

    def __init__(self):

        self.context_builder = ContextBuilder()
        self.story_engine = StoryEngine()
        self.grade_engine = GradeEngine()

    def analyze(
        self,
        market
    ) -> DXYAnalysis:

        result = DXYAnalysis()

        context = self.context_builder.build(market)

        if context is None or context.h4 is None:

            result.summary = "Missing H4 context."
            return result

        # ----------------------------------
        # Story
        # ----------------------------------

        story = self.story_engine.build(
            context.h4
        )

        grade = self.grade_engine.analyze(
            story
        )

        # ----------------------------------
        # Copy Story
        # ----------------------------------

        result.trend = story.trend
        result.liquidity = story.liquidity

        result.manipulation = story.manipulation
        result.displacement = story.displacement
        result.delivery = story.delivery
        result.cisd = story.cisd

        result.premium = story.premium
        result.discount = story.discount

        result.bullish_fvg = story.bullish_fvg
        result.bearish_fvg = story.bearish_fvg

        result.confirmations.extend(
            story.confirmations
        )

        result.confirmations.extend(
            grade.reasons
        )

        # ----------------------------------
        # DXY -> GBP Correlation
        # ----------------------------------

        trend = story.trend.upper()

        if trend == "BULLISH":

            result.expected_gbp_direction = "BEARISH"
            result.gbp_alignment = True

        elif trend == "BEARISH":

            result.expected_gbp_direction = "BULLISH"
            result.gbp_alignment = True

        else:

            result.expected_gbp_direction = "UNKNOWN"
            result.gbp_alignment = False

        # ----------------------------------
        # Summary
        # ----------------------------------

        result.summary = (

            f"DXY Trend={result.trend} | "
            f"Stage={story.stage} | "
            f"GBP Bias={result.expected_gbp_direction} | "
            f"Decision={grade.decision}"

        )

        return result
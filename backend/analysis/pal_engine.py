from analysis.context_builder import ContextBuilder
from analysis.story_engine import StoryEngine
from analysis.grade_engine import GradeEngine

from models.pal_analysis import (
    PALAnalysis,
    TimeframeAnalysis
)


class PALEngine:

    def __init__(self):

        self.context_builder = ContextBuilder()
        self.story_engine = StoryEngine()
        self.grade_engine = GradeEngine()

    def analyze(
        self,
        market
    ) -> PALAnalysis:

        context = self.context_builder.build(market)

        analysis = PALAnalysis(
            context=context
        )

        if context is None:

            analysis.summary = "Failed to build context."
            return analysis

        timeframes = [

            context.weekly,
            context.daily,
            context.h4,
            context.h1,
            context.m30,
            context.m15,
            context.m5

        ]

        for tf in timeframes:

            if tf is None:
                continue

            print("\n" + "=" * 70)
            print(f"TIMEFRAME : {tf.timeframe}")

            if tf.structure:
                print(f"Structure Trend : {tf.structure.trend}")
            else:
                print("Structure Trend : None")

            if tf.liquidity:
                print(f"Current Objective : {tf.liquidity.current_objective}")
            else:
                print("Current Objective : None")

            # ----------------------------
            # Story
            # ----------------------------

            story = self.story_engine.build(tf)

            print(f"Story Trend : {story.trend}")
            print(f"Stage : {story.stage}")
            print(f"Ready : {story.ready_for_entry}")
            print(f"Completed : {story.completed_steps}")
            print(f"Missing : {story.missing_steps}")

            # ----------------------------
            # Grade
            # ----------------------------

            grade = self.grade_engine.analyze(story)

            print(f"Grade : {grade.grade}")
            print(f"Decision : {grade.decision}")
            print(f"Trade Allowed : {grade.trade_allowed}")

            print("=" * 70)

            analysis.timeframes.append(

                TimeframeAnalysis(

                    timeframe=tf.timeframe,

                    structure=tf.structure,
                    liquidity=tf.liquidity,
                    manipulation=tf.manipulation,
                    displacement=tf.displacement,
                    delivery=tf.delivery,
                    cisd=tf.cisd,
                    premium_discount=tf.premium_discount,
                    fvg=tf.fvg,

                    story=story,
                    grade=grade

                )

            )

        # --------------------------------------------------
        # Overall Bias (H4)
        # --------------------------------------------------

        h4 = next(

            (
                item
                for item in analysis.timeframes
                if item.timeframe == "H4"
            ),

            None

        )

        print("\n")
        print("#" * 70)

        if h4:

            analysis.overall_bias = h4.story.trend

            print(f"H4 Trend : {h4.story.trend}")
            print(f"H4 Stage : {h4.story.stage}")

        else:

            analysis.overall_bias = "UNKNOWN"

            print("H4 NOT FOUND")

        print(f"Overall Bias : {analysis.overall_bias}")

        print("#" * 70)

        # --------------------------------------------------
        # Execution Timeframe
        # --------------------------------------------------

        for timeframe in [

            "M5",
            "M15",
            "M30"

        ]:

            tf = next(

                (
                    item
                    for item in analysis.timeframes
                    if item.timeframe == timeframe
                ),

                None

            )

            if tf is None:
                continue

            if tf.grade.trade_allowed:

                analysis.execution_timeframe = timeframe
                analysis.ready_for_entry = True
                break

        analysis.summary = (

            f"Bias={analysis.overall_bias} | "
            f"Execution={analysis.execution_timeframe or 'None'} | "
            f"Ready={analysis.ready_for_entry}"

        )

        return analysis
from models.story_analysis import StoryAnalysis
from models.grade_analysis import GradeAnalysis


class GradeEngine:
    """
    PAL Grade Engine

    StoryEngine determines WHERE the market is.
    GradeEngine determines WHAT the trader should do.
    """

    def analyze(
        self,
        story: StoryAnalysis
    ) -> GradeAnalysis:

        grade = GradeAnalysis()

        grade.stage = story.stage

        grade.reasons.extend(story.confirmations)

        # ----------------------------------
        # READY
        # ----------------------------------

        if story.stage == "READY":

            grade.grade = "A+"
            grade.score = 100
            grade.decision = "EXECUTE"
            grade.trade_allowed = True

            grade.reasons.append(
                "All PAL conditions satisfied."
            )

        # ----------------------------------
        # PREPARE
        # ----------------------------------

        elif story.stage in (

            "WAIT_FVG",
            "WAIT_PREMIUM_DISCOUNT"

        ):

            grade.grade = "A"
            grade.score = 90
            grade.decision = "PREPARE"

            grade.reasons.append(
                story.next_step
            )

        # ----------------------------------
        # WAIT
        # ----------------------------------

        elif story.stage in (

            "WAIT_CISD",
            "WAIT_DELIVERY",
            "WAIT_DISPLACEMENT"

        ):

            grade.grade = "B"
            grade.score = 70
            grade.decision = "WAIT"

            grade.reasons.append(
                story.next_step
            )

        # ----------------------------------
        # NO TRADE
        # ----------------------------------

        else:

            grade.grade = "NO TRADE"
            grade.score = 0
            grade.decision = "NO TRADE"

            grade.reasons.append(
                story.next_step
            )

        grade.summary = (

            f"{grade.grade} | "
            f"{grade.decision} | "
            f"{story.stage}"

        )

        return grade
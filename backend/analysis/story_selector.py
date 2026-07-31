from models.liquidity_analysis import LiquidityAnalysis


class StorySelector:
    """
    Selects the active liquidity objective.

    Objectives are already validated and ranked by
    ObjectiveDetector.

    This class only exposes the current and next
    objective for the remainder of the PAL pipeline.
    """

    def select(
        self,
        analysis: LiquidityAnalysis
    ) -> LiquidityAnalysis:

        objectives = (
            analysis.remaining_buy +
            analysis.remaining_sell
        )

        analysis.current_objective = None
        analysis.next_objective = None
        analysis.total_remaining = len(objectives)

        if not objectives:

            analysis.story = "No remaining liquidity objectives."
            analysis.summary = analysis.story
            return analysis

        analysis.current_objective = objectives[0]

        if len(objectives) > 1:
            analysis.next_objective = objectives[1]

        current = analysis.current_objective

        analysis.story = (
            f"Current Objective → "
            f"{current.timeframe} "
            f"{current.side} "
            f"{current.level_type}"
        )

        if analysis.next_objective:

            nxt = analysis.next_objective

            analysis.summary = (
                f"Current: "
                f"{current.timeframe} "
                f"{current.side} "
                f"{current.level_type} | "
                f"Next: "
                f"{nxt.timeframe} "
                f"{nxt.side} "
                f"{nxt.level_type}"
            )

        else:

            analysis.summary = (
                f"Only Objective: "
                f"{current.timeframe} "
                f"{current.side} "
                f"{current.level_type}"
            )

        return analysis
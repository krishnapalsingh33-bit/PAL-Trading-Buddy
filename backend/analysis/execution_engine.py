from models.pal_analysis import PALAnalysis
from models.dxy_analysis import DXYAnalysis
from models.execution_decision import ExecutionDecision


class ExecutionEngine:
    """
    PAL Execution Engine

    Produces the final trading decision by combining
    PAL analysis with DXY confirmation.
    """

    def analyze(
        self,
        analysis: PALAnalysis,
        dxy: DXYAnalysis
    ) -> ExecutionDecision:

        decision = ExecutionDecision()

        # ==================================================
        # Validation
        # ==================================================

        if analysis is None:
            decision.reason = "Missing PAL analysis."
            decision.summary = decision.reason
            return decision

        if dxy is None:
            decision.reason = "Missing DXY analysis."
            decision.summary = decision.reason
            return decision

        if analysis.overall_bias == "UNKNOWN":
            decision.reason = "Higher timeframe bias is unknown."
            decision.summary = decision.reason
            return decision

        if not dxy.gbp_alignment:
            decision.reason = "DXY does not confirm GBP direction."
            decision.summary = decision.reason
            return decision

        if analysis.overall_bias != dxy.expected_gbp_direction:

            decision.reason = (
                f"Bias mismatch "
                f"(PAL={analysis.overall_bias}, "
                f"DXY={dxy.expected_gbp_direction})"
            )

            decision.summary = decision.reason
            return decision

        if not analysis.execution_timeframe:
            decision.reason = "No execution timeframe selected."
            decision.summary = decision.reason
            return decision

        execution = next(
            (
                tf
                for tf in analysis.timeframes
                if tf.timeframe == analysis.execution_timeframe
            ),
            None
        )

        if execution is None:
            decision.reason = "Execution timeframe not found."
            decision.summary = decision.reason
            return decision

        if execution.story is None:
            decision.reason = "Story analysis missing."
            decision.summary = decision.reason
            return decision

        if execution.grade is None:
            decision.reason = "Grade analysis missing."
            decision.summary = decision.reason
            return decision

        # ==================================================
        # Common Information
        # ==================================================

        decision.stage = execution.story.stage
        decision.timeframe = analysis.execution_timeframe
        decision.trend = execution.story.trend

        # ==================================================
        # WAIT / PREPARE
        # ==================================================

        if not execution.grade.trade_allowed:

            decision.action = execution.grade.decision

            decision.reason = execution.story.next_step

            decision.confirmations = [

                f"✓ {step}"
                for step in execution.story.completed_steps

            ]

            decision.warnings = [

                f"✗ {step}"
                for step in execution.story.missing_steps

            ]

            decision.confirmations.extend(dxy.confirmations)

            decision.summary = (
                f"{decision.action} | "
                f"{decision.stage} | "
                f"{execution.story.next_step}"
            )

            return decision

        # ==================================================
        # EXECUTE
        # ==================================================

        if execution.story.trend == "BULLISH":
            decision.action = "BUY"

        elif execution.story.trend == "BEARISH":
            decision.action = "SELL"

        else:
            decision.action = "WAIT"

        decision.reason = (
            "All PAL workflow steps are complete "
            "and DXY confirms the setup."
        )

        decision.confirmations = [

            f"✓ {step}"
            for step in execution.story.completed_steps

        ]

        decision.confirmations.extend(dxy.confirmations)

        decision.summary = (
            f"{decision.action} "
            f"{decision.timeframe} | "
            f"{decision.stage}"
        )

        return decision
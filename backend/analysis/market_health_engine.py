from models.pal_analysis import PALAnalysis
from models.dxy_analysis import DXYAnalysis


class MarketHealthEngine:
    """
    PAL Market Health Engine

    Evaluates the overall quality of the market
    before allowing aggressive execution.
    """

    def analyze(
        self,
        pal: PALAnalysis,
        dxy: DXYAnalysis
    ) -> dict:

        result = {
            "status": "POOR",
            "score": 0,
            "reasons": []
        }

        score = 0

        # ----------------------------------
        # Validation
        # ----------------------------------

        if pal is None:

            result["reasons"].append(
                "Missing PAL analysis."
            )

            return result

        if dxy is None:

            result["reasons"].append(
                "Missing DXY analysis."
            )

            return result

        # ----------------------------------
        # Higher Timeframe Bias
        # ----------------------------------

        if pal.overall_bias != "UNKNOWN":

            score += 30

            result["reasons"].append(
                "Higher timeframe bias established."
            )

        else:

            result["reasons"].append(
                "Higher timeframe bias unknown."
            )

        # ----------------------------------
        # Execution Workflow
        # ----------------------------------

        if pal.execution_timeframe:

            execution = next(

                (
                    tf
                    for tf in pal.timeframes
                    if tf.timeframe == pal.execution_timeframe
                ),

                None

            )

            if execution:

                if execution.grade.trade_allowed:

                    score += 30

                    result["reasons"].append(
                        "Execution timeframe is READY."
                    )

                elif execution.grade.decision == "PREPARE":

                    score += 20

                    result["reasons"].append(
                        "Execution timeframe is PREPARING."
                    )

                elif execution.grade.decision == "WAIT":

                    score += 10

                    result["reasons"].append(
                        f"Waiting: {execution.story.stage}"
                    )

                else:

                    result["reasons"].append(
                        f"No Trade: {execution.story.stage}"
                    )

        else:

            result["reasons"].append(
                "No execution timeframe available."
            )

        # ----------------------------------
        # DXY Alignment
        # ----------------------------------

        if dxy.gbp_alignment:

            score += 40

            result["reasons"].append(
                "DXY confirms GBP direction."
            )

        else:

            result["reasons"].append(
                "DXY does not confirm GBP direction."
            )

        result["score"] = score

        # ----------------------------------
        # Market Status
        # ----------------------------------

        if score >= 90:

            result["status"] = "EXCELLENT"

        elif score >= 70:

            result["status"] = "GOOD"

        elif score >= 50:

            result["status"] = "MODERATE"

        else:

            result["status"] = "POOR"

        return result
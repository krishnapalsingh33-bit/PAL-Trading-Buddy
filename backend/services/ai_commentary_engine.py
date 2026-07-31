from typing import Dict, List


class AICommentaryEngine:
    """
    Converts PAL engine output into trader-friendly commentary.
    This engine never analyzes charts directly.
    It only explains the existing PAL workflow.
    """

    STAGE_CONFIDENCE = {
        "WAIT_STRUCTURE": 10,
        "WAIT_LIQUIDITY": 25,
        "WAIT_MANIPULATION": 40,
        "WAIT_DISPLACEMENT": 55,
        "WAIT_DELIVERY": 70,
        "WAIT_CISD": 82,
        "WAIT_PREMIUM_DISCOUNT": 92,
        "WAIT_FVG": 97,
        "READY": 100,
    }

    @classmethod
    def generate(
        cls,
        workflow: Dict,
        execution: Dict,
        market_health: Dict,
        dxy: Dict,
        news: Dict,
    ) -> Dict:

        stage = workflow.get("stage", "")
        bias = workflow.get("trend", "UNKNOWN")
        next_step = workflow.get("next_step", "Wait for confirmation.")

        completed = workflow.get("completed_steps", [])
        missing = workflow.get("missing_steps", [])

        confidence = cls.STAGE_CONFIDENCE.get(stage, 0)

        # ---------------------------------------------------------
        # Headline
        # ---------------------------------------------------------

        if execution.get("action") == "EXECUTE":
            headline = "Trade execution allowed"

        elif execution.get("action") == "PREPARE":
            headline = "Setup developing"

        elif "Bias mismatch" in execution.get("reason", ""):
            headline = "Bias mismatch detected"

        else:
            headline = "Waiting for confirmation"

        # ---------------------------------------------------------
        # Summary
        # ---------------------------------------------------------

        if "Bias mismatch" in execution.get("reason", ""):
            summary = (
                "PAL and DXY are currently not aligned. "
                "Execution should be avoided until both models agree."
            )

        else:
            summary = (
                f"The workflow is currently in the "
                f"{stage.replace('_', ' ').title()} stage."
            )

        # ---------------------------------------------------------
        # Market Story
        # ---------------------------------------------------------

        story_parts = []

        if completed:
            story_parts.append(
                "Completed: " + ", ".join(completed) + "."
            )

        if missing:
            story_parts.append(
                "Waiting for: " + ", ".join(missing) + "."
            )

        story_parts.append(
            f"Current objective: {next_step}"
        )

        market_story = " ".join(story_parts)

        # ---------------------------------------------------------
        # Next Action
        # ---------------------------------------------------------

        if execution.get("action") == "WAIT":

            if "Bias mismatch" in execution.get("reason", ""):
                next_action = (
                    "Wait until PAL and DXY align before looking for an entry."
                )

            else:
                next_action = next_step

        elif execution.get("action") == "PREPARE":
            next_action = (
                "Monitor lower timeframes for remaining confirmations."
            )

        else:
            next_action = (
                "All confirmations are complete. Follow your execution plan."
            )

        # ---------------------------------------------------------
        # Risk
        # ---------------------------------------------------------

        status = market_health.get("status", "GOOD")

        if status == "GOOD":
            risk = "LOW"

        elif status == "MODERATE":
            risk = "MEDIUM"

        else:
            risk = "HIGH"

        # ---------------------------------------------------------
        # Reasoning
        # ---------------------------------------------------------

        reasoning: List[str] = []

        reasoning.append(
            f"Overall workflow bias: {bias}."
        )

        if dxy.get("aligned"):
            reasoning.append(
                "DXY aligns with the current market narrative."
            )
        else:
            reasoning.append(
                "DXY is not aligned with the current market narrative."
            )

        for step in completed:
            reasoning.append(f"✓ {step} completed.")

        for step in missing:
            reasoning.append(f"Waiting for {step}.")

        if news.get("safe_to_trade"):
            reasoning.append(
                "No high-impact news is blocking execution."
            )
        else:
            reasoning.append(
                "High-impact news requires additional caution."
            )

        if execution.get("reason"):
            reasoning.append(
                execution["reason"]
            )

        return {

            "headline": headline,

            "summary": summary,

            "market_story": market_story,

            "next_action": next_action,

            "confidence": confidence,

            "risk": risk,

            "reasoning": reasoning,

        }
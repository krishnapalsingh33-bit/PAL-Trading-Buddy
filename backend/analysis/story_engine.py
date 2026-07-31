from models.market_narrative import MarketNarrative
from models.story_analysis import StoryAnalysis


class StoryEngine:
    """
    PAL Story Engine

    Builds the complete market narrative for a timeframe.

    This engine NEVER exits early.
    It evaluates every PAL component before deciding the
    current workflow stage.
    """

    def build(
        self,
        narrative: MarketNarrative
    ) -> StoryAnalysis:

        story = StoryAnalysis()

        # ----------------------------------
        # Structure
        # ----------------------------------

        if narrative.structure:

            story.timeframe = narrative.structure.timeframe
            story.trend = narrative.structure.trend

            story.completed_steps.append("Structure")

        else:

            story.missing_steps.append("Structure")

        # ----------------------------------
        # Liquidity
        # ----------------------------------

        if (
            narrative.liquidity
            and narrative.liquidity.current_objective
        ):

            objective = narrative.liquidity.current_objective

            story.liquidity = (
                f"{objective.side} {objective.level_type}"
            )

            story.completed_steps.append("Liquidity")

            story.confirmations.append(
                f"Liquidity Objective: {objective.side}"
            )

        else:

            story.missing_steps.append("Liquidity")

        # ----------------------------------
        # Manipulation
        # ----------------------------------

        if (
            narrative.manipulation
            and narrative.manipulation.exists
        ):

            story.manipulation = True

            story.completed_steps.append("Manipulation")

            story.confirmations.append(
                "Manipulation confirmed"
            )

        else:

            story.missing_steps.append("Manipulation")

        # ----------------------------------
        # Displacement
        # ----------------------------------

        if (
            narrative.displacement
            and narrative.displacement.confirmed
        ):

            story.displacement = True

            story.completed_steps.append("Displacement")

            story.confirmations.append(
                "Displacement confirmed"
            )

        else:

            story.missing_steps.append("Displacement")

        # ----------------------------------
        # Delivery
        # ----------------------------------

        if (
            narrative.delivery
            and narrative.delivery.confirmed
        ):

            story.delivery = True

            story.completed_steps.append("Delivery")

            story.confirmations.append(
                "Delivery confirmed"
            )

        else:

            story.missing_steps.append("Delivery")

        # ----------------------------------
        # CISD
        # ----------------------------------

        if (
            narrative.cisd
            and narrative.cisd.confirmed
        ):

            story.cisd = True

            story.completed_steps.append("CISD")

            story.confirmations.append(
                "CISD confirmed"
            )

        else:

            story.missing_steps.append("CISD")

        # ----------------------------------
        # Premium / Discount
        # ----------------------------------

        if narrative.premium_discount:

            story.premium = narrative.premium_discount.premium
            story.discount = narrative.premium_discount.discount

            if story.premium or story.discount:

                story.completed_steps.append("Premium/Discount")

            else:

                story.missing_steps.append("Premium/Discount")

        else:

            story.missing_steps.append("Premium/Discount")

        # ----------------------------------
        # Fair Value Gap
        # ----------------------------------

        if narrative.fvg:

            story.bullish_fvg = (
                narrative.fvg.active_bullish is not None
            )

            story.bearish_fvg = (
                narrative.fvg.active_bearish is not None
            )

            if story.bullish_fvg or story.bearish_fvg:

                story.completed_steps.append("FVG")

            else:

                story.missing_steps.append("FVG")

        else:

            story.missing_steps.append("FVG")

        # ----------------------------------
        # Workflow Stage
        # ----------------------------------

        if "Structure" in story.missing_steps:

            story.stage = "WAIT_STRUCTURE"

        elif "Liquidity" in story.missing_steps:

            story.stage = "WAIT_LIQUIDITY"

        elif "Manipulation" in story.missing_steps:

            story.stage = "WAIT_MANIPULATION"

        elif "Displacement" in story.missing_steps:

            story.stage = "WAIT_DISPLACEMENT"

        elif "Delivery" in story.missing_steps:

            story.stage = "WAIT_DELIVERY"

        elif "CISD" in story.missing_steps:

            story.stage = "WAIT_CISD"

        elif "Premium/Discount" in story.missing_steps:

            story.stage = "WAIT_PREMIUM_DISCOUNT"

        elif "FVG" in story.missing_steps:

            story.stage = "WAIT_FVG"

        else:

            story.stage = "READY"

            story.ready_for_entry = True

        # ----------------------------------
        # Next Step
        # ----------------------------------

        stage_messages = {

            "WAIT_STRUCTURE":
                "Waiting for market structure.",

            "WAIT_LIQUIDITY":
                "Waiting for liquidity objective.",

            "WAIT_MANIPULATION":
                "Waiting for manipulation.",

            "WAIT_DISPLACEMENT":
                "Waiting for displacement.",

            "WAIT_DELIVERY":
                "Waiting for delivery confirmation.",

            "WAIT_CISD":
                "Waiting for CISD confirmation.",

            "WAIT_PREMIUM_DISCOUNT":
                "Waiting for Premium / Discount location.",

            "WAIT_FVG":
                "Waiting for Fair Value Gap.",

            "READY":
                "All PAL conditions satisfied."

        }

        story.next_step = stage_messages.get(
            story.stage,
            ""
        )

        story.entry_reason = story.next_step

        story.summary = (
            f"{story.stage} | "
            f"Trend={story.trend} | "
            f"Completed={len(story.completed_steps)} | "
            f"Missing={len(story.missing_steps)}"
        )

        return story
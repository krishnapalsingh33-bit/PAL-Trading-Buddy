from models.market_story import MarketStory


class StoryBuilder:

    def build(

        self,

        mission,

        execution

    ) -> MarketStory:

        story = MarketStory()

        # -------------------------
        # Mission
        # -------------------------

        story.mission = mission.target_liquidity

        story.objective = mission.current_objective

        story.next_objective = mission.next_objective

        # -------------------------
        # Planner
        # -------------------------

        story.status = mission.current_stage

        story.summary = mission.current_story

        story.confidence = mission.confidence

        # -------------------------
        # Execution Narrative
        # -------------------------

        if execution.ready:

            story.waiting_for = "Execute Trade"

        elif not execution.manipulation:

            story.waiting_for = (

                "Wait for manipulation."

            )

        elif not execution.displacement:

            story.waiting_for = (

                "Wait for displacement."

            )

        elif not execution.fvg:

            story.waiting_for = (

                "Optional lower timeframe FVG."

            )

        elif not execution.cisd:

            story.waiting_for = (

                "Wait for CISD confirmation."

            )

        else:

            story.waiting_for = (

                "Observe."

            )

        # -------------------------
        # Bias
        # -------------------------

        if "Bearish" in mission.current_story:

            story.bias = "Bearish"

            story.direction = "SELL"

        elif "Bullish" in mission.current_story:

            story.bias = "Bullish"

            story.direction = "BUY"

        else:

            story.bias = "Neutral"

            story.direction = "WAIT"

        return story
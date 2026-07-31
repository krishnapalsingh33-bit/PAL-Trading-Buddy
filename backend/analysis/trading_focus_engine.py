from models.trading_focus import TradingFocus


class TradingFocusEngine:

    def build(

        self,

        market_state

    ) -> TradingFocus:

        focus = TradingFocus()

        # ----------------------------------
        # No Story
        # ----------------------------------

        if market_state.current_objective is None:

            focus.waiting_for = "Waiting for market story."

            return focus

        story = market_state.current_objective

        focus.direction = story.side

        # ----------------------------------
        # Higher Timeframe Story
        # ----------------------------------

        if story.timeframe in ("Weekly", "Daily"):

            focus.timeframe = "15M / 30M / 1H"

            focus.objective = (

                f"Find {story.side} setup"

            )

            focus.waiting_for = (

                "Wait for lower timeframe alignment."

            )

            focus.confidence = 70

            return focus

        # ----------------------------------
        # Already Trading Timeframe
        # ----------------------------------

        focus.timeframe = story.timeframe

        focus.objective = (

            f"{story.side} Internal"

        )

        focus.waiting_for = (

            "Wait for manipulation."

        )

        focus.confidence = 80

        return focus
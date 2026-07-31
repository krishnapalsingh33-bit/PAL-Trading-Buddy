from models.pal_context import PALContext
from models.pal_decision import PALDecision


class PALBrain:
    """
    PAL's final decision engine.

    It does NOT analyze candles.

    It combines the outputs from Story, Trading,
    and Execution into one final trading decision.
    """

    def analyze(
        self,
        context: PALContext,
    ) -> PALDecision:

        decision = PALDecision()

        # ==========================================
        # STORY
        # ==========================================

        if context.story:

            decision.market_story = context.story.story
            decision.confidence = context.story.confidence

        # ==========================================
        # TRADING
        # ==========================================

        if context.trading:

            decision.mission = context.trading.mission
            decision.trading_focus = context.trading.trading_focus

        # ==========================================
        # EXECUTION
        # ==========================================

        if context.execution:

            decision.action = context.execution.action

            if context.execution.ready:

                decision.next_event = (
                    "Wait for entry confirmation."
                )

            else:

                decision.next_event = (
                    context.execution.reason
                )

        else:

            decision.action = "NO TRADE"

            decision.next_event = (
                "Execution analysis unavailable."
            )

        return decision
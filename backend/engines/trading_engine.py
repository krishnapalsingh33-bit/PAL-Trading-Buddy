from models.trading_plan import TradingPlan
from models.trend_analysis import TrendAnalysis


class TradingEngine:

    def analyze(
        self,
        h1: TrendAnalysis,
        m30: TrendAnalysis,
        m15: TrendAnalysis,
    ) -> TradingPlan:

        plan = TradingPlan()

        plan.h1 = h1

        plan.m30 = m30

        plan.m15 = m15

        if (
            h1.direction ==
            m30.direction ==
            m15.direction
        ):

            plan.ready = True

            plan.mission = (
                "Wait for execution model."
            )

            plan.trading_focus = (
                "Higher timeframe alignment confirmed."
            )

        else:

            plan.ready = False

            plan.mission = (
                "Wait for lower timeframe alignment."
            )

            plan.trading_focus = (
                "No execution until trends align."
            )

        return plan
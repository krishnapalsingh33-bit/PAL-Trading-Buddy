from models.market_context import MarketContext
from models.mission import Mission


class ExternalLiquidityEngine:

    def analyze(
        self,
        context: MarketContext,
        mission: Mission
    ):

        # Pick the correct swing analysis
        mapping = {
            "Weekly": context.weekly,
            "Daily": context.daily,
            "4H": context.h4,
            "1H": context.h1,
            "30M": context.m30,
            "15M": context.m15,
            "5M": context.m5,
        }

        swings = mapping.get(mission.target_timeframe)

        if swings is None:
            return False

        return swings
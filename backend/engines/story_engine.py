from models.market_story import MarketStory
from models.trend_analysis import TrendAnalysis


class StoryEngine:

    def analyze(
        self,
        weekly: TrendAnalysis,
        daily: TrendAnalysis,
        h4: TrendAnalysis,
    ) -> MarketStory:

        story = MarketStory()

        story.weekly = weekly

        story.daily = daily

        story.h4 = h4

        bullish = 0
        bearish = 0

        for trend in [weekly, daily, h4]:

            if trend.direction == "BULLISH":
                bullish += 1

            elif trend.direction == "BEARISH":
                bearish += 1

        if bullish > bearish:

            story.overall_bias = "BULLISH"

        elif bearish > bullish:

            story.overall_bias = "BEARISH"

        else:

            story.overall_bias = "RANGE"

        alignment = max(bullish, bearish)

        story.confidence = int(
            alignment / 3 * 100
        )

        if story.overall_bias == "BULLISH":

            story.objective = (
                "Higher timeframe buy-side liquidity."
            )

            story.story = (
                "Bullish continuation expected."
            )

        elif story.overall_bias == "BEARISH":

            story.objective = (
                "Higher timeframe sell-side liquidity."
            )

            story.story = (
                "Bearish continuation expected."
            )

        else:

            story.objective = (
                "Await higher timeframe alignment."
            )

            story.story = (
                "Mixed higher timeframe conditions."
            )

        return story
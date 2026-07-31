from models.trend_analysis import TrendAnalysis


class TrendEngine:
    """
    PAL Trend Engine

    This engine combines multiple higher-level factors
    to determine the trend direction.

    NOTE:
    The evaluation methods currently return placeholder
    values. They will be replaced with your actual PAL
    trading rules.
    """

    def analyze(
        self,
        candles,
        timeframe: str = "",
    ) -> TrendAnalysis:

        trend = TrendAnalysis()

        trend.timeframe = timeframe

        trend.delivery = self.evaluate_delivery(
            candles
        )

        trend.liquidity_objective = self.evaluate_liquidity(
            candles
        )

        trend.displacement = self.evaluate_displacement(
            candles
        )

        trend.candle_closes = self.evaluate_candle_closes(
            candles
        )

        bullish = 0
        bearish = 0

        values = [
            trend.delivery,
            trend.liquidity_objective,
            trend.displacement,
            trend.candle_closes,
        ]

        for value in values:

            if value == "BULLISH":
                bullish += 1

            elif value == "BEARISH":
                bearish += 1

        trend.score = bullish - bearish

        if bullish > bearish:

            trend.direction = "BULLISH"
            trend.confidence = int((bullish / 4) * 100)

        elif bearish > bullish:

            trend.direction = "BEARISH"
            trend.confidence = int((bearish / 4) * 100)

        else:

            trend.direction = "NEUTRAL"
            trend.confidence = 50

        trend.reason = (
            f"Delivery={trend.delivery}, "
            f"Liquidity={trend.liquidity_objective}, "
            f"Displacement={trend.displacement}, "
            f"CandleCloses={trend.candle_closes}"
        )

        return trend

    # ======================================================
    # Placeholder Methods
    # ======================================================

    def evaluate_delivery(self, candles):

        return "UNKNOWN"

    def evaluate_liquidity(self, candles):

        return "UNKNOWN"

    def evaluate_displacement(self, candles):

        return "UNKNOWN"

    def evaluate_candle_closes(self, candles):

        return "UNKNOWN"
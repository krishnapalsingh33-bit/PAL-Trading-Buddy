from models.manipulation_analysis import ManipulationAnalysis
from models.liquidity_analysis import LiquidityAnalysis


class ManipulationEngine:

    def analyze(
        self,
        candles,
        liquidity: LiquidityAnalysis,
        timeframe: str,
    ) -> ManipulationAnalysis:

        analysis = ManipulationAnalysis(
            timeframe=timeframe
        )

        if len(candles) < 2:

            analysis.reason = (
                "Not enough candles."
            )

            return analysis

        latest = candles[-1]

        if liquidity.external_buy_taken:

            analysis.detected = True
            analysis.direction = "BEARISH"
            analysis.liquidity_type = "EXTERNAL_BUY"
            analysis.sweep_candle = latest
            analysis.reason = (
                "External buy-side liquidity swept."
            )

            return analysis

        if liquidity.external_sell_taken:

            analysis.detected = True
            analysis.direction = "BULLISH"
            analysis.liquidity_type = "EXTERNAL_SELL"
            analysis.sweep_candle = latest
            analysis.reason = (
                "External sell-side liquidity swept."
            )

            return analysis

        analysis.reason = (
            "No manipulation detected."
        )

        return analysis
from models.candle import Candle
from models.market_narrative import MarketNarrative
from models.manipulation_analysis import ManipulationAnalysis


class ManipulationEngine:
    """
    Detects liquidity manipulation (liquidity sweep)
    before displacement begins.
    """

    def analyze(
        self,
        candles: list[Candle],
        narrative: MarketNarrative
    ) -> ManipulationAnalysis:

        result = ManipulationAnalysis()

        # ----------------------------------
        # Validation
        # ----------------------------------

        if not candles:
            result.reason = "No candles."
            return result

        if (
            narrative.liquidity is None
            or narrative.liquidity.current_objective is None
        ):
            result.reason = "No active liquidity objective."
            return result

        current = candles[-1]
        objective = narrative.liquidity.current_objective

        result.timeframe = objective.timeframe
        result.liquidity = objective

        body = abs(current.close - current.open)

        if body == 0:
            body = 0.0000001

        # ----------------------------------
        # BUY-SIDE Sweep
        # ----------------------------------

        if objective.side == "BUY":

            level = objective.candle.high

            if current.high >= level:

                upper_wick = (
                    current.high -
                    max(current.open, current.close)
                )

                result.exists = True
                result.direction = "Bearish"
                result.sweep_candle = current
                result.sweep_price = current.high
                result.wick_ratio = upper_wick / body
                result.rejection = current.close < level

                objective.mark_manipulation()

                result.reason = "Buy-side liquidity swept."

                result.summary = (
                    f"BUY liquidity swept on "
                    f"{objective.timeframe}."
                )

                return result

        # ----------------------------------
        # SELL-SIDE Sweep
        # ----------------------------------

        if objective.side == "SELL":

            level = objective.candle.low

            if current.low <= level:

                lower_wick = (
                    min(current.open, current.close)
                    - current.low
                )

                result.exists = True
                result.direction = "Bullish"
                result.sweep_candle = current
                result.sweep_price = current.low
                result.wick_ratio = lower_wick / body
                result.rejection = current.close > level

                objective.mark_manipulation()

                result.reason = "Sell-side liquidity swept."

                result.summary = (
                    f"SELL liquidity swept on "
                    f"{objective.timeframe}."
                )

                return result

        # ----------------------------------
        # No Sweep
        # ----------------------------------

        result.reason = "No manipulation."
        result.summary = result.reason

        return result
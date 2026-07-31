from models.candle import Candle
from models.market_narrative import MarketNarrative
from models.displacement_analysis import DisplacementAnalysis


class DisplacementEngine:
    """
    Detects the initial displacement after a confirmed
    manipulation. This version remains compatible with the
    current pipeline while preparing for the future
    momentum-sequence implementation.
    """

    def analyze(
        self,
        candles: list[Candle],
        narrative: MarketNarrative
    ) -> DisplacementAnalysis:

        result = DisplacementAnalysis()

        # ----------------------------------
        # Need manipulation first
        # ----------------------------------

        if (
            narrative.manipulation is None
            or not narrative.manipulation.exists
        ):
            result.reason = "No manipulation."
            return result

        if len(candles) < 3:
            result.reason = "Not enough candles."
            return result

        previous = candles[-2]
        current = candles[-1]

        # ----------------------------------
        # Candle Quality
        # ----------------------------------

        current_body = abs(
            current.close - current.open
        )

        previous_body = abs(
            previous.close - previous.open
        )

        if previous_body == 0:
            previous_body = 0.0000001

        result.body_ratio = (
            current_body / previous_body
        )

        if current.close >= current.open:
            opposite_wick = current.lower_wick
        else:
            opposite_wick = current.upper_wick

        if current_body == 0:
            result.opposite_wick_ratio = 1.0
        else:
            result.opposite_wick_ratio = (
                opposite_wick / current_body
            )

        result.strong_body = (
            result.body_ratio >= 1.5
        )

        result.small_opposite_wick = (
            result.opposite_wick_ratio <= 0.30
        )

        # ----------------------------------
        # Bullish Displacement
        # ----------------------------------

        bullish = (

            narrative.manipulation.direction == "Bullish"

            and current.bullish

            and result.strong_body

            and result.small_opposite_wick

            and current.close > previous.high

        )

        # ----------------------------------
        # Bearish Displacement
        # ----------------------------------

        bearish = (

            narrative.manipulation.direction == "Bearish"

            and current.bearish

            and result.strong_body

            and result.small_opposite_wick

            and current.close < previous.low

        )

        if bullish:

            result.confirmed = True
            result.direction = "Bullish"

        elif bearish:

            result.confirmed = True
            result.direction = "Bearish"

        else:

            result.reason = "No displacement."
            return result

        # ----------------------------------
        # Sequence (V1 Compatible)
        # ----------------------------------

        result.start_candle = current
        result.end_candle = current
        result.candles.append(current)
        result.candle_count = 1

        result.reason = (
            f"{result.direction} displacement confirmed."
        )

        result.summary = (
            f"{result.direction} displacement "
            f"({result.candle_count} candle)."
        )

        return result
from models.candle import Candle
from models.market_narrative import MarketNarrative
from models.fvg_analysis import (
    FVGAnalysis,
    FairValueGap
)


class FVGEngine:
    """
    Detects Fair Value Gaps created during
    confirmed market displacement.
    """

    def analyze(
        self,
        candles: list[Candle],
        narrative: MarketNarrative
    ) -> FVGAnalysis:

        result = FVGAnalysis()

        # ----------------------------------------
        # Validation
        # ----------------------------------------

        if len(candles) < 3:

            result.story = "Not enough candles."
            return result

        if (
            narrative.displacement is None
            or not narrative.displacement.confirmed
        ):

            result.story = "No confirmed displacement."
            return result

        if (
            narrative.delivery is None
            or not narrative.delivery.confirmed
        ):

            result.story = "Delivery not confirmed."
            return result

        if narrative.premium_discount is None:

            result.story = "No premium/discount."
            return result

        direction = narrative.displacement.direction

        # ----------------------------------------
        # Scan
        # ----------------------------------------

        for i in range(2, len(candles)):

            left = candles[i - 2]
            middle = candles[i - 1]
            right = candles[i]

            # ------------------------------------
            # Bullish FVG
            # ------------------------------------

            if (
                direction == "Bullish"
                and left.high < right.low
            ):

                gap = FairValueGap()

                gap.direction = "BUY"
                gap.top = right.low
                gap.bottom = left.high
                gap.midpoint = (
                    gap.top + gap.bottom
                ) / 2

                gap.creation_candle = middle
                gap.reason = "Bullish Fair Value Gap"

                result.bullish.append(gap)

            # ------------------------------------
            # Bearish FVG
            # ------------------------------------

            elif (
                direction == "Bearish"
                and left.low > right.high
            ):

                gap = FairValueGap()

                gap.direction = "SELL"
                gap.top = left.low
                gap.bottom = right.high
                gap.midpoint = (
                    gap.top + gap.bottom
                ) / 2

                gap.creation_candle = middle
                gap.reason = "Bearish Fair Value Gap"

                result.bearish.append(gap)

        # ----------------------------------------
        # Active Gap
        # ----------------------------------------

        if result.bullish:
            result.active_bullish = result.bullish[-1]

        if result.bearish:
            result.active_bearish = result.bearish[-1]

        result.total = (
            len(result.bullish)
            + len(result.bearish)
        )

        if result.total:

            result.story = (
                f"{result.total} active Fair Value Gap(s)."
            )

        else:

            result.story = (
                "No Fair Value Gaps found."
            )

        return result
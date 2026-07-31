from models.structure_analysis import StructureAnalysis
from models.swing_analysis import SwingAnalysis


class StructureEngine:

    def analyze(
        self,
        swings: SwingAnalysis
    ) -> StructureAnalysis:

        structure = StructureAnalysis(
            timeframe=swings.timeframe,
            swing_highs=swings.swing_highs,
            swing_lows=swings.swing_lows,
        )

        # --------------------------------------------------
        # Need swings
        # --------------------------------------------------

        if (
            len(swings.swing_highs) < 2
            or
            len(swings.swing_lows) < 2
        ):

            structure.trend = "UNKNOWN"
            structure.story = "Not enough structure."

            return structure

        latest_high = swings.swing_highs[-1]
        previous_high = swings.swing_highs[-2]

        latest_low = swings.swing_lows[-1]
        previous_low = swings.swing_lows[-2]

        structure.latest_swing_high = latest_high
        structure.latest_swing_low = latest_low

        # --------------------------------------------------
        # Bullish Structure
        # --------------------------------------------------

        if (
            latest_high.high > previous_high.high
            and
            latest_low.low > previous_low.low
        ):

            structure.trend = "BULLISH"
            structure.story = "Bullish structure."
            structure.summary = "Higher High + Higher Low"

            structure.external_high = latest_high
            structure.external_low = previous_low
            structure.protected_low = previous_low
            structure.active_side = "BUY"

        # --------------------------------------------------
        # Bearish Structure
        # --------------------------------------------------

        elif (
            latest_high.high < previous_high.high
            and
            latest_low.low < previous_low.low
        ):

            structure.trend = "BEARISH"
            structure.story = "Bearish structure."
            structure.summary = "Lower High + Lower Low"

            structure.external_low = latest_low
            structure.external_high = previous_high
            structure.protected_high = previous_high
            structure.active_side = "SELL"

        # --------------------------------------------------
        # Transitional Structure
        # --------------------------------------------------

        else:

            structure.trend = "TRANSITION"
            structure.story = "Waiting for market confirmation."
            structure.summary = "Mixed swing structure"

            structure.active_side = "NONE"

        return structure
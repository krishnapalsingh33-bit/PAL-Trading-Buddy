from models.structure_analysis import StructureAnalysis


class StructureEngine:

    def analyze(
        self,
        candles,
        timeframe: str,
    ) -> StructureAnalysis:

        analysis = StructureAnalysis(
            timeframe=timeframe,
            swing_highs=[],
            swing_lows=[],
        )

        if len(candles) < 5:

            analysis.summary = (
                "Not enough candles."
            )

            return analysis

        # -----------------------------
        # Detect Pivot Highs
        # -----------------------------

        for i in range(2, len(candles) - 2):

            c = candles[i]

            if (
                c.high > candles[i - 1].high
                and c.high > candles[i - 2].high
                and c.high > candles[i + 1].high
                and c.high > candles[i + 2].high
            ):
                analysis.swing_highs.append(c)

            if (
                c.low < candles[i - 1].low
                and c.low < candles[i - 2].low
                and c.low < candles[i + 1].low
                and c.low < candles[i + 2].low
            ):
                analysis.swing_lows.append(c)

        if analysis.swing_highs:
            analysis.latest_swing_high = analysis.swing_highs[-1]

        if analysis.swing_lows:
            analysis.latest_swing_low = analysis.swing_lows[-1]

        if (
            analysis.latest_swing_high
            and analysis.latest_swing_low
        ):

            if (
                analysis.latest_swing_high.datetime
                >
                analysis.latest_swing_low.datetime
            ):
                analysis.trend = "BULLISH"
            else:
                analysis.trend = "BEARISH"

        analysis.summary = (
            f"Swing Highs: {len(analysis.swing_highs)} | "
            f"Swing Lows: {len(analysis.swing_lows)} | "
            f"Trend: {analysis.trend}"
        )

        return analysis
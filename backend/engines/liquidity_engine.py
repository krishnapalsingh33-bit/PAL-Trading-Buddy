from models.liquidity_analysis import LiquidityAnalysis
from models.structure_analysis import StructureAnalysis


class LiquidityEngine:

    def analyze(
        self,
        candles,
        structure: StructureAnalysis,
        timeframe: str,
    ) -> LiquidityAnalysis:

        analysis = LiquidityAnalysis(
            timeframe=timeframe
        )

        if len(candles) < 5:

            analysis.summary = "Not enough candles."

            return analysis

        latest = candles[-1]

        # -----------------------------
        # External Liquidity
        # -----------------------------

        analysis.external_buy_side = (
            structure.latest_swing_high
        )

        analysis.external_sell_side = (
            structure.latest_swing_low
        )

        if (
            analysis.external_buy_side
            and latest.high > analysis.external_buy_side.high
        ):

            analysis.external_buy_taken = True

            analysis.last_sweep = "EXTERNAL_BUY"

        if (
            analysis.external_sell_side
            and latest.low < analysis.external_sell_side.low
        ):

            analysis.external_sell_taken = True

            analysis.last_sweep = "EXTERNAL_SELL"

        analysis.summary = (
            f"Trend: {structure.trend} | "
            f"Last Sweep: {analysis.last_sweep}"
        )

        return analysis
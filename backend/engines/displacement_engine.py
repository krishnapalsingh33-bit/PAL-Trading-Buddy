from models.displacement_analysis import DisplacementAnalysis
from models.manipulation_analysis import ManipulationAnalysis


class DisplacementEngine:

    def analyze(
        self,
        candles,
        manipulation: ManipulationAnalysis,
        timeframe: str,
    ) -> DisplacementAnalysis:

        analysis = DisplacementAnalysis(
            timeframe=timeframe,
            candles=[],
        )

        if not manipulation.detected:

            analysis.reason = (
                "No manipulation detected."
            )

            return analysis

        if len(candles) < 2:

            analysis.reason = (
                "Not enough candles."
            )

            return analysis

        # Placeholder implementation.
        # Real PAL momentum rules will replace this.

        analysis.confirmed = True

        analysis.direction = manipulation.direction

        analysis.start_candle = candles[-2]

        analysis.end_candle = candles[-1]

        analysis.candles = candles[-2:]

        analysis.candle_count = len(
            analysis.candles
        )

        analysis.reason = (
            "Momentum sequence detected."
        )

        return analysis
from models.delivery_analysis import DeliveryAnalysis
from models.displacement_analysis import DisplacementAnalysis


class DeliveryEngine:

    def analyze(
        self,
        displacement: DisplacementAnalysis,
        timeframe: str,
    ) -> DeliveryAnalysis:

        analysis = DeliveryAnalysis(
            timeframe=timeframe
        )

        analysis.displacement = displacement

        if not displacement.confirmed:

            analysis.story = (
                "No confirmed displacement."
            )

            return analysis

        analysis.confirmed = True

        analysis.direction = displacement.direction

        analysis.origin = displacement.start_candle

        analysis.active_candle = displacement.end_candle

        analysis.story = (
            "Delivery active."
        )

        return analysis
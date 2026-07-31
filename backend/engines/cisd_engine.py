from models.cisd_analysis import CISDAnalysis
from models.delivery_analysis import DeliveryAnalysis


class CISDEngine:

    def analyze(
        self,
        delivery: DeliveryAnalysis,
    ) -> CISDAnalysis:

        analysis = CISDAnalysis(
            timeframe=delivery.timeframe
        )

        analysis.delivery = delivery

        if not delivery.confirmed:

            analysis.reason = (
                "Delivery not confirmed."
            )

            return analysis

        if delivery.origin is None:

            analysis.reason = (
                "No delivery origin."
            )

            return analysis

        analysis.confirmed = True

        analysis.exists = True

        analysis.direction = (
            delivery.direction
        )

        analysis.close_candle = (
            delivery.active_candle
        )

        analysis.reason = (
            "CISD confirmed."
        )

        return analysis
from models.candle import Candle
from models.cisd_analysis import CISDAnalysis
from models.market_narrative import MarketNarrative


class CISDEngine:
    """
    Detects a Change In State of Delivery (CISD)
    after a confirmed delivery sequence.
    """

    def analyze(
        self,
        candles: list[Candle],
        narrative: MarketNarrative
    ) -> CISDAnalysis:

        result = CISDAnalysis()

        # ----------------------------------
        # Context
        # ----------------------------------

        result.delivery = narrative.delivery

        if narrative.delivery:
            result.timeframe = narrative.delivery.timeframe

        # ----------------------------------
        # Validation
        # ----------------------------------

        if not candles:

            result.reason = "No candles."
            result.summary = result.reason
            return result

        delivery = narrative.delivery

        if delivery is None:

            result.reason = "No delivery."
            result.summary = result.reason
            return result

        if not delivery.confirmed:

            result.reason = "Delivery not confirmed."
            result.summary = result.reason
            return result

        if delivery.origin is None:

            result.reason = "No delivery origin."
            result.summary = result.reason
            return result

        current = candles[-1]

        result.trigger_candle = current

        # ----------------------------------
        # Bullish Delivery
        # ----------------------------------

        if delivery.direction == "BULLISH":

            if current.close < delivery.origin.low:

                result.exists = True
                result.confirmed = True
                result.direction = "Bearish"

                result.reason = "Bearish CISD confirmed."
                result.summary = result.reason

                return result

        # ----------------------------------
        # Bearish Delivery
        # ----------------------------------

        elif delivery.direction == "BEARISH":

            if current.close > delivery.origin.high:

                result.exists = True
                result.confirmed = True
                result.direction = "Bullish"

                result.reason = "Bullish CISD confirmed."
                result.summary = result.reason

                return result

        # ----------------------------------
        # Unknown Direction
        # ----------------------------------

        elif delivery.direction == "NONE":

            result.reason = "Unknown delivery direction."
            result.summary = result.reason

            return result

        # ----------------------------------
        # No CISD
        # ----------------------------------

        result.reason = "No CISD."
        result.summary = result.reason

        return result
from models.candle import Candle
from models.market_narrative import MarketNarrative
from models.delivery_analysis import DeliveryAnalysis


class DeliveryEngine:
    """
    Detects active market delivery after a confirmed
    displacement sequence.
    """

    def analyze(
        self,
        candles: list[Candle],
        narrative: MarketNarrative,
        timeframe: str
    ) -> DeliveryAnalysis:

        result = DeliveryAnalysis(
            timeframe=timeframe
        )

        result.manipulation = narrative.manipulation
        result.displacement = narrative.displacement

        # ----------------------------------
        # Validation
        # ----------------------------------

        if not candles:
            result.story = "No candles."
            result.summary = result.story
            return result

        if (
            narrative.manipulation is None
            or not narrative.manipulation.exists
        ):
            result.story = "No manipulation."
            result.summary = result.story
            return result

        if (
            narrative.displacement is None
            or not narrative.displacement.confirmed
        ):
            result.story = "No displacement."
            result.summary = result.story
            return result

        displacement = (
            narrative.displacement.end_candle
            or narrative.displacement.start_candle
        )

        if displacement is None:
            result.story = "Missing displacement candle."
            result.summary = result.story
            return result

        # ----------------------------------
        # Delivery Direction
        # ----------------------------------

        if narrative.displacement.direction == "Bullish":

            result.direction = "BULLISH"

        elif narrative.displacement.direction == "Bearish":

            result.direction = "BEARISH"

        else:

            result.story = "Unknown displacement direction."
            result.summary = result.story
            return result

        # ----------------------------------
        # Delivery Origin
        # ----------------------------------

        origin = None

        try:
            index = candles.index(displacement)
        except ValueError:
            result.story = "Displacement candle not found."
            result.summary = result.story
            return result

        if result.direction == "BULLISH":

            for i in range(index, -1, -1):

                if candles[i].bearish:
                    origin = candles[i]
                    break

        else:

            for i in range(index, -1, -1):

                if candles[i].bullish:
                    origin = candles[i]
                    break

        result.origin = origin
        result.active_candle = candles[-1]
        result.confirmed = origin is not None

        # ----------------------------------
        # Story
        # ----------------------------------

        if result.confirmed:

            result.story = (
                f"{result.direction} delivery active."
            )

        else:

            result.story = (
                "Delivery detected but origin candle not found."
            )

        result.summary = result.story

        return result
from models.candle import Candle
from brain.events import Event


class LiquidityDetector:

    def detect(self, candles: list[Candle], observation):

        if len(candles) < 3:
            return

        latest = candles[-1]

        previous_high = max(
            candle.high
            for candle in candles[:-1]
        )

        previous_low = min(
            candle.low
            for candle in candles[:-1]
        )

        if latest.high >= previous_high:

            observation.add_event(
                Event.EXTERNAL_LIQUIDITY
            )

            observation.evidence.append(

                f"Previous High Taken ({previous_high})"

            )

        if latest.low <= previous_low:

            observation.add_event(
                Event.INTERNAL_LIQUIDITY
            )

            observation.evidence.append(

                f"Previous Low Taken ({previous_low})"

            )
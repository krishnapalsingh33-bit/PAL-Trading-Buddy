from models.candle import Candle


class PivotDetector:

    def detect(

        self,

        candles: list[Candle]

    ):

        swing_highs = []

        swing_lows = []

        for i in range(2, len(candles) - 2):

            current = candles[i]

            # -----------------------
            # Swing High
            # -----------------------

            if (

                current.high >

                candles[i - 1].high

                and current.high >

                candles[i - 2].high

                and current.high >

                candles[i + 1].high

                and current.high >

                candles[i + 2].high

            ):

                swing_highs.append(

                    current

                )

            # -----------------------
            # Swing Low
            # -----------------------

            if (

                current.low <

                candles[i - 1].low

                and current.low <

                candles[i - 2].low

                and current.low <

                candles[i + 1].low

                and current.low <

                candles[i + 2].low

            ):

                swing_lows.append(

                    current

                )

        return swing_highs, swing_lows
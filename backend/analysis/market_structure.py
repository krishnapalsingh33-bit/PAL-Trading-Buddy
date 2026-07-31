from models.candle import Candle


class MarketStructureAnalyzer:

    def analyze(self, candles: list[Candle]):

        if len(candles) < 10:

            return {
                "trend": "Unknown",
                "confidence": 0,
                "reason": "Not enough candles."
            }

        recent = candles[-10:]

        first = recent[0]
        last = recent[-1]

        higher_high = last.high > first.high
        higher_low = last.low > first.low

        lower_high = last.high < first.high
        lower_low = last.low < first.low

        if higher_high and higher_low:

            return {

                "trend": "Bullish",

                "confidence": 80,

                "reason": "Market is making higher highs and higher lows."

            }

        if lower_high and lower_low:

            return {

                "trend": "Bearish",

                "confidence": 80,

                "reason": "Market is making lower highs and lower lows."

            }

        return {

            "trend": "Range",

            "confidence": 40,

            "reason": "Market is ranging."

        }
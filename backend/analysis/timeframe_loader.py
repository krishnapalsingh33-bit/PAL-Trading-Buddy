from services.market_data_service import MarketDataService


class TimeframeLoader:

    def __init__(self, service: MarketDataService):

        self.service = service

    def load(self, symbol):

        return {

            "Weekly": self.service.get_candles(
                symbol,
                "1week",
                300
            ),

            "Daily": self.service.get_candles(
                symbol,
                "1day",
                300
            ),

            "4H": self.service.get_candles(
                symbol,
                "4h",
                300
            ),

            "1H": self.service.get_candles(
                symbol,
                "1h",
                300
            ),

            "30M": self.service.get_candles(
                symbol,
                "30min",
                300
            ),

            "15M": self.service.get_candles(
                symbol,
                "15min",
                300
            ),

            "5M": self.service.get_candles(
                symbol,
                "5min",
                300
            )

        }
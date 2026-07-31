from datetime import datetime
import logging

from tvDatafeed import TvDatafeed, Interval

from models.candle import Candle
from models.market_data import MarketData
from providers.base_provider import BaseProvider


logger = logging.getLogger(__name__)


class TradingViewProvider(BaseProvider):
    """
    Downloads market data from TradingView.
    """

    def __init__(self):
        self.tv = TvDatafeed()

    def _download(
        self,
        symbol: str,
        exchange: str,
        interval: Interval,
        n_bars: int,
        name: str,
    ) -> list[Candle]:

        try:

            df = self.tv.get_hist(
                symbol=symbol,
                exchange=exchange,
                interval=interval,
                n_bars=n_bars,
            )

            if df is None or df.empty:
                logger.warning(
                    "%s returned no data.",
                    name,
                )
                return []

            candles: list[Candle] = []

            for index, row in df.iterrows():

                candles.append(
                    Candle(
                        datetime=index.to_pydatetime()
                        if isinstance(index, datetime)
                        else index,
                        open=float(row["open"]),
                        high=float(row["high"]),
                        low=float(row["low"]),
                        close=float(row["close"]),
                        volume=float(row["volume"])
                        if "volume" in row
                        else None,
                    )
                )

            logger.info(
                "%s : %s candles downloaded.",
                name,
                len(candles),
            )

            return candles

        except Exception as ex:

            logger.warning(
                "%s failed : %s",
                name,
                ex,
            )

            return []

    def get_market_data(
        self,
        symbol: str,
    ) -> MarketData:

        exchange = "FX_IDC"

        data = MarketData(symbol=symbol)

        downloads = [

            ("monthly", Interval.in_monthly, 300),

            ("weekly", Interval.in_weekly, 500),

            ("daily", Interval.in_daily, 1000),

            ("h4", Interval.in_4_hour, 1000),

            ("h1", Interval.in_1_hour, 2000),

            ("m30", Interval.in_30_minute, 3000),

            ("m15", Interval.in_15_minute, 5000),

            ("m5", Interval.in_5_minute, 5000),

            # tvDatafeed often doesn't support this interval.
            # We'll derive it later if necessary.
            ("m1", Interval.in_1_minute, 5000),
        ]

        for field, interval, bars in downloads:

            setattr(
                data,
                field,
                self._download(
                    symbol,
                    exchange,
                    interval,
                    bars,
                    field.upper(),
                ),
            )

        # ---------------------------------------------------
        # Build M3 from M1 if TradingView doesn't support it.
        # ---------------------------------------------------

        data.m3 = []

        if len(data.m1) >= 3:

            for i in range(2, len(data.m1), 3):

                group = data.m1[i - 2:i + 1]

                data.m3.append(
                    Candle(
                        datetime=group[-1].datetime,
                        open=group[0].open,
                        high=max(c.high for c in group),
                        low=min(c.low for c in group),
                        close=group[-1].close,
                        volume=sum(
                            c.volume or 0
                            for c in group
                        ),
                    )
                )

        return data

    def get_dxy_data(
        self,
    ) -> MarketData:

        return self.get_market_data("DXY")
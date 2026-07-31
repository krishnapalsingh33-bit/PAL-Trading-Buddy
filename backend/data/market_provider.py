from datetime import datetime

import MetaTrader5 as mt5

from models.candle import Candle
from models.market_context import (
    MarketContext,
    TimeframeData,
)

# Number of candles to download per timeframe
DEFAULT_BARS = 500

TIMEFRAMES = {
    "W1": mt5.TIMEFRAME_W1,
    "D1": mt5.TIMEFRAME_D1,
    "H4": mt5.TIMEFRAME_H4,
    "H1": mt5.TIMEFRAME_H1,
    "M30": mt5.TIMEFRAME_M30,
    "M15": mt5.TIMEFRAME_M15,
    "M5": mt5.TIMEFRAME_M5,
    "M1": mt5.TIMEFRAME_M1,
}


def _initialize_mt5():

    if mt5.initialize():
        return

    raise RuntimeError(
        f"MetaTrader5 initialization failed: {mt5.last_error()}"
    )


def _shutdown_mt5():
    mt5.shutdown()


def _download(symbol: str, timeframe, bars: int):

    rates = mt5.copy_rates_from_pos(
        symbol,
        timeframe,
        0,
        bars,
    )

    if rates is None:
        raise RuntimeError(
            f"Unable to download {symbol} candles: {mt5.last_error()}"
        )

    candles = []

    for r in rates:

        candles.append(
            Candle(
                datetime=datetime.fromtimestamp(r["time"]),
                open=float(r["open"]),
                high=float(r["high"]),
                low=float(r["low"]),
                close=float(r["close"]),
                volume=float(r["tick_volume"]),
            )
        )

    return candles


def _build_m3(m1_candles):

    if len(m1_candles) < 3:
        return []

    candles = []

    for i in range(0, len(m1_candles) - 2, 3):

        group = m1_candles[i:i + 3]

        candles.append(
            Candle(
                datetime=group[0].datetime,
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

    return candles


def get_symbol_data(symbol: str) -> MarketContext:

    symbol = symbol.upper()

    _initialize_mt5()

    try:

        if not mt5.symbol_select(symbol, True):
            raise RuntimeError(
                f"Unable to select symbol {symbol}"
            )

        weekly = _download(
            symbol,
            TIMEFRAMES["W1"],
            DEFAULT_BARS,
        )

        daily = _download(
            symbol,
            TIMEFRAMES["D1"],
            DEFAULT_BARS,
        )

        h4 = _download(
            symbol,
            TIMEFRAMES["H4"],
            DEFAULT_BARS,
        )

        h1 = _download(
            symbol,
            TIMEFRAMES["H1"],
            DEFAULT_BARS,
        )

        m30 = _download(
            symbol,
            TIMEFRAMES["M30"],
            DEFAULT_BARS,
        )

        m15 = _download(
            symbol,
            TIMEFRAMES["M15"],
            DEFAULT_BARS,
        )

        m5 = _download(
            symbol,
            TIMEFRAMES["M5"],
            DEFAULT_BARS,
        )

        m1 = _download(
            symbol,
            TIMEFRAMES["M1"],
            DEFAULT_BARS,
        )

        m3 = _build_m3(m1)

        context = MarketContext()

        context.symbol = symbol

        context.weekly = TimeframeData(
            timeframe="W1",
            candles=weekly,
        )

        context.daily = TimeframeData(
            timeframe="D1",
            candles=daily,
        )

        context.h4 = TimeframeData(
            timeframe="H4",
            candles=h4,
        )

        context.h1 = TimeframeData(
            timeframe="H1",
            candles=h1,
        )

        context.m30 = TimeframeData(
            timeframe="M30",
            candles=m30,
        )

        context.m15 = TimeframeData(
            timeframe="M15",
            candles=m15,
        )

        context.m5 = TimeframeData(
            timeframe="M5",
            candles=m5,
        )

        context.m3 = TimeframeData(
            timeframe="M3",
            candles=m3,
        )

        context.m1 = TimeframeData(
            timeframe="M1",
            candles=m1,
        )

        return context

    finally:

        _shutdown_mt5()
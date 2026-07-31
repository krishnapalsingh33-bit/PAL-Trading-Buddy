from abc import ABC, abstractmethod

from models.market_data import MarketData


class BaseProvider(ABC):
    """
    Abstract base class for all market data providers.

    Every provider (TradingView, MT5, CSV, Binance, etc.)
    must implement these methods.
    """

    @abstractmethod
    def get_market_data(self, symbol: str) -> MarketData:
        """
        Return all required timeframe data for the given symbol.
        """
        pass

    @abstractmethod
    def get_dxy_data(self) -> MarketData:
        """
        Return DXY market data.
        """
        pass
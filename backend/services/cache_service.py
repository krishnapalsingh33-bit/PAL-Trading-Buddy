from datetime import datetime, timedelta
from typing import Dict

from models.market_data import MarketData


class CacheService:
    """
    Singleton in-memory cache for market data.
    """

    _instance = None

    def __new__(cls, ttl_minutes: int = 1):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.ttl = timedelta(minutes=ttl_minutes)
            cls._instance._cache: Dict[str, tuple[datetime, MarketData]] = {}
        return cls._instance

    def get(self, symbol: str) -> MarketData | None:
        if symbol not in self._cache:
            return None

        timestamp, data = self._cache[symbol]

        if datetime.now() - timestamp > self.ttl:
            del self._cache[symbol]
            return None

        return data

    def set(self, symbol: str, data: MarketData):
        self._cache[symbol] = (
            datetime.now(),
            data,
        )

    def clear(self):
        self._cache.clear()
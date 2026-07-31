from providers.provider_factory import ProviderFactory
from services.cache_service import CacheService
from models.market_data import MarketData


class MarketDataService:
    """
    Responsible for providing market data to the application.

    - Uses cache whenever possible.
    - Downloads fresh data when needed.
    """

    def __init__(self):
        self.provider = ProviderFactory.get_provider()
        self.cache = CacheService()

    def get_market_data(
        self,
        symbol: str,
        force_refresh: bool = False,
    ) -> MarketData:

        if not force_refresh:
            cached = self.cache.get(symbol)

            if cached is not None:
                return cached

        data = self.provider.get_market_data(symbol)

        self.cache.set(symbol, data)

        return data

    def get_dxy_data(
        self,
        force_refresh: bool = False,
    ) -> MarketData:

        symbol = "DXY"

        if not force_refresh:
            cached = self.cache.get(symbol)

            if cached is not None:
                return cached

        data = self.provider.get_dxy_data()

        self.cache.set(symbol, data)

        return data

    def clear_cache(self):
        self.cache.clear()
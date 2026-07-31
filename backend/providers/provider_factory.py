from providers.tradingview_provider import TradingViewProvider


class ProviderFactory:
    """
    Creates and manages provider instances.
    """

    _provider = None

    @classmethod
    def get_provider(cls):
        if cls._provider is None:
            cls._provider = TradingViewProvider()

        return cls._provider
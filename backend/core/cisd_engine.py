from core.models import CISDData


def analyze_cisd():

    """
    Placeholder version.

    Later this engine will detect
    real CISD from market data.
    """

    return CISDData(

        confirmed=True,

        timeframe="3m",

        candle_count=3,

        direction="BUY",

        displacement=True,

        imbalance_created=True,

        quality="STRONG"
    )
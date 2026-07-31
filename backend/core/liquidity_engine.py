from core.models import LiquidityData


def analyze_liquidity():

    """
    Placeholder version.

    Later this engine will detect
    real liquidity from market data.
    """

    return LiquidityData(

        external_buy_side_taken=True,
        external_sell_side_taken=False,

        internal_buy_side_taken=True,
        internal_sell_side_taken=False,

        current_external_side="BUY",
        current_internal_side="BUY",

        sweep_count=2
    )
from dataclasses import dataclass

from models.candle import Candle


@dataclass
class PremiumDiscountAnalysis:
    """
    PAL Premium / Discount Analysis

    Determines where the current market price is trading
    within the active dealing range.
    """

    # ----------------------------------
    # Dealing Range
    # ----------------------------------

    dealing_range_high: Candle | None = None

    dealing_range_low: Candle | None = None

    equilibrium: float = 0.0

    # ----------------------------------
    # Current Price
    # ----------------------------------

    current_price: float = 0.0

    # ----------------------------------
    # Market Position
    # ----------------------------------

    premium: bool = False

    discount: bool = False

    equilibrium_zone: bool = False

    # ----------------------------------
    # Summary
    # ----------------------------------

    story: str = ""

    summary: str = ""
from dataclasses import dataclass

from models.candle import Candle
from models.delivery_analysis import DeliveryAnalysis


@dataclass
class CISDAnalysis:
    """
    PAL Change In State of Delivery (CISD)

    Represents the confirmation that market delivery has
    changed state after a valid delivery sequence.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str = ""

    # ----------------------------------
    # Detection
    # ----------------------------------

    exists: bool = False

    confirmed: bool = False

    direction: str = "NONE"      # Bullish / Bearish

    # ----------------------------------
    # Context
    # ----------------------------------

    delivery: DeliveryAnalysis | None = None

    trigger_candle: Candle | None = None

    # ----------------------------------
    # Summary
    # ----------------------------------

    reason: str = ""

    summary: str = ""
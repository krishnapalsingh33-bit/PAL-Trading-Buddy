from dataclasses import dataclass

from models.candle import Candle
from models.displacement_analysis import DisplacementAnalysis
from models.manipulation_analysis import ManipulationAnalysis


@dataclass
class DeliveryAnalysis:
    """
    PAL Delivery Analysis

    Represents active market delivery after a confirmed
    displacement sequence.
    """

    # ----------------------------------
    # Identity
    # ----------------------------------

    timeframe: str = ""

    # ----------------------------------
    # Context
    # ----------------------------------

    manipulation: ManipulationAnalysis | None = None

    displacement: DisplacementAnalysis | None = None

    # ----------------------------------
    # Detection
    # ----------------------------------

    confirmed: bool = False

    direction: str = "NONE"      # BULLISH / BEARISH

    # ----------------------------------
    # Delivery Information
    # ----------------------------------

    origin: Candle | None = None

    active_candle: Candle | None = None

    # ----------------------------------
    # Summary
    # ----------------------------------

    story: str = ""

    summary: str = ""
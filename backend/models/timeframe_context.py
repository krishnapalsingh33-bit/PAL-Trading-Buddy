from dataclasses import dataclass

from models.swing_analysis import SwingAnalysis
from models.structure_analysis import StructureAnalysis
from models.liquidity_analysis import LiquidityAnalysis
from models.manipulation_analysis import ManipulationAnalysis
from models.displacement_analysis import DisplacementAnalysis
from models.delivery_analysis import DeliveryAnalysis
from models.cisd_analysis import CISDAnalysis
from models.market_state import MarketState
from models.premium_discount_analysis import PremiumDiscountAnalysis
from models.fvg_analysis import FVGAnalysis


@dataclass
class TimeframeContext:

    timeframe: str

    swings: SwingAnalysis

    structure: StructureAnalysis

    liquidity: LiquidityAnalysis

    manipulation: ManipulationAnalysis

    displacement: DisplacementAnalysis

    delivery: DeliveryAnalysis

    cisd: CISDAnalysis

    premium_discount: PremiumDiscountAnalysis

    fvg: FVGAnalysis

    market_state: MarketState
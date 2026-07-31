from dataclasses import dataclass

from models.structure_analysis import StructureAnalysis
from models.liquidity_analysis import LiquidityAnalysis
from models.manipulation_analysis import ManipulationAnalysis
from models.displacement_analysis import DisplacementAnalysis
from models.delivery_analysis import DeliveryAnalysis
from models.cisd_analysis import CISDAnalysis
from models.premium_discount_analysis import PremiumDiscountAnalysis
from models.fvg_analysis import FVGAnalysis


@dataclass
class MarketNarrative:

    structure: StructureAnalysis

    liquidity: LiquidityAnalysis

    manipulation: ManipulationAnalysis | None = None

    displacement: DisplacementAnalysis | None = None

    delivery: DeliveryAnalysis | None = None

    cisd: CISDAnalysis | None = None

    premium_discount: PremiumDiscountAnalysis | None = None

    fvg: FVGAnalysis | None = None
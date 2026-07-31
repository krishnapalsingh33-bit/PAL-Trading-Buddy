from dataclasses import dataclass

from models.structure_analysis import StructureAnalysis
from models.liquidity_analysis import LiquidityAnalysis
from models.manipulation_analysis import ManipulationAnalysis
from models.displacement_analysis import DisplacementAnalysis
from models.delivery_analysis import DeliveryAnalysis
from models.cisd_analysis import CISDAnalysis


@dataclass
class GBPUSDAnalysis:
    timeframe: str

    structure: StructureAnalysis | None = None

    liquidity: LiquidityAnalysis | None = None

    manipulation: ManipulationAnalysis | None = None

    displacement: DisplacementAnalysis | None = None

    delivery: DeliveryAnalysis | None = None

    cisd: CISDAnalysis | None = None

    summary: str = ""
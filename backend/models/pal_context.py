from dataclasses import dataclass

from models.structure_analysis import StructureAnalysis
from models.liquidity_analysis import LiquidityAnalysis
from models.manipulation_analysis import ManipulationAnalysis
from models.displacement_analysis import DisplacementAnalysis
from models.delivery_analysis import DeliveryAnalysis
from models.cisd_analysis import CISDAnalysis

from models.market_story import MarketStory
from models.trading_plan import TradingPlan
from models.execution_plan import ExecutionPlan


@dataclass
class PALContext:
    """
    Shared analysis context used by PAL.
    Every engine writes its analysis here so the PAL Brain
    can make the final decision.
    """

    timeframe: str = ""

    # -------------------------
    # Core Analysis
    # -------------------------

    structure: StructureAnalysis | None = None

    liquidity: LiquidityAnalysis | None = None

    manipulation: ManipulationAnalysis | None = None

    displacement: DisplacementAnalysis | None = None

    delivery: DeliveryAnalysis | None = None

    cisd: CISDAnalysis | None = None

    # -------------------------
    # Decision Layers
    # -------------------------

    story: MarketStory | None = None

    trading: TradingPlan | None = None

    execution: ExecutionPlan | None = None